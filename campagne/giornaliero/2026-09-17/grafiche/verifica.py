# -*- coding: utf-8 -*-
"""Controllo qualita' misurato sulle artboard, prima del PNG.

Non sostituisce lo sguardo sul PNG a dimensione telefono: risponde alle domande
che l'occhio non sa misurare in fretta.

  1. TRABOCCO — una riga `nowrap` piu' larga del suo contenitore (e' cosi' che
     salta l'altezza identica dei blocchi di confronto).
  2. FUORI FRAME — qualunque elemento che esce dai 1080 x H dell'artboard.
  3. ALTEZZE — i blocchi di confronto di C3/C4 devono essere alti uguali.
  4. SAFE AREA — testo leggibile sopra 180 o sotto (H - 320) sui 9:16.
  5. VUOTI — fasce verticali vuote piu' alte di 260 px dentro l'area utile.

    python3 verifica.py
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
  const out = {w: fr.width, h: fr.height, trabocco: [], fuori: [], box: []};
  document.querySelectorAll('.frame *').forEach(el => {
    const r = el.getBoundingClientRect();
    const t = (el.textContent || '').trim().slice(0, 46);
    if (el.scrollWidth > el.clientWidth + 1 && el.clientWidth > 0) {
      out.trabocco.push({t: t, need: el.scrollWidth, have: el.clientWidth});
    }
    if (r.width > 0 && r.height > 0 &&
        (r.left < fr.left - 0.5 || r.right > fr.right + 0.5 ||
         r.top < fr.top - 0.5 || r.bottom > fr.bottom + 0.5)) {
      out.fuori.push({t: t, l: r.left - fr.left, r: r.right - fr.left,
                      top: r.top - fr.top, bot: r.bottom - fr.top});
    }
    if (el.parentElement === frame && r.width > 0 && r.height > 0) {
      out.box.push({t: t, l: Math.round(r.left - fr.left), r: Math.round(r.right - fr.left),
                    top: Math.round(r.top - fr.top), bot: Math.round(r.bottom - fr.top),
                    tag: el.tagName});
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
        altezze = {}
        for f in files:
            nome = os.path.basename(f).replace('.dc.html', '')
            page.goto('file://' + f)
            page.wait_for_timeout(700)
            m = page.evaluate(MISURA)
            righe = []
            for t in m['trabocco']:
                righe.append('  TRABOCCO  «%s» serve %d px, ne ha %d'
                             % (t['t'], t['need'], t['have']))
            for t in m['fuori']:
                righe.append('  FUORI     «%s» x %d..%d  y %d..%d'
                             % (t['t'], t['l'], t['r'], t['top'], t['bot']))
            h = m['h']
            # 6. SOVRAPPOSIZIONI fra blocchi di primo livello: e' l'errore che
            #    il conteggio dei pixel vede e l'occhio perdona finche' non e'
            #    troppo tardi (la banda del dato sopra l'ultimo confronto).
            # gli strati a tutto campo (foto, velo, radiale) non contano: non
            # sono blocchi, sono il fondo.
            solidi = [b for b in m['box']
                      if b['bot'] - b['top'] > 20 and b['r'] - b['l'] > 300
                      and not (b['top'] <= 1 and b['bot'] >= h - 1
                               and b['l'] <= 1 and b['r'] >= m['w'] - 1)]
            for i in range(len(solidi)):
                for j in range(i + 1, len(solidi)):
                    a, c = solidi[i], solidi[j]
                    contiene = ((not a['t'] and a['top'] <= c['top'] + 1 and
                                 a['bot'] >= c['bot'] - 1 and a['l'] <= c['l'] + 1 and
                                 a['r'] >= c['r'] - 1) or
                                (not c['t'] and c['top'] <= a['top'] + 1 and
                                 c['bot'] >= a['bot'] - 1 and c['l'] <= a['l'] + 1 and
                                 c['r'] >= a['r'] - 1))
                    if contiene:      # piastra di fondo sotto il testo: voluta
                        continue
                    if a['top'] < c['bot'] - 1 and c['top'] < a['bot'] - 1 and \
                            a['l'] < c['r'] - 1 and c['l'] < a['r'] - 1:
                        righe.append('  SOVRAPPOSTI «%s» y %d..%d  e  «%s» y %d..%d'
                                     % (a['t'][:22], a['top'], a['bot'],
                                        c['t'][:22], c['top'], c['bot']))
            if h == 1920:
                for b in m['box']:
                    if b['t'] and b['top'] < 180 and 'HADRIANUS' not in b['t'] \
                            and 'MULTISERVICE' not in b['t']:
                        righe.append('  SAFE-ALTO «%s» y %d' % (b['t'], b['top']))
                    if b['t'] and b['bot'] > h - 320:
                        righe.append('  SAFE-BASSO «%s» y %d' % (b['t'], b['bot']))
            # vuoti: solo dove il fondo e' piatto. Su una foto la fascia libera
            # E' il contenuto (e' l'immagine), e nelle scene del reel la riga
            # unica al centro ottico e' il formato stesso: li' il controllo 3 non
            # si applica.
            su_foto = '<img' in page.content()
            e_reel = nome.startswith('R')
            if su_foto or e_reel:
                if righe:
                    problemi += len(righe)
                    print('%s (%dx%d)' % (nome, m['w'], m['h']))
                    print('\n'.join(righe))
                continue
            # vuoti: fasce libere nell'area utile
            occupati = sorted([(b['top'], b['bot']) for b in m['box'] if b['t'] or b['bot'] - b['top'] < 400])
            limite_alto = 180 if h == 1920 else 64
            limite_basso = (h - 320) if h == 1920 else (h - 64)
            cur = limite_alto
            for a, b in occupati:
                if a - cur > 260:
                    righe.append('  VUOTO     %d px fra y %d e y %d' % (a - cur, cur, a))
                cur = max(cur, b)
            if limite_basso - cur > 260:
                righe.append('  VUOTO     %d px fra y %d e y %d' % (limite_basso - cur, cur, limite_basso))
            altezze[nome] = [(b['top'], b['bot']) for b in m['box']]
            if righe:
                problemi += len(righe)
                print('%s (%dx%d)' % (nome, m['w'], m['h']))
                print('\n'.join(righe))
        # altezza identica dei blocchi di confronto
        for nome in ('C3', 'C4'):
            page.goto('file://' + os.path.join(HERE, nome + '.dc.html'))
            page.wait_for_timeout(400)
            hs = page.evaluate("""() => [...document.querySelectorAll('.frame > div')]
                .map(d => Math.round(d.getBoundingClientRect().height))
                .filter(h => h > 200 && h < 400)""")
            ok = len(set(hs)) <= 1
            print('%s  blocchi di confronto: %s  %s' % (nome, hs, 'IDENTICI' if ok else 'DISUGUALI'))
            if not ok:
                problemi += 1
        browser.close()
    print('\n%s' % ('NESSUN PROBLEMA' if problemi == 0 else '%d PROBLEMI' % problemi))
    return 0 if problemi == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
