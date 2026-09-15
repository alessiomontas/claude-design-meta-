# Reel "Il calendario di Roma" — 18,0 s, Struttura C di .claude/reference/reel-virali.md.
#
# Regole di quel manuale, applicate qui perche' i due reel precedenti sono stati
# bocciati come "poveri" proprio per la loro assenza:
#  - il frame 0 non e' uno stato di riposo: la prima notifica e' gia' a meta' corsa
#  - almeno 3 eventi nei primi 2 s (qui 5) e piu' grammatiche di movimento (qui 7)
#  - easing che decelera, mai lineare: l'easing lineare e' la firma dell'amatoriale
#  - il testo entra con maschera/traslazione e esce A TAGLIO, mai in dissolvenza
#  - curva di accelerazione + 400 ms di immobilita' dopo ogni picco
#  - loop di stato: l'ultimo fotogramma torna identico al primo
#
# Lo scrubbing regge perche' OGNI animazione dura quanto il reel e usa fill-mode
# both: lo stato a un dato istante non dipende dall'ordine di partenza.
import os

D = 18.0
HERE = os.path.dirname(os.path.abspath(__file__))
G = '../grafiche/'

FUME_DEEP = '#2E2A25'
FUME      = '#3F3A33'
FUME_CARD = '#4A443C'
ORO       = '#C8A24B'
SABBIA    = '#F5F0E6'
T_CHIARO  = '#E6DFD4'
AR = "'Archivo','Helvetica Neue',Arial,sans-serif"
MA = "'Manrope','Helvetica Neue',Arial,sans-serif"

EASE = 'cubic-bezier(.16,1,.3,1)'          # decelera forte: il movimento "di qualita'"
OMBRA = ('text-shadow:0 3px 10px rgba(0,0,0,.68),0 12px 44px rgba(0,0,0,.55),'
         '0 1px 2px rgba(0,0,0,.85);')


def p(t):
    return round(max(0.0, min(D, t)) / D * 100, 4)


def kf(nome, passi):
    """passi: (secondi, css) oppure (secondi, css, easing_del_segmento_seguente)."""
    righe = []
    for x in passi:
        t, css = x[0], x[1]
        e = x[2] if len(x) > 2 else None
        if e:
            css = css + '; animation-timing-function: ' + e
        righe.append('  %s%% { %s }' % (p(t), css))
    return '@keyframes %s {\n%s\n}\n' % (nome, '\n'.join(righe))


def anim(*nomi):
    return 'animation: ' + ', '.join('%s %ss linear both' % (n, D) for n in nomi) + ';'


# ---------------------------------------------------------------- contenuti
NOTIFICHE = [  # (testo, istante di entrata)
    ('Richiesta · 24 ottobre',  -0.22),   # negativo: al frame 0 e' gia' a meta' corsa
    ('Richiesta · 3 novembre',   0.50),
    ('Richiesta · 8 dicembre',   1.10),
    ('Richiesta · 25 ottobre',   1.60),
    ('Richiesta · 1 novembre',   2.10),
    ('Richiesta · 7 dicembre',   2.50),
]
GANCIO = ['Ci sono notti', 'che valgono il doppio.']
RIBALTA = ['A', 'Roma', 'il', 'prezzo', 'lo', 'decide', 'il', 'calendario.']
FASI = [
    ('01', 'Il calendario di Roma', 'Fiere, festival, ponti, feste.',            5.0),
    ('02', 'La base e il minimo',   'Sotto una soglia non si scende.',           6.6),
    ('03', 'Le date calde',         'Una notte di evento fa storia a sé.',       8.2),
    ('04', 'Ogni giorno, di nuovo', 'Si guarda la città e si corregge.',         9.8),
]
CHIAVE_PRE = 'Il calendario di Roma '
CHIAVE_EVID = 'lo teniamo noi.'
CTA = 'Scrivi CALCOLO in DM'
FIRMA = 'Guadagniamo solo se guadagni tu.'

CAL_COL, CAL_RIG = 7, 5
CAL_ONDA_IN, CAL_ONDA_DUR = 12.2, 0.9


def costruisci():
    k = ''

    # ---- notifiche: entrata con overshoot, poi scivolano giu' e sbiadiscono
    for i, (_, t0) in enumerate(NOTIFICHE):
        giu = 'translateY(%dpx) scale(1)' % (i * 8)
        k += kf('not%d' % i, [
            (0, 'opacity:0; transform: translateY(-40px) scale(.94)', EASE),
            (max(0, t0 - 0.001),
             'opacity:0; transform: translateY(-40px) scale(.94)', EASE),
            (t0 + 0.22, 'opacity:1; transform: translateY(0) scale(1)', EASE),
            (2.8, 'opacity:%s; transform: %s' % ('1' if i == 5 else '.45', giu), EASE),
            (3.2, 'opacity:%s; transform: translateY(%dpx) scale(1)'
                  % ('1' if i == 5 else '.45', i * 8 - 6)),
            (3.201, 'opacity:0; transform: translateY(-40px) scale(.94)'),   # stacco netto
            (D, 'opacity:0; transform: translateY(-40px) scale(.94)'),
        ])
    # il loop: la prima notifica ricomincia a entrare negli ultimi 400 ms
    k += kf('not_loop', [
        (0, 'opacity:0; transform: translateY(-40px) scale(.94)'),
        (17.599, 'opacity:0; transform: translateY(-40px) scale(.94)', EASE),
        (17.82, 'opacity:1; transform: translateY(0) scale(1)'),
        (D, 'opacity:1; transform: translateY(0) scale(1)'),
    ])

    # ---- gancio in maschera dal basso + filo oro che si disegna
    k += kf('gancio', [
        (0, 'opacity:0; clip-path: inset(100% 0 0 0)'),
        (1.099, 'opacity:0; clip-path: inset(100% 0 0 0)', EASE),
        (1.28, 'opacity:1; clip-path: inset(0 0 0 0)'),
        (3.2, 'opacity:1; clip-path: inset(0 0 0 0)'),
        (3.201, 'opacity:0; clip-path: inset(0 0 0 0)'),
        (D, 'opacity:0; clip-path: inset(0 0 0 0)'),
    ])
    k += kf('filo_gancio', [
        (0, 'transform: scaleX(0)'),
        (1.28, 'transform: scaleX(0)', EASE),
        (1.5, 'transform: scaleX(1)'),
        (3.2, 'transform: scaleX(1)'),
        (3.201, 'transform: scaleX(0)'),
        (D, 'transform: scaleX(0)'),
    ])

    # ---- frase che ribalta: parola per parola, in accumulo
    for i, _ in enumerate(RIBALTA):
        t0 = 3.2 + i * 0.17
        k += kf('par%d' % i, [
            (0, 'opacity:0; transform: translateY(12px)'),
            (max(0, t0 - 0.001), 'opacity:0; transform: translateY(12px)', EASE),
            (t0 + 0.16, 'opacity:1; transform: translateY(0)'),
            (4.8, 'opacity:1; transform: translateY(0)'),
            (4.801, 'opacity:0; transform: translateY(12px)'),          # esce a taglio
            (D, 'opacity:0; transform: translateY(12px)'),
        ])

    # ---- kicker con kerning che si chiude
    k += kf('kicker', [
        (0, 'opacity:0; letter-spacing:.4em'),
        (4.799, 'opacity:0; letter-spacing:.4em', EASE),
        (5.2, 'opacity:1; letter-spacing:.02em'),
        (11.4, 'opacity:1; letter-spacing:.02em'),
        (11.401, 'opacity:0; letter-spacing:.02em'),
        (D, 'opacity:0; letter-spacing:.02em'),
    ])

    # ---- barra di avanzamento a scatti di 1/4, con scatto di scala sul quarto
    passi = [(0, 'transform: scaleX(0) scaleY(1)'), (4.999, 'transform: scaleX(0) scaleY(1)', EASE)]
    for i, (_, _, _, t0) in enumerate(FASI):
        passi.append((t0 + 0.18, 'transform: scaleX(%.2f) scaleY(1)' % ((i + 1) / 4.0), EASE))
        if i == 3:
            passi.append((t0 + 0.30, 'transform: scaleX(1) scaleY(1.08)', EASE))
            passi.append((t0 + 0.48, 'transform: scaleX(1) scaleY(1)'))
        if i < 3:
            passi.append((FASI[i + 1][3] - 0.001, 'transform: scaleX(%.2f) scaleY(1)'
                          % ((i + 1) / 4.0), EASE))
    passi += [(11.4, 'transform: scaleX(1) scaleY(1)'),
              (11.401, 'transform: scaleX(0) scaleY(1)'), (D, 'transform: scaleX(0) scaleY(1)')]
    k += kf('barra', passi)

    # ---- fasi: il numero scorre in maschera (esce in alto, entra dal basso)
    for i, (_, _, _, t0) in enumerate(FASI):
        t1 = FASI[i + 1][3] if i < 3 else 11.4
        k += kf('num%d' % i, [
            (0, 'opacity:0; transform: translateY(100%)'),
            (max(0, t0 - 0.001), 'opacity:0; transform: translateY(100%)', EASE),
            (t0 + 0.20, 'opacity:1; transform: translateY(0)'),
            (max(0, t1 - 0.20), 'opacity:1; transform: translateY(0)', EASE),
            (t1, 'opacity:0; transform: translateY(-100%)'),
            (D, 'opacity:0; transform: translateY(-100%)'),
        ])
        for j, rit in enumerate((0.10, 0.35)):     # titolo e dettaglio sfasati
            k += kf('fase%d_%d' % (i, j), [
                (0, 'opacity:0; transform: translateX(28px)'),
                (max(0, t0 + rit - 0.001), 'opacity:0; transform: translateX(28px)', EASE),
                (t0 + rit + 0.18, 'opacity:1; transform: translateX(0)'),
                (max(0, t1 - 0.001), 'opacity:1; transform: translateX(0)'),
                (t1, 'opacity:0; transform: translateX(0)'),
                (D, 'opacity:0; transform: translateX(0)'),
            ])
    # micro-zoom del fondo durante la fase 03: terza grammatica di movimento
    k += kf('zoom_fondo', [
        (0, 'transform: scale(1.00)'), (8.2, 'transform: scale(1.00)', 'ease-in-out'),
        (9.8, 'transform: scale(1.03)'), (D, 'transform: scale(1.03)'),
    ])

    # ---- compressione delle quattro fasi in alto
    k += kf('compressa', [
        (0, 'opacity:0; transform: scale(1)'),
        (11.399, 'opacity:0; transform: scale(1)', EASE),
        (11.8, 'opacity:.4; transform: scale(.25)'),
        (17.2, 'opacity:.4; transform: scale(.25)'),
        (17.6, 'opacity:0; transform: scale(.25)'),
        (D, 'opacity:0; transform: scale(.25)'),
    ])

    # ---- calendario: entra in maschera, poi le celle si riempiono a onda
    k += kf('cal', [
        (0, 'opacity:0; clip-path: inset(100% 0 0 0); filter: blur(0px)'),
        (11.799, 'opacity:0; clip-path: inset(100% 0 0 0); filter: blur(0px)', EASE),
        (12.02, 'opacity:1; clip-path: inset(0 0 0 0); filter: blur(0px)'),
        (15.4, 'opacity:1; clip-path: inset(0 0 0 0); filter: blur(0px)', EASE),
        (15.7, 'opacity:1; clip-path: inset(0 0 0 0); filter: blur(10px)'),
        (17.2, 'opacity:1; clip-path: inset(0 0 0 0); filter: blur(10px)', EASE),
        (17.6, 'opacity:0; clip-path: inset(0 0 0 0); filter: blur(0px)'),
        (D, 'opacity:0; clip-path: inset(0 0 0 0); filter: blur(0px)'),
    ])
    n_diag = CAL_COL + CAL_RIG - 1
    for d in range(n_diag):
        t0 = CAL_ONDA_IN + (d / float(n_diag - 1)) * CAL_ONDA_DUR
        k += kf('cella%d' % d, [
            (0, 'background:%s; transform: scale(1)' % FUME_CARD),
            (max(0, t0 - 0.001), 'background:%s; transform: scale(1)' % FUME_CARD, EASE),
            (t0 + 0.10, 'background:%s; transform: scale(1.14)' % ORO, EASE),
            (t0 + 0.22, 'background:%s; transform: scale(1)' % ORO),
            (D, 'background:%s; transform: scale(1)' % ORO),
        ])

    # ---- riga chiave + evidenziatore che corre
    k += kf('chiave', [
        (0, 'opacity:0; clip-path: inset(100% 0 0 0)'),
        (13.599, 'opacity:0; clip-path: inset(100% 0 0 0)', EASE),
        (13.82, 'opacity:1; clip-path: inset(0 0 0 0)'),
        (17.2, 'opacity:1; clip-path: inset(0 0 0 0)'),
        (17.201, 'opacity:0; clip-path: inset(0 0 0 0)'),
        (D, 'opacity:0; clip-path: inset(0 0 0 0)'),
    ])
    k += kf('evid', [
        (0, 'background-size: 0% 100%; color:#FFF'),
        (13.9, 'background-size: 0% 100%; color:#FFF', EASE),
        (14.03, 'background-size: 50%% 100%%; color:%s' % FUME_DEEP, EASE),
        (14.16, 'background-size: 100%% 100%%; color:%s' % FUME_DEEP),
        (D, 'background-size: 100%% 100%%; color:%s' % FUME_DEEP),
    ])

    # ---- CTA: entra dal basso, si ferma di colpo, poi si ritira
    k += kf('cta', [
        (0, 'opacity:0; transform: translateY(90px)'),
        (15.699, 'opacity:0; transform: translateY(90px)', EASE),
        (15.96, 'opacity:1; transform: translateY(0)'),
        (17.2, 'opacity:1; transform: translateY(0)', EASE),
        (17.6, 'opacity:0; transform: translateY(90px)'),
        (D, 'opacity:0; transform: translateY(90px)'),
    ])
    return k


def html():
    k = costruisci()

    notifiche = ''
    for i, (testo, _) in enumerate(NOTIFICHE):
        notifiche += ('  <div class="nota" style="top:%dpx; %s">%s</div>\n'
                      % (420 + i * 112, anim('not%d' % i), testo))
    notifiche += ('  <div class="nota" style="top:420px; %s">%s</div>\n'
                  % (anim('not_loop'), NOTIFICHE[0][0]))

    parole = ''
    for i, w in enumerate(RIBALTA):
        col = ORO if w.startswith('calendario') else '#FFF'
        parole += ('<span style="display:inline-block; color:%s; %s">%s</span> '
                   % (col, anim('par%d' % i), w))

    fasi = ''
    for i, (num, titolo, dett, _) in enumerate(FASI):
        fasi += ('  <div class="numwrap"><div class="num" style="%s">%s</div></div>\n'
                 % (anim('num%d' % i), num))
        fasi += ('  <div class="ftit" style="%s">%s</div>\n' % (anim('fase%d_0' % i), titolo))
        fasi += ('  <div class="fdet" style="%s">%s</div>\n' % (anim('fase%d_1' % i), dett))

    celle = ''
    for r in range(CAL_RIG):
        for c in range(CAL_COL):
            celle += '<div class="cella" style="%s"></div>' % anim('cella%d' % (r + c))

    compressa = ''.join('<span>%s</span>' % f[0] for f in FASI)

    css = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;background:%(fd)s}
.stage{position:relative;width:1080px;height:1920px;overflow:hidden;
  background:radial-gradient(120%% 80%% at 50%% 8%%, %(f)s 0%%, %(fd)s 62%%)}
.sfondo{position:absolute;inset:0;background-image:url(%(g)scamera-9x16.jpg);
  background-size:cover;background-position:center;opacity:.13;filter:saturate(.45) brightness(.62)}
.marchio{position:absolute;left:0;right:0;text-align:center;color:#fff;%(ombra)s}
.h{top:112px;font-family:%(ar)s;font-weight:800;font-size:33px;letter-spacing:10px}
.m{top:176px;font-family:%(ma)s;font-weight:600;font-size:17px;letter-spacing:7px;color:rgba(255,255,255,.86)}
.barra-sfondo{position:absolute;left:64px;right:64px;top:250px;height:6px;border-radius:3px;
  background:rgba(87,80,71,.45)}
.barra{position:absolute;left:64px;right:64px;top:250px;height:6px;border-radius:3px;
  background:%(oro)s;transform-origin:left center}
.nota{position:absolute;left:64px;right:64px;height:96px;border-radius:20px;background:%(card)s;
  border:1px solid rgba(200,162,75,.28);display:flex;align-items:center;padding:0 34px;gap:18px;
  font-family:%(ma)s;font-weight:600;font-size:40px;color:#fff;
  box-shadow:0 18px 40px rgba(0,0,0,.35)}
.nota::before{content:'';width:14px;height:14px;border-radius:50%%;background:%(oro)s;flex:0 0 auto}
.gancio{position:absolute;left:64px;right:64px;top:1180px;font-family:%(ar)s;font-weight:900;
  font-size:70px;line-height:1.13;letter-spacing:-.4px;color:#fff;%(ombra)s}
.filo{position:absolute;left:64px;width:952px;top:1352px;height:3px;background:%(oro)s;
  transform-origin:left center}
.ribalta{position:absolute;left:64px;right:64px;top:820px;font-family:%(ar)s;font-weight:900;
  font-size:70px;line-height:1.18;letter-spacing:-.4px;text-align:center;%(ombra)s}
.kicker{position:absolute;left:0;right:0;top:330px;text-align:center;font-family:%(ma)s;
  font-weight:600;font-size:17px;text-transform:uppercase;color:%(oro)s}
.numwrap{position:absolute;left:64px;top:700px;width:300px;height:250px;overflow:hidden}
.num{font-family:%(ar)s;font-weight:900;font-size:240px;line-height:1;color:%(oro)s}
.ftit{position:absolute;left:380px;right:56px;top:742px;font-family:%(ar)s;font-weight:800;
  font-size:62px;line-height:1.1;color:#fff;letter-spacing:-.4px}
.fdet{position:absolute;left:380px;right:56px;top:952px;font-family:%(ma)s;font-weight:600;
  font-size:40px;line-height:1.25;color:%(tc)s}
.compressa{position:absolute;left:0;right:0;top:330px;text-align:center;font-family:%(ar)s;
  font-weight:900;font-size:240px;color:%(oro)s;transform-origin:center top}
.compressa span{margin:0 14px}
.calwrap{position:absolute;left:64px;top:760px;width:952px}
.cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:12px}
.cella{aspect-ratio:1;border-radius:14px;background:%(card)s}
.chiave{position:absolute;left:64px;right:64px;top:1330px;font-family:%(ar)s;font-weight:800;
  font-size:62px;line-height:1.14;letter-spacing:-.4px;color:#fff;%(ombra)s}
.evid{background-image:linear-gradient(%(oro)s,%(oro)s);background-repeat:no-repeat;
  background-position:left center;background-size:0%% 100%%;padding:2px 10px;margin:0 -4px;
  border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.cta{position:absolute;left:64px;right:64px;top:1470px;height:120px;border-radius:999px;
  background:%(oro)s;display:flex;align-items:center;justify-content:center;font-family:%(ma)s;
  font-weight:700;font-size:45px;letter-spacing:1px;text-transform:uppercase;color:%(fd)s}
.firma{position:absolute;left:0;right:0;top:1616px;text-align:center;font-family:%(ma)s;
  font-weight:600;font-size:31px;color:%(tc)s}
""" % dict(fd=FUME_DEEP, f=FUME, card=FUME_CARD, oro=ORO, tc=T_CHIARO, ar=AR, ma=MA,
           g=G, ombra=OMBRA)

    return """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
<style>%(css)s
%(kf)s</style></head><body><div class="stage">
  <div class="sfondo" style="%(zoom)s"></div>
  <div class="marchio h">HADRIANUS</div>
  <div class="marchio m">MULTISERVICE</div>
  <div class="barra-sfondo"></div>
  <div class="barra" style="%(barra)s"></div>

%(notifiche)s
  <div class="gancio" style="%(gancio)s">%(g1)s<br>%(g2)s</div>
  <div class="filo" style="%(filo)s"></div>

  <div class="ribalta">%(parole)s</div>
  <div class="kicker" style="%(kicker)s">IL PREZZO, IN ORDINE</div>
%(fasi)s
  <div class="compressa" style="%(compressa)s">%(comp)s</div>

  <div class="calwrap" style="%(cal)s"><div class="cal">%(celle)s</div></div>
  <div class="chiave" style="%(chiave)s">%(cpre)s<span class="evid" style="%(evid)s">%(cevid)s</span></div>

  <div class="cta" style="%(cta)s">%(ctatxt)s</div>
  <div class="firma" style="%(cta)s">%(firma)s</div>
</div></body></html>
""" % dict(css=css, kf=k, notifiche=notifiche, parole=parole, fasi=fasi, celle=celle,
           comp=compressa, g1=GANCIO[0], g2=GANCIO[1], cpre=CHIAVE_PRE, cevid=CHIAVE_EVID,
           ctatxt=CTA, firma=FIRMA,
           zoom=anim('zoom_fondo'), barra=anim('barra'), gancio=anim('gancio'),
           filo=anim('filo_gancio'), kicker=anim('kicker'), compressa=anim('compressa'),
           cal=anim('cal'), chiave=anim('chiave'), evid=anim('evid'), cta=anim('cta'))


if __name__ == '__main__':
    with open(os.path.join(HERE, 'reel.html'), 'w') as f:
        f.write(html())
    print('reel.html — %.1f s · %d notifiche · %d fasi · calendario %dx%d'
          % (D, len(NOTIFICHE), len(FASI), CAL_COL, CAL_RIG))
