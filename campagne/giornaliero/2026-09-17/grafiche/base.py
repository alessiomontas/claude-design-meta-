# -*- coding: utf-8 -*-
"""Libreria della giornata 17/09/2026 — variante FUME' scura.

FIRMA DEL GIORNO: **lo scalino**.

Il contenuto mette a confronto due mesi. La tabella a due colonne e' vietata dal
copy, e tutti i pattern gia' usati (calendario a 12 caselle, scontrino, blocchi
invertiti, frase al centro, barra, spazio vuoto misurato, step numerati giganti,
card Q&A) sono bruciati. Qui il confronto non si mette affianco: si mette
**sotto e rientrato**. AGOSTO sta sulla linea di base, NOVEMBRE e' un pannello
che rientra di 72 px, poggia su fondo oro velato e ha una **stecca oro verticale
di 3 px** sul suo bordo sinistro. Leggendo dall'alto si scende uno scalino.

Due conseguenze volute:

1. **Nessun filo oro orizzontale in tutto il pacchetto.** La stecca oro e'
   sempre verticale, sempre nella gronda a sinistra di un pannello, mai sopra o
   sotto una riga: e' l'unico modo per non ripetere il difetto della riga oro
   che taglia una parola come una cancellatura.
2. **Omogeneita'.** Tutti gli scalini di una stessa artboard hanno identico
   fondo, identica stecca, identico rientro, identica altezza. Il testo di
   NOVEMBRE va SEMPRE su due righe spezzate a mano (`nowrap`), cosi' l'altezza
   non dipende dal numero di caratteri e tre blocchi restano alti uguali.
"""

FUME_DEEP = '#2E2A25'
FUME      = '#3F3A33'
FUME_MID  = '#4a443a'
ORO       = '#C8A24B'
ORO_SCURO = '#a8863b'
SABBIA    = '#F5F0E6'
BIANCO    = '#FFFFFF'

T1 = 'rgba(255,255,255,0.88)'   # corpo su fume'
T2 = 'rgba(255,255,255,0.72)'   # riga AGOSTO
T3 = 'rgba(255,255,255,0.55)'   # etichetta AGOSTO
T4 = 'rgba(255,255,255,0.60)'   # fonti

GROUND_A = 'rgba(255,255,255,0.06)'   # la base: agosto
GROUND_N = 'rgba(200,162,75,0.10)'    # lo scalino: novembre

AR = "'Archivo', 'Helvetica Neue', Arial, sans-serif"
MA = "'Manrope', 'Helvetica Neue', Arial, sans-serif"

OMBRA = ('text-shadow: 0 3px 10px rgba(0,0,0,0.60), 0 12px 44px rgba(0,0,0,0.45), '
         '0 1px 2px rgba(0,0,0,0.80);')

# Lock di brand sulle foto: senza, i verdi e i bianchi freddi dominano e la
# grafica legge "smunta" (difetto gia' bocciato dal titolare).
FILTRO_FOTO = 'saturate(0.72) sepia(0.14) brightness(0.90) contrast(1.06)'

HEAD = """<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; font-family: 'Manrope', system-ui, sans-serif; }
    a { color: #C8A24B; } a:hover { color: #a8863b; }
  </style>
</helmet>
"""
FOOT = "</x-dc>\n</body>\n</html>\n"

GRAD_BASE = ('radial-gradient(ellipse 84%% 42%% at 50%% 24%%, rgba(200,162,75,0.10), transparent 70%%), '
             'linear-gradient(180deg, %s 0%%, %s 48%%, %s 100%%)' % (FUME_MID, FUME, FUME_DEEP))


def frame(w, h, bg=FUME):
    return ('  <div class="frame" style="position: relative; width: %dpx; height: %dpx; '
            'overflow: hidden; background: %s;">\n' % (w, h, bg))


def chiudi():
    return '  </div>\n'


def strato(css):
    return '  <div style="position: absolute; inset: 0; background: %s;"></div>\n' % css


def foto(src):
    return ('  <img src="%s" alt="" style="position: absolute; inset: 0; width: 100%%; '
            'height: 100%%; object-fit: cover; filter: %s;">\n' % (src, FILTRO_FOTO))


def velo(*strati):
    return strato(', '.join(strati))


# --------------------------------------------------------------- marchio
def marchio(y=112, x=64, colore=BIANCO, ombra=False):
    """Allineato a sinistra: il 14 e il 15/09 lo avevano centrato, e la colonna
    unica a sinistra e' il primo segnale che questa e' un'altra giornata."""
    sh = OMBRA if ombra else ''
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; font-family: %s; '
            'font-weight: 800; font-size: 33px; letter-spacing: 9px; color: %s; %s">HADRIANUS</div>\n'
            '  <div style="position: absolute; left: %dpx; top: %dpx; font-family: %s; '
            'font-weight: 600; font-size: 17px; letter-spacing: 7px; color: %s; %s">MULTISERVICE</div>\n'
            % (x, y, AR, colore, sh, x, y + 48, MA,
               'rgba(255,255,255,0.72)' if colore == BIANCO else colore, sh))


def indice(testo, y, right=64, colore=ORO, ombra=False):
    """L'indice di slide sale in alto a destra, in asse col marchio: sotto, il
    fondo della slide serve alla banda del dato (C4) e alla CTA (C5)."""
    return ('  <div style="position: absolute; right: %dpx; top: %dpx; font-family: %s; '
            'font-weight: 600; font-size: 17px; letter-spacing: 5px; color: %s; %s">%s</div>\n'
            % (right, y, MA, colore, OMBRA if ombra else '', testo))


# ----------------------------------------------------------------- testo
def blocco(righe, y, size, peso, colore=BIANCO, font=None, left=64, right=64,
           lh=1.16, tracking=-0.4, ombra=False, allinea='left'):
    font = font or AR
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'text-align: %s; font-family: %s; font-weight: %d; font-size: %dpx; '
            'line-height: %s; letter-spacing: %spx; color: %s; %s">%s</div>\n'
            % (left, right, y, allinea, font, peso, size, lh, tracking, colore,
               OMBRA if ombra else '', corpo))


def kicker(testo, y, left=64, colore=ORO, size=17, ombra=False):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; font-family: %s; '
            'font-weight: 600; font-size: %dpx; letter-spacing: 0.18em; '
            'text-transform: uppercase; color: %s; %s">%s</div>\n'
            % (left, y, MA, size, colore, OMBRA if ombra else '', testo))


def fonte(testo, y, left=64, right=64, size=17, colore=T4):
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'font-family: %s; font-weight: 500; font-size: %dpx; line-height: 1.4; '
            'color: %s;">%s</div>\n' % (left, right, y, MA, size, colore, testo))


# --------------------------------------------------------------- scalino
def _riga_mese(tag, righe, size, peso, colore_tag, colore_testo, font=None):
    """Etichetta di mese e testo sulla stessa linea di base. Ogni riga e' un
    div `nowrap`: l'altezza del blocco diventa cosi' un fatto di geometria, non
    di conteggio caratteri (ed e' misurabile, vedi verifica.py)."""
    font = font or AR
    corpo = ''.join('<div style="white-space: nowrap;">%s</div>' % r for r in righe)
    return ('<div style="display: flex; align-items: baseline; gap: 18px;">'
            '<span style="flex: 0 0 auto; font-family: %s; font-weight: 600; font-size: 17px; '
            'letter-spacing: 0.18em; text-transform: uppercase; color: %s;">%s</span>'
            '<div style="flex: 1; min-width: 0; font-family: %s; font-weight: %d; '
            'font-size: %dpx; line-height: 1.26; letter-spacing: -0.4px; color: %s;">%s</div>'
            '</div>' % (MA, colore_tag, tag, font, peso, size, colore_testo, corpo))


def gradino(y, kick, ago, nov, left=64, right=64, h=264, indent=72,
            size_ago=33, size_nov=33, peso_ago=800, peso_nov=900):
    """LO SCALINO — il blocco di confronto della giornata.

    `ago` e' una riga sola, `nov` sono SEMPRE due righe: e' quello che tiene
    identica l'altezza dei tre blocchi di C3 e C4 (il punto lasciato aperto dal
    copywriter). Il corpo resta a 33: a 40 le voci «Novembre» andavano a capo
    in modo diseguale.
    """
    pad = 34
    top_kick = 24
    top_ago = top_kick + 22 + 16
    h_pannello = 18 + int(size_nov * 1.26) * 2 + 18
    top_nov = h - 22 - h_pannello
    return (
        '  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
        'background: %s; border-radius: 22px; overflow: hidden;">'
        # etichetta del criterio
        '<div style="position: absolute; left: %dpx; top: %dpx; font-family: %s; font-weight: 600; '
        'font-size: 17px; letter-spacing: 0.18em; text-transform: uppercase; color: %s;">%s</div>'
        # la base: agosto
        '<div style="position: absolute; left: %dpx; right: %dpx; top: %dpx;">%s</div>'
        # lo scalino: novembre, rientrato, fondo oro velato, stecca oro verticale
        '<div style="position: absolute; left: %dpx; right: 0; top: %dpx; height: %dpx; '
        'background: %s; border-radius: 16px 0 0 16px; border-left: 3px solid %s; '
        'padding: 18px 34px 18px 26px;">%s</div>'
        '</div>\n'
        % (left, right, y, h, GROUND_A,
           pad, top_kick, MA, ORO, kick,
           pad, pad, top_ago,
           _riga_mese('Agosto', [ago], size_ago, peso_ago, T3, T2),
           indent, top_nov, h_pannello, GROUND_N, ORO,
           _riga_mese('Novembre', nov, size_nov, peso_nov, ORO, BIANCO)))


def scalino(y, righe, left=64, right=64, indent=72, size=33, peso=600,
            font=None, colore=BIANCO, pad_v=24, lh=1.32, tag=None, h=None):
    """Lo scalino SENZA confronto: un pannello rientrato con stecca oro.

    E' la firma che torna su ogni artboard del pacchetto, anche dove non ci sono
    due mesi da mettere a fronte: la riga che conta sta sempre un gradino piu'
    dentro delle altre.
    """
    font = font or MA
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    testa = ''
    if tag:
        testa = ('<div style="font-family: %s; font-weight: 600; font-size: 17px; '
                 'letter-spacing: 0.18em; text-transform: uppercase; color: %s; '
                 'margin-bottom: 12px;">%s</div>' % (MA, ORO, tag))
    altezza = (' height: %dpx;' % h) if h else ''
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx;%s '
            'background: %s; border-left: 3px solid %s; border-radius: 16px; '
            'padding: %dpx 34px %dpx 27px;">%s'
            '<div style="font-family: %s; font-weight: %d; font-size: %dpx; line-height: %s; '
            'letter-spacing: -0.3px; color: %s;">%s</div></div>\n'
            % (left + indent, right, y, altezza, GROUND_N, ORO, pad_v, pad_v,
               testa, font, peso, size, lh, colore, corpo))


def banda(y, h, testo_sx, righe_dx, fonte_dx, left=64, right=64, size_num=62,
          size_riga=31):
    """La banda del dato: numero a sinistra, frase e fonte a destra, tutto
    dentro la stessa superficie oro. Il 61,5% non deve mai poter essere letto
    come occupazione di Hadrianus: numero, frase e fonte non si separano."""
    dx = ''.join('<div>%s</div>' % r for r in righe_dx)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
            'background: %s; border-radius: 22px; padding: 0 36px; display: flex; '
            'align-items: center; gap: 30px;">'
            '<span style="flex: 0 0 auto; font-family: %s; font-weight: 900; font-size: %dpx; '
            'letter-spacing: -1.5px; color: %s;">%s</span>'
            '<span style="flex: 1; min-width: 0;">'
            '<span style="display: block; font-family: %s; font-weight: 700; font-size: %dpx; '
            'line-height: 1.2; letter-spacing: -0.3px; color: %s;">%s</span>'
            '<span style="display: block; font-family: %s; font-weight: 500; font-size: 17px; '
            'line-height: 1.35; color: rgba(46,42,37,0.74); margin-top: 10px;">%s</span>'
            '</span></div>\n'
            % (left, right, y, h, ORO, AR, size_num, FUME_DEEP, testo_sx,
               MA, size_riga, FUME_DEEP, dx, MA, fonte_dx))


def cta_banda(y, testo, h=88, left=64, right=64, size=31):
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
            'background: %s; border-radius: 18px; display: flex; align-items: center; '
            'justify-content: center; font-family: %s; font-weight: 600; font-size: %dpx; '
            'letter-spacing: 0.14em; text-transform: uppercase; color: %s;">%s</div>\n'
            % (left, right, y, h, ORO, MA, size, FUME_DEEP, testo))


def cta_pillola(y, testo, h=88, left=64, right=64, size=31):
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
            'background: %s; border-radius: 999px; display: flex; align-items: center; '
            'justify-content: center; font-family: %s; font-weight: 600; font-size: %dpx; '
            'letter-spacing: 0.14em; text-transform: uppercase; color: %s;">%s</div>\n'
            % (left, right, y, h, ORO, MA, size, FUME_DEEP, testo))


def freccia(y, right=64, size=44, colore=ORO):
    return ('  <div style="position: absolute; right: %dpx; top: %dpx; font-family: %s; '
            'font-weight: 800; font-size: %dpx; color: %s;">&#8594;</div>\n'
            % (right, y, AR, size, colore))


def scrivi(percorso, corpo):
    with open(percorso, 'w') as f:
        f.write(HEAD + corpo + chiudi() + FOOT)
