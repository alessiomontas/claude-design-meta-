"""Monta il reel di una giornata partendo dai PNG delle battute.

    python3 .claude/skills/giornata/monta_reel.py campagne/giornaliero/<AAAA-MM-GG>

Legge reel/battute.json — [["Main", 2.6], ["R1b2", 1.4], ...], cioe' il nome
del PNG in png/ e la durata in secondi, nell'ordine della tabella "Battute"
di copy.md — e produce un MP4 9:16 pronto per Instagram e Facebook.

Nota sull'ambiente: l'ffmpeg incluso in Playwright e' una build ridotta che
codifica solo VP8/WebM, che Instagram non accetta in caricamento. Qui si usa
quello di imageio-ffmpeg, che ha libx264 (`pip install imageio-ffmpeg`).
"""
import json
import os
import subprocess
import sys

import imageio_ffmpeg


def main(giorno):
    reel_dir = os.path.join(giorno, 'reel')
    png_dir = os.path.abspath(os.path.join(giorno, 'png'))
    with open(os.path.join(reel_dir, 'battute.json')) as f:
        battute = json.load(f)

    righe = []
    for nome, durata in battute:
        righe.append("file '%s'" % os.path.join(png_dir, nome + '.png'))
        righe.append('duration %.3f' % durata)
    # Il demuxer concat ignora la durata dell'ultima voce: si ripete il frame.
    righe.append("file '%s'" % os.path.join(png_dir, battute[-1][0] + '.png'))
    lista = os.path.join(reel_dir, 'scene.txt')
    with open(lista, 'w') as f:
        f.write('\n'.join(righe) + '\n')

    out = os.path.join(reel_dir, 'reel.mp4')
    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error',
           '-f', 'concat', '-safe', '0', '-i', lista,
           '-vf', 'fps=30,format=yuv420p',
           '-c:v', 'libx264', '-preset', 'medium', '-crf', '19',
           '-movflags', '+faststart', out]
    subprocess.run(cmd, check=True)
    durata = sum(d for _, d in battute)
    print('%s — %.1f s su %d battute' % (out, durata, len(battute)))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
