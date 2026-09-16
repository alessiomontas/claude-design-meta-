# -*- coding: utf-8 -*-
"""Da `scene.json` a `reel.html` — il montatore del reel.

Questo file e' la meta' invisibile dell'editor: l'interfaccia modifica
`scene.json`, questo lo trasforma in pagina animata, e `anima_reel.py` la
trasforma in MP4. Quindi quello che il titolare sposta a schermo e' esattamente
quello che finisce nel video, senza passaggi a mano.

    python3 scene_to_html.py <scene.json> <uscita.html>

Vocabolario delle animazioni (nomi in italiano, sono quelli che compaiono
nell'editor):

  entrata: nessuna · sfuma · maschera-basso · maschera-alto · maschera-sinistra
           entra-basso · entra-alto · entra-sinistra · entra-destra · scatto
  uscita:  taglio · sfuma · esce-alto · esce-basso · maschera-chiude
"""
import json
import os
import sys

EASE = 'cubic-bezier(.16,1,.3,1)'
DUR_IN_DEF = 0.26
DUR_OUT_DEF = 0.2

FONT_STACK = {
    'Archivo': "'Archivo', 'Helvetica Neue', Arial, sans-serif",
    'Manrope': "'Manrope', 'Helvetica Neue', Arial, sans-serif",
}


def _stato(anim, fase, dentro):
    """Restituisce (opacita', transform, clip) per un'animazione.

    `dentro=False` e' lo stato fuori campo (prima dell'entrata o dopo l'uscita),
    `dentro=True` lo stato a regime.
    """
    if dentro:
        return ('1', 'translate(0px, 0px) scale(1)', 'inset(0 0 0 0)')
    tavola = {
        'nessuna':           ('1', 'translate(0px,0px) scale(1)', 'inset(0 0 0 0)'),
        'sfuma':             ('0', 'translate(0px,0px) scale(1)', 'inset(0 0 0 0)'),
        'maschera-basso':    ('1', 'translate(0px,0px) scale(1)', 'inset(100% 0 0 0)'),
        'maschera-alto':     ('1', 'translate(0px,0px) scale(1)', 'inset(0 0 100% 0)'),
        'maschera-sinistra': ('1', 'translate(0px,0px) scale(1)', 'inset(0 100% 0 0)'),
        'maschera-chiude':   ('1', 'translate(0px,0px) scale(1)', 'inset(0 0 100% 0)'),
        'entra-basso':       ('0', 'translate(0px,120px) scale(1)', 'inset(0 0 0 0)'),
        'entra-alto':        ('0', 'translate(0px,-120px) scale(1)', 'inset(0 0 0 0)'),
        'entra-sinistra':    ('0', 'translate(-80px,0px) scale(1)', 'inset(0 0 0 0)'),
        'entra-destra':      ('0', 'translate(80px,0px) scale(1)', 'inset(0 0 0 0)'),
        'esce-alto':         ('0', 'translate(0px,-150px) scale(1)', 'inset(0 0 0 0)'),
        'esce-basso':        ('0', 'translate(0px,150px) scale(1)', 'inset(0 0 0 0)'),
        'scatto':            ('0', 'translate(0px,0px) scale(1.14)', 'inset(0 0 0 0)'),
        'taglio':            ('0', 'translate(0px,0px) scale(1)', 'inset(0 0 0 0)'),
    }
    return tavola.get(anim, tavola['sfuma'])


def _css_stato(s):
    return 'opacity:%s; transform:%s; clip-path:%s' % s


def keyframes(el, durata):
    """Una sola animazione per elemento: due che toccano transform si annullano.
    Ogni sequenza parte da uno step 0 ESPLICITO, altrimenti il browser lo
    sintetizza dallo stile calcolato e al fotogramma 0 compare tutto."""
    nome = 'a_' + el['id']
    t_in = float(el.get('t_in', 0.0))
    t_out = float(el.get('t_out', durata))
    d_in = float(el.get('dur_in', DUR_IN_DEF))
    d_out = float(el.get('dur_out', DUR_OUT_DEF))
    a_in = el.get('anim_in', 'sfuma')
    a_out = el.get('anim_out', 'taglio')

    fuori_in = _css_stato(_stato(a_in, 'in', False))
    dentro = _css_stato(_stato(None, None, True))
    fuori_out = _css_stato(_stato(a_out, 'out', False))

    passi = []
    if t_in <= 0.001:
        passi.append((0.0, dentro))
    else:
        passi.append((0.0, fuori_in))
        passi.append((max(t_in - 0.001, 0.0), fuori_in, EASE))
        passi.append((min(t_in + d_in, t_out), dentro))
    if t_out < durata - 0.001:
        passi.append((max(t_out - 0.001, t_in + d_in), dentro,
                      EASE if a_out != 'taglio' else None))
        passi.append((min(t_out + (0.0 if a_out == 'taglio' else d_out), durata), fuori_out))
        passi.append((durata, fuori_out))
    else:
        passi.append((durata, dentro))

    corpo = ''
    visti = set()
    for p in passi:
        t, css = p[0], p[1]
        e = p[2] if len(p) > 2 else None
        pct = round(max(0.0, min(100.0, t / durata * 100.0)), 4)
        if pct in visti:
            continue
        visti.add(pct)
        corpo += '  %s%% { %s%s }\n' % (pct, css,
                                        ('; animation-timing-function: ' + e) if e else '')
    return '@keyframes %s {\n%s}\n' % (nome, corpo), nome


def elemento_html(el, nome_anim, durata):
    stile = ('position:absolute; left:%dpx; top:%dpx; width:%dpx; '
             'animation:%s %ss linear both;'
             % (int(el.get('x', 0)), int(el.get('y', 0)), int(el.get('w', 952)),
                nome_anim, durata))
    if el.get('rotazione'):
        stile += ' transform-origin:center center;'

    tipo = el.get('tipo', 'testo')
    if tipo == 'immagine':
        alt = ' object-fit:%s;' % el.get('fit', 'cover')
        return ('<div style="%s height:%dpx; overflow:hidden; border-radius:%dpx;">'
                '<img src="%s" style="width:100%%; height:100%%;%s display:block;">'
                '</div>' % (stile, int(el.get('h', 600)), int(el.get('raggio', 0)),
                            el.get('src', ''), alt))

    if tipo == 'fascia':
        return ('<div style="%s height:%dpx; background:%s; border-radius:%dpx;"></div>'
                % (stile, int(el.get('h', 200)), el.get('fondo', '#F5F0E6'),
                   int(el.get('raggio', 0))))

    # testo (ed etichette su fondo: pill, badge, card)
    fondo = el.get('fondo')
    box = ''
    if fondo:
        box = ('background:%s; border-radius:%dpx; padding:%s;'
               % (fondo, int(el.get('raggio', 0)), el.get('padding', '22px 30px')))
        if el.get('h'):
            box += (' height:%dpx; display:flex; align-items:center; justify-content:%s;'
                    % (int(el['h']),
                       {'center': 'center', 'right': 'flex-end'}.get(el.get('allinea'), 'flex-start')))
    testo = el.get('testo', '').replace('\n', '<br>')
    # Dentro un contenitore flex ogni pezzo diventa un elemento a se' e il <br>
    # non ha effetto: il testo va sempre avvolto in un blocco suo.
    if fondo and el.get('h'):
        testo = '<div style="width:100%%">%s</div>' % testo
    return ('<div style="%s %s font-family:%s; font-weight:%d; font-size:%dpx; '
            'line-height:%s; letter-spacing:%spx; color:%s; text-align:%s;">%s</div>'
            % (stile, box, FONT_STACK.get(el.get('font', 'Archivo'), FONT_STACK['Archivo']),
               int(el.get('peso', 800)), int(el.get('size', 45)), el.get('lh', 1.16),
               el.get('tracking', -0.4), el.get('colore', '#2E2A25'),
               el.get('allinea', 'left'), testo))


def costruisci(scena):
    durata = float(scena.get('durata', 20.0))
    kfs, corpi = [], []
    for el in scena.get('elementi', []):
        kf, nome = keyframes(el, durata)
        kfs.append(kf)
        corpi.append('  ' + elemento_html(el, nome, durata))

    sfondo = ''
    if scena.get('sfondo_immagine'):
        sfondo = ('  <img src="%s" style="position:absolute; inset:0; width:100%%; '
                  'height:100%%; object-fit:cover;">\n' % scena['sfondo_immagine'])

    return """<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;overflow:hidden}
.scena{position:relative;width:1080px;height:1920px;background:%s;overflow:hidden}
%s
</style></head><body>
<div class="scena">
%s%s
</div>
</body></html>
""" % (scena.get('fondo', '#FAF7F1'), ''.join(kfs), sfondo, '\n'.join(corpi))


if __name__ == '__main__':
    sorgente, uscita = sys.argv[1], sys.argv[2]
    with open(sorgente) as f:
        scena = json.load(f)
    pagina = costruisci(scena)
    with open(uscita, 'w') as f:
        f.write(pagina)
    print('%s — %.1f s · %d elementi'
          % (os.path.basename(uscita), scena.get('durata', 0), len(scena.get('elementi', []))))
