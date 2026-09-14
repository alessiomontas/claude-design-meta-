"""Renderizza le artboard .dc.html di una giornata in PNG.

    python3 .claude/skills/giornata/render.py campagne/giornaliero/<AAAA-MM-GG>

Legge grafiche/canvas.json, apre ogni .dc.html in Chromium alla dimensione
esatta dell'artboard e salva lo screenshot in png/. Serve per i sei controlli
di qualita' di master-template.md, che si fanno sul PNG renderizzato.
"""
import json
import os
import sys

from playwright.sync_api import sync_playwright


def main(giorno):
    grafiche = os.path.join(giorno, 'grafiche')
    png_dir = os.path.join(giorno, 'png')
    os.makedirs(png_dir, exist_ok=True)

    with open(os.path.join(grafiche, 'canvas.json')) as f:
        artboards = json.load(f)['artboards']

    with sync_playwright() as p:
        # Il Chromium preinstallato puo' avere un numero di build diverso da
        # quello che si aspetta la libreria: si punta al binario presente
        # invece di scaricarne un altro.
        import glob
        cands = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
        browser = p.chromium.launch(executable_path=cands[-1]) if cands else p.chromium.launch()
        for ab in artboards:
            page = browser.new_page(viewport={'width': ab['w'], 'height': ab['h']},
                                    device_scale_factor=1)
            page.goto('file://' + os.path.abspath(os.path.join(grafiche, ab['file'])))
            page.wait_for_timeout(1200)  # webfont Archivo/Manrope
            out = os.path.join(png_dir, ab['file'].replace('.dc.html', '.png'))
            page.locator('.frame').screenshot(path=out)
            page.close()
            print('%-16s -> %s' % (ab['file'], out))
        browser.close()
    print('\n%d PNG in %s' % (len(artboards), png_dir))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
