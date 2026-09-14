# Artboard del pacchetto v2 — angolo "Ti hanno scattato le foto col telefono".
# Firma grafica: "la tendina che attraversa" — linea oro verticale con maniglia,
# che avanza di slide in slide nel carosello (216 → 432 → 648 → 864 → fuori).
# Le y vengono dalle tabelle LAYOUT di copy-v2-foto.md.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

FUME       = '#3F3A33'
FUME_DEEP  = '#2E2A25'
FUME_MID   = '#4a443a'
ORO        = '#C8A24B'
ORO_SCURO  = '#b3892f'
SABBIA     = '#F5F0E6'
T_SCURO    = '#26241F'
T_SCURO_2  = '#46423a'
T_CHIARO   = '#d8d2c4'
T_CHIARO_2 = '#b7ad9a'
BIANCO     = '#FFFFFF'

GRAD = ('radial-gradient(120%% 80%% at 50%% 10%%, %s 0%%, %s 55%%, %s 100%%)'
        % (FUME_MID, FUME, FUME_DEEP))
OMBRA = ('text-shadow: 0 3px 10px rgba(0,0,0,0.68), 0 12px 44px rgba(0,0,0,0.55), '
         '0 1px 2px rgba(0,0,0,0.85);')
AR = "'Archivo', 'Helvetica Neue', Arial, sans-serif"
MA = "'Manrope', 'Helvetica Neue', Arial, sans-serif"

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
FOOT = "</div>\n</x-dc>\n</body>\n</html>\n"


def frame(w, h, bg):
    return ('<div class="frame" style="width: %dpx; height: %dpx; box-sizing: border-box; '
            'position: relative; background: %s; overflow: hidden;">\n' % (w, h, bg))


def foto(src, extra=''):
    return ('  <img src="%s" alt="" style="position: absolute; inset: 0; width: 100%%; '
            'height: 100%%; object-fit: cover; %s">\n' % (src, extra))


def velo(*strati):
    return ('  <div style="position: absolute; inset: 0; background: %s;"></div>\n'
            % ', '.join(strati))


def marchio(y_h=112, y_m=176, colore=BIANCO, ombra=True):
    sh = OMBRA if ombra else ''
    op = 'rgba(255,255,255,0.86)' if colore == BIANCO else colore
    return (
        '  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: center; '
        'font-family: %s; font-weight: 800; font-size: 33px; letter-spacing: 10px; color: %s; %s">'
        '<span style="margin-right: -10px; display: inline-block;">HADRIANUS</span></div>\n'
        '  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: center; '
        'font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 7px; color: %s; %s">'
        '<span style="margin-right: -7px; display: inline-block;">MULTISERVICE</span></div>\n'
        % (y_h, AR, colore, sh, y_m, MA, op, sh))


def blocco(righe, y, size, peso, colore, font=AR, allinea='left', lh=1.13,
           ombra=False, tracking=-0.4, left=64, right=64):
    """Ancorato al centro ottico della fascia (top = centro, translateY(-50%))."""
    sh = OMBRA if ombra else ''
    fam = AR if font == AR else MA
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'transform: translateY(-50%%); text-align: %s; font-family: %s; font-weight: %d; '
            'font-size: %dpx; line-height: %s; letter-spacing: %spx; color: %s; %s">%s</div>\n'
            % (left, right, y, allinea, fam, peso, size, lh, tracking, colore, sh, corpo))


def kicker(testo, y, colore=ORO, ombra=False, allinea='left', left=64):
    sh = OMBRA if ombra else ''
    pos = ('left: %dpx; right: 64px; text-align: left;' % left if allinea == 'left'
           else 'left: %dpx; right: 64px; text-align: right;' % left)
    return ('  <div style="position: absolute; %s top: %dpx; transform: translateY(-50%%); '
            'font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 8px; '
            'text-transform: uppercase; color: %s; %s">'
            '<span style="margin-right: -8px; display: inline-block;">%s</span></div>\n'
            % (pos, y, MA, colore, sh, testo))


def chip(testo, y, x=700, w=316, colore=ORO):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; width: %dpx; height: 56px; '
            'box-sizing: border-box; background: rgba(26,23,19,0.62); border: 1px solid rgba(200,162,75,0.55); '
            'border-radius: 999px; display: flex; align-items: center; justify-content: center; '
            'font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 8px; color: %s;">'
            '<span style="margin-right: -8px; display: inline-block;">%s</span></div>\n'
            % (x, y, w, MA, colore, testo))


def pill(y, h, testo, size=40, fondo=ORO, testo_col=FUME_DEEP, maniglia=False):
    out = ('  <div style="position: absolute; left: 64px; right: 64px; top: %dpx; '
           'transform: translateY(-50%%); height: %dpx; box-sizing: border-box; background: %s; '
           'border-radius: 999px; display: flex; align-items: center; justify-content: center; '
           'font-family: %s; font-weight: 800; font-size: %dpx; color: %s;">%s</div>\n'
           % (y, h, fondo, AR, size, testo_col, testo))
    if maniglia:
        out += ('  <div style="position: absolute; left: 86px; top: %dpx; width: 44px; height: 44px; '
                'border-radius: 50%%; border: 3px solid rgba(46,42,37,0.42);"></div>\n' % (y - 22))
    return out


def pill_outline(y, x, w, h, testo, colore=ORO):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; transform: translateY(-50%%); '
            'width: %dpx; height: %dpx; box-sizing: border-box; background: rgba(200,162,75,0.16); '
            'border: 2px solid %s; border-radius: 999px; display: flex; align-items: center; '
            'justify-content: center; gap: 18px; font-family: %s; font-weight: 700; font-size: 33px; '
            'color: %s;"><span>%s</span><span style="font-size: 34px;">&rarr;</span></div>\n'
            % (x, y, w, h, colore, AR, colore, testo))


def tendina(x, h, y_maniglia, colore='rgba(200,162,75,0.35)', maniglia=True, spessore=6):
    """La firma della giornata: linea verticale oro con maniglia circolare.
    Attenuata di proposito: attraversa i blocchi di testo, e a piena intensita'
    competerebbe con la lettura invece di firmare la pagina."""
    out = ('  <div style="position: absolute; left: %dpx; top: 0; width: %dpx; height: %dpx; '
           'background: %s;"></div>\n'
           % (x, spessore, h, colore))
    if maniglia:
        out += ('  <div style="position: absolute; left: %dpx; top: %dpx; width: 44px; height: 44px; '
                'border-radius: 50%%; border: 3px solid %s;"></div>\n'
                % (x - 19, y_maniglia - 22, ORO))
    return out


def filo(y, colore=ORO, left=64, right=64, h=3):
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
            'background: %s;"></div>\n' % (left, right, y, h, colore))


def inserto(src, y=980, h=306, fili=False):
    """Banda fotografica con angoli arrotondati; `fili` disegna le due verticali oro."""
    out = ('  <div style="position: absolute; left: 64px; top: %dpx; width: 952px; height: %dpx; '
           'border-radius: 20px; overflow: hidden;"><img src="%s" alt="" '
           'style="width: 100%%; height: 100%%; object-fit: cover;">' % (y, h, src))
    if fili:
        for fx in (238, 714):
            out += ('<div style="position: absolute; left: %dpx; top: 0; width: 2px; height: 100%%; '
                    'background: rgba(200,162,75,0.85);"></div>' % fx)
    return out + '</div>\n'


def scrivi(nome, corpo):
    with open(os.path.join(HERE, nome), 'w') as f:
        f.write(HEAD + corpo + FOOT)
    return nome


VELO_SCURO = [
    'radial-gradient(ellipse 92% 32% at 50% 56%, rgba(26,23,19,0.66) 0%, rgba(26,23,19,0.34) 46%, rgba(26,23,19,0) 70%)',
    'linear-gradient(180deg, rgba(46,42,37,0.88) 0%, rgba(46,42,37,0.30) 32%, rgba(46,42,37,0.44) 62%, rgba(46,42,37,0.92) 100%)',
]


# =====================================================================
#  K1-K5 · CAROSELLO 1080×1350
# =====================================================================
def carosello():
    nomi = []

    # ---- K1 · il confronto: la tendina a 216, a sinistra il "dopo" ----
    c = frame(1080, 1350, FUME_DEEP)
    c += foto('k-tel-45.jpg')
    c += ('  <div style="position: absolute; left: 540px; top: 0; width: 540px; height: 1350px; '
          'overflow: hidden;"><img src="k-pro-45.jpg" alt="" style="position: absolute; right: 0; '
          'top: 0; width: 1080px; height: 1350px; object-fit: cover;"></div>\n')
    c += velo(*VELO_SCURO)
    c += marchio(80, 138)
    c += chip('SIMULAZIONE', 200, x=64, w=316)
    c += chip('FATTA BENE', 200, x=700, w=316)
    c += tendina(540, 1350, 330)
    c += blocco(['Ti hanno scattato', 'le foto', 'col telefono.'], 770, 70, 900, BIANCO, ombra=True)
    c += blocco(['Quattro cose rendono una foto', 'capace di vendere la casa.'], 980, 40, 500,
                T_CHIARO, font=MA, lh=1.3, tracking=0, ombra=True)
    c += blocco(['La foto qui sopra è una simulazione:',
                 'una foto rovinata apposta da noi.'], 1130, 31, 500, T_CHIARO_2,
                font=MA, lh=1.3, tracking=0, ombra=True)
    c += pill_outline(1245, 64, 356, 80, 'Scorri')
    nomi.append(scrivi('Main.dc.html', c))

    # ---- K2 · la luce ----
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD)
    c += tendina(648, 1350, 675)
    c += marchio(80, 138, colore=SABBIA, ombra=False)
    c += kicker('01 · LA LUCE', 220)
    c += blocco(['Una sola luce', 'alla volta.'], 470, 62, 800, SABBIA)
    c += blocco(['Lampade accese e luce di finestra', 'insieme danno una foto di due colori.',
                 'Spegni le lampade. Scosta le tende.', 'Scatta a metà mattina.'],
                710, 40, 500, T_CHIARO, font=MA, lh=1.32, tracking=0)
    c += blocco(['La casa torna del colore che ha davvero.'], 890, 40, 700, ORO)
    c += inserto('k-banda-pro.jpg')
    nomi.append(scrivi('K2.dc.html', c))

    # ---- K3 · l'ordine (unica slide chiara) ----
    c = frame(1080, 1350, SABBIA)
    c += tendina(756, 1350, 675, colore='rgba(179,137,47,0.35)')
    c += marchio(80, 138, colore=T_SCURO, ombra=False)
    c += kicker("02 · L'ORDINE", 220, colore=ORO_SCURO)
    c += blocco(['Fotografi la casa finita,', 'non la casa in pausa.'], 470, 62, 800, T_SCURO)
    c += blocco(['Via telecomandi, cavi, ciabatte,', 'detersivi, scolapiatti.',
                 'Letto teso, cuscini battuti,', 'lavabo libero, tende tirate uguali.'],
                710, 40, 500, T_SCURO_2, font=MA, lh=1.32, tracking=0)
    c += blocco(['Chi guarda vede una casa pronta.'], 890, 40, 700, ORO_SCURO)
    c += inserto('k-banda-openspace.jpg')
    nomi.append(scrivi('K3.dc.html', c))

    # ---- K4 · l'inquadratura ----
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD)
    c += tendina(918, 1350, 675)
    c += marchio(80, 138, colore=SABBIA, ombra=False)
    c += kicker("03 · L'INQUADRATURA", 220)
    c += blocco(['Le verticali devono', 'restare verticali.'], 470, 62, 800, SABBIA)
    c += blocco(["Macchina all'altezza del petto e dritta:", 'stipiti e spigoli non devono pendere.',
                 'Scatta da un angolo, mai dal centro.', 'E tieni il telefono in orizzontale.'],
                710, 40, 500, T_CHIARO, font=MA, lh=1.32, tracking=0)
    c += blocco(['La stanza sembra grande quanto è.'], 890, 40, 700, ORO)
    c += inserto('k-banda-pro.jpg', fili=True)
    nomi.append(scrivi('K4.dc.html', c))

    # ---- K5 · la sequenza + chiusura ----
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD)
    c += marchio(80, 138, colore=SABBIA, ombra=False)
    c += kicker('04 · LA SEQUENZA', 220)
    c += blocco(["L'ordine delle foto", 'è mezzo annuncio.'], 330, 62, 800, SABBIA)
    voci = [('01', "Copertina: l'ambiente migliore, in orizzontale"),
            ('02', 'Il resto del giorno: soggiorno e cucina'),
            ('03', 'Le camere, una per volta'),
            ('04', 'Bagno, esterno, vista')]
    righe = ''
    for n, t in voci:
        righe += ('<div style="display: flex; align-items: baseline; gap: 22px; height: 60px;">'
                  '<span style="font-family: %s; font-weight: 800; font-size: 31px; color: %s; '
                  'flex: 0 0 auto;">%s</span>'
                  '<span style="font-family: %s; font-weight: 600; font-size: 31px; color: %s;">%s</span>'
                  '</div>' % (AR, ORO, n, MA, T_CHIARO, t))
    c += ('  <div style="position: absolute; left: 64px; right: 64px; top: 440px; '
          'display: flex; flex-direction: column;">%s</div>\n' % righe)
    c += filo(722)
    c += blocco(['Con noi non le scatti tu.', 'Il servizio fotografico è incluso.'],
                830, 50, 900, SABBIA)
    c += blocco(['Gestione completa. 15% sul fatturato generato.'], 960, 31, 600, T_CHIARO_2,
                font=MA, lh=1.3, tracking=0)
    c += blocco(['Guadagniamo solo se guadagni tu.'], 1050, 33, 800, ORO)
    c += pill(1200, 116, 'Scrivi CALCOLO in DM', maniglia=True)
    nomi.append(scrivi('K5.dc.html', c))
    return nomi


# =====================================================================
#  FB1-FB3 · FACEBOOK
# =====================================================================
def facebook():
    nomi = []

    # ---- FB1 · 1080×1920 · gancio ----
    c = frame(1080, 1920, FUME_DEEP)
    c += foto('salone-telefono.jpg')
    c += velo(*VELO_SCURO)
    c += marchio()
    c += chip('SIMULAZIONE', 260)
    c += blocco(['Ti hanno scattato', 'le foto', 'col telefono.'], 930, 70, 900, BIANCO, ombra=True)
    c += blocco(['La prima foto è l\'unica cosa', 'che vede chi sta scorrendo.'],
                1220, 62, 800, BIANCO, ombra=True)
    c += filo(1310, 'rgba(245,240,230,0.22)')
    c += blocco(['Il resto lo legge solo', 'chi si è già fermato.'], 1400, 50, 800, ORO, ombra=True)
    c += blocco(['La foto qui sopra è una simulazione: una foto',
                 'reale rovinata apposta da noi.'],
                1530, 33, 500, T_CHIARO, font=MA, lh=1.3, tracking=0, ombra=True)
    nomi.append(scrivi('FB1.dc.html', c))

    # ---- FB2 · 1080×1080 · le quattro differenze ----
    c = frame(1080, 1080, SABBIA)
    c += ('  <div style="position: absolute; left: 540px; top: 0; width: 6px; height: 1080px; '
          'background: rgba(200,162,75,0.35);"></div>\n')
    c += marchio(72, 130, colore=T_SCURO, ombra=False)
    c += blocco(['Stessa stanza. Quattro differenze.'], 235, 50, 800, T_SCURO)
    c += filo(285, 'rgba(38,36,31,0.14)')
    voci = [('LUCE', 'una sola alla volta: o le lampade, o la finestra', 380),
            ('ORDINE', 'niente cavi, niente detersivi, letto teso', 500),
            ('INQUADRATURA', 'dritta, da un angolo, in orizzontale', 620),
            ('SEQUENZA', 'copertina, giorno, camere, bagno ed esterno', 740)]
    for k, t, y in voci:
        c += ('  <div style="position: absolute; left: 64px; top: %dpx; width: 3px; height: 74px; '
              'background: %s;"></div>\n' % (y - 37, ORO_SCURO))
        c += kicker(k, y - 22, colore=ORO_SCURO, left=86)
        c += blocco([t], y + 18, 40, 500, T_SCURO, font=MA, lh=1.25, tracking=0, left=86)
    c += pill(938, 156, 'Con noi la tua casa la fotografiamo noi.', size=40)
    nomi.append(scrivi('FB2.dc.html', c))

    # ---- FB3 · 1080×1080 · offerta ----
    c = frame(1080, 1080, FUME_DEEP)
    c += foto('salone-pro.jpg')
    c += velo('radial-gradient(ellipse 98% 44% at 50% 46%, rgba(26,23,19,0.58) 0%, rgba(26,23,19,0.34) 56%, rgba(26,23,19,0.14) 80%)',
              'linear-gradient(180deg, rgba(46,42,37,0.78) 0%, rgba(46,42,37,0.30) 34%, rgba(46,42,37,0.44) 64%, rgba(46,42,37,0.90) 100%)')
    c += marchio(72, 130, colore=SABBIA, ombra=True)
    c += kicker('GESTIONE COMPLETA', 215, ombra=True)
    c += blocco(['Il servizio fotografico', 'è incluso.'], 340, 62, 900, ORO, ombra=True)
    c += blocco(['La casa la fotografiamo noi.', "L'annuncio lo scriviamo noi.",
                 'Tu ricevi il bonifico netto a fine mese.'],
                540, 40, 700, SABBIA, lh=1.32, ombra=True)
    c += filo(640, 'rgba(245,240,230,0.18)')
    c += blocco(['15% sul fatturato generato.'], 700, 45, 800, SABBIA, ombra=True)
    c += blocco(['Guadagniamo solo se guadagni tu.'], 785, 33, 800, ORO, ombra=True)
    c += pill(958, 116, 'Scrivi CALCOLO in DM', maniglia=True)
    nomi.append(scrivi('FB3.dc.html', c))
    return nomi


# =====================================================================
#  S3-S4 · STORIE (le due nuove; S1 e S2 restano invariate)
# =====================================================================
def storie():
    nomi = []
    dati = [
        ('S3', 'openspace-9x16.jpg', 'ERRORE · MINIMO NOTTI',
         ['Hai messo', 'minimo 3 notti.'],
         ['Roma si visita in due giorni.', 'Con il minimo a tre notti,', 'chi ne cerca due non ti trova.'],
         ['Tieni il minimo alto solo in alta', 'stagione. Nei periodi bassi e in',
          'settimana scendi a una o due notti.'],
         ['Con noi le tariffe si muovono', 'data per data. Ci pensiamo noi.']),
        ('S4', 'salone-pro.jpg', 'ERRORE · ORARI DI ARRIVO',
         ['Check-in', 'dalle 15 alle 19.'],
         ['Chi atterra a Fiumicino la sera', 'e chi arriva col treno tardi', 'cerca una casa che lo aspetti.'],
         ["Allarga la finestra di arrivo e scrivilo", "nell'annuncio. E a qualunque ora,",
          "l'ospite va identificato prima di entrare."],
         ['Ti assicuriamo il check-in', 'smart H24, a qualsiasi ora.']),
    ]
    for sid, img, etichetta, gancio, problema, consiglio, garanzia in dati:
        c = frame(1080, 1920, FUME_DEEP)
        c += foto(img)
        c += velo(*VELO_SCURO)
        c += tendina(108, 1920, 0, colore='rgba(200,162,75,0.55)', maniglia=False)
        c += marchio()
        c += chip(etichetta, 260, x=1016 - 420, w=420)
        c += blocco(gancio, 640, 70, 900, BIANCO, ombra=True)
        c += blocco(problema, 810, 40, 500, T_CHIARO, font=MA, lh=1.32, tracking=0, ombra=True)
        c += kicker('IL CONSIGLIO', 955, ombra=True)
        c += blocco(consiglio, 1080, 45, 700, SABBIA, lh=1.28, ombra=True)
        c += filo(1190, 'rgba(245,240,230,0.22)')
        c += blocco(garanzia, 1275, 50, 800, ORO, ombra=True)
        c += pill(1480, 120, 'Scrivi CALCOLO in DM')
        nomi.append(scrivi(sid + '.dc.html', c))
    return nomi


TITOLI = {
    'Main.dc.html': 'Carosello 1/5 · il confronto',
    'K2.dc.html': 'Carosello 2/5 · 01 la luce',
    'K3.dc.html': "Carosello 3/5 · 02 l'ordine",
    'K4.dc.html': "Carosello 4/5 · 03 l'inquadratura",
    'K5.dc.html': 'Carosello 5/5 · 04 la sequenza + offerta',
    'FB1.dc.html': 'FB 1 · 9:16 — il gancio',
    'FB2.dc.html': 'FB 2 · 1:1 — le quattro differenze',
    'FB3.dc.html': 'FB 3 · 1:1 — offerta e CTA',
    'S3.dc.html': 'Storia 3 · minimo notti',
    'S4.dc.html': 'Storia 4 · orari di check-in',
}
ALTEZZA = {'Main.dc.html': 1350, 'K2.dc.html': 1350, 'K3.dc.html': 1350, 'K4.dc.html': 1350,
           'K5.dc.html': 1350, 'FB2.dc.html': 1080, 'FB3.dc.html': 1080}


def canvas(file_vecchi, righe):
    ab, y = [], 0
    for fila in righe:
        h_max = 0
        for i, n in enumerate(fila):
            h = ALTEZZA.get(n, 1920)
            h_max = max(h_max, h)
            ab.append({'file': n, 'x': i * 1240, 'y': y, 'w': 1080, 'h': h,
                       'title': TITOLI.get(n, n), 'print': 'fixed'})
        y += h_max + 280
    with open(os.path.join(HERE, 'canvas.json'), 'w') as f:
        json.dump({'artboards': ab}, f, indent=2, ensure_ascii=False)
    return len(ab)


if __name__ == '__main__':
    k = carosello()
    f = facebook()
    s = storie()
    # S1 e S2 restano quelle approvate dal pacchetto precedente
    n = canvas([], [k, f + ['S1.dc.html', 'S2.dc.html'], s])
    print('artboard v2: %d (carosello %d · facebook %d · storie nuove %d) + S1/S2 invariate'
          % (n, len(k), len(f), len(s)))
