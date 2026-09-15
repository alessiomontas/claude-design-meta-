# Artboard della giornata 15/09 — angolo "Il calendario di Roma".
# Firma visiva della giornata: LA RIGA DI CALENDARIO — una fila di celle quadrate
# con quelle "calde" piene d'oro. Nasce dall'angolo (il prezzo lo decide il
# calendario) e non ripete nessuno dei pattern gia' usati: binario delle scadenze,
# tendina che attraversa, scontrino, blocchi invertiti, step numerati, card Q&A.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

FUME_DEEP = '#2E2A25'
FUME      = '#3F3A33'
FUME_MID  = '#4a443a'
FUME_CARD = '#4A443C'
ORO       = '#C8A24B'
SABBIA    = '#F5F0E6'
T_CHIARO  = '#E6DFD4'
T_CHIARO2 = '#b7ad9a'
BIANCO    = '#FFFFFF'

GRAD = ('radial-gradient(120%% 80%% at 50%% 8%%, %s 0%%, %s 58%%, %s 100%%)'
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

DATE = [
    ('23-25 ottobre',  'Maker Faire Rome — Gazometro'),
    ('1-24 novembre',  'Roma Jazz Festival, 50ª edizione'),
    ('1° novembre',    'Cade di domenica: weekend lungo'),
    ('7-8 dicembre',   "L'8 cade di martedì: ponte pieno"),
]
FASI = [
    ('01', 'Il calendario di Roma', 'Fiere, festival, ponti, feste. Prima della casa, si guarda la città.'),
    ('02', 'La base e il minimo',   'Un prezzo feriale, uno weekend, una soglia sotto cui non si scende.'),
    ('03', 'Le date calde',         'Una notte di evento fa storia a sé. Non vale come quella dopo.'),
    ('04', 'Ogni giorno, di nuovo', 'Si guarda cosa resta libero in zona e si corregge.'),
]


def frame(w, h, bg):
    return ('<div class="frame" style="width: %dpx; height: %dpx; box-sizing: border-box; '
            'position: relative; background: %s; overflow: hidden;">\n' % (w, h, bg))


def foto(src):
    return ('  <img src="%s" alt="" style="position: absolute; inset: 0; width: 100%%; '
            'height: 100%%; object-fit: cover;">\n' % src)


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
    sh = OMBRA if ombra else ''
    fam = AR if font == AR else MA
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'transform: translateY(-50%%); text-align: %s; font-family: %s; font-weight: %d; '
            'font-size: %dpx; line-height: %s; letter-spacing: %spx; color: %s; %s">%s</div>\n'
            % (left, right, y, allinea, fam, peso, size, lh, tracking, colore, sh, corpo))


def kicker(testo, y, colore=ORO, ombra=False, left=64, size=31, peso=700):
    sh = OMBRA if ombra else ''
    return ('  <div style="position: absolute; left: %dpx; right: 64px; top: %dpx; '
            'transform: translateY(-50%%); font-family: %s; font-weight: %d; font-size: %dpx; '
            'letter-spacing: 0.18em; text-transform: uppercase; color: %s; %s">'
            '<span style="margin-right: -0.18em; display: inline-block;">%s</span></div>\n'
            % (left, y, MA, peso, size, colore, sh, testo))


def filo(y, larghezza=220, colore=ORO, left=64, h=3):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; width: %dpx; height: %dpx; '
            'background: %s;"></div>\n' % (left, y, larghezza, h, colore))


def pill(y, h, testo, size=45, fondo=ORO, testo_col=FUME_DEEP):
    return ('  <div style="position: absolute; left: 64px; right: 64px; top: %dpx; '
            'transform: translateY(-50%%); height: %dpx; box-sizing: border-box; background: %s; '
            'border-radius: 999px; display: flex; align-items: center; justify-content: center; '
            'font-family: %s; font-weight: 700; font-size: %dpx; letter-spacing: 1px; '
            'text-transform: uppercase; color: %s;">%s</div>\n'
            % (y, h, fondo, MA, size, testo_col, testo))


# ---- LA FIRMA DELLA GIORNATA -------------------------------------------
def riga_calendario(y, piene, n=7, cella=120, gap=12, left=64, etichette=None):
    """Fila di celle quadrate: `piene` sono gli indici pieni d'oro.
    E' il motivo grafico ricorrente della giornata."""
    out = ('  <div style="position: absolute; left: %dpx; top: %dpx; display: flex; gap: %dpx;">'
           % (left, y, gap))
    for i in range(n):
        piena = i in piene
        et = ''
        if etichette and i < len(etichette) and etichette[i]:
            et = ('<span style="font-family: %s; font-weight: 700; font-size: 40px; color: %s;">%s</span>'
                  % (MA, FUME_DEEP if piena else T_CHIARO2, etichette[i]))
        out += ('<div style="width: %dpx; height: %dpx; border-radius: 16px; background: %s; '
                'display: flex; align-items: center; justify-content: center;">%s</div>'
                % (cella, cella, ORO if piena else FUME_CARD, et))
    return out + '</div>\n'


def card_date(y, altezza=160, gap=16, dati=None, size_data=50, size_ev=40):
    """Le righe data · evento: e' la card che verra' screenshottata."""
    out = ''
    for i, (data, ev) in enumerate(dati or DATE):
        top = y + i * (altezza + gap)
        out += ('  <div style="position: absolute; left: 64px; right: 64px; top: %dpx; '
                'height: %dpx; box-sizing: border-box; background: %s; border-radius: 20px; '
                'border-left: 6px solid %s; padding: 0 32px; display: flex; flex-direction: column; '
                'justify-content: center; gap: 8px;">'
                '<span style="font-family: %s; font-weight: 800; font-size: %dpx; color: %s;">%s</span>'
                '<span style="font-family: %s; font-weight: 600; font-size: %dpx; color: %s;">%s</span>'
                '</div>\n' % (top, altezza, FUME_CARD, ORO, AR, size_data, ORO, data,
                              MA, size_ev, BIANCO, ev))
    return out


def blocchi_fasi(y, altezza=160, gap=18, size_t=45, size_d=33, dettagli=True):
    out = ''
    for i, (num, tit, det) in enumerate(FASI):
        top = y + i * (altezza + gap)
        det_html = ('<span style="font-family: %s; font-weight: 600; font-size: %dpx; '
                    'color: %s; line-height: 1.25;">%s</span>' % (MA, size_d, T_CHIARO, det)) if dettagli else ''
        out += ('  <div style="position: absolute; left: 64px; right: 64px; top: %dpx; height: %dpx; '
                'display: flex; align-items: center; gap: 26px;">'
                '<span style="font-family: %s; font-weight: 900; font-size: 62px; color: %s; '
                'flex: 0 0 120px;">%s</span>'
                '<span style="display: flex; flex-direction: column; gap: 6px;">'
                '<span style="font-family: %s; font-weight: 800; font-size: %dpx; color: %s;">%s</span>'
                '%s</span></div>\n'
                % (top, altezza, AR, ORO, num, AR, size_t, BIANCO, tit, det_html))
    return out


def spunta(colore=ORO, d=26):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" '
            'stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" '
            'style="flex: 0 0 auto;"><path d="M20 6L9 17l-5-5"/></svg>' % (d, d, colore))


def scrivi(nome, corpo):
    with open(os.path.join(HERE, nome), 'w') as f:
        f.write(HEAD + corpo + FOOT)
    return nome


VELO_FOTO = [
    'linear-gradient(180deg, rgba(38,34,29,0.92) 0%, rgba(38,34,29,0.66) 42%, rgba(38,34,29,0.95) 100%)',
    'radial-gradient(ellipse 96% 36% at 50% 52%, rgba(26,23,19,0.45) 0%, rgba(26,23,19,0) 72%)',
]

# Le storie sono alte 1920 e hanno testo su quasi tutta l'altezza: serve un velo
# piatto e denso, non una fascia chiara a meta'. Regola di progetto: piu' velo,
# non piu' ombra.
VELO_STORIA = [
    'linear-gradient(180deg, rgba(38,34,29,0.93) 0%, rgba(38,34,29,0.86) 26%, '
    'rgba(38,34,29,0.84) 62%, rgba(38,34,29,0.94) 100%)',
    'radial-gradient(ellipse 110% 50% at 42% 50%, rgba(26,23,19,0.42) 0%, rgba(26,23,19,0) 78%)',
]


def carosello():
    nomi = []

    # ---- C1 · gancio (foto) ----
    c = frame(1080, 1350, FUME_DEEP)
    c += foto('camera-4x5.jpg')
    c += velo(*VELO_FOTO)
    c += marchio(100, 158)
    c += riga_calendario(300, piene=[2, 5], n=7, cella=104, gap=12)
    c += blocco(['Non tutte le notti di Roma',
                 'valgono <span style="color:%s">uguale.</span>' % ORO],
                610, 70, 900, BIANCO, ombra=True)
    c += filo(732)
    c += blocco(['23 ottobre e 3 novembre', 'non sono lo stesso prezzo.'],
                840, 45, 600, T_CHIARO, font=MA, lh=1.3, tracking=0, ombra=True)
    c += kicker('→ scorri', 1250)
    nomi.append(scrivi('Main.dc.html', c))

    # ---- C2 · la slide da screenshottare ----
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD)
    c += marchio(100, 158, colore=SABBIA, ombra=False)
    c += kicker('Le date da segnare', 280)
    c += blocco(['Autunno 2026 a Roma'], 365, 62, 900, BIANCO)
    c += card_date(460)
    c += kicker('Salva questa slide', 1230, colore=T_CHIARO, peso=600)
    nomi.append(scrivi('C2.dc.html', c))

    # ---- C3 · il metodo ----
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD)
    c += marchio(100, 158, colore=SABBIA, ombra=False)
    c += blocco(['Come si costruisce', 'il prezzo di una notte'], 345, 62, 900, BIANCO)
    c += blocco(['Quattro passaggi, in ordine.'], 440, 33, 600, T_CHIARO2,
                font=MA, lh=1.3, tracking=0)
    c += blocchi_fasi(520)
    c += kicker('→ scorri', 1250)
    nomi.append(scrivi('C3.dc.html', c))

    # ---- C4 · la notte-buco ----
    c = frame(1080, 1350, FUME_DEEP)
    c += velo(GRAD)
    c += marchio(100, 158, colore=SABBIA, ombra=False)
    c += kicker('La notte che resta vuota', 280)
    c += riga_calendario(340, piene=[0, 1, 3, 4, 5, 6], n=7, cella=120, gap=12,
                         etichette=['', '', '?', '', '', '', ''])
    c += blocco(['La notte singola', 'fra due prenotazioni'], 620, 62, 900, BIANCO)
    c += blocco(['A listino resta vuota.', 'Si abbassa e si vende.'], 790, 45, 600,
                T_CHIARO, font=MA, lh=1.3, tracking=0)
    c += filo(900, larghezza=180)
    c += blocco(['È il pezzo che chi gestisce da solo', 'non ha tempo di guardare.'],
                1000, 40, 600, T_CHIARO2, font=MA, lh=1.28, tracking=0)
    c += blocco(['Noi lo guardiamo <span style="color:%s">ogni giorno.</span>' % ORO],
                1140, 45, 800, BIANCO)
    c += kicker('→ scorri', 1250)
    nomi.append(scrivi('C4.dc.html', c))

    # ---- C5 · offerta + CTA ----
    c = frame(1080, 1350, FUME_DEEP)
    c += foto('cucina-4x5.jpg')
    c += velo(*VELO_FOTO)
    c += marchio(100, 158)
    c += riga_calendario(270, piene=[0, 1, 2, 3, 4, 5, 6], n=7, cella=104, gap=12)
    c += blocco(['Il calendario di Roma',
                 'lo teniamo <span style="color:%s">noi.</span>' % ORO],
                520, 62, 900, BIANCO, ombra=True)
    c += blocco(['Aggiornato tutti i giorni,', 'incluso nella gestione.'], 680, 45, 600,
                T_CHIARO, font=MA, lh=1.3, tracking=0, ombra=True)
    c += filo(806, larghezza=180)
    c += blocco(['Pricing dinamico · Check-in smart H24 · Gestione ospiti',
                 'Pulizie in standard alberghiero · Foto e annuncio'],
                858, 29, 600, T_CHIARO, font=MA, lh=1.42, tracking=0, ombra=True)
    c += blocco(['15% sul fatturato generato.',
                 'A fine mese ricevi il bonifico netto.'], 980, 36, 800, SABBIA, ombra=True)
    c += blocco(['Guadagniamo solo se guadagni tu.'], 1098, 30, 600, ORO,
                font=MA, lh=1.3, tracking=0, ombra=True)
    c += pill(1180, 116, 'Scrivi CALCOLO in DM')
    nomi.append(scrivi('C5.dc.html', c))
    return nomi


def facebook():
    nomi = []

    # ---- F1 · 9:16 · gancio + date ----
    c = frame(1080, 1920, FUME_DEEP)
    c += foto('cucina-9x16.jpg')
    c += velo('linear-gradient(180deg, rgba(38,34,29,0.92) 0%, rgba(38,34,29,0.56) 34%, rgba(38,34,29,0.94) 100%)',
              'radial-gradient(ellipse 96% 30% at 50% 46%, rgba(26,23,19,0.42) 0%, rgba(26,23,19,0) 70%)')
    c += marchio()
    c += blocco(['Le notti di Roma',
                 'non valgono tutte <span style="color:%s">uguale.</span>' % ORO],
                500, 70, 900, BIANCO, ombra=True)
    c += filo(612, larghezza=240)
    c += card_date(680, altezza=150, gap=16)
    c += blocco(['Le date dell\'autunno che portano gente a Roma,',
                 'in chiaro. Le teniamo noi.'], 1402, 38, 600,
                T_CHIARO, font=MA, lh=1.32, tracking=0, ombra=True)
    c += kicker('Salva questo post', 1542, colore=T_CHIARO, peso=600)
    nomi.append(scrivi('F1.dc.html', c))

    # ---- F2 · 1:1 · il metodo ----
    c = frame(1080, 1080, FUME_DEEP)
    c += velo(GRAD)
    c += marchio(64, 122, colore=SABBIA, ombra=False)
    c += blocco(['Come si costruisce il prezzo'], 235, 62, 900, BIANCO)
    c += blocco(['Quattro passaggi, in ordine.'], 310, 33, 600, T_CHIARO2,
                font=MA, lh=1.3, tracking=0)
    c += blocchi_fasi(390, altezza=110, gap=16, size_t=40, dettagli=False)
    c += filo(962, larghezza=952)
    nomi.append(scrivi('F2.dc.html', c))

    # ---- F3 · 1:1 · offerta ----
    c = frame(1080, 1080, FUME_DEEP)
    c += velo(GRAD)
    c += marchio(64, 122, colore=SABBIA, ombra=False)
    c += blocco(['Il calendario lo teniamo <span style="color:%s">noi.</span>' % ORO],
                245, 62, 900, BIANCO)
    c += blocco(['Aggiornato tutti i giorni,', 'incluso nel 15%.'], 360, 40, 600,
                T_CHIARO, font=MA, lh=1.3, tracking=0)
    righe = ''
    for t in ('Pricing dinamico',
              'Check-in smart H24 e gestione ospiti',
              'Pulizie in standard alberghiero'):
        righe += ('<div style="display:flex; align-items:center; gap:20px; height:70px;">'
                  '%s<span style="font-family:%s; font-weight:600; font-size:40px; color:%s;">%s</span>'
                  '</div>' % (spunta(), MA, BIANCO, t))
    c += ('  <div style="position:absolute; left:64px; right:64px; top:460px; '
          'display:flex; flex-direction:column;">%s</div>\n' % righe)
    c += blocco(['Foto e annuncio inclusi. A fine mese ricevi il bonifico netto.'],
                760, 33, 600, T_CHIARO2, font=MA, lh=1.3, tracking=0)
    c += pill(870, 96, 'Scrivi CALCOLO in DM')
    c += blocco(['Guadagniamo solo se guadagni tu.'], 960, 31, 600, ORO,
                font=MA, lh=1.3, tracking=0)
    nomi.append(scrivi('F3.dc.html', c))
    return nomi


def storie():
    nomi = []

    # ---- S1 · il prezzo che non si muove ----
    c = frame(1080, 1920, FUME_DEEP)
    c += foto('camera-9x16.jpg')
    c += velo(*VELO_STORIA)
    c += marchio()
    c += kicker('Il criterio', 300, ombra=True)
    c += blocco(['Il prezzo della tua casa', 'non deve restare fermo.'], 640, 70, 900,
                BIANCO, ombra=True)
    c += filo(752)
    c += blocco(['Prima del tuo calendario,', 'apri quello di Roma.'], 860, 45, 600,
                T_CHIARO, font=MA, lh=1.3, tracking=0, ombra=True)
    c += riga_calendario(980, piene=[3, 4], n=7, cella=104, gap=12)
    c += blocco(['L\'1 novembre cade di domenica.', 'Il 7 e l\'8 dicembre sono ponte pieno.'],
                1200, 40, 600, T_CHIARO, font=MA, lh=1.32, tracking=0, ombra=True)
    c += blocco(['Due prezzi diversi, <span style="color:%s">non uno.</span>' % ORO],
                1320, 50, 800, BIANCO, ombra=True)
    c += pill(1480, 120, 'Scrivi CALCOLO in DM')
    c += blocco(['Guadagniamo solo se guadagni tu.'], 1640, 32, 600, ORO,
                font=MA, lh=1.3, tracking=0, allinea='center', ombra=True)
    nomi.append(scrivi('S1.dc.html', c))

    # ---- S2 · una data in arrivo ----
    c = frame(1080, 1920, FUME_DEEP)
    c += foto('mare-9x16.jpg')
    c += velo(*VELO_STORIA)
    c += marchio()
    c += kicker('Una data in arrivo', 300, ombra=True)
    c += blocco(['23-25 ottobre:', 'Maker Faire Rome.'], 640, 70, 900, BIANCO, ombra=True)
    c += filo(752)
    c += blocco(['Tre giorni di fiera al Gazometro.', 'La città si riempie,',
                 'e quelle notti non valgono', 'come le altre.'],
                920, 40, 600, T_CHIARO, font=MA, lh=1.32, tracking=0, ombra=True)
    c += riga_calendario(1090, piene=[2, 3, 4], n=7, cella=104, gap=12)
    c += blocco(['Il calendario lo teniamo noi,', 'aggiornato tutti i giorni.'],
                1300, 50, 800, ORO, ombra=True)
    c += pill(1480, 120, 'Scrivi CALCOLO in DM')
    c += blocco(['Guadagniamo solo se guadagni tu.'], 1640, 32, 600, ORO,
                font=MA, lh=1.3, tracking=0, allinea='center', ombra=True)
    nomi.append(scrivi('S2.dc.html', c))
    return nomi


TITOLI = {
    'Main.dc.html': 'Carosello 1/5 · il gancio',
    'C2.dc.html': 'Carosello 2/5 · le date da segnare',
    'C3.dc.html': 'Carosello 3/5 · il metodo',
    'C4.dc.html': 'Carosello 4/5 · la notte che resta vuota',
    'C5.dc.html': 'Carosello 5/5 · offerta e CTA',
    'F1.dc.html': 'FB 1 · 9:16 — gancio e date',
    'F2.dc.html': 'FB 2 · 1:1 — il metodo',
    'F3.dc.html': 'FB 3 · 1:1 — offerta e CTA',
    'S1.dc.html': 'Storia 1 · il criterio',
    'S2.dc.html': 'Storia 2 · Maker Faire',
}
ALTEZZA = {'Main.dc.html': 1350, 'C2.dc.html': 1350, 'C3.dc.html': 1350,
           'C4.dc.html': 1350, 'C5.dc.html': 1350, 'F2.dc.html': 1080, 'F3.dc.html': 1080}


def canvas(righe):
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
    c = carosello()
    f = facebook()
    s = storie()
    n = canvas([c, f, s])
    print('artboard: %d (carosello %d · facebook %d · storie %d)' % (n, len(c), len(f), len(s)))
