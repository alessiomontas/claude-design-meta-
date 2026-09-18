# -*- coding: utf-8 -*-
"""Libreria della giornata 18/09/2026 — variante FUME' scura.

FIRMA DEL GIORNO: **la catena ad anelli**.

Il contenuto non e' un elenco: e' una cosa sola che si trasforma. Quattro
cerchi oro su un filo orizzontale (recensione -> visibilita' -> prezzo ->
chi prenota). A ogni schermata se ne accende uno e il filo avanza fino a
quello. L'indice di lettura e' quindi COSTANTE: in qualunque fotogramma si
capisce a che punto della catena si e', anche entrando a meta' reel.

Tre conseguenze volute, tutte pensate per NON somigliare ai giorni scorsi:

1. **Il lockup e' centrato, non a sinistra.** Marchio centrato + catena
   centrata subito sotto, a tutta colonna utile. L'impianto "marchio in alto
   a sinistra + blocco di testo a meta' altezza" e' uscito quattro giorni di
   fila ed e' vietato oggi. La colonna di testo resta allineata a sinistra,
   ma NON e' piu' il primo elemento che si legge: lo e' la catena.
2. **Nessuna barra di avanzamento a tacche, nessuno scalino, nessuna colonna
   di voci, nessun prima/dopo.** L'avanzamento e' il filo della catena.
3. **L'unica zona luminosa e' la card recensione**: sabbia #F5F0E6 con bordo
   sinistro oro da 6 px. Su un feed scuro deve leggersi come un foglio di
   carta appoggiato sul fumè. E' li' che deve cadere l'occhio. Per questo su
   ogni artboard che porta una recensione **non c'e' nessun'altra superficie
   chiara**: la fascia offerta e la card non convivono mai.

Regole di brand sulle recensioni (sono prova, non decorazione):
  - a schermo solo stelle, testo verbatim, nome di battesimo, mese, e la riga
    «traduzione di Airbnb» dove il copy la prevede;
  - mai nome della casa, indirizzo, foto dell'immobile, logo o interfaccia
    Airbnb ricostruiti, finti screenshot;
  - nessun punteggio aggregato, da nessuna parte.
"""

FUME_DEEP = '#2E2A25'
FUME      = '#3F3A33'
FUME_MID  = '#4a443a'
ORO       = '#C8A24B'
ORO_TESTO = '#86692A'    # oro leggibile SU SABBIA (su chiaro #C8A24B fa 2,25:1)
SABBIA    = '#F5F0E6'
BIANCO    = '#FFFFFF'
INK       = '#26241F'
INK_3     = '#6f695c'

T1 = 'rgba(255,255,255,0.88)'
T2 = 'rgba(255,255,255,0.80)'
T3 = 'rgba(255,255,255,0.72)'
T4 = 'rgba(255,255,255,0.62)'
T5 = 'rgba(255,255,255,0.55)'

VUOTO = 'rgba(255,255,255,0.30)'          # anello spento
FILO_SPENTO = 'rgba(255,255,255,0.18)'    # filo oltre l'anello acceso

AR = "'Archivo', 'Helvetica Neue', Arial, sans-serif"
MA = "'Manrope', 'Helvetica Neue', Arial, sans-serif"

HEAD = """<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
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

# Fondo: il vertice chiaro del gradiente sta in ALTO AL CENTRO, sotto la
# catena, non piu' in alto a sinistra. E' la luce che tiene su il lockup.
GRAD = ('radial-gradient(ellipse 76%% 34%% at 50%% 16%%, rgba(200,162,75,0.13), transparent 72%%), '
        'radial-gradient(120%% 80%% at 50%% 12%%, %s 0%%, %s 52%%, %s 100%%)'
        % (FUME_MID, FUME, FUME_DEEP))


def frame(w, h, bg=None):
    return ('  <div class="frame" style="position: relative; width: %dpx; height: %dpx; '
            'overflow: hidden; background: %s;">\n' % (w, h, bg or GRAD))


def chiudi():
    return '  </div>\n'


# ------------------------------------------------------------------ lockup
def marchio(y=112, colore=BIANCO, w=1080):
    """CENTRATO. E' il primo segnale che questa e' un'altra giornata."""
    return ('  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: center; '
            'font-family: %s; font-weight: 800; font-size: 33px; letter-spacing: 9px; '
            'color: %s;">HADRIANUS</div>\n'
            '  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: center; '
            'font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 7px; '
            'color: %s;">MULTISERVICE</div>\n'
            % (y, AR, colore, y + 44, MA, T3))


ETICHETTE = ('RECENSIONE', 'VISIBILITÀ', 'PREZZO', 'CHI PRENOTA')


def catena(y, accesi, d=26, left=64, right=64, w=1080, etichette=False,
           n=4, spessore=3):
    """LA CATENA — l'indice di lettura, costante su tutto il pacchetto.

    `accesi` = quanti anelli sono pieni (0-4). Il filo e' oro fino al centro
    dell'ultimo anello acceso e spento oltre: e' l'avanzamento, e sostituisce
    ogni barra a tacche.
    """
    util = w - left - right
    passo = util - d
    cx = [left + d / 2.0 + passo * i / float(n - 1) for i in range(n)]
    cy = y + d / 2.0
    fine = cx[accesi - 1] if accesi >= 1 else cx[0]

    out = []
    # filo spento (tutta la corsa) e filo acceso (fino all'ultimo pieno)
    out.append('  <div style="position: absolute; left: %.1fpx; width: %.1fpx; top: %.1fpx; '
               'height: %dpx; background: %s; border-radius: 2px;"></div>\n'
               % (cx[0], cx[-1] - cx[0], cy - spessore / 2.0, spessore, FILO_SPENTO))
    if accesi >= 2:
        out.append('  <div style="position: absolute; left: %.1fpx; width: %.1fpx; top: %.1fpx; '
                   'height: %dpx; background: %s; border-radius: 2px;"></div>\n'
                   % (cx[0], fine - cx[0], cy - spessore / 2.0, spessore, ORO))
    for i in range(n):
        pieno = i < accesi
        stile = ('background: %s; border: none;' % ORO if pieno
                 else 'background: %s; border: %dpx solid %s;' % (FUME_DEEP, max(2, spessore - 1), VUOTO))
        out.append('  <div style="position: absolute; left: %.1fpx; top: %dpx; width: %dpx; '
                   'height: %dpx; border-radius: 999px; %s"></div>\n'
                   % (cx[i] - d / 2.0, y, d, d, stile))
        if etichette:
            # Le etichette agli estremi si ancorano al margine, non al centro
            # dell'anello: centrate uscirebbero dal frame.
            # Etichette a larghezza di contenuto: agli estremi ancorate al
            # margine, in mezzo centrate sull'anello con translateX(-50%).
            # Con box a larghezza fissa si accavallavano sul passo stretto.
            if i == 0:
                pos = 'left: %dpx;' % left
            elif i == n - 1:
                pos = 'right: %dpx;' % right
            else:
                pos = 'left: %.1fpx; transform: translateX(-50%%);' % cx[i]
            out.append('  <div style="position: absolute; %s top: %dpx; white-space: nowrap; '
                       'font-family: %s; font-weight: 600; font-size: 17px; '
                       'letter-spacing: 0.16em; text-transform: uppercase; color: %s;">%s</div>\n'
                       % (pos, y + d + 18, MA, ORO if pieno else T5, ETICHETTE[i]))
    return ''.join(out)


def anello_grande(y, numero, etichetta, d=104, acceso=True, w=1080):
    """L'anello singolo, grande e centrato: e' il ritmo delle STORIE.

    Una storia non e' un percorso, e' un punto della catena: quindi un solo
    anello, grande, con dentro il numero. Stesso vocabolario, terzo ritmo.
    """
    if acceso:
        cerchio = ('background: %s; color: %s;' % (ORO, FUME_DEEP))
    else:
        cerchio = ('background: transparent; border: 3px solid %s; color: %s;' % (ORO, ORO))
    return ('  <div style="position: absolute; left: %.1fpx; top: %dpx; width: %dpx; height: %dpx; '
            'border-radius: 999px; display: flex; align-items: center; justify-content: center; '
            'font-family: %s; font-weight: 900; font-size: 45px; letter-spacing: -1px; %s">%s</div>\n'
            '  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: center; '
            'font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 0.18em; '
            'text-transform: uppercase; color: %s;">%s</div>\n'
            % (w / 2.0 - d / 2.0, y, d, d, AR, cerchio, numero,
               y + d + 16, MA, ORO, etichetta))


# ------------------------------------------------------------------- testo
def blocco(righe, y, size, peso, colore=BIANCO, font=None, left=64, right=64,
           lh=1.16, tracking=-0.4, allinea='left'):
    font = font or AR
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'text-align: %s; font-family: %s; font-weight: %d; font-size: %dpx; '
            'line-height: %s; letter-spacing: %spx; color: %s;">%s</div>\n'
            % (left, right, y, allinea, font, peso, size, lh, tracking, colore, corpo))


def kicker(testo, y, left=64, right=64, colore=ORO, size=31, allinea='left'):
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'text-align: %s; font-family: %s; font-weight: 600; font-size: %dpx; '
            'letter-spacing: 0.18em; text-transform: uppercase; color: %s;">%s</div>\n'
            % (left, right, y, allinea, MA, size, colore, testo))


def filo_oro(y, larghezza=180, left=64, h=3, colore=ORO):
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; width: %dpx; '
            'height: %dpx; background: %s; border-radius: 2px;"></div>\n'
            % (left, y, larghezza, h, colore))


def fonte(righe, y, left=64, right=64, size=17, colore=T4):
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'font-family: %s; font-weight: 500; font-size: %dpx; line-height: 1.42; '
            'color: %s;">%s</div>\n' % (left, right, y, MA, size, colore, corpo))


# ------------------------------------------------------- la card recensione
def stelle(y, left=64, size=31, colore=ORO, allinea='left', right=64):
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'text-align: %s; font-size: %dpx; letter-spacing: 6px; color: %s; '
            'line-height: 1;">★★★★★</div>\n'
            % (left, right, y, allinea, size, colore))


def card_recensione(y, righe, meta, traduzione=True, left=64, right=64,
                    size=38, size_meta=31, lh=1.34, pad_v=34, pad_h=40):
    """L'ELEMENTO CHE ROMPE: sabbia su fumè, bordo sinistro oro da 6 px.

    Unica zona luminosa dell'artboard. Nessun logo, nessuna interfaccia, nessun
    avatar, nessun punteggio aggregato: e' chiaramente grafica Hadrianus, non la
    riproduzione di uno screenshot.
    """
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    trad = ''
    if traduzione:
        trad = ('<div style="font-family: %s; font-weight: 500; font-size: 17px; '
                'letter-spacing: 0.04em; color: %s; margin-top: 8px;">traduzione di Airbnb</div>'
                % (MA, INK_3))
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'background: %s; border-left: 6px solid %s; border-radius: 6px 20px 20px 6px; '
            'padding: %dpx %dpx %dpx %dpx; box-shadow: 0 18px 48px rgba(20,17,13,0.34);">'
            '<div style="font-family: %s; font-weight: 500; font-size: %dpx; line-height: %s; '
            'letter-spacing: -0.2px; color: %s;">%s</div>'
            '<div style="margin-top: 22px; font-family: %s; font-weight: 600; font-size: %dpx; '
            'letter-spacing: 0.02em; color: %s;">%s</div>%s</div>\n'
            % (left, right, y, SABBIA, ORO, pad_v, pad_h, pad_v, pad_h - 6,
               MA, size, lh, INK, corpo, MA, size_meta, ORO_TESTO, meta, trad))


# ----------------------------------------------------------------- superfici
def fascia_sabbia(y, righe, left=64, right=64, size=33, pad_v=34, pad_h=40,
                  lh=1.42, peso=600, evidenza=None):
    """Fascia chiara piena: la usano SOLO le artboard senza card recensione."""
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'background: %s; border-radius: 20px; padding: %dpx %dpx;">'
            '<div style="font-family: %s; font-weight: %d; font-size: %dpx; line-height: %s; '
            'letter-spacing: -0.2px; color: %s;">%s</div></div>\n'
            % (left, right, y, SABBIA, pad_v, pad_h, MA, peso, size, lh, INK, corpo))


def cta_pillola(y, testo, h=90, left=64, right=64, size=40):
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
            'background: %s; border-radius: 999px; display: flex; align-items: center; '
            'justify-content: center; font-family: %s; font-weight: 800; font-size: %dpx; '
            'letter-spacing: 0.06em; text-transform: uppercase; color: %s;">%s</div>\n'
            % (left, right, y, h, ORO, AR, size, FUME_DEEP, testo))


def evidenziatore(righe, y, size, peso=900, left=64, right=64, font=None, lh=1.14,
                  allinea='center'):
    """Testo su banda oro che corre: e' l'unico evidenziatore del pacchetto
    (scena 7 del reel). Il testo passa a fumè profondo."""
    font = font or AR
    corpo = ''.join('<span style="display: inline; background: %s; color: %s; '
                    'box-decoration-break: clone; -webkit-box-decoration-break: clone; '
                    'padding: 4px 12px; border-radius: 4px;">%s</span><br>' % (ORO, FUME_DEEP, r)
                    for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'text-align: %s; font-family: %s; font-weight: %d; font-size: %dpx; '
            'line-height: %s; letter-spacing: -0.5px;">%s</div>\n'
            % (left, right, y, allinea, font, peso, size, lh, corpo))


def scrivi(percorso, corpo):
    with open(percorso, 'w') as f:
        f.write(HEAD + corpo + chiudi() + FOOT)
