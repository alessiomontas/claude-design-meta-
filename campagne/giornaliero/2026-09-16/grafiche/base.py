# -*- coding: utf-8 -*-
"""Libreria della variante CHIARA (fondo bianco caldo).

Regola che governa tutto il file: sul chiaro l'oro #C8A24B da' 2,25:1 e come
testo non si legge. Resta quindi solo SUPERFICIE (banda CTA, celle piene,
fili, bordi); le parole in oro usano ORO_INK #86692A, che da' 4,8:1.
Corollario: niente veli e niente text-shadow — su fondo chiaro sporcano.
"""

FONDO     = '#FAF7F1'   # bianco caldo, mai #FFFFFF
CARD      = '#F5F0E6'   # sabbia
INK       = '#2E2A25'   # titoli
INK_CORPO = '#3F3A33'
INK_2     = '#5A5349'   # secondario, minimo per il testo piccolo
ORO       = '#C8A24B'   # SOLO riempimento
ORO_INK   = '#86692A'   # l'oro quando e' testo
LINEA     = 'rgba(46,42,37,0.14)'

AR = "'Archivo', 'Helvetica Neue', Arial, sans-serif"
MA = "'Manrope', 'Helvetica Neue', Arial, sans-serif"

HEAD = """<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; }
  </style>
</head>
<body>
"""
FOOT = "</body>\n</html>\n"


def frame(w, h, bg=FONDO):
    # La classe .frame e' quella che render.py aspetta per ritagliare l'artboard.
    return ('  <div class="frame" style="position: relative; width: %dpx; height: %dpx; '
            'overflow: hidden; background: %s;">\n' % (w, h, bg))


def chiudi():
    return '  </div>\n'


def foto(src, y, h, x=0, w=1080, raggio=0):
    """Sul chiaro la foto e' un BLOCCO accanto al testo, non un fondo sotto."""
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; width: %dpx; '
            'height: %dpx; overflow: hidden; border-radius: %dpx;">'
            '<img src="%s" style="width: 100%%; height: 100%%; object-fit: cover; display: block;">'
            '</div>\n' % (x, y, w, h, raggio, src))


def marchio(y=100, colore=INK, allinea='center'):
    return ('  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: %s;">'
            '<div style="font-family: %s; font-weight: 800; font-size: 33px; letter-spacing: 9px; '
            'color: %s;">HADRIANUS</div>'
            '<div style="font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 7px; '
            'color: %s; margin-top: 12px;">MULTISERVICE</div></div>\n'
            % (y, allinea, AR, colore, MA, INK_2))


def blocco(righe, y, size, peso, colore=INK, font=AR, allinea='left',
           lh=1.14, tracking=-0.4, left=64, right=64):
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'text-align: %s; font-family: %s; font-weight: %d; font-size: %dpx; '
            'line-height: %s; letter-spacing: %spx; color: %s;">%s</div>\n'
            % (left, right, y, allinea, font, peso, size, lh, tracking, colore, corpo))


def kicker(testo, y, colore=ORO_INK, left=64, size=29, peso=700):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; font-family: %s; '
            'font-weight: %d; font-size: %dpx; letter-spacing: 0.22em; text-transform: uppercase; '
            'color: %s;">%s</div>\n' % (left, y, AR, peso, size, colore, testo))


def filo(y, larghezza=220, colore=ORO, left=64, h=3):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; width: %dpx; '
            'height: %dpx; background: %s;"></div>\n' % (left, y, larghezza, h, colore))


def pill(y, h, testo, size=45, left=64, right=64):
    """Oro pieno con inchiostro fume' sopra: 5,9:1, l'unico uso corretto
    dell'oro acceso sul chiaro."""
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
            'background: %s; border-radius: 999px; display: flex; align-items: center; '
            'justify-content: center; font-family: %s; font-weight: 800; font-size: %dpx; '
            'letter-spacing: 0.02em; color: %s;">%s</div>\n'
            % (left, right, y, h, ORO, AR, size, INK, testo.upper()))


def badge(y, testo, left=64, size=32, h=64):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; height: %dpx; '
            'display: inline-flex; align-items: center; padding: 0 30px; border-radius: %dpx; '
            # Oro PIENO con inchiostro fume': a contorno si leggeva beige su beige.
            'background: %s; font-family: %s; '
            'font-weight: 800; font-size: %dpx; color: %s;">%s</div>\n'
            % (left, y, h, h // 2, ORO, AR, size, INK, testo))


def modulo(y, voci, altezza=124, gap=14, left=64, right=64, size=38, casella=250):
    """LA FIRMA DEL GIORNO — "il modulo a caselle vuote".

    Ogni voce e' una riga su fondo sabbia con, a destra, una casella VUOTA
    bordata d'oro: il numero non lo mettiamo noi, lo scrive il lettore coi suoi
    bollettini. E' l'opposto del pattern scontrino gia' usato, che chiudeva su
    un totale: qui il totale non esiste apposta, ed e' il senso del contenuto.
    """
    out = ''
    for i, (voce, nota) in enumerate(voci):
        top = y + i * (altezza + gap)
        nota_html = ('<div style="font-family: %s; font-weight: 500; font-size: 26px; '
                     'color: %s; margin-top: 7px;">%s</div>' % (MA, INK_2, nota)) if nota else ''
        out += ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
                'height: %dpx; background: %s; border-radius: 18px; padding: 0 28px; '
                'display: flex; align-items: center; justify-content: space-between; gap: 22px;">'
                '<div><div style="font-family: %s; font-weight: 800; font-size: %dpx; color: %s;">%s</div>%s</div>'
                '<div style="flex: 0 0 %dpx; height: %dpx; border: 3px solid %s; border-radius: 12px; '
                'background: %s;"></div>'
                '</div>\n' % (left, right, top, altezza, CARD, AR, size, INK, voce, nota_html,
                              casella, int(altezza * 0.52), ORO, FONDO))
    return out


def elenco_voci_brevi(y, voci, altezza=104, gap=12, left=64, right=64):
    """Versione corta del modulo, senza campo euro: la storia non e' il posto
    dove si compila, e ripetere il modulo per la terza volta lo svuotava."""
    out = ''
    for i, (voce, det) in enumerate(voci):
        out += ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
                'height: %dpx; background: %s; border-radius: 18px; padding: 0 28px; '
                'display: flex; flex-direction: column; justify-content: center; gap: 5px;">'
                '<span style="font-family: %s; font-weight: 800; font-size: 40px; color: %s;">%s</span>'
                '<span style="font-family: %s; font-weight: 500; font-size: 27px; color: %s;">%s</span>'
                '</div>\n' % (left, right, y + i * (altezza + gap), altezza, CARD,
                              AR, INK, voce, MA, INK_2, det))
    return out


def fonte(testo, y, left=64, size=22):
    return ('  <div style="position: absolute; left: %dpx; right: 64px; top: %dpx; '
            'font-family: %s; font-weight: 500; font-size: %dpx; color: %s;">%s</div>\n'
            % (left, y, MA, size, INK_2, testo))


def scrivi(percorso, corpo):
    with open(percorso, 'w') as f:
        f.write(HEAD + corpo + chiudi() + FOOT)
