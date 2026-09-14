"""Renderizza un reel ANIMATO da una pagina HTML, fotogramma per fotogramma.

    python3 .claude/skills/giornata/anima_reel.py <pagina.html> <uscita.mp4> [durata_s] [fps]

Perche' esiste: montare PNG fermi con il demuxer concat produce una
presentazione, non un reel — nessun movimento dentro la scena. Qui la pagina
HTML porta l'animazione vera (movimento di camera sulle foto, tipografia in
movimento, tendine), e questo script la "scrubba" come una timeline.

Come funziona: ogni animazione CSS dura quanto l'intero reel e usa
`animation-fill-mode: both`, quindi lo stato a un istante t e' deterministico.
Lo script mette in pausa tutte le animazioni della pagina, porta `currentTime`
a t per ognuna, scatta il fotogramma, e passa al successivo. Niente
registrazione in tempo reale: nessun fotogramma perso, nessun jitter.

Il sonoro non si aggiunge qui: le tracce musicali hanno una licenza, e si
mettono in fase di pubblicazione (Instagram ha la propria libreria).
"""
import glob
import os
import subprocess
import sys
import tempfile

import imageio_ffmpeg
from playwright.sync_api import sync_playwright

LARGHEZZA, ALTEZZA = 1080, 1920


def chromium():
    c = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    return c[-1] if c else None


def main(pagina, uscita, durata=15.0, fps=30):
    n = int(round(durata * fps))
    tmp = tempfile.mkdtemp(prefix='reel-')

    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chromium())
        pg = b.new_page(viewport={'width': LARGHEZZA, 'height': ALTEZZA},
                        device_scale_factor=1)
        pg.goto('file://' + os.path.abspath(pagina))
        pg.wait_for_timeout(1500)  # webfont + decodifica immagini

        n_anim = pg.evaluate('document.getAnimations().length')
        if not n_anim:
            print('ATTENZIONE: nessuna animazione CSS trovata nella pagina — '
                  'uscirebbe di nuovo un fermo immagine.', file=sys.stderr)

        for i in range(n):
            t = (i / fps) * 1000.0
            pg.evaluate("""(t) => {
                for (const a of document.getAnimations()) {
                    a.pause();
                    a.currentTime = t;
                }
            }""", t)
            pg.screenshot(path=os.path.join(tmp, 'f%05d.png' % i), animations='disabled')
        b.close()

    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error',
           '-framerate', str(fps), '-i', os.path.join(tmp, 'f%05d.png'),
           '-vf', 'format=yuv420p', '-c:v', 'libx264', '-preset', 'slow',
           '-crf', '18', '-movflags', '+faststart', uscita]
    subprocess.run(cmd, check=True)
    print('%s — %d fotogrammi, %.1f s a %d fps, %d animazioni'
          % (uscita, n, durata, fps, n_anim))


if __name__ == '__main__':
    a = sys.argv[1:]
    main(a[0], a[1], float(a[2]) if len(a) > 2 else 15.0, int(a[3]) if len(a) > 3 else 30)
