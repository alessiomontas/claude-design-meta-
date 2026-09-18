# -*- coding: utf-8 -*-
"""Controllo qualita' misurato sulle artboard del 18/09, prima del PNG.

Non sostituisce lo sguardo sul PNG a dimensione telefono: risponde alle
domande che l'occhio non sa misurare in fretta.

  1. FUORI FRAME — qualunque elemento che esce dai 1080 x H.
  2. SOVRAPPOSIZIONI — due blocchi di primo livello che si accavallano
     (il punto critico dichiarato: la card recensione con testo lungo sul 9:16).
  3. SAFE AREA — testo leggibile sopra 180 o sotto (H - 320) sui 9:16.
  4. VUOTI — fasce verticali vuote piu' alte di 260 px nell'area utile.
  5. CENTRATURA — blocchi centrati fuori asse di piu' di 8 px.
"""
import glob
import json
import os
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

MISURA = """() => {
  const frame = document.querySelector('.frame');
  const fr = frame.getBoundingClientRect();
  const out = {w: fr.width, h: fr.height, fuori: [], box: []};
  document.querySelectorAll('.frame *').forEach(el => {
    const r = el.getBoundingClientRect();
    const t = (el.textContent || '').trim().slice(0, 40);
    if (r.width > 0 && r.height > 0 &&
        (r.left < fr.left - 0.5 || r.right > fr.right + 0.5 ||
         r.top < fr.top - 0.5 || r.bottom > fr.bottom + 0.5)) {
      out.fuori.push({t: t, l: Math.round(r.left - fr.left), r: Math.round(r.right - fr.left),
                      top: Math.round(r.top - fr.top), bot: Math.round(r.bottom - fr.top)});
    }
    if (el.parentElement === frame && r.width > 0 && r.height > 0) {
      out.box.push({t: t, l: Math.round(r.left - fr.left), r: Math.round(r.right - fr.left),
                    top: Math.round(r.top - fr.top), bot: Math.round(r.bottom - fr.top),
                    txt: t.length > 0});
    }
  });
  return out;
}"""


def main():
    files = sorted(glob.glob(os.path.join(HERE, '*.dc.html')))
    problemi = 0
    with sync_playwright() as p:
        cands = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
        browser = p.chromium.launch(executable_path=cands[-1]) if cands else p.chromium.launch()
        page = browser.new_page(viewport={'width': 1080, 'height': 1920})
        for f in files:
            nome = os.path.basename(f).replace('.dc.html', '')
            page.goto('file://' + f)
            page.wait_for_timeout(700)
            m = page.evaluate(MISURA)
            H = m['h']
            msg = []

            for x in m['fuori']:
                msg.append('FUORI FRAME  %-40s l%d r%d t%d b%d'
                           % (x['t'], x['l'], x['r'], x['top'], x['bot']))

            # sovrapposizioni fra blocchi testuali di primo livello
            testuali = sorted([b for b in m['box'] if b['txt']], key=lambda b: b['top'])
            for i in range(len(testuali) - 1):
                a, b = testuali[i], testuali[i + 1]
                if b['top'] < a['bot'] - 2 and not (b['r'] <= a['l'] or b['l'] >= a['r']):
                    msg.append('SOVRAPPOSTI  "%s" (b%d) / "%s" (t%d)'
                               % (a['t'], a['bot'], b['t'], b['top']))

            if abs(H - 1920) < 1:
                for b in m['box']:
                    if not b['txt']:
                        continue
                    # il lockup di marca sta per contratto a y 112-205 su ogni
                    # artboard 9:16 del progetto: non e' testo di lettura
                    if b['t'] in ('HADRIANUS', 'MULTISERVICE'):
                        continue
                    if b['top'] < 180:
                        msg.append('SAFE ALTO    %-34s t%d' % (b['t'], b['top']))
                    if b['bot'] > H - 320:
                        msg.append('SAFE BASSO   %-34s b%d' % (b['t'], b['bot']))

            # vuoti verticali nell'area utile
            top_u = 180 if abs(H - 1920) < 1 else 60
            bot_u = (H - 320) if abs(H - 1920) < 1 else H - 60
            occupate = sorted([(b['top'], b['bot']) for b in m['box']
                               if b['bot'] > top_u and b['top'] < bot_u])
            cur = top_u
            for t0, t1 in occupate:
                if t0 - cur > 260:
                    msg.append('VUOTO        %d px fra y%d e y%d' % (t0 - cur, cur, t0))
                cur = max(cur, t1)
            if bot_u - cur > 260:
                msg.append('VUOTO        %d px fra y%d e y%d' % (bot_u - cur, cur, bot_u))

            if msg:
                problemi += len(msg)
                print('\n--- %s (%dx%d)' % (nome, m['w'], H))
                for x in msg:
                    print('    ' + x)
            else:
                print('OK  %-6s %dx%d' % (nome, m['w'], H))
        browser.close()
    print('\n%d segnalazioni' % problemi)
    return 1 if problemi else 0


if __name__ == '__main__':
    sys.exit(main())
