# -*- coding: utf-8 -*-
"""Artboard del 16/09/2026 — "Il costo del vuoto", variante CHIARA.

Firma del giorno: il modulo a caselle vuote. Nessuna cifra nostra accanto a
nessuna voce; il totale e' un campo vuoto, e questo e' il contenuto.
"""
import os
from base import *

HERE = os.path.dirname(os.path.abspath(__file__))

VOCI = [
    ('01', 'IMU',                    'Acconto 16 giugno, saldo 16 dicembre'),
    ('02', 'Tassa rifiuti',          'Anche se non risiede nessuno'),
    ('03', 'Quote condominiali ordinarie',     'Sui millesimi, non sulle presenze'),
    ('04', 'Assicurazione',          "Copre l'anno, chiusa o aperta"),
    ('05', 'Quota fissa contatori',  "C'e' anche a consumo zero"),
]
SERVIZI = ['Pricing dinamico', 'Check-in smart H24', 'Gestione ospiti',
           'Pulizie in standard alberghiero', 'Annuncio e foto']
FONTE_ISTAT = 'ISTAT, Censimento permanente 2021'


def spunta(d=34):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" '
            'stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" '
            'style="flex: 0 0 auto;"><path d="M20 6L9 17l-5-5"/></svg>' % (d, d, ORO))


def modulo_euro(y, altezza=104, left=64, right=64, size_voce=45, size_det=29,
                campo=250, totale=True):
    """Le cinque voci in una fascia sabbia unica, ognuna col suo campo vuoto.
    Se `totale`, chiude con la banda oro del TOTALE: anch'essa vuota."""
    n = len(VOCI)
    h = altezza * n
    out = ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
           'background: %s; border-radius: 24px; overflow: hidden;">' % (left, right, y, CARD))
    for i, (num, voce, det) in enumerate(VOCI):
        bordo = '' if i == 0 else 'border-top: 1px solid #E2DACB;'
        out += ('<div style="height: %dpx; %s padding: 0 28px; display: flex; '
                'align-items: center; gap: 22px;">'
                '<span style="font-family: %s; font-weight: 900; font-size: 40px; color: %s; '
                'flex: 0 0 76px;">%s</span>'
                '<span style="flex: 1; min-width: 0;">'
                '<span style="display: block; font-family: %s; font-weight: 800; font-size: %dpx; '
                'color: %s;">%s</span>'
                '<span style="display: block; font-family: %s; font-weight: 500; font-size: %dpx; '
                'color: %s; margin-top: 4px;">%s</span></span>'
                # Il campo: la "€" appoggiata sulla riga, non sospesa sopra.
                '<span style="flex: 0 0 %dpx; display: flex; align-items: flex-end; gap: 10px;">'
                '<span style="font-family: %s; font-weight: 600; font-size: 36px; color: %s; '
                'line-height: 1;">&euro;</span>'
                '<span style="flex: 1; border-bottom: 2px solid %s; height: 34px;"></span></span>'
                '</div>' % (altezza, bordo, AR, ORO_INK, num, AR, size_voce, INK, voce,
                            MA, size_det, INK_2, det.replace("C'e'", "C'è"),
                            campo, MA, INK_2, ORO))
    out += '</div>\n'
    if totale:
        out += ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: 88px; '
                'background: %s; border-radius: 18px; padding: 0 28px; display: flex; '
                'align-items: center; justify-content: space-between; font-family: %s; '
                'font-weight: 800; font-size: 44px; letter-spacing: 0.02em; color: %s;">'
                "<span>TOTALE IN UN ANNO</span>"
                '<span style="display: flex; align-items: flex-end; gap: 12px; width: 250px;">'
                '<span style="line-height: 1;">&euro;</span>'
                '<span style="flex: 1; border-bottom: 3px solid %s; height: 36px;"></span></span>'
                '</div>\n' % (left, right, y + h + 18, ORO, AR, INK, INK))
    return out


def fascia(y, h, etichetta, righe, oro=False, left=64, right=64, size=45):
    """Blocco pieno a tutta colonna: sabbia (casa chiusa) o oro (casa a reddito)."""
    fondo = ORO if oro else CARD
    col_et = INK if oro else ORO_INK
    col_tx = INK if oro else INK_CORPO
    corpo = ''.join('<div>%s</div>' % r for r in righe)
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
            'background: %s; border-radius: 24px; padding: 30px 34px; display: flex; '
            'flex-direction: column; justify-content: center; gap: 16px;">'
            '<div style="font-family: %s; font-weight: 700; font-size: 29px; letter-spacing: 0.18em; '
            'text-transform: uppercase; color: %s;">%s</div>'
            '<div style="font-family: %s; font-weight: 800; font-size: %dpx; line-height: 1.2; '
            'color: %s;">%s</div></div>\n'
            % (left, right, y, h, fondo, MA, col_et, etichetta, AR, size, col_tx, corpo))


def freccia_giu(y, d=56):
    return ('  <div style="position: absolute; left: 0; right: 0; top: %dpx; text-align: center; '
            'font-size: %dpx; line-height: 1; color: %s; font-weight: 700;">&#8595;</div>\n'
            % (y, d, ORO))


def elenco_spunte(y, voci, size=40, passo=68, left=64):
    out = ''
    for i, t in enumerate(voci):
        out += ('  <div style="position: absolute; left: %dpx; top: %dpx; display: flex; '
                'align-items: center; gap: 20px;">%s'
                '<span style="font-family: %s; font-weight: 600; font-size: %dpx; color: %s;">%s</span>'
                '</div>\n' % (left, y + i * passo, spunta(), MA, size, INK, t))
    return out


def barra_proporzione(y, h=58, piene=1, n=4, gap=12, left=64, right=64):
    """Una casella su quattro accesa: il 27,2% reso senza scrivere una cifra in piu'."""
    out = ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; height: %dpx; '
           'display: flex; gap: %dpx;">' % (left, right, y, h, gap))
    for i in range(n):
        acceso = i < piene
        out += ('<div style="flex: 1; border-radius: 12px; background: %s; %s"></div>'
                % (ORO if acceso else CARD,
                   '' if acceso else 'border: 2px solid #E2DACB;'))
    return out + '</div>\n'


MESI = ['G', 'F', 'M', 'A', 'M', 'G', 'L', 'A', 'S', 'O', 'N', 'D']


def barra_mesi(y, piene, cella=68, alta=92, gap=10, left=64):
    """Dodici caselle, nessun numero e nessuna percentuale: i mesi pieni e i vuoti."""
    out = ('  <div style="position: absolute; left: %dpx; top: %dpx; display: flex; gap: %dpx;">'
           % (left, y, gap))
    for i in range(12):
        acceso = i in piene
        out += ('<div style="width: %dpx;"><div style="height: %dpx; border-radius: 12px; '
                'background: %s; %s"></div>'
                '<div style="text-align: center; margin-top: 10px; font-family: %s; font-weight: 700; '
                'font-size: 20px; letter-spacing: 0.06em; color: %s;">%s</div></div>'
                % (cella, alta, ORO if acceso else CARD,
                   '' if acceso else 'border: 2px solid #E2DACB;',
                   MA, INK if acceso else INK_2, MESI[i]))
    return out + '</div>\n'


def pastiglia_dato(y, cifra, testo, left=64, larghezza=560):
    """Si sovrappone al bordo basso del blocco foto: e' il punto in cui il dato
    tocca l'immagine, l'unico contatto fra foto e testo su fondo chiaro."""
    return ('  <div style="position: absolute; left: %dpx; top: %dpx; width: %dpx; '
            'background: %s; border-radius: 20px; padding: 22px 30px; '
            'box-shadow: 0 10px 30px rgba(46,42,37,0.10);">'
            '<div style="font-family: %s; font-weight: 900; font-size: 62px; line-height: 1; '
            'color: %s;">%s</div>'
            '<div style="font-family: %s; font-weight: 500; font-size: 29px; color: %s; '
            'margin-top: 10px;">%s</div></div>\n'
            % (left, y, larghezza, FONDO, AR, INK, cifra, MA, INK_2, testo))


def oroink(t):
    return '<span style="color:%s">%s</span>' % (ORO_INK, t)


# ----------------------------------------------------------------- carosello
def carosello():
    nomi = []

    # ---- C1 · gancio (foto in blocco, testo accanto) ----
    c  = frame(1080, 1350)
    c += marchio(100)
    c += foto('salotto-banda.jpg', 250, 400, x=64, w=952, raggio=24)
    # Tre righe volute: a due, "al mese." andava a capo da solo e il filo oro
    # finiva sopra la parola come una cancellatura.
    c += blocco(['La tua casa chiusa', 'non costa %s' % oroink('zero euro'), 'al mese.'],
                710, 62, 900)
    c += filo(955, larghezza=220)
    c += blocco(["L'hai solo sempre visto", 'diviso in cinque pezzi.'],
                1000, 44, 500, INK_2, font=MA, lh=1.32, tracking=0)
    c += kicker('→ scorri', 1235)
    nomi.append(('Main.dc.html', c))

    # ---- C2 · il dato, con la fonte a video ----
    c  = frame(1080, 1350)
    c += marchio(100)
    c += kicker('Il dato', 270)
    c += blocco(['27,2%'], 330, 180, 900, INK, lh=0.92)
    c += blocco(['Più di 1 casa su 4', 'in Italia non è occupata.'], 560, 60, 800)
    c += barra_proporzione(740, piene=1, n=4)
    c += blocco(['9.581.772 abitazioni su 35.271.829.'], 840, 38, 500, INK_2,
                font=MA, lh=1.3, tracking=0)
    c += blocco(['Non è un problema di pochi.', 'È come è fatto il Paese.'], 950, 45, 800)
    c += fonte(FONTE_ISTAT, 1250)
    nomi.append(('C2.dc.html', c))

    # ---- C3 · IL MODULO — la slide da salvare ----
    c  = frame(1080, 1350)
    c += marchio(100)
    c += kicker('Il conto del vuoto', 235)
    c += blocco(['Le cinque voci che paghi', 'anche a casa chiusa'], 290, 60, 900)
    c += modulo_euro(450, altezza=104)
    c += blocco(['Non ci sono cifre nostre: questo conto è solo tuo.'], 1105, 30, 500,
                INK_2, font=MA, lh=1.3, tracking=0)
    c += kicker('Salva questa slide', 1265)
    nomi.append(('C3.dc.html', c))

    # ---- C4 · il ribaltamento ----
    c  = frame(1080, 1350)
    c += marchio(100)
    c += blocco(['Quelle voci non spariscono.'], 250, 60, 900)
    c += blocco(['Cambia da dove escono i soldi.'], 340, 40, 500, INK_2,
                font=MA, lh=1.3, tracking=0)
    c += fascia(440, 230, 'Casa chiusa', ['Le cinque voci escono', 'dal tuo stipendio.'])
    c += freccia_giu(700)
    c += fascia(790, 250, 'Casa a reddito',
                ['Le stesse voci escono da quello', 'che la casa ha incassato.'], oro=True)
    c += blocco(['Non esiste la casa a costo zero.',
                 'Esiste la casa che i suoi costi %s.' % oroink('se li paga')],
                1090, 44, 800)
    c += kicker('→ scorri', 1265)
    nomi.append(('C4.dc.html', c))

    # ---- C5 · offerta + CTA ----
    c  = frame(1080, 1350)
    c += marchio(100)
    c += blocco(['La nostra voce compare', '%s.' % oroink('solo se la casa ha incassato')],
                250, 58, 900)
    c += badge(430, '15% SUL FATTURATO GENERATO', size=31, h=70)
    c += elenco_spunte(560, SERVIZI, size=38, passo=66)
    c += blocco(["Si parte da com'è la casa: il primo passo",
                 'è una valutazione, non un cantiere.'], 930, 32, 500, INK_2,
                font=MA, lh=1.34, tracking=0)
    c += blocco(['Guadagniamo solo se guadagni tu.'], 1030, 31, 600, INK_CORPO,
                font=MA, lh=1.3, tracking=0)
    c += pill(1150, 110, 'Scrivi CALCOLO in DM')
    nomi.append(('C5.dc.html', c))
    return nomi


# ------------------------------------------------------------------ facebook
def facebook():
    nomi = []

    # ---- F1 · 9:16 — la prima del collage, deve avere la CTA ----
    c  = frame(1080, 1920)
    c += marchio(112)
    c += foto('vuota-banda.jpg', 260, 560, x=64, w=952, raggio=24)
    c += pastiglia_dato(740, '27,2%', 'abitazioni non occupate in Italia', left=64, larghezza=600)
    c += blocco(['La tua casa chiusa', 'non costa %s' % oroink('zero euro'), 'al mese.'],
                940, 62, 900)
    c += filo(1185, larghezza=240)
    c += blocco(['Cinque voci corrono uguale,', 'serranda alzata o abbassata.'],
                1235, 44, 500, INK_2, font=MA, lh=1.32, tracking=0)
    c += fonte(FONTE_ISTAT, 1390)
    c += blocco(['Guadagniamo solo se guadagni tu.'], 1450, 31, 600, INK_CORPO,
                font=MA, lh=1.3, tracking=0)
    c += pill(1530, 110, 'Scrivi CALCOLO in DM')
    c += kicker('Salva questo post', 1690)
    nomi.append(('F1.dc.html', c))

    # ---- F2 · 1:1 — l'elenco ----
    c  = frame(1080, 1080)
    c += marchio(64)
    c += blocco(['Cinque voci a casa chiusa'], 190, 58, 900)
    c += blocco(['Il totale fallo tu, coi tuoi bollettini.'], 268, 32, 500, INK_2,
                font=MA, lh=1.3, tracking=0)
    c += modulo_euro(340, altezza=86, size_voce=38, size_det=25, campo=190, totale=False)
    c += blocco(["Nessuno te l'ha mai messo su una riga sola."], 810, 44, 800)
    c += filo(900, larghezza=952)
    nomi.append(('F2.dc.html', c))

    # ---- F3 · 1:1 — ribaltamento + offerta ----
    c  = frame(1080, 1080)
    c += marchio(64)
    c += blocco(['Quelle voci non spariscono.'], 190, 58, 900)
    c += blocco(['Cambia da dove escono i soldi.'], 268, 38, 500, INK_2,
                font=MA, lh=1.3, tracking=0)
    c += fascia(350, 160, 'Casa chiusa', ['Escono dal tuo stipendio.'], size=40)
    c += freccia_giu(528, d=44)
    c += fascia(590, 170, 'Casa a reddito',
                ['Escono da quello che la casa ha incassato.'], oro=True, size=38)
    c += blocco(['La nostra voce compare solo a incasso avvenuto:',
                 '%s sul fatturato generato.' % oroink('15%')], 800, 32, 500, INK_2,
                font=MA, lh=1.34, tracking=0)
    c += blocco(['Guadagniamo solo se guadagni tu.'], 900, 30, 600, INK_CORPO,
                font=MA, lh=1.3, tracking=0)
    c += pill(955, 96, 'Scrivi CALCOLO in DM')
    nomi.append(('F3.dc.html', c))
    return nomi


# -------------------------------------------------------------------- storie
def storie():
    nomi = []

    # ---- S1 · "la casa dei tuoi" ----
    c  = frame(1080, 1920)
    c += marchio(112)
    c += foto('camera-banda.jpg', 270, 300, x=64, w=952, raggio=24)
    c += blocco(['«Tanto chiusa', 'non costa niente.»'], 640, 68, 900)
    c += filo(810, larghezza=220)
    c += modulo_euro(870, altezza=92, size_voce=38, size_det=25, campo=170, totale=False)
    c += blocco(["Nessuno te l'ha mai messo", 'su una riga sola.'], 1360, 44, 800)
    c += blocco(['Quelle voci non spariscono se la casa lavora:',
                 'cambia solo %s.' % oroink('da dove escono i soldi')],
                1480, 34, 500, INK_2, font=MA, lh=1.34, tracking=0)
    c += blocco(['15% sul fatturato generato.'], 1580, 32, 600, INK)
    c += blocco(['Guadagniamo solo se guadagni tu.'], 1632, 29, 600, INK_2,
                font=MA, lh=1.3, tracking=0)
    c += pill(1700, 108, 'Scrivi CALCOLO in DM')
    nomi.append(('S1.dc.html', c))

    # ---- S2 · "i mesi vuoti" ----
    c  = frame(1080, 1920)
    c += marchio(112)
    c += barra_mesi(320, piene=[5, 6, 7, 9], cella=68, alta=92)
    # Tre righe volute: a due, "dei mesi pieni." andava a capo da solo e il filo
    # oro finiva sopra la parola come una cancellatura.
    c += blocco(['I mesi vuoti pagano', 'le %s' % oroink('stesse spese'), 'dei mesi pieni.'],
                510, 60, 900)
    c += filo(740, larghezza=220)
    c += blocco(['La tassa rifiuti, le quote condominiali,',
                 "l'assicurazione e la quota fissa dei contatori",
                 'non guardano il calendario: arrivano uguali', 'a febbraio e ad agosto.'],
                790, 36, 500, INK_2, font=MA, lh=1.34, tracking=0)
    c += fascia(1010, 200, 'Perché succede',
                ['Tenere un calendario aperto tutto', "l'anno è un mestiere a parte."], size=40)
    c += blocco(['Il calendario %s, aperto e aggiornato,' % oroink('lo teniamo noi'),
                 'dentro la gestione completa: check-in smart H24,',
                 'gestione ospiti, pulizie in standard alberghiero.'],
                1250, 33, 500, INK_2, font=MA, lh=1.36, tracking=0)
    c += blocco(["15% sul fatturato generato: l'unica voce",
                 'che compare solo se la casa ha incassato.'], 1410, 31, 600, INK,
                font=MA, lh=1.32, tracking=0)
    c += blocco(['Guadagniamo solo se guadagni tu.'], 1512, 29, 600, INK_2,
                font=MA, lh=1.3, tracking=0)
    c += pill(1660, 108, 'Scrivi CALCOLO in DM')
    nomi.append(('S2.dc.html', c))
    return nomi


TITOLI = {
    'Main.dc.html': 'Carosello 1/5 · il gancio',
    'C2.dc.html':   'Carosello 2/5 · il dato ISTAT',
    'C3.dc.html':   'Carosello 3/5 · il modulo da salvare',
    'C4.dc.html':   'Carosello 4/5 · il ribaltamento',
    'C5.dc.html':   'Carosello 5/5 · offerta e CTA',
    'F1.dc.html':   'Facebook 1/3 · verticale 9:16',
    'F2.dc.html':   "Facebook 2/3 · l'elenco",
    'F3.dc.html':   'Facebook 3/3 · offerta',
    'S1.dc.html':   'Storia 1 · la casa dei tuoi',
    'S2.dc.html':   'Storia 2 · i mesi vuoti',
}
MISURE = {'Main.dc.html': (1080, 1350), 'C2.dc.html': (1080, 1350), 'C3.dc.html': (1080, 1350),
          'C4.dc.html': (1080, 1350), 'C5.dc.html': (1080, 1350),
          'F1.dc.html': (1080, 1920), 'F2.dc.html': (1080, 1080), 'F3.dc.html': (1080, 1080),
          'S1.dc.html': (1080, 1920), 'S2.dc.html': (1080, 1920)}


def canvas(nomi):
    import json
    arts, x, y, riga_h = [], 0, 0, 0
    for i, n in enumerate(nomi):
        w, h = MISURE[n]
        if i in (5, 8):
            x, y, riga_h = 0, y + riga_h + 200, 0
        arts.append({'file': n, 'x': x, 'y': y, 'w': w, 'h': h,
                     'title': TITOLI[n], 'print': 'fixed'})
        x += w + 160
        riga_h = max(riga_h, h)
    with open(os.path.join(HERE, 'canvas.json'), 'w') as f:
        json.dump({'artboards': arts}, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    tutti = carosello() + facebook() + storie()
    for nome, corpo in tutti:
        scrivi(os.path.join(HERE, nome), corpo)
    canvas([n for n, _ in tutti])
    print('artboard: %d (carosello 5 · facebook 3 · storie 2)' % len(tutti))
