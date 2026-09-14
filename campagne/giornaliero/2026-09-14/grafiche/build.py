# Generatore artboard .dc.html — pacchetto giornaliero 14/09/2026
# Impianto: "il binario delle scadenze" (marca temporale in alto + arco che si chiude)
# Le y provengono dalle tabelle LAYOUT di copy.md. Ogni blocco è ancorato al
# centro ottico della sua fascia (top = centro, translateY(-50%)).
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- palette
FUME       = '#3F3A33'
FUME_DEEP  = '#2E2A25'
FUME_MID   = '#4a443a'
ORO        = '#C8A24B'
ORO_SCURO  = '#b3892f'
SABBIA     = '#F5F0E6'
T_SCURO    = '#26241F'
T_SCURO_2  = '#46423a'
T_SCURO_3  = '#6f695c'
T_CHIARO   = '#d8d2c4'
T_CHIARO_2 = '#b7ad9a'
T_CHIARO_3 = '#9a8f7c'
BIANCO     = '#FFFFFF'

GRAD_SCURO = ('radial-gradient(120%% 80%% at 50%% 10%%, %s 0%%, %s 55%%, %s 100%%)'
              % (FUME_MID, FUME, FUME_DEEP))

OMBRA = ('text-shadow: 0 3px 10px rgba(0,0,0,0.68), 0 12px 44px rgba(0,0,0,0.55), '
         '0 1px 2px rgba(0,0,0,0.85);')

HEAD = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
  <style>
    body { margin: 0; font-family: 'Manrope', system-ui, sans-serif; }
    a { color: #C8A24B; } a:hover { color: #a8863b; }
  </style>
</helmet>
"""
FOOT = """</div>
</x-dc>
</body>
</html>
"""

AR = "'Archivo', 'Helvetica Neue', Arial, sans-serif"
MA = "'Manrope', 'Helvetica Neue', Arial, sans-serif"


def frame(w, h, bg):
    return ('<div class="frame" style="width: %dpx; height: %dpx; box-sizing: border-box; '
            'position: relative; background: %s; overflow: hidden;">\n' % (w, h, bg))


def foto(src):
    # Lock di brand: le foto vanno portate sul fumè caldo prima del velo, altrimenti
    # i verdi e i bianchi freddi dominano e la grafica legge "smunta".
    return ('  <img src="%s" alt="" style="position: absolute; inset: 0; width: 100%%; '
            'height: 100%%; object-fit: cover; '
            'filter: saturate(0.72) sepia(0.14) brightness(0.90) contrast(1.06);">\n' % src)


def velo(*strati):
    return ('  <div style="position: absolute; inset: 0; background: %s;"></div>\n'
            % ', '.join(strati))


# ------------------------------------------------------- marchio (lockup)
def marchio(y_h=112, y_m=176, colore=BIANCO, ombra=True, size_h=33, size_m=17):
    sh = OMBRA if ombra else ''
    op = 'rgba(255,255,255,0.86)' if colore == BIANCO else colore
    return (
        '  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: center; '
        'font-family: %s; font-weight: 800; font-size: %dpx; letter-spacing: 10px; color: %s; %s">'
        '<span style="margin-right: -10px; display: inline-block;">HADRIANUS</span></div>\n'
        '  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: center; '
        'font-family: %s; font-weight: 600; font-size: %dpx; letter-spacing: 7px; color: %s; %s">'
        '<span style="margin-right: -7px; display: inline-block;">MULTISERVICE</span></div>\n'
        % (y_h, AR, size_h, colore, sh, y_m, MA, size_m, op, sh))


# ---------------------------------------------- marca temporale (la firma)
def marca(testo, y, allinea='left', colore=ORO, ombra=False, x=64):
    """Marca temporale: 17px Manrope 600 maiuscolo tracking 8 + trattino oro."""
    sh = OMBRA if ombra else ''
    rule = ('<span style="display: inline-block; width: 28px; height: 2px; background: %s; '
            'vertical-align: middle; margin-bottom: 4px;"></span>' % colore)
    txt = ('<span style="font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 8px; '
           'text-transform: uppercase; color: %s; vertical-align: middle; %s">'
           '<span style="margin-right: -8px; display: inline-block;">%s</span></span>'
           % (MA, colore, sh, testo))
    if allinea == 'right':
        inner = txt + '<span style="display:inline-block; width: 18px;"></span>' + rule
        side = 'right: %dpx; text-align: right;' % x
        pos = 'left: 64px; %s' % side
    else:
        inner = rule + '<span style="display:inline-block; width: 18px;"></span>' + txt
        pos = 'left: %dpx; right: 64px; text-align: left;' % x
    return ('  <div style="position: absolute; %s top: %dpx; transform: translateY(-50%%); '
            'line-height: 1;">%s</div>\n' % (pos, y, inner))


# --------------------------------------------------- arco di avanzamento
def arco(n, tot, x, y, d=140, sw=6, colore=ORO, traccia='rgba(245,240,230,0.14)'):
    r = (d - sw) / 2.0
    circ = 2 * 3.141592653589793 * r
    off = circ * (1 - float(n) / tot)
    c = d / 2.0
    return (
        '  <svg width="%d" height="%d" viewBox="0 0 %d %d" style="position: absolute; left: %dpx; '
        'top: %dpx;">\n'
        '    <circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%d"/>\n'
        '    <circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%d" '
        'stroke-linecap="round" stroke-dasharray="%.2f" stroke-dashoffset="%.2f" '
        'transform="rotate(-90 %.1f %.1f)"/>\n'
        '  </svg>\n'
        % (d, d, d, d, x, y, c, c, r, traccia, sw, c, c, r, colore, sw, circ, off, c, c))


def anello_chiuso(x, y, d, sw, colore):
    r = (d - sw) / 2.0
    c = d / 2.0
    return ('  <svg width="%d" height="%d" viewBox="0 0 %d %d" style="position: absolute; left: %dpx; '
            'top: %dpx;"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" '
            'stroke-width="%d"/></svg>\n' % (d, d, d, d, x, y, c, c, r, colore, sw))


# ------------------------------------------------------------- blocchi di testo
def blocco(righe, y, size, peso, colore, font=AR, allinea='center', lh=1.13,
           ombra=False, tracking=-0.4, left=64, right=64, gap=0):
    """righe: lista di stringhe. Ancorato al centro ottico della fascia."""
    sh = OMBRA if ombra else ''
    fam = AR if font == AR else MA
    corpo = ''
    for i, r in enumerate(righe):
        mt = gap if i else 0
        corpo += ('<div style="margin: %dpx 0 0 0;">%s</div>' % (mt, r))
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'transform: translateY(-50%%); text-align: %s; font-family: %s; font-weight: %d; '
            'font-size: %dpx; line-height: %s; letter-spacing: %spx; color: %s; %s">%s</div>\n'
            % (left, right, y, allinea, fam, peso, size, lh, tracking, colore, sh, corpo))


def pill_oro(y, h, testo, size=40, fondo=ORO, testo_col=FUME_DEEP, anello=None):
    extra = ''
    if anello:
        extra = anello_chiuso(92, y - h // 2 + (h - 44) // 2, 44, 4, 'rgba(46,42,37,0.38)')
    return ('  <div style="position: absolute; left: 64px; right: 64px; top: %dpx; '
            'transform: translateY(-50%%); height: %dpx; box-sizing: border-box; background: %s; '
            'border-radius: 999px; display: flex; align-items: center; justify-content: center; '
            'font-family: %s; font-weight: 800; font-size: %dpx; letter-spacing: 0.4px; '
            'color: %s;">%s</div>\n' % (y, h, fondo, AR, size, testo_col, testo)) + extra


def pill_outline(y, x, w, h, testo):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; transform: translateY(-50%%); '
            'width: %dpx; height: %dpx; box-sizing: border-box; background: rgba(200,162,75,0.16); '
            'border: 2px solid %s; border-radius: 999px; display: flex; align-items: center; '
            'justify-content: center; gap: 18px; font-family: %s; font-weight: 700; font-size: 33px; '
            'color: %s;"><span>%s</span><span style="font-size: 34px;">&rarr;</span></div>\n'
            % (x, y, w, h, ORO, AR, ORO, testo))


def spunta(colore=ORO, d=28):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" '
            'stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" '
            'style="flex: 0 0 auto;"><path d="M20 6L9 17l-5-5"/></svg>' % (d, d, colore))


def scrivi(nome, corpo):
    with open(os.path.join(HERE, nome), 'w') as f:
        f.write(HEAD + corpo + FOOT)
    return nome


# =====================================================================
#  R1 · REEL · 1080x1920 · 9 battute
# =====================================================================
VELO_REEL = [
    'radial-gradient(ellipse 96% 34% at 50% 50%, rgba(26,23,19,0.76) 0%, rgba(26,23,19,0.48) 46%, rgba(26,23,19,0) 68%)',
    'linear-gradient(180deg, rgba(46,42,37,0.90) 0%, rgba(46,42,37,0.44) 34%, rgba(46,42,37,0.52) 62%, rgba(46,42,37,0.92) 100%)',
    'linear-gradient(0deg, rgba(63,58,51,0.34), rgba(63,58,51,0.34))',
]

def binario(t):
    """Binario 322 px a x 379, y 220. t = frazione di 15,4 s trascorsa."""
    w = int(round(322 * t))
    s = ('  <div style="position: absolute; left: 379px; top: 220px; width: 322px; height: 3px; '
         'background: rgba(245,240,230,0.24);"></div>\n')
    if w > 0:
        s += ('  <div style="position: absolute; left: 379px; top: 220px; width: %dpx; height: 3px; '
              'background: %s;"></div>\n' % (w, ORO))
    return s


REEL = [
    # id, immagine, t_fine, righe, kicker
    ('R1b1', 'r-balcone.jpg',  2.6, ['Non ti sanzionano', 'per quanto guadagni.'], 'AFFITTO BREVE'),
    ('R1b2', 'r-balcone.jpg',  4.0, ['Per una casella.'], None),
    ('R1b3', 'r-cucina-a.jpg', 5.4, ['Arriva una prenotazione.'], None),
    ('R1b4', 'r-cucina-b.jpg', 6.8, ['Parte un orologio.'], None),
    ('R1b5', 'n-notte-1.jpg',  8.2, ['Tu domani hai', 'un altro lavoro.'], None),
    ('R1b6', 'n-notte-2.jpg',  9.6, ["L'orologio va avanti", 'lo stesso.'], None),
    ('R1b7', 'n-notte-3.jpg', 11.0, ['E non suona.'], None),
    ('R1b8', 'r-busto.jpg',   13.0, ['Il CIN resta tuo.', "L'orologio", 'lo guardiamo noi.'], None),
    ('R1b9', None,            15.4, ['Gestione completa.', '15% sul fatturato.'], None),
]

def build_reel():
    nomi = []
    for i, (bid, img, tfin, righe, kick) in enumerate(REEL):
        primo = (i == 0)
        nome = 'Main.dc.html' if primo else bid + '.dc.html'
        c = frame(1080, 1920, FUME_DEEP)
        if img:
            c += foto(img)
            c += velo(*VELO_REEL)
        else:
            c += velo(GRAD_SCURO)
            # logo di brand come momento di chiusura
            c += ('  <img src="logo-bronzo.jpg" alt="" style="position: absolute; left: 270px; '
                  'top: 420px; width: 540px; height: 540px; object-fit: cover; '
                  '-webkit-mask-image: radial-gradient(ellipse 58% 58% at 50% 48%, #000 46%, '
                  'rgba(0,0,0,0) 76%); mask-image: radial-gradient(ellipse 58% 58% at 50% 48%, '
                  '#000 46%, rgba(0,0,0,0) 76%);">\n')
        c += marchio()
        c += binario(tfin / 15.4)
        if kick:
            c += ('  <div style="position: absolute; left: 0; right: 0; top: 820px; '
                  'transform: translateY(-50%%); text-align: center; font-family: %s; '
                  'font-weight: 600; font-size: 17px; letter-spacing: 8px; text-transform: uppercase; '
                  'color: %s; %s"><span style="margin-right: -8px; display: inline-block;">%s</span>'
                  '</div>\n' % (MA, ORO, OMBRA, kick))
        centro = 960 if len(righe) > 1 else 960
        c += blocco(righe, centro, 70, 900, BIANCO, allinea='center', ombra=bool(img), gap=0)
        if bid == 'R1b9':
            c += blocco(['GUADAGNIAMO SOLO SE GUADAGNI TU'], 1210, 31, 800, ORO,
                        allinea='center', tracking=2, ombra=False)
            c += ('  <div style="position: absolute; left: 0; right: 0; top: 1330px; '
                  'transform: translateY(-50%%); text-align: center; font-family: %s; '
                  'font-weight: 600; font-size: 31px; letter-spacing: 6px; text-transform: uppercase; '
                  'color: %s;"><span style="margin-right: -6px; display: inline-block;">'
                  'Ne parliamo in DM</span></div>\n' % (MA, SABBIA))
        nomi.append(scrivi(nome, c))
    return nomi


# =====================================================================
#  C1-C5 · CAROSELLO · 1080x1350
# =====================================================================
VELO_C1 = [
    'radial-gradient(ellipse 96% 38% at 50% 52%, rgba(26,23,19,0.74) 0%, rgba(26,23,19,0.46) 48%, rgba(26,23,19,0) 68%)',
    'linear-gradient(180deg, rgba(46,42,37,0.90) 0%, rgba(46,42,37,0.46) 36%, rgba(46,42,37,0.54) 64%, rgba(46,42,37,0.92) 100%)',
    'linear-gradient(0deg, rgba(63,58,51,0.32), rgba(63,58,51,0.32))',
]

ANELLI = [
    "Il CIN nell'annuncio",
    "L'identificazione dell'ospite, de visu",
    'La comunicazione delle generalità entro 24 ore',
    "L'imposta di soggiorno a Roma: incasso e versamento",
    'Il controllo delle dotazioni di sicurezza',
    "L'incasso dei canoni e la certificazione a fine anno",
]


def filo(y, colore='rgba(245,240,230,0.16)', left=64, right=64):
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: 1px; '
            'background: %s;"></div>\n' % (left, right, y, colore))


def chip(testo, y, x=64, w=236, h=66, colore=ORO, fondo='rgba(200,162,75,0.14)', allinea='left'):
    pos = ('left: %dpx;' % x) if allinea == 'left' else ('right: %dpx;' % x)
    return ('  <div style="position: absolute; %s top: %dpx; transform: translateY(-50%%); '
            'width: %dpx; height: %dpx; box-sizing: border-box; background: %s; border: 2px solid %s; '
            'border-radius: 999px; display: flex; align-items: center; justify-content: center; '
            'font-family: %s; font-weight: 800; font-size: 33px; letter-spacing: 1px; color: %s;">'
            '%s</div>\n' % (pos, y, w, h, fondo, colore, AR, colore, testo))


def build_carosello():
    nomi = []

    # ---------------- C1 · T ZERO -------------------------------------
    c = frame(1080, 1350, FUME_DEEP)
    c += foto('c-salotto.jpg')
    c += velo(*VELO_C1)
    c += marchio(80, 138)
    c += marca('T ZERO', 220, ombra=True)
    c += blocco(['Cosa parte davvero', 'quando ricevi', 'una prenotazione.'], 730, 70, 900,
                BIANCO, allinea='left', ombra=True)
    c += blocco(['Sei anelli. Ognuno con la sua scadenza.'], 940, 40, 500, T_CHIARO,
                font=MA, allinea='left', lh=1.25, tracking=0, ombra=True)
    c += pill_outline(1180, 64, 316, 80, 'Scorri')
    c += arco(1, 5, 820, 1120)
    nomi.append(scrivi('C1.dc.html', c))

    # ---------------- C2 · anello 01 ----------------------------------
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD_SCURO)
    c += marchio(80, 138, colore=SABBIA, ombra=False)
    c += marca("01 · PRIMA CHE L'ANNUNCIO SIA ONLINE", 220)
    c += blocco(['Il CIN deve essere', "nell'annuncio.", 'E deve corrispondere.'], 510, 62, 800,
                SABBIA, allinea='left')
    c += blocco(['Oggi il codice lo controlla anche', 'la piattaforma, prima di pubblicare.'],
                740, 40, 500, T_CHIARO, font=MA, allinea='left', lh=1.25, tracking=0)
    c += filo(940)
    c += blocco(["Va anche esposto all'esterno dello stabile."], 1110, 31, 500, T_CHIARO_3,
                font=MA, allinea='left', lh=1.3, tracking=0)
    c += arco(2, 5, 820, 1120)
    nomi.append(scrivi('C2.dc.html', c))

    # ---------------- C3 · anello 02 ----------------------------------
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD_SCURO)
    c += marchio(80, 138, colore=SABBIA, ombra=False)
    c += marca("02 · QUANDO L'OSPITE ARRIVA", 220)
    c += blocco(['Prima lo riconosci.', 'Poi gli dai', "l'accesso."], 510, 62, 800,
                SABBIA, allinea='left')
    c += blocco(["L'identificazione è de visu: di persona", 'o in videochiamata in tempo reale.'],
                740, 40, 500, T_CHIARO, font=MA, allinea='left', lh=1.25, tracking=0)
    c += chip('+24:00', 920, x=64, w=236, h=66)
    c += blocco(['Da lì partono le 24 ore per comunicare le generalità.',
                 'Sei, se il soggiorno dura meno di un giorno.'],
                1040, 31, 500, T_CHIARO_2, font=MA, allinea='left', lh=1.3, tracking=0)
    c += arco(3, 5, 820, 1120)
    nomi.append(scrivi('C3.dc.html', c))

    # ---------------- C4 · anello 03 (unica slide chiara) -------------
    c = frame(1080, 1350, SABBIA)
    c += marchio(80, 138, colore=T_SCURO, ombra=False)
    c += marca('03 · DURANTE E DOPO IL SOGGIORNO', 220, colore=ORO_SCURO)
    c += blocco(["L'imposta di soggiorno", 'la incassi tu.', 'E la versi tu.'], 490, 62, 800,
                T_SCURO, allinea='left')
    c += blocco(['A Roma sono 6 € a persona a notte,', 'fino a 10 notti consecutive.'],
                720, 40, 500, T_SCURO_2, font=MA, allinea='left', lh=1.25, tracking=0)
    c += blocco(['Resti responsabile del versamento anche', "se l'ospite non paga la sua quota."],
                880, 40, 700, ORO_SCURO, allinea='left', lh=1.22, tracking=-0.2)
    c += blocco(['Estintore e rilevatori al loro posto e manutenuti.',
                 'Poi la casa torna in ordine, in standard alberghiero.'],
                1050, 31, 500, T_SCURO_3, font=MA, allinea='left', lh=1.3, tracking=0)
    c += arco(4, 5, 820, 1120, colore=ORO_SCURO, traccia='rgba(38,36,31,0.14)')
    nomi.append(scrivi('C4.dc.html', c))

    # ---------------- C5 · chi esegue + chiusura -----------------------
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD_SCURO)
    c += marchio(80, 138, colore=SABBIA, ombra=False)
    c += marca('04 · CHI ESEGUE LA CATENA', 220)
    righe = ''
    for a in ANELLI:
        righe += ('<div style="display: flex; align-items: center; gap: 20px; height: 56px;">'
                  '%s<span style="font-family: %s; font-weight: 600; font-size: 31px; '
                  'line-height: 1.2; color: %s;">%s</span></div>' % (spunta(), MA, T_CHIARO, a))
    c += ('  <div style="position: absolute; left: 64px; right: 64px; top: 300px; '
          'display: flex; flex-direction: column;">%s</div>\n' % righe)
    c += blocco(['La responsabilità resta tua.', 'Il lavoro no.'], 775, 62, 900, SABBIA,
                allinea='left')
    c += blocco(['Il proprietario riceve solo', 'il bonifico netto a fine mese.'], 950, 50, 800,
                ORO, allinea='left', lh=1.18)
    c += blocco(['Tutto dentro il 15% sul fatturato.', 'Guadagniamo solo se guadagni tu.'],
                1090, 31, 600, T_CHIARO_2, font=MA, allinea='left', lh=1.3, tracking=0)
    c += pill_oro(1228, 116, 'Scrivi CATENA in DM', size=40, anello=True)
    nomi.append(scrivi('C5.dc.html', c))
    return nomi


# =====================================================================
#  F1-F3 · FACEBOOK
# =====================================================================
VELO_F1 = [
    'radial-gradient(ellipse 96% 36% at 50% 54%, rgba(26,23,19,0.76) 0%, rgba(26,23,19,0.48) 46%, rgba(26,23,19,0) 68%)',
    'linear-gradient(180deg, rgba(46,42,37,0.90) 0%, rgba(46,42,37,0.46) 32%, rgba(46,42,37,0.56) 60%, rgba(46,42,37,0.92) 100%)',
    'linear-gradient(0deg, rgba(63,58,51,0.34), rgba(63,58,51,0.34))',
]

TRACCIA_CHIARA = 'rgba(38,36,31,0.14)'


def build_facebook():
    nomi = []

    # ---------------- F1 · 1080x1920 · gancio + la data ----------------
    c = frame(1080, 1920, FUME_DEEP)
    c += foto('d-ingresso-giorno.jpg')
    c += velo(*VELO_F1)
    c += marchio()
    c += marca('20 MAGGIO 2026', 320, ombra=True)
    c += blocco(['Dal 20 maggio', 'le piattaforme', 'verificano il codice', 'della tua casa.'],
                860, 70, 900, BIANCO, allinea='left', ombra=True)
    c += blocco(['Non ti sanzionano', 'per quanto guadagni.'], 1160, 62, 800, BIANCO,
                allinea='left', ombra=True)
    c += filo(1250, 'rgba(245,240,230,0.20)')
    c += blocco(['Ti sanzionano per', 'una casella dimenticata.'], 1345, 50, 800, ORO,
                allinea='left', ombra=True)
    c += blocco(['Non è una stretta. È un cambio di meccanismo.'], 1480, 33, 500, T_CHIARO,
                font=MA, allinea='left', lh=1.3, tracking=0, ombra=True)
    nomi.append(scrivi('F1.dc.html', c))

    # ---------------- F2 · 1080x1080 · la catena in 3 momenti ----------
    c = frame(1080, 1080, SABBIA)
    c += marchio(60, 118, colore=T_SCURO, ombra=False)
    c += blocco(['Cosa parte a ogni prenotazione'], 200, 50, 800, T_SCURO, allinea='left')
    c += filo(250, TRACCIA_CHIARA)

    c += marca('PRIMA', 300, colore=ORO_SCURO)
    c += blocco(["il CIN nell'annuncio,", 'e deve corrispondere.'], 375, 40, 500, T_SCURO_2,
                font=MA, allinea='left', lh=1.3, tracking=0)

    c += marca("ALL'ARRIVO · +24:00", 480, colore=ORO_SCURO)
    c += blocco(["prima identifichi l'ospite,", "poi gli dai l'accesso. Da lì: 24 ore",
                 'per comunicare le generalità.'], 581, 40, 500, T_SCURO_2,
                font=MA, allinea='left', lh=1.3, tracking=0)

    c += marca('DURANTE E DOPO', 715, colore=ORO_SCURO)
    c += blocco(['imposta di soggiorno da incassare e versare,',
                 'dotazioni di sicurezza al loro posto,',
                 'casa in standard alberghiero.'], 816, 40, 500, T_SCURO_2,
                font=MA, allinea='left', lh=1.3, tracking=0)

    nomi.append(scrivi('F2.dc.html', c))

    # ---------------- F3 · 1080x1080 · offerta / CTA -------------------
    c = frame(1080, 1080, FUME_DEEP)
    c += velo(GRAD_SCURO)
    c += marchio(72, 130, colore=SABBIA, ombra=False)
    c += marca('FINE MESE', 215)
    c += blocco(['Sei anelli. Tutti eseguiti.'], 290, 50, 800, SABBIA, allinea='left')
    c += blocco(['Il proprietario riceve solo', 'il bonifico netto', 'a fine mese.'],
                480, 62, 900, ORO, allinea='left')
    c += filo(600)
    c += blocco(['La dichiarazione dei redditi resta col tuo commercialista.',
                 'Noi facciamo gli adempimenti operativi della gestione.'],
                660, 31, 500, T_CHIARO_2, font=MA, allinea='left', lh=1.3, tracking=0)
    c += blocco(['15% sul fatturato.'], 780, 40, 700, SABBIA, allinea='left')
    c += blocco(['Guadagniamo solo se guadagni tu.'], 875, 33, 800, ORO, allinea='left')
    c += pill_oro(973, 86, 'Commenta CATENA o scrivici in privato', size=33)
    nomi.append(scrivi('F3.dc.html', c))
    return nomi


# =====================================================================
#  S1-S2 · STORIE · 1080x1920 · autoconclusive
# =====================================================================
VELO_S1 = [
    'radial-gradient(ellipse 96% 36% at 50% 56%, rgba(26,23,19,0.74) 0%, rgba(26,23,19,0.46) 46%, rgba(26,23,19,0) 68%)',
    'linear-gradient(180deg, rgba(46,42,37,0.90) 0%, rgba(46,42,37,0.44) 34%, rgba(46,42,37,0.56) 62%, rgba(46,42,37,0.92) 100%)',
    'linear-gradient(0deg, rgba(63,58,51,0.34), rgba(63,58,51,0.34))',
]
VELO_S2 = [
    'radial-gradient(ellipse 90% 30% at 50% 50%, rgba(26,23,19,0.64) 0%, rgba(26,23,19,0.32) 42%, rgba(26,23,19,0) 62%)',
    'linear-gradient(180deg, rgba(46,42,37,0.90) 0%, rgba(46,42,37,0.46) 36%, rgba(46,42,37,0.58) 64%, rgba(46,42,37,0.93) 100%)',
    'linear-gradient(0deg, rgba(63,58,51,0.30), rgba(63,58,51,0.30))',
]


def build_storie():
    nomi = []

    # ---------------- S1 · l'estremo "prima" ---------------------------
    c = frame(1080, 1920, FUME_DEEP)
    c += foto('s-balcone.jpg')
    c += velo(*VELO_S1)
    c += marchio()
    c += marca('PRIMA DELLA PUBBLICAZIONE', 280, allinea='right', ombra=True)
    c += blocco(["Il CIN nell'annuncio", 'è quello giusto?'], 860, 70, 900, BIANCO,
                allinea='left', ombra=True)
    c += blocco(['Se manca, o non corrisponde,', "l'annuncio può non passare la verifica."],
                1060, 40, 500, T_CHIARO, font=MA, allinea='left', lh=1.3, tracking=0, ombra=True)
    c += filo(1140, 'rgba(245,240,230,0.20)')
    c += blocco(["L'annuncio lo curiamo noi.", 'Il codice sarà presente', 'dal primo giorno.'],
                1250, 50, 800, ORO, allinea='left', ombra=True)
    c += pill_oro(1480, 120, 'Scrivi in DM', size=40)
    nomi.append(scrivi('S1.dc.html', c))

    # ---------------- S2 · l'estremo "dopo" ----------------------------
    ora = ('<span style="color: %s;">23:40</span>' % ORO)
    c = frame(1080, 1920, FUME_DEEP)
    c += foto('n-notte-storia.jpg')
    c += velo(*VELO_S2)
    c += marchio()
    c += chip('+24:00', 280, x=64, w=200, h=66, allinea='right')
    c += blocco(["L'ospite entra", 'alle %s.' % ora], 780, 70, 900, BIANCO,
                allinea='left', ombra=True)
    c += blocco(['Lo identifichi. Poi entra.', 'Da lì: 24 ore per la comunicazione.',
                 "E l'imposta di soggiorno la versi tu,", "anche se l'ospite non la paga."],
                1010, 40, 500, T_CHIARO, font=MA, allinea='left', lh=1.3, tracking=0, ombra=True)
    c += filo(1120, 'rgba(245,240,230,0.20)')
    c += blocco(['Da noi succede mentre dormi.', 'È già dentro la gestione.'], 1220, 50, 800,
                ORO, allinea='left', ombra=True)
    c += pill_oro(1480, 120, 'Scrivi in DM', size=40)
    nomi.append(scrivi('S2.dc.html', c))
    return nomi


# =====================================================================
#  CANVAS
# =====================================================================
TITOLI = {
    'Main.dc.html':  'Reel 1/9 · 0,0-2,6 s — il gancio',
    'R1b2.dc.html':  'Reel 2/9 · 2,6-4,0 s — la svolta',
    'R1b3.dc.html':  'Reel 3/9 · 4,0-5,4 s — arriva una prenotazione',
    'R1b4.dc.html':  'Reel 4/9 · 5,4-6,8 s — parte un orologio',
    'R1b5.dc.html':  'Reel 5/9 · 6,8-8,2 s — hai un altro lavoro',
    'R1b6.dc.html':  'Reel 6/9 · 8,2-9,6 s — va avanti lo stesso',
    'R1b7.dc.html':  'Reel 7/9 · 9,6-11,0 s — e non suona',
    'R1b8.dc.html':  'Reel 8/9 · 11,0-13,0 s — la presa in carico',
    'R1b9.dc.html':  'Reel 9/9 · 13,0-15,4 s — chiusura',
    'C1.dc.html':    'Carosello 1/5 · T zero — il gancio',
    'C2.dc.html':    "Carosello 2/5 · anello 01 — il CIN nell'annuncio",
    'C3.dc.html':    "Carosello 3/5 · anello 02 — l'arrivo e le 24 ore",
    'C4.dc.html':    'Carosello 4/5 · anello 03 — durante e dopo',
    'C5.dc.html':    'Carosello 5/5 · chi esegue la catena',
    'F1.dc.html':    'FB 1 · 9:16 — la data: dal 20 maggio',
    'F2.dc.html':    'FB 2 · 1:1 — la catena in tre momenti',
    'F3.dc.html':    'FB 3 · 1:1 — sei anelli, offerta e CTA',
    'S1.dc.html':    'Storia 1 · prima della pubblicazione',
    'S2.dc.html':    'Storia 2 · le 23:40',
}

FILE_H = {'C1.dc.html': 1350, 'C2.dc.html': 1350, 'C3.dc.html': 1350, 'C4.dc.html': 1350,
          'C5.dc.html': 1350, 'F2.dc.html': 1080, 'F3.dc.html': 1080}


def canvas(righe):
    """righe: liste di nomi file, una lista per fila della canvas."""
    ab, y = [], 0
    for fila in righe:
        h_max = 0
        for i, n in enumerate(fila):
            h = FILE_H.get(n, 1920)
            h_max = max(h_max, h)
            ab.append({'file': n, 'x': i * 1240, 'y': y, 'w': 1080, 'h': h,
                       'title': TITOLI.get(n, n), 'print': 'fixed'})
        y += h_max + 280
    with open(os.path.join(HERE, 'canvas.json'), 'w') as f:
        json.dump({'artboards': ab}, f, indent=2, ensure_ascii=False)
    return len(ab)


if __name__ == '__main__':
    reel = build_reel()
    caro = build_carosello()
    fb   = build_facebook()
    sto  = build_storie()
    n = canvas([reel, caro, fb, sto])
    print('artboard scritte: %d  (reel %d · carosello %d · facebook %d · storie %d)'
          % (n, len(reel), len(caro), len(fb), len(sto)))
