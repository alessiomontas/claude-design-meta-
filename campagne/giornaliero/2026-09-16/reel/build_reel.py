# -*- coding: utf-8 -*-
"""Reel 16/09 — "Il costo del vuoto", 17,0 s, variante CHIARA.

Formato 1.3 di reel-virali.md (checklist che si accumula) aperto in negazione.
Regole ereditate dal reel del 15/09, che sono costate errori veri:
  - ogni animazione dura TUTTO il reel con fill-mode both, cosi' il frame si
    puo' pescare impostando currentTime (scrubbing);
  - ogni keyframe parte da uno step 0 ESPLICITO: senza, il browser lo sintetizza
    dallo stile calcolato e al frame 0 compare tutto;
  - un elemento ha UNA sola animazione che tocca transform: due si annullano a
    vicenda, vince l'ultima dichiarata.
"""
import os

D = 17.0
EASE = 'cubic-bezier(.16,1,.3,1)'
HERE = os.path.dirname(os.path.abspath(__file__))

FONDO, CARD, INK, INK_2, ORO, ORO_INK = '#FAF7F1', '#F5F0E6', '#2E2A25', '#5A5349', '#C8A24B', '#86692A'
BORDO = '#E7E0D3'
AR = "'Archivo', 'Helvetica Neue', Arial, sans-serif"
MA = "'Manrope', 'Helvetica Neue', Arial, sans-serif"

GANCIO = 'Una casa vuota non costa niente.'
TITOLO = ['Cinque voci che corrono', 'a serranda chiusa']
VOCI = [
    ('01', 'IMU',                          'Acconto 16 giugno, saldo 16 dicembre.', 2.5),
    ('02', 'Tassa rifiuti',                'Anche se non risiede nessuno.',         3.6),
    ('03', 'Quote condominiali ordinarie', 'Sui millesimi, non sulle presenze.',    4.6),
    ('04', 'Assicurazione',                "Copre l'anno, chiusa o aperta.",        5.5),
    ('05', 'Quota fissa dei contatori',    "C'è anche a consumo zero.",             6.3),
]

_kf = []


def kf(nome, passi):
    """passi: (secondi, css) oppure (secondi, css, easing_del_segmento_seguente)."""
    corpo = ''
    for p in passi:
        t, css = p[0], p[1]
        e = p[2] if len(p) > 2 else None
        pct = max(0.0, min(100.0, t / D * 100.0))
        corpo += '  %.4f%% { %s%s }\n' % (pct, css,
                                          ('; animation-timing-function: ' + e) if e else '')
    _kf.append('@keyframes %s {\n%s}\n' % (nome, corpo))
    return ''


def anim(*nomi):
    return 'animation: ' + ', '.join('%s %ss linear both' % (n, D) for n in nomi) + ';'


def app(t0, t1, extra_in='', extra_out='', dur_in=0.2):
    """Comparsa netta fra t0 e t1: niente dissolvenze, stacchi a taglio."""
    return [(0, 'opacity:0; %s' % extra_in),
            (max(t0 - 0.001, 0), 'opacity:0; %s' % extra_in, EASE),
            (t0 + dur_in, 'opacity:1; %s' % extra_out),
            (max(t1 - 0.001, t0 + dur_in), 'opacity:1; %s' % extra_out),
            (t1, 'opacity:0; %s' % extra_out),
            (D, 'opacity:0; %s' % extra_out)]


def costruisci():
    # ---------- 1 · il gancio negato, gia' in corsa al frame 0 ----------
    kf('gancio_in', [
        (0, 'clip-path: inset(46% 0 0 0)'),
        (0.16, 'clip-path: inset(0 0 0 0)', EASE),
        (0.9, 'clip-path: inset(0 0 0 0)'),
        (1.1, 'clip-path: inset(0 0 100% 0)'),
        (16.7, 'clip-path: inset(100% 0 0 0)', EASE),
        (16.9, 'clip-path: inset(46% 0 0 0)'),     # loop: si richiude sul frame 0
        (D, 'clip-path: inset(46% 0 0 0)'),
    ])
    kf('gancio_su', [
        (0, 'transform: translateY(0)'),
        (0.9, 'transform: translateY(0)', EASE),
        (1.1, 'transform: translateY(-150px)'),
        (16.69, 'transform: translateY(-150px)'),
        (16.7, 'transform: translateY(0)'),
        (D, 'transform: translateY(0)'),
    ])
    kf('gancio_op', [(0, 'opacity:1'), (1.1, 'opacity:1'), (1.101, 'opacity:0'),
                     (16.69, 'opacity:0'), (16.7, 'opacity:1'), (D, 'opacity:1')])
    kf('fascia_dietro', [
        (0, 'transform: translateX(-18px)'),
        (0.24, 'transform: translateX(0)', EASE),
        (D, 'transform: translateX(0)'),
    ])
    # la cancellatura oro: secondo evento, a 0,4 s
    kf('cancella', [
        (0, 'width: 0%'),
        (0.4, 'width: 0%', EASE),
        (0.6, 'width: 100%'),
        (1.1, 'width: 100%'),
        (1.101, 'width: 0%'),
        (D, 'width: 0%'),
    ])
    kf('falso', [
        (0, 'opacity:0; transform: translateY(150px)'),
        (0.899, 'opacity:0; transform: translateY(150px)', EASE),
        (1.1, 'opacity:1; transform: translateY(0)'),
        (1.899, 'opacity:1; transform: translateY(0)'),
        (1.9, 'opacity:0; transform: translateY(0)'),
        (D, 'opacity:0; transform: translateY(0)'),
    ])

    # ---------- 2 · titolo parola per parola + barra di avanzamento ----------
    parole = (TITOLO[0] + ' | ' + TITOLO[1]).split(' ')
    for i, _ in enumerate(parole):
        t0 = 1.9 + i * 0.11
        kf('par%d' % i, [
            (0, 'opacity:0; transform: translateY(14px)'),
            (max(t0 - 0.001, 0), 'opacity:0; transform: translateY(14px)', EASE),
            (t0 + 0.13, 'opacity:1; transform: translateY(0)'),
            (7.399, 'opacity:1; transform: translateY(0)'),
            (7.4, 'opacity:0; transform: translateY(0)'),
            (D, 'opacity:0; transform: translateY(0)'),
        ])
    passi_barra = [(0, 'transform: scaleX(0)'), (1.899, 'transform: scaleX(0)', EASE)]
    for i, (_, _, _, t) in enumerate(VOCI):
        passi_barra.append((t + 0.22, 'transform: scaleX(%.2f)' % ((i + 1) / 5.0), EASE))
    passi_barra += [(7.399, 'transform: scaleX(1)'), (7.4, 'transform: scaleX(0)'),
                    (D, 'transform: scaleX(0)')]
    kf('barra', passi_barra)
    kf('barra_op', [(0, 'opacity:0'), (1.899, 'opacity:0'), (1.9, 'opacity:1'),
                    (7.399, 'opacity:1'), (7.4, 'opacity:0'), (D, 'opacity:0')])

    # ---------- 3 · la lista che si ACCUMULA (non si sostituisce) ----------
    for i, (_, _, _, t0) in enumerate(VOCI):
        # una sola animazione per il transform: entrata da sinistra con
        # overshoot, poi il rimpicciolimento quando arriva la riga dopo
        t_dopo = VOCI[i + 1][3] if i + 1 < len(VOCI) else None
        passi = [(0, 'opacity:0; transform: translateX(-60px) scale(1)'),
                 (max(t0 - 0.001, 0), 'opacity:0; transform: translateX(-60px) scale(1)', EASE),
                 (t0 + 0.18, 'opacity:1; transform: translateX(8px) scale(1)', EASE),
                 (t0 + 0.26, 'opacity:1; transform: translateX(0) scale(1)')]
        if t_dopo:
            passi += [(t_dopo, 'opacity:1; transform: translateX(0) scale(1)', EASE),
                      (t_dopo + 0.2, 'opacity:.45; transform: translateX(0) scale(.86)')]
            fine = 'opacity:.45; transform: translateX(0) scale(.86)'
        else:
            fine = 'opacity:1; transform: translateX(0) scale(1)'
        passi += [(7.4, fine, EASE),
                  (7.8, 'opacity:.35; transform: translateX(-190px) scale(.55)'),
                  (8.599, 'opacity:.35; transform: translateX(-190px) scale(.55)'),
                  (8.6, 'opacity:0; transform: translateX(-190px) scale(.55)'),
                  (D, 'opacity:0; transform: translateX(-190px) scale(.55)')]
        kf('voce%d' % i, passi)
        kf('spunta%d' % i, [
            (0, 'stroke-dashoffset: 40'),
            (max(t0 + 0.18, 0), 'stroke-dashoffset: 40', EASE),
            (t0 + 0.4, 'stroke-dashoffset: 0'),
            (D, 'stroke-dashoffset: 0'),
        ])

    # ---------- 4 · la frase di riscatto ----------
    kf('riscatto', [
        (0, 'opacity:0; clip-path: inset(0 100% 0 0)'),
        (7.799, 'opacity:0; clip-path: inset(0 100% 0 0)', EASE),
        (8.1, 'opacity:1; clip-path: inset(0 0 0 0)'),
        (8.599, 'opacity:1; clip-path: inset(0 0 0 0)'),
        (8.6, 'opacity:0; clip-path: inset(0 0 0 0)'),
        (D, 'opacity:0; clip-path: inset(0 0 0 0)'),
    ])

    # ---------- 5 · la serranda che scende e il quadrante che non si ferma ----------
    kf('serranda', [
        (0, 'opacity:0; transform: scaleY(0)'),
        (8.599, 'opacity:0; transform: scaleY(0)', EASE),
        (9.02, 'opacity:1; transform: scaleY(1)'),
        (9.999, 'opacity:1; transform: scaleY(1)'),
        (10.0, 'opacity:0; transform: scaleY(1)'),
        (D, 'opacity:0; transform: scaleY(1)'),
    ])
    # il quadrante gira per tutta la durata: e' il punto del contenuto,
    # il contatore non si ferma perche' la casa e' chiusa
    kf('quadrante', [(0, 'transform: rotate(0deg)'), (D, 'transform: rotate(900deg)')])
    kf('quadrante_op', [(0, 'opacity:0'), (8.699, 'opacity:0'), (8.9, 'opacity:1'),
                        (9.999, 'opacity:1'), (10.0, 'opacity:0'), (D, 'opacity:0')])
    kf('serr_testo', app(8.75, 10.0, 'transform: translateY(16px)', 'transform: translateY(0)'))

    # ---------- 6 · il ribaltamento ----------
    kf('rib1', app(10.0, 11.4, 'transform: translateY(14px)', 'transform: translateY(0)'))
    kf('rib2', app(10.3, 11.4, 'transform: translateY(14px)', 'transform: translateY(0)'))
    kf('split_su', [
        (0, 'opacity:0; height: 310px'),
        (11.399, 'opacity:0; height: 310px', EASE),
        (11.5, 'opacity:1; height: 310px', EASE),
        (12.0, 'opacity:1; height: 0px'),
        (12.999, 'opacity:1; height: 0px'),
        (13.0, 'opacity:0; height: 0px'),
        (D, 'opacity:0; height: 0px'),
    ])
    kf('split_giu', [
        (0, 'opacity:0; height: 310px'),
        (11.399, 'opacity:0; height: 310px', EASE),
        (11.5, 'opacity:1; height: 310px', EASE),
        (12.0, 'opacity:1; height: 620px'),
        (12.999, 'opacity:1; height: 620px'),
        (13.0, 'opacity:0; height: 620px'),
        (D, 'opacity:0; height: 620px'),
    ])

    # ---------- 7 · la riga chiave, l'evidenziatore e il badge ----------
    kf('chiave', [
        (0, 'opacity:0; clip-path: inset(0 0 100% 0)'),
        (12.999, 'opacity:0; clip-path: inset(0 0 100% 0)', EASE),
        (13.25, 'opacity:1; clip-path: inset(0 0 0 0)'),
        (16.399, 'opacity:1; clip-path: inset(0 0 0 0)'),
        (16.4, 'opacity:0; clip-path: inset(0 0 0 0)'),
        (D, 'opacity:0; clip-path: inset(0 0 0 0)'),
    ])
    kf('evidenzia', [
        (0, 'background-size: 0% 100%'),
        (13.4, 'background-size: 0% 100%', EASE),
        (13.66, 'background-size: 100% 100%'),
        (16.399, 'background-size: 100% 100%'),
        (16.4, 'background-size: 0% 100%'),
        (D, 'background-size: 0% 100%'),
    ])
    kf('badge', [
        (0, 'opacity:0; transform: scale(1.12)'),
        (14.399, 'opacity:0; transform: scale(1.12)', EASE),
        (14.58, 'opacity:1; transform: scale(1)'),
        (16.399, 'opacity:1; transform: scale(1)'),
        (16.4, 'opacity:0; transform: scale(1)'),
        (D, 'opacity:0; transform: scale(1)'),
    ])

    # ---------- 8 · CTA che entra secca e si ritira per il loop ----------
    kf('cta', [
        (0, 'opacity:0; transform: translateY(160px)'),
        (15.199, 'opacity:0; transform: translateY(160px)', EASE),
        (15.46, 'opacity:1; transform: translateY(0)'),
        (16.399, 'opacity:1; transform: translateY(0)', EASE),
        (16.7, 'opacity:1; transform: translateY(160px)'),
        (16.701, 'opacity:0; transform: translateY(160px)'),
        (D, 'opacity:0; transform: translateY(160px)'),
    ])
    kf('firma', app(15.35, 16.45, 'transform: translateY(12px)', 'transform: translateY(0)'))


def html():
    costruisci()
    voci_html = ''
    for i, (num, voce, det, _) in enumerate(VOCI):
        voci_html += (
            '<div class="voce" style="top: %dpx; %s">'
            '<span class="vnum">%s</span>'
            '<span class="vtxt"><span class="vtit">%s</span><span class="vdet">%s</span></span>'
            '<svg class="vspunta" width="56" height="56" viewBox="0 0 24 24" fill="none" '
            'stroke="%s" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" '
            'style="%s"><path d="M20 6L9 17l-5-5" stroke-dasharray="40"/></svg>'
            '</div>' % (570 + i * 166, anim('voce%d' % i), num, voce, det, ORO,
                        anim('spunta%d' % i)))
    parole = (TITOLO[0] + ' | ' + TITOLO[1]).split(' ')
    tit_html = ''
    for i, w in enumerate(parole):
        if w == '|':
            tit_html += '<span style="flex-basis:100%; height:0;"></span>'
            continue
        tit_html += '<span class="par" style="%s">%s</span>' % (anim('par%d' % i), w)

    doghe = ''.join('<div class="doga"></div>' for _ in range(9))

    return """<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;overflow:hidden}
.scena{position:relative;width:1080px;height:1920px;background:%(fondo)s;overflow:hidden}
.marchio{position:absolute;left:0;right:0;top:112px;text-align:center}
.marchio b{display:block;font-family:%(ar)s;font-weight:800;font-size:33px;letter-spacing:9px;color:%(ink)s}
.marchio i{display:block;font-family:%(ma)s;font-style:normal;font-weight:600;font-size:17px;letter-spacing:7px;color:%(ink2)s;margin-top:12px}
.barra_sfondo{position:absolute;left:64px;right:64px;top:250px;height:6px;background:%(bordo)s;border-radius:3px;overflow:hidden}
.barra{height:100%%;background:%(oro)s;transform-origin:left center}
.fascia_dietro{position:absolute;left:0;right:0;top:790px;height:230px;background:%(card)s}
.gancio{position:absolute;left:64px;right:64px;top:820px;font-family:%(ar)s;font-weight:900;font-size:70px;line-height:1.14;letter-spacing:-0.4px;color:%(ink)s}
.cancella{position:absolute;left:64px;top:900px;height:6px;background:%(oro)s}
.falso{position:absolute;left:64px;right:64px;top:830px;font-family:%(ar)s;font-weight:900;font-size:130px;line-height:1;letter-spacing:-1px;color:%(oroink)s}
.titolo{position:absolute;left:64px;right:64px;top:360px;display:flex;flex-wrap:wrap;gap:0 18px;font-family:%(ar)s;font-weight:900;font-size:62px;line-height:1.16;color:%(ink)s}
.voce{position:absolute;left:64px;right:64px;height:150px;background:%(card)s;border-radius:20px;padding:0 28px;display:flex;align-items:center;gap:24px;transform-origin:left center}
.vnum{font-family:%(ar)s;font-weight:900;font-size:50px;color:%(oroink)s;flex:0 0 90px}
.vtxt{flex:1;min-width:0}
.vtit{display:block;font-family:%(ar)s;font-weight:800;font-size:50px;color:%(ink)s}
.vdet{display:block;font-family:%(ma)s;font-weight:500;font-size:33px;color:%(ink2)s;margin-top:6px}
.vspunta{flex:0 0 56px}
.riscatto{position:absolute;left:430px;right:64px;top:1180px;font-family:%(ar)s;font-weight:800;font-size:58px;line-height:1.18;color:%(ink)s}
.serranda{position:absolute;left:64px;right:64px;top:420px;height:520px;background:#C9BFA9;border-radius:20px;transform-origin:top center;overflow:hidden;display:flex;flex-direction:column;gap:6px;padding:14px}
.doga{flex:1;background:#D9CFBC;border-radius:4px;box-shadow:inset 0 -3px 0 rgba(46,42,37,.10)}
.quadrante{position:absolute;left:430px;top:1010px;width:220px;height:220px;border-radius:50%%;border:10px solid %(bordo)s;display:flex;align-items:center;justify-content:center}
.lancetta{width:8px;height:78px;background:%(oro)s;border-radius:4px;transform-origin:bottom center;position:absolute;top:24px}
.serr_testo{position:absolute;left:64px;right:64px;top:1290px;font-family:%(ar)s;font-weight:900;font-size:66px;line-height:1.16;color:%(ink)s}
.rib{position:absolute;left:64px;right:64px;font-family:%(ar)s;font-weight:900;font-size:62px;line-height:1.18;color:%(ink)s}
.split{position:absolute;left:64px;right:64px;border-radius:24px;overflow:hidden;display:flex;align-items:center;padding:0 40px;font-family:%(ar)s;font-weight:800;font-size:58px}
.split_su{top:620px;background:%(card)s;color:%(ink2)s}
.split_giu{top:940px;background:%(oro)s;color:%(ink)s}
.chiave{position:absolute;left:64px;right:64px;top:1240px;font-family:%(ar)s;font-weight:800;font-size:60px;line-height:1.22;color:%(ink)s}
.evid{background-image:linear-gradient(%(oro)s,%(oro)s);background-repeat:no-repeat;background-position:left center;padding:2px 6px}
.badge{position:absolute;left:64px;top:1470px;background:%(oro)s;color:%(ink)s;border-radius:999px;padding:16px 40px;font-family:%(ar)s;font-weight:900;font-size:56px}
.firma{position:absolute;left:64px;right:64px;top:1610px;font-family:%(ma)s;font-weight:600;font-size:33px;color:%(ink2)s}
.cta{position:absolute;left:64px;right:64px;top:1680px;height:120px;background:%(oro)s;border-radius:999px;display:flex;align-items:center;justify-content:center;font-family:%(ar)s;font-weight:800;font-size:50px;letter-spacing:.02em;color:%(ink)s}
%(kf)s
</style></head><body>
<div class="scena">
  <div class="marchio"><b>HADRIANUS</b><i>MULTISERVICE</i></div>

  <div class="fascia_dietro" style="%(fasciad)s"></div>
  <div class="gancio" style="%(ganciop)s"><span style="display:block;%(ganciosu)s"><span style="display:block;%(gancioin)s">%(g)s</span></span></div>
  <div class="cancella" style="%(cancella)s"></div>
  <div class="falso" style="%(falso)s">Falso.</div>

  <div class="barra_sfondo" style="%(barraop)s"><div class="barra" style="%(barra)s"></div></div>
  <div class="titolo">%(titolo)s</div>
  %(voci)s
  <div class="riscatto" style="%(riscatto)s">Nessuno te l'ha mai messo<br>su una riga sola.</div>

  <div class="serranda" style="%(serranda)s">%(doghe)s</div>
  <div class="quadrante" style="%(quadop)s"><div class="lancetta" style="%(quad)s"></div></div>
  <div class="serr_testo" style="%(serrt)s">Il contatore gira anche<br>a serranda chiusa.</div>

  <div class="rib" style="top:820px;%(rib1)s">Quelle voci non spariscono.</div>
  <div class="rib" style="top:960px;font-family:%(ma)s;font-weight:500;font-size:46px;color:%(ink2)s;%(rib2)s">Cambia da dove escono i soldi.</div>

  <div class="split split_su" style="%(splitsu)s">Dal tuo stipendio</div>
  <div class="split split_giu" style="%(splitgiu)s">Dalla casa</div>

  <div class="chiave" style="%(chiave)s">L'unica voce che compare solo<br><span class="evid" style="%(evid)s">se la casa ha incassato.</span></div>
  <div class="badge" style="%(badge)s">15%%</div>

  <div class="firma" style="%(firma)s">Guadagniamo solo se guadagni tu.</div>
  <div class="cta" style="%(cta)s">SCRIVI CALCOLO IN DM</div>
</div>
</body></html>
""" % dict(fondo=FONDO, card=CARD, ink=INK, ink2=INK_2, oro=ORO, oroink=ORO_INK,
           bordo=BORDO, ar=AR, ma=MA, kf=''.join(_kf), g=GANCIO,
           fasciad=anim('fascia_dietro'), ganciop=anim('gancio_op'),
           ganciosu=anim('gancio_su'), gancioin=anim('gancio_in'),
           cancella=anim('cancella'), falso=anim('falso'),
           barra=anim('barra'), barraop=anim('barra_op'), titolo=tit_html,
           voci=voci_html, riscatto=anim('riscatto'),
           serranda=anim('serranda'), doghe=doghe,
           quad=anim('quadrante'), quadop=anim('quadrante_op'),
           serrt=anim('serr_testo'), rib1=anim('rib1'), rib2=anim('rib2'),
           splitsu=anim('split_su'), splitgiu=anim('split_giu'),
           chiave=anim('chiave'), evid=anim('evidenzia'), badge=anim('badge'),
           firma=anim('firma'), cta=anim('cta'))


if __name__ == '__main__':
    pagina = html()
    with open(os.path.join(HERE, 'reel.html'), 'w') as f:
        f.write(pagina)
    print('reel.html — %.1f s · %d voci · %d animazioni'
          % (D, len(VOCI), pagina.count('@keyframes')))
