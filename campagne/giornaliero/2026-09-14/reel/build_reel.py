# Genera reel.html — la pagina animata da cui anima_reel.py ricava l'MP4.
#
# Regola che tiene in piedi lo scrubbing: OGNI animazione dura quanto il reel
# (D secondi) e usa fill-mode both. Cosi' lo stato a un dato istante non dipende
# dall'ordine in cui partono le animazioni, e il fotogramma a t e' deterministico.
# Le percentuali dei keyframe si calcolano da secondi/D — mai a mano.
import os

D = 15.6                                   # durata del reel
HERE = os.path.dirname(os.path.abspath(__file__))
G = '../grafiche/'                         # le foto stanno accanto alle artboard

FUME_DEEP = '#2E2A25'
FUME      = '#3F3A33'
ORO       = '#C8A24B'
SABBIA    = '#F5F0E6'
AR = "'Archivo','Helvetica Neue',Arial,sans-serif"
MA = "'Manrope','Helvetica Neue',Arial,sans-serif"

BAND_Y, BAND_H = 470, 810                  # banda nitida centrata nel 9:16


def p(t):
    """secondi -> percentuale di keyframe"""
    return round(t / D * 100, 4)


def kf(nome, passi):
    """passi: lista di (secondi, css)"""
    corpo = '\n'.join('  %s%% { %s }' % (p(t), css) for t, css in passi)
    return '@keyframes %s {\n%s\n}\n' % (nome, corpo)


def anim(*nomi):
    """Una sola proprieta' `animation` con i valori separati da virgola: dichiararla
    piu' volte sullo stesso elemento farebbe vincere solo l'ultima."""
    return 'animation: ' + ', '.join('%s %ss linear both' % (n, D) for n in nomi) + ';'


# ----------------------------------------------------------------- scene
# (id, inizio, fine, righe di testo)
SCENE = [
    ('s1',  0.0,  1.6, ['Foto col telefono.']),
    ('s2',  1.6,  3.2, ['È la prima cosa', 'che vede chi cerca.']),
    ('s3',  3.2,  4.8, ['E decide lì.']),
    ('s4',  4.8,  7.0, ['Guarda.']),
    ('s5',  7.0,  8.6, ['Stessa stanza.', 'Altro annuncio.']),
    ('s6',  8.6, 10.2, ['Cambia solo', 'chi tiene la macchina.']),
    ('s7', 10.2, 12.0, ['Ti garantiamo', 'il servizio fotografico.']),
    ('s8', 12.0, 13.6, ['Dentro la gestione.', 'Non lo paghi a parte.']),
    ('s9', 13.6, 15.6, ['Gestione completa.', '15% sul fatturato.']),
]
FINE_GUARDA = 5.4          # "Guarda." esce quando parte la tendina
TENDINA_IN, TENDINA_OUT = 5.4, 6.6


def testo_keyframes():
    """Ogni blocco di testo entra da sotto in 0,18 s e sparisce a fine scena."""
    out = ''
    for sid, t0, t1, _ in SCENE:
        fine = FINE_GUARDA if sid == 's4' else t1
        entra = t0 + 0.35 if sid == 's1' else t0 + 0.08
        out += kf('t_' + sid, [
            (0,            'opacity:0; transform:translateY(38px)'),
            (max(0, entra - 0.001), 'opacity:0; transform:translateY(38px)'),
            (entra + 0.18, 'opacity:1; transform:translateY(0)'),
            (max(0, fine - 0.12),   'opacity:1; transform:translateY(0)'),
            (fine,         'opacity:0; transform:translateY(-16px)'),
            (D,            'opacity:0; transform:translateY(-16px)'),
        ])
    return out


def visibilita(nome, t0, t1, dissolvenza=0.12):
    """Compare/scompare secco, con una micro-dissolvenza per non sfarfallare."""
    if t0 <= 0:
        passi = [(0, 'opacity:1')]
    else:
        passi = [(0, 'opacity:0'), (max(0, t0 - 0.001), 'opacity:0'),
                 (min(t0 + dissolvenza, t1), 'opacity:1')]
    passi.append((max(t0, t1 - dissolvenza), 'opacity:1'))
    passi.append((t1, 'opacity:0'))
    if t1 < D:
        passi.append((D, 'opacity:0'))
    return kf(nome, passi)


def tremolio():
    """Timeline unica del transform della foto degradata: mano libera + push-in.
    Tremolio e push-in non possono stare in due animazioni separate — animano la
    stessa proprieta' e vincerebbe solo l'ultima dichiarata.
    La scala parte da 1,10 perche' una foto ruotata dentro un riquadro scoprirebbe
    gli angoli."""
    import math
    passi, t = [], 0.0
    while t <= 4.8:
        if t < 1.6:
            amp, scala = 6.0, 1.10 + 0.02 * (t / 1.6)
        elif t < 3.2:
            amp, scala = 3.0, 1.12 + 0.02 * ((t - 1.6) / 1.6)
        else:
            amp, scala = 0.0, 1.14 + 0.03 * ((t - 3.2) / 1.6)
        dx = amp * math.sin(t * 2 * math.pi * 2.0)
        dy = amp * 0.6 * math.sin(t * 2 * math.pi * 2.0 + 1.1)
        rot = -3.5
        if 0.75 <= t < 1.05:            # prova a raddrizzarsi...
            rot = -3.5 + 2.4 * ((t - 0.75) / 0.30)
        elif 1.05 <= t < 1.35:          # ...e ricade
            rot = -1.1 - 2.4 * ((t - 1.05) / 0.30)
        passi.append((round(t, 3),
                      'transform: translate(%.2fpx,%.2fpx) rotate(%.2fdeg) scale(%.3f)'
                      % (dx, dy, rot, scala)))
        t += 0.08
    passi.append((D, 'transform: translate(0,0) rotate(-3.5deg) scale(1.17)'))
    return kf('tremolio', passi)


CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;background:%(fume_deep)s}
.stage{position:relative;width:1080px;height:1920px;overflow:hidden;background:%(fume_deep)s}
.fondo{position:absolute;inset:-8%%;width:116%%;height:116%%;object-fit:cover;
  filter:blur(38px) saturate(.55) brightness(.42);}
.velo{position:absolute;inset:0;background:
  radial-gradient(ellipse 92%% 30%% at 50%% 48%%, rgba(26,23,19,.50) 0%%, rgba(26,23,19,.26) 46%%, rgba(26,23,19,0) 70%%),
  linear-gradient(180deg, rgba(46,42,37,.90) 0%%, rgba(46,42,37,.34) 30%%, rgba(46,42,37,.40) 64%%, rgba(46,42,37,.94) 100%%);}
.banda{position:absolute;left:0;top:%(band_y)spx;width:1080px;height:%(band_h)spx;overflow:hidden;
  box-shadow:0 30px 90px rgba(0,0,0,.55);}
.banda img{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover}
.pro-wrap{position:absolute;inset:0;overflow:hidden}
.marchio{position:absolute;left:0;right:0;text-align:center;color:#fff;
  text-shadow:0 3px 10px rgba(0,0,0,.68),0 12px 44px rgba(0,0,0,.55)}
.h{top:112px;font-family:%(ar)s;font-weight:800;font-size:33px;letter-spacing:10px}
.m{top:176px;font-family:%(ma)s;font-weight:600;font-size:17px;letter-spacing:7px;color:rgba(255,255,255,.86)}
.binario{position:absolute;left:379px;top:220px;width:322px;height:3px;background:rgba(245,240,230,.24)}
.barra{position:absolute;left:379px;top:220px;height:3px;background:%(oro)s;transform-origin:left center;width:322px}
.testo{position:absolute;left:64px;right:64px;top:1360px;text-align:center;
  font-family:%(ar)s;font-weight:900;font-size:70px;line-height:1.13;letter-spacing:-.4px;color:#fff;
  text-shadow:0 3px 10px rgba(0,0,0,.68),0 12px 44px rgba(0,0,0,.55)}
.chip{position:absolute;left:700px;top:%(chip_y)spx;width:316px;height:56px;
  display:flex;align-items:center;justify-content:center;background:rgba(26,23,19,.62);
  border:1px solid rgba(200,162,75,.55);border-radius:999px;
  font-family:%(ma)s;font-weight:600;font-size:17px;letter-spacing:8px;color:%(oro)s}
.tendina{position:absolute;top:%(band_y)spx;height:%(band_h)spx;width:6px;background:%(oro)s;left:0;
  box-shadow:0 0 30px rgba(200,162,75,.75)}
.maniglia{position:absolute;left:-19px;top:%(handle_y)spx;width:44px;height:44px;border-radius:50%%;
  background:%(oro)s;box-shadow:0 0 26px rgba(200,162,75,.8)}
.finale{position:absolute;inset:0;background:radial-gradient(120%% 80%% at 50%% 12%%, %(fume)s 0%%, %(fume_deep)s 70%%)}
.logo{position:absolute;left:340px;top:640px;width:400px;height:400px;object-fit:cover;
  -webkit-mask-image:radial-gradient(ellipse 56%% 56%% at 50%% 48%%, #000 44%%, rgba(0,0,0,0) 74%%);
  mask-image:radial-gradient(ellipse 56%% 56%% at 50%% 48%%, #000 44%%, rgba(0,0,0,0) 74%%)}
.riga-oro{position:absolute;left:64px;right:64px;top:1180px;text-align:center;font-family:%(ar)s;
  font-weight:800;font-size:31px;letter-spacing:2px;color:%(oro)s}
.banda-cta{position:absolute;left:64px;right:64px;top:1290px;height:116px;border-radius:999px;
  background:%(oro)s;display:flex;align-items:center;justify-content:center;
  font-family:%(ar)s;font-weight:800;font-size:40px;color:%(fume_deep)s}
.filo{position:absolute;left:64px;top:1500px;height:3px;background:%(oro)s;width:952px;transform-origin:left center}
""" % dict(fume_deep=FUME_DEEP, fume=FUME, oro=ORO, ar=AR, ma=MA,
           band_y=BAND_Y, band_h=BAND_H, chip_y=BAND_Y + BAND_H - 84,
           handle_y=BAND_H // 2 - 22)


def build():
    k = ''
    # --- fondi sfocati: telefono (0-7), pro (7-10,2), caldo (10,2-13,6)
    k += visibilita('f_tel', 0.0, 7.0)
    k += visibilita('f_pro', 6.6, 10.2)
    k += visibilita('f_cal', 10.2, 13.6)
    # --- banda e livelli
    k += visibilita('b_banda', 0.0, 13.6)
    k += visibilita('b_tel', 0.0, 7.0, 0.05)
    k += visibilita('b_cal', 10.2, 13.6)
    # la foto "pro" non sfuma: viene scoperta dalla tendina
    k += kf('b_pro', [(0, 'opacity:0'), (TENDINA_IN - 0.001, 'opacity:0'),
                      (TENDINA_IN, 'opacity:1'), (10.2, 'opacity:1'),
                      (10.24, 'opacity:0'), (D, 'opacity:0')])
    k += kf('taglio_pro', [
        (0, 'clip-path: inset(0 100% 0 0)'),
        (TENDINA_IN, 'clip-path: inset(0 100% 0 0)'),
        (TENDINA_OUT, 'clip-path: inset(0 0 0 0)'),
        (D, 'clip-path: inset(0 0 0 0)')])
    k += kf('tendina', [
        (0, 'opacity:0; transform: translateX(0)'),
        (TENDINA_IN - 0.001, 'opacity:0; transform: translateX(0)'),
        (TENDINA_IN, 'opacity:1; transform: translateX(0)'),
        (TENDINA_OUT, 'opacity:1; transform: translateX(1074px)'),
        (TENDINA_OUT + 0.18, 'opacity:0; transform: translateX(1074px)'),
        (D, 'opacity:0; transform: translateX(1074px)')])
    k += tremolio()
    # movimenti di camera
    k += kf('push_pro', [(0, 'transform: scale(1.02) translateX(0)'),
                         (7.0, 'transform: scale(1.02) translateX(0)'),
                         (8.6, 'transform: scale(1.04) translateX(0)'),
                         (10.2, 'transform: scale(1.06) translateX(-32px)'),
                         (D, 'transform: scale(1.06) translateX(-32px)')])
    k += kf('sale_cal', [(0, 'transform: translateY(40px)'), (10.2, 'transform: translateY(40px)'),
                         (10.5, 'transform: translateY(0)'), (D, 'transform: translateY(0)')])
    # scatto della scena 3: la colonna di provini si ferma di colpo e rimbalza
    k += kf('scatto', [(0, 'transform: translateY(0)'), (3.2, 'transform: translateY(0)'),
                       (3.62, 'transform: translateY(-12px)'), (3.74, 'transform: translateY(4px)'),
                       (3.82, 'transform: translateY(0)'), (D, 'transform: translateY(0)')])
    k += kf('barra', [(0, 'transform: scaleX(0)'), (D, 'transform: scaleX(1)')])
    k += visibilita('cronaca', 0.0, 13.6)          # marchio + binario spariscono sul finale
    k += kf('chip', [(0, 'opacity:1'), (TENDINA_IN, 'opacity:1'),
                     (TENDINA_OUT, 'opacity:0'), (D, 'opacity:0')])
    # finale
    k += kf('finale', [(0, 'opacity:0'), (13.59, 'opacity:0'), (13.6, 'opacity:1'), (D, 'opacity:1')])
    k += kf('sale_cta', [(0, 'opacity:0; transform: translateY(70px)'),
                         (13.6, 'opacity:0; transform: translateY(70px)'),
                         (13.95, 'opacity:1; transform: translateY(0)'),
                         (D, 'opacity:1; transform: translateY(0)')])
    k += kf('filo', [(0, 'transform: scaleX(0)'), (12.0, 'transform: scaleX(0)'),
                     (12.5, 'transform: scaleX(1)'), (D, 'transform: scaleX(1)')])
    k += visibilita('filo_v', 12.0, 13.6)
    k += testo_keyframes()

    testi = ''
    for sid, t0, t1, righe in SCENE:
        if sid == 's9':
            continue
        corpo = ''.join('<div>%s</div>' % r for r in righe)
        testi += ('<div class="testo" style="%s">%s</div>\n'
                  % (anim('t_' + sid), corpo))

    html = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
<style>%(css)s
%(kf)s</style></head><body><div class="stage">

  <img class="fondo" src="%(g)ssalone-telefono.jpg" style="%(f_tel)s">
  <img class="fondo" src="%(g)ssalone-pro.jpg" style="%(f_pro)s">
  <img class="fondo" src="%(g)ssalotto-caldo-banda.jpg" style="%(f_cal)s">
  <div class="velo"></div>

  <div class="banda" style="%(b_banda)s">
    <div style="position:absolute;inset:0;%(scatto)s">
      <img src="%(g)ssalone-telefono.jpg" style="%(b_tel)s">
    </div>
    <div class="pro-wrap" style="%(taglio)s">
      <img src="%(g)ssalone-pro.jpg" style="%(b_pro)s">
    </div>
    <img src="%(g)ssalotto-caldo-banda.jpg" style="%(b_cal)s">
  </div>
  <div class="tendina" style="%(tendina)s"><div class="maniglia"></div></div>
  <div class="chip" style="%(chip)s">SIMULAZIONE</div>

  <div class="marchio h" style="%(cronaca)s">HADRIANUS</div>
  <div class="marchio m" style="%(cronaca)s">MULTISERVICE</div>
  <div class="binario" style="%(cronaca)s"></div>
  <div class="barra" style="%(barra)s"></div>
  <div class="filo" style="%(filo)s"></div>

%(testi)s
  <div class="finale" style="%(finale)s">
    <img class="logo" src="%(g)slogo-bronzo.jpg">
    <div class="testo" style="top:1000px;opacity:1"><div>Gestione completa.</div><div>15%% sul fatturato.</div></div>
    <div class="riga-oro">GUADAGNIAMO SOLO SE GUADAGNI TU</div>
    <div class="banda-cta" style="%(cta)s">Scrivi CALCOLO in DM</div>
  </div>
</div></body></html>
""" % dict(css=CSS, kf=k, g=G, testi=testi,
           f_tel=anim('f_tel'), f_pro=anim('f_pro'), f_cal=anim('f_cal'),
           b_banda=anim('b_banda'), scatto=anim('scatto'),
           b_tel=anim('b_tel', 'tremolio'),
           b_pro=anim('b_pro', 'push_pro'),
           b_cal=anim('b_cal', 'sale_cal'),
           taglio=anim('taglio_pro'), tendina=anim('tendina'), chip=anim('chip'),
           cronaca=anim('cronaca'), barra=anim('barra'),
           filo=anim('filo', 'filo_v'),
           finale=anim('finale'), cta=anim('sale_cta'))

    with open(os.path.join(HERE, 'reel.html'), 'w') as f:
        f.write(html)
    print('reel.html scritto — %.1f s, %d scene' % (D, len(SCENE)))


if __name__ == '__main__':
    build()
