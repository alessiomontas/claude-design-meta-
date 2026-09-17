# -*- coding: utf-8 -*-
"""Da `scene.json` a un HTML che Canva importa come documento a pagine.

Perche' esiste: il collegamento a Canva sa creare forme e testi, ma **non sa
scegliere il carattere** — ogni scritta atterrerebbe nel font predefinito, non
in Archivo/Manrope. L'importatore di Canva, invece, legge un file HTML e ne
ricava un documento con gli elementi separati, tenendo la tipografia.

Ogni scena del reel diventa una pagina, marcata `data-document-role="page"`
come vuole l'importatore. Le animazioni non passano (Canva non le riceve da
nessuna strada): le pagine sono i fotogrammi chiave, e le animazioni si
rimettono a mano dentro Canva.

    python3 scene_to_canva.py <scene.json> <uscita.html>
"""
import json
import os
import html
import re
import sys

FONT_STACK = {
    'Archivo': "'Archivo', 'Helvetica Neue', Arial, sans-serif",
    'Manrope': "'Manrope', 'Helvetica Neue', Arial, sans-serif",
}

# Una pagina per scena. Le scene si ricavano dal file, mai scritte a mano:
# gli id degli elementi portano il prefisso della scena (s01_, s02_, ...), e
# ogni gruppo da' il suo intervallo. L'istante rappresentativo e' il punto in
# cui la scena e' completa — dopo l'ultima entrata, prima dell'uscita.
SCENA_ID = re.compile(r'^s(\d+)_')


def scene_dal_file(dati):
    """[(titolo, istante)] — una voce per scena, in ordine di tempo."""
    gruppi = {}
    for el in dati['elementi']:
        m = SCENA_ID.match(el.get('id', ''))
        if not m:
            continue                      # marchio, barra, foto: non sono scene
        g = gruppi.setdefault(m.group(1), {'in': [], 'out': [], 'testi': []})
        g['in'].append(float(el.get('t_in', 0)))
        g['out'].append(float(el.get('t_out') or dati['durata']))
        if el.get('tipo') == 'testo' and el.get('testo'):
            g['testi'].append((float(el.get('size') or 0), el['testo']))

    scene = []
    for numero in sorted(gruppi):
        g = gruppi[numero]
        ultima_entrata, prima_uscita = max(g['in']), min(g['out'])
        # A meta' fra l'ultima entrata e la prima uscita: tutto e' a schermo.
        istante = ultima_entrata + (prima_uscita - ultima_entrata) / 2
        # Il titolo lo da' il testo piu' grande della scena, ridotto a una riga.
        testo = max(g['testi'])[1] if g['testi'] else ''
        # Il testo arriva gia' marcato: <br> e entita' vanno via, altrimenti
        # l'etichetta della pagina in Canva mostra il codice invece della frase.
        testo = re.sub(r'<[^>]+>', ' ', testo)
        testo = html.unescape(testo)
        testo = ' '.join(testo.replace('\n', ' ').split())
        if len(testo) > 42:
            testo = testo[:41].rstrip() + '...'
        scene.append(('Scena %d%s' % (int(numero), ' - ' + testo if testo else ''),
                      round(istante, 2)))
    return scene



def visibile(el, t, durata):
    return float(el.get('t_in', 0)) <= t < float(el.get('t_out', durata) or durata)


def elemento(el):
    """Stato finale, nessuna animazione: e' un fotogramma, non un movimento."""
    geo = ('position:absolute; left:%dpx; top:%dpx; width:%dpx;'
           % (int(el.get('x', 0)), int(el.get('y', 0)), int(el.get('w', 952))))
    tipo = el.get('tipo', 'testo')

    if tipo == 'immagine':
        return ('<div style="%s height:%dpx; overflow:hidden; border-radius:%dpx;">'
                '<img src="%s" style="width:100%%; height:100%%; object-fit:cover; display:block;" alt="">'
                '</div>' % (geo, int(el.get('h', 600)), int(el.get('raggio', 0)), el.get('src', '')))

    if tipo == 'fascia':
        return ('<div style="%s height:%dpx; background:%s; border-radius:%dpx;"></div>'
                % (geo, int(el.get('h', 200)), el.get('fondo', '#F5F0E6'),
                   int(el.get('raggio', 0))))

    fondo, box = el.get('fondo'), ''
    testo = str(el.get('testo', '')).replace('\n', '<br>')
    if fondo:
        box = ('background:%s; border-radius:%dpx; padding:%s;'
               % (fondo, int(el.get('raggio', 0)), el.get('padding', '22px 30px')))
        if el.get('h'):
            box += (' height:%dpx; display:flex; align-items:center; justify-content:%s;'
                    % (int(el['h']),
                       {'center': 'center', 'right': 'flex-end'}.get(el.get('allinea'), 'flex-start')))
            testo = '<div style="width:100%%">%s</div>' % testo
    return ('<div style="%s %s font-family:%s; font-weight:%d; font-size:%dpx; '
            'line-height:%s; letter-spacing:%spx; color:%s; text-align:%s;">%s</div>'
            % (geo, box, FONT_STACK.get(el.get('font', 'Archivo'), FONT_STACK['Archivo']),
               int(el.get('peso', 800)), int(el.get('size', 45)), el.get('lh', 1.16),
               el.get('tracking', -0.4), el.get('colore', '#2E2A25'),
               el.get('allinea', 'left'), testo))


def costruisci(scena):
    durata = float(scena.get('durata', 25.0))
    fondo = scena.get('fondo', '#FAF7F1')
    pagine = ''
    for titolo, t in scene_dal_file(scena):
        dentro = [e for e in scena['elementi'] if visibile(e, t, durata)]
        if not dentro:
            continue
        corpo = ''.join('    ' + elemento(e) + '\n' for e in dentro)
        pagine += ('  <div data-document-role="page" data-label="%s" '
                   'style="position:relative; width:1080px; height:1920px; overflow:hidden; '
                   'background:%s;">\n%s  </div>\n' % (titolo, fondo, corpo))

    return """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>%s</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:%s}
</style>
</head>
<body>
%s</body>
</html>
""" % (scena.get('titolo', 'Reel'), fondo, pagine)


if __name__ == '__main__':
    sorgente, uscita = sys.argv[1], sys.argv[2]
    with open(sorgente) as f:
        scena = json.load(f)
    pagina = costruisci(scena)
    with open(uscita, 'w') as f:
        f.write(pagina)
    print('%s — %d pagine' % (os.path.basename(uscita), pagina.count('data-document-role')))
