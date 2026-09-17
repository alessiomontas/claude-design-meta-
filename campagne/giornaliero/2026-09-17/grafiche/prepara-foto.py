# -*- coding: utf-8 -*-
"""Preparazione delle foto reali prima che entrino nelle artboard.

Due lavori, in quest'ordine:

1. **Marchi di terzi** (controllo 6 di master-template.md). La foto
   `brand-assets/immobili/cucina-soggiorno-open-space.png` porta due diciture
   leggibili — `KOENIC` sul tostapane e `PHILIPS` sul bollitore. In un contenuto
   di acquisizione clienti non ci vanno: si lavora su una COPIA
   (`fonte-cucina-pulita.png`), l'originale in `brand-assets/` non si tocca.
   La toppa e' un pezzo della stessa superficie presa poco sopra/sotto, incollata
   con bordo sfumato: l'acciaio e' un gradiente liscio, la giunzione non si vede.

2. **Ritagli sul formato esatto del canale**, dalle sorgenti pulite.

    python3 prepara-foto.py
"""
import os

from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'brand-assets'))

# (regione da coprire, spostamento da cui prendere la toppa)
# Il bordo sfumato non deve mai mangiarsi il centro della toppa: con una
# fascia bassa (la scritta del bollitore) una sfumatura larga lascia passare
# l'originale in trasparenza. Sfumatura piccola, riquadro largo.
# Due modi, perche' i due oggetti non hanno lo stesso intorno.
#  'toppa'  — si incolla un pezzo di superficie presa poco sopra: va bene dove
#             sopra la scritta c'e' altro acciaio (tostapane).
#  'sfuma'  — si ricostruisce la fascia interpolando riga per riga fra la riga
#             sopra e la riga sotto: sul bollitore e' l'unico modo, perche'
#             sopra c'e' il muro con la placca e sotto le foglie della pianta,
#             e qualunque toppa porterebbe dentro un pezzo di scena.
MARCHI = [
    ('toppa', (2504, 1528, 2590, 1586), (0, -80), 8),   # KOENIC, tostapane
    ('sfuma', (3186, 1466, 3276, 1516), None, 0),       # PHILIPS, bollitore
]


def togli_marchio(im, modo, box, dx_dy, sfuma=8):
    x0, y0, x1, y1 = box
    if modo == 'toppa':
        dx, dy = dx_dy
        toppa = im.crop((x0 + dx, y0 + dy, x1 + dx, y1 + dy))
        m = Image.new('L', toppa.size, 0)
        m.paste(255, (sfuma, sfuma, toppa.size[0] - sfuma, toppa.size[1] - sfuma))
        im.paste(toppa, (x0, y0), m.filter(ImageFilter.GaussianBlur(sfuma)))
        return im

    # 'sfuma': l'acciaio ha un gradiente ORIZZONTALE e su questa fascia e'
    # uniforme in verticale. Colonna per colonna si interpola fra la riga
    # sopra e quella sotto: il gradiente resta, la scritta sparisce.
    px = im.load()
    sopra, sotto = y0 - 6, y1 + 6
    h = sotto - sopra
    for x in range(x0, x1):
        ca, cb = px[x, sopra], px[x, sotto]
        for y in range(y0, y1):
            t = (y - sopra) / h
            px[x, y] = tuple(int(ca[i] + (cb[i] - ca[i]) * t) for i in range(3))
    # un filo di sfocatura sui bordi della fascia ricostruita
    reg = im.crop((x0 - 6, y0 - 6, x1 + 6, y1 + 6)).filter(ImageFilter.GaussianBlur(1.6))
    im.paste(reg, (x0 - 6, y0 - 6))
    return im


def crop(im, out, W, H, anchor=0.5, vanchor=0.5):
    w, h = im.size
    tr = W / H
    if w / h > tr:
        nw = int(h * tr); x = int((w - nw) * anchor); box = (x, 0, x + nw, h)
    else:
        nh = int(w / tr); y = int((h - nh) * vanchor); box = (0, y, w, y + nh)
    im.crop(box).resize((W, H), Image.LANCZOS).save(out, quality=92)
    print('%-26s %dx%d' % (os.path.basename(out), W, H))


def main():
    cucina = Image.open(os.path.join(BRAND, 'immobili', 'cucina-soggiorno-open-space.png')).convert('RGB')
    for modo, box, d, sf in MARCHI:
        cucina = togli_marchio(cucina, modo, box, d, sf)
    pulita = os.path.join(HERE, 'fonte-cucina-pulita.png')
    cucina.save(pulita)
    print('fonte-cucina-pulita.png  (KOENIC e PHILIPS rimossi)')

    crop(cucina, os.path.join(HERE, 'foto-cucina-4x5.jpg'), 1080, 1350, 0.55)
    crop(cucina, os.path.join(HERE, 'foto-cucina-1x1.jpg'), 1080, 1080, 0.50)
    crop(cucina, os.path.join(HERE, 'foto-cucina-9x16.jpg'), 1080, 1920, 0.55)

    tram = Image.open(os.path.join(BRAND, 'ambientazione', 'tramonto-litorale-romano.jpg')).convert('RGB')
    crop(tram, os.path.join(HERE, 'foto-tramonto-9x16.jpg'), 1080, 1920, 0.5, 0.5)

    balc = Image.open(os.path.join(BRAND, 'immobili', 'balcone-terrazzo.jpeg')).convert('RGB')
    crop(balc, os.path.join(HERE, 'foto-balcone-4x5.jpg'), 1080, 1350, 0.5, 0.35)


if __name__ == '__main__':
    main()
