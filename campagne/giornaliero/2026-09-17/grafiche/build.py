# -*- coding: utf-8 -*-
"""Artboard della giornata 17/09/2026 — «Ad agosto sei pieno come tutti».

Firma del giorno: LO SCALINO (vedi base.py). Tutti i testi vengono da copy.md,
gia' passato da compliance-checker: qui non si riscrive nulla, si impagina.
Le uniche liberta' prese sono le spezzature di riga, ed esistono per una ragione
sola — tenere identica l'altezza dei blocchi di confronto.
"""
import json
import os

from base import *   # noqa: F401,F403

HERE = os.path.dirname(os.path.abspath(__file__))
GIORNO = os.path.dirname(HERE)

# ---------------------------------------------------------------- foto
BALCONE_45  = 'foto-balcone-4x5.jpg'
CUCINA_45   = 'foto-cucina-4x5.jpg'
CUCINA_11   = 'foto-cucina-1x1.jpg'
CUCINA_916  = 'foto-cucina-9x16.jpg'
TRAMONTO_916 = 'foto-tramonto-9x16.jpg'

# Velo: la fascia centrale e' quella che porta il testo, quindi va caricata li'.
# Regola di qualita' 4: serve piu' VELO, non piu' ombra.
VELO_45 = ('radial-gradient(ellipse 94% 36% at 50% 52%, rgba(26,23,19,0.66), transparent 66%)',
           'linear-gradient(180deg, rgba(63,58,51,0.92) 0%, rgba(63,58,51,0.40) 42%, '
           'rgba(63,58,51,0.94) 100%)')
# La domanda in oro sta al 31-37% dell'altezza: li' il velo va tenuto carico,
# altrimenti l'oro sul piano chiaro scende sotto il 4,5:1.
VELO_C5 = ('radial-gradient(ellipse 98% 46% at 50% 56%, rgba(26,23,19,0.62), transparent 72%)',
           'linear-gradient(180deg, rgba(63,58,51,0.94) 0%, rgba(63,58,51,0.88) 34%, '
           'rgba(63,58,51,0.64) 52%, rgba(46,42,37,0.92) 100%)')
VELO_F1 = ('radial-gradient(ellipse 90% 30% at 50% 56%, rgba(26,23,19,0.64), transparent 62%)',
           'linear-gradient(180deg, rgba(63,58,51,0.82) 0%, rgba(63,58,51,0.10) 30%, '
           'rgba(46,42,37,0.92) 82%, rgba(46,42,37,0.94) 100%)')
VELO_F3 = ('radial-gradient(ellipse 98% 50% at 50% 54%, rgba(26,23,19,0.64), transparent 72%)',
           'linear-gradient(180deg, rgba(63,58,51,0.92) 0%, rgba(63,58,51,0.66) 44%, '
           'rgba(46,42,37,0.92) 100%)')
VELO_REEL = ('radial-gradient(ellipse 90% 28% at 50% 46%, rgba(26,23,19,0.62), transparent 64%)',
             'linear-gradient(180deg, rgba(63,58,51,0.86) 0%, rgba(63,58,51,0.10) 30%, '
             'rgba(63,58,51,0.66) 40%, rgba(63,58,51,0.66) 57%, '
             'rgba(63,58,51,0.88) 100%)')

RAD_C3 = 'radial-gradient(ellipse 80% 40% at 50% 30%, rgba(200,162,75,0.10), transparent 70%)'
RAD_F2 = 'radial-gradient(ellipse 80% 45% at 50% 25%, rgba(200,162,75,0.12), transparent 70%)'
RAD_S2 = 'radial-gradient(circle 420px at 50% 38%, rgba(200,162,75,0.16), transparent 70%)'

CTA = 'Scrivi "NOVEMBRE" in DM'

# ------------------------------------------------- le coppie di confronto
# (criterio, riga AGOSTO — 1 riga, righe NOVEMBRE — SEMPRE 2)
COPPIE_C3 = [
    ('Prezzo',  'si alza e basta.',
     ['si muove ogni settimana,', 'a volte ogni giorno.']),
    ('Durata',  'soggiorni brevi, tanti check-in.',
     ['soggiorni pi&ugrave; lunghi,', 'non pi&ugrave; rari.']),
    ('Ospite',  'chi viene per il mare o per Roma.',
     ['congressi, fiere, aeroporto,', 'ospedali, universit&agrave;.']),
]
COPPIE_C4 = [
    ('Canali', 'la domanda ti trova.',
     ['la domanda va cercata, e l&rsquo;annuncio', 'va riscritto per un altro cliente.']),
    ('Risposte', 'rispondere conta.',
     ['chi risponde per primo', 'prende la prenotazione.']),
    ('Manutenzione', 'si rimanda, la casa &egrave; occupata.',
     ['&egrave; la finestra. Se non si fa adesso,', 'tocca farla a luglio, con la casa piena.']),
]


# ============================================================ CAROSELLO
def c1():
    o = frame(1080, 1350, FUME_DEEP)
    o += foto(BALCONE_45)
    o += velo(*VELO_45)
    o += strato('linear-gradient(0deg, rgba(74,68,58,0.34), rgba(74,68,58,0.34))')
    o += marchio(y=80, ombra=True)
    o += indice('1/5', y=88, ombra=True)
    o += blocco(['Ad agosto sei pieno', 'come tutti.'], 470, 70, 900, BIANCO,
                lh=1.12, ombra=True)
    o += scalino(700, ['Non &egrave; l&igrave; che si vede', 'chi ti gestisce la casa.'],
                 size=50, peso=800, font=AR, colore=T1, lh=1.22, pad_v=26)
    o += freccia(1210)
    return o


def c2():
    o = frame(1080, 1350, FUME)
    o += strato(RAD_C3)
    o += marchio(y=80)
    o += indice('2/5', y=88)
    o += blocco(['E non &egrave; un tuo errore.'], 380, 62, 900, ORO, lh=1.14)
    o += blocco(['Nessuno ti ha mai dato', 'un metro per giudicare.'], 540, 50, 800, BIANCO,
                lh=1.22)
    o += scalino(780, ['Agosto non &egrave; un esame.', '&Egrave; un regalo del calendario.'],
                 size=33, peso=600, colore=T1, lh=1.36, pad_v=28)
    o += freccia(1180)
    return o


def c3():
    o = frame(1080, 1350, FUME)
    o += strato(RAD_C3)
    o += marchio(y=80)
    o += indice('3/5', y=88)
    o += blocco(['Stessa casa, due mestieri.'], 232, 50, 900, BIANCO, lh=1.2)
    y = 348
    for k, a, n in COPPIE_C3:
        o += gradino(y, k, a, n)
        y += 264 + 20
    o += freccia(1210)
    return o


def c4():
    o = frame(1080, 1350, FUME)
    o += strato(RAD_C3)
    o += marchio(y=80)
    o += indice('4/5', y=88)
    o += blocco(['E poi c&rsquo;&egrave; il lavoro che non si vede.'], 206, 45, 900, BIANCO,
                lh=1.2)
    y = 300
    for k, a, n in COPPIE_C4:
        o += gradino(y, k, a, n)
        y += 264 + 20
    o += banda(1160, 126, '61,5%',
               ['di occupazione alberghiera a Roma,', 'gennaio-marzo 2026.'],
               'Uno dei trimestri pi&ugrave; bassi dell&rsquo;anno. Federalberghi Roma su dati STR.')
    return o


def c5():
    o = frame(1080, 1350, FUME_DEEP)
    o += foto(CUCINA_45)
    o += velo(*VELO_C5)
    o += marchio(y=80, ombra=True)
    o += indice('5/5', y=88, ombra=True)
    o += blocco(['La domanda da fare', 'a chi ti gestisce la casa.'], 240, 50, 900, BIANCO,
                lh=1.22, ombra=True)
    o += blocco(['&laquo;Cosa fai a novembre?&raquo;'], 420, 62, 900, ORO, lh=1.16, ombra=True)
    o += scalino(540, ['Gestione completa a Roma e Ostia, in standard',
                       'alberghiero: prezzo mosso ogni settimana, annuncio',
                       'riscritto per chi viaggia fuori stagione, check-in',
                       'H24, ospiti seguiti, pulizie e controlli.'],
                 size=33, peso=600, colore=T1, lh=1.36, pad_v=26)
    o += blocco(['15% sul fatturato generato.'], 806, 50, 800, BIANCO, lh=1.2, ombra=True)
    o += fonte('Pagamento il 10 di ogni mese. Le utenze restano tue.', 878, size=31,
               colore=T1)
    o += blocco(['Ad agosto ci guadagnano tutti.',
                 'Da ottobre guadagniamo solo se guadagni tu.'], 944, 40, 800, ORO, lh=1.3,
                ombra=True)
    o += cta_banda(1130, CTA)
    return o


# ============================================================= FACEBOOK
def f1():
    o = frame(1080, 1920, FUME_DEEP)
    o += foto(TRAMONTO_916)
    o += velo(*VELO_F1)
    o += marchio(y=112, ombra=True)
    o += blocco(['Ad agosto sei pieno', 'come tutti.'], 820, 70, 900, BIANCO, lh=1.12,
                ombra=True)
    o += scalino(1050, ['E non &egrave; un tuo errore:', 'ad agosto si riempie anche da soli.'],
                 size=45, peso=800, font=AR, colore=T1, lh=1.24, pad_v=26, indent=56)
    o += kicker('Roma &middot; Ostia &middot; Litorale', 1300, size=31, ombra=True)
    return o


def f2():
    o = frame(1080, 1080, FUME)
    o += strato(RAD_F2)
    o += marchio(y=64)
    o += blocco(['Stessa casa, due mestieri.'], 170, 62, 900, BIANCO, lh=1.16)
    o += kicker('Cosa cambia da ottobre', 262, size=31)
    righe = [
        ['Il prezzo si muove', 'ogni settimana'],
        ['L&rsquo;annuncio si riscrive per chi', 'viaggia fuori stagione'],
        ['Richieste seguite subito,', 'manutenzione nei mesi bassi'],
    ]
    y = 320
    for r in righe:
        o += scalino(y, r, size=40, peso=600, colore=BIANCO, lh=1.28, pad_v=22, h=146)
        y += 146 + 18
    o += blocco(['Ad agosto il lavoro lo fa il calendario.',
                 'Da ottobre lo deve fare qualcuno.'], 860, 45, 800, ORO, lh=1.22)
    return o


def f3():
    o = frame(1080, 1080, FUME_DEEP)
    o += foto(CUCINA_11)
    o += velo(*VELO_F3)
    o += marchio(y=64, ombra=True)
    o += kicker('La domanda da fare', 172, size=31, ombra=True)
    o += kicker('a chi ti gestisce la casa', 216, size=31, ombra=True)
    o += blocco(['&laquo;Cosa fai a novembre?&raquo;'], 286, 62, 900, BIANCO, lh=1.16,
                ombra=True)
    o += scalino(394, ['15% sul fatturato generato.',
                       'Pagamento il 10 di ogni mese.',
                       'Le utenze restano tue.'],
                 size=33, peso=600, colore=T1, lh=1.38, pad_v=26)
    o += blocco(['Ad agosto ci guadagnano tutti.',
                 'Da ottobre guadagniamo solo se guadagni tu.'], 650, 40, 800, ORO, lh=1.24,
                ombra=True)
    o += cta_banda(836, CTA)
    return o


# =============================================================== STORIE
def s1():
    o = frame(1080, 1920, FUME)
    o += strato(RAD_C3)
    o += marchio(y=200)
    o += blocco(['Il tuo agosto pieno', 'non dimostra niente.'], 500, 62, 900, BIANCO, lh=1.16)
    o += blocco(['E non &egrave; colpa tua: ad agosto si riempie',
                 'anche da soli. Il mese facile lo vince',
                 'il calendario.'], 740, 33, 500, T1, font=MA, lh=1.44)
    o += scalino(950, ['Il gestore si vede da ottobre a marzo:',
                       'come muove il prezzo, per chi riscrive',
                       'l&rsquo;annuncio, quanto ci mette a rispondere.'],
                 size=33, peso=600, colore=BIANCO, lh=1.40, pad_v=28)
    o += blocco(['Ad agosto ci guadagnano tutti.',
                 'Da ottobre guadagniamo solo se guadagni tu.'], 1270, 40, 800, ORO, lh=1.26)
    o += cta_pillola(1450, CTA)
    return o


def s2():
    o = frame(1080, 1920, FUME)
    o += strato(RAD_S2)
    o += marchio(y=200)
    o += blocco(['Agosto non fa testo.', 'Gennaio s&igrave;.'], 380, 62, 900, BIANCO, lh=1.16)
    # Numero, frase e fonte nella STESSA card: il 61,5% non deve mai poter essere
    # letto come occupazione di Hadrianus.
    o += ('  <div style="position: absolute; left: 136px; right: 64px; top: 600px; '
          'background: %s; border-left: 3px solid %s; border-radius: 16px; '
          'padding: 28px 34px 26px 27px;">'
          '<div style="font-family: %s; font-weight: 900; font-size: 70px; line-height: 1; '
          'letter-spacing: -2px; color: %s;">61,5%%</div>'
          '<div style="font-family: %s; font-weight: 600; font-size: 33px; line-height: 1.34; '
          'color: %s; margin-top: 18px;">occupazione alberghiera a Roma,<br>'
          'gennaio-marzo 2026 &mdash; uno dei trimestri<br>pi&ugrave; bassi dell&rsquo;anno.</div>'
          '<div style="font-family: %s; font-weight: 500; font-size: 17px; line-height: 1.4; '
          'color: %s; margin-top: 16px;">Federalberghi Roma su dati STR.</div>'
          '</div>\n' % (GROUND_N, ORO, AR, ORO, MA, BIANCO, MA, T4))
    o += ('  <div style="position: absolute; left: 64px; right: 64px; top: 950px; '
          'background: %s; border-radius: 16px; padding: 26px 32px;">'
          '<div style="font-family: %s; font-weight: 500; font-size: 33px; line-height: 1.42; '
          'color: %s;">Non &egrave; che non viene nessuno: viene gente<br>'
          'diversa. Congressi, fiere, scalo di<br>Fiumicino, ospedali, universit&agrave;.<br>'
          'E l&rsquo;annuncio va scritto per loro, non per<br>il turista di agosto.</div>'
          '</div>\n' % (GROUND_A, MA, T1))
    o += fonte('Gestione completa in standard alberghiero,<br>15% sul fatturato generato.',
               1272, size=33, colore=T1)
    o += blocco(['Ad agosto ci guadagnano tutti.',
                 'Da ottobre guadagniamo solo se guadagni tu.'], 1380, 40, 800, ORO, lh=1.26)
    o += cta_pillola(1500, CTA)
    return o


# ================================================================= REEL
# La sceneggiatura e' quella di copy.md: 17 scene, durate calcolate sui tempi
# minimi di lettura. Qui sta una volta sola e alimenta DUE uscite: le artboard
# R01-R17 e reel/scene.json (il montaggio e le pagine Canva).
SCENE = [
    (1,  0.0,  1.8,  'foto',    ['Ad agosto sei pieno', 'come tutti.']),
    (2,  1.8,  3.6,  'pieno',   ['Non &egrave; l&igrave; che si vede', 'il gestore.']),
    (3,  3.6,  4.7,  'svolta',  ['Meglio cos&igrave;.']),
    (4,  4.7,  6.5,  'pieno',   ['Agosto non &egrave; un esame.', '&Egrave; un regalo del calendario.']),
    (5,  6.5,  7.0,  'kicker',  []),
    (6,  7.0,  8.6,  'coppia',  ('il prezzo si alza e basta',
                                 ['il prezzo si muove', 'ogni settimana'])),
    (7,  8.6,  10.2, 'coppia',  ('soggiorni brevi, tanti check-in',
                                 ['soggiorni pi&ugrave; lunghi,', 'non pi&ugrave; rari'])),
    (8,  10.2, 11.8, 'coppia',  ('la domanda ti trova',
                                 ['la domanda', 'va cercata'])),
    (9,  11.8, 13.4, 'coppia',  ('rispondere conta',
                                 ['rispondere in un&rsquo;ora', '&egrave; fatturato'])),
    (10, 13.4, 15.0, 'coppia',  ('la manutenzione si rimanda',
                                 ['&egrave; la finestra', 'per farla'])),
    (11, 15.0, 15.4, 'fermo',   ('la manutenzione si rimanda',
                                 ['&egrave; la finestra', 'per farla'])),
    (12, 15.4, 17.2, 'pieno',   ['Ad agosto il lavoro', 'lo fa il calendario.']),
    (13, 17.2, 19.0, 'pieno',   ['Da ottobre', 'lo deve fare qualcuno.']),
    (14, 19.0, 20.8, 'dato',    ['Roma, gennaio-marzo 2026:', '61,5% di occupazione alberghiera.']),
    (15, 20.8, 22.6, 'chiusa',  ['Ad agosto ci guadagnano tutti.',
                                 'Da ottobre guadagniamo solo se guadagni tu.']),
    (16, 22.6, 24.6, 'cta',     [CTA]),
    (17, 24.6, 24.6, 'loop',    []),
]

# Geometria della coppia, identica per tutte e cinque (regola di omogeneita').
Y_AGO, H_AGO = 746, 160
Y_NOV, H_NOV = 926, 246
BARRA_Y, BARRA_SEG, BARRA_GAP = 230, 180, 13


def barra(attive):
    o = ''
    for i in range(5):
        x = 64 + i * (BARRA_SEG + BARRA_GAP)
        col = ORO if i < attive else 'rgba(255,255,255,0.18)'
        o += ('  <div style="position: absolute; left: %dpx; top: %dpx; width: %dpx; '
              'height: 6px; border-radius: 3px; background: %s;"></div>\n'
              % (x, BARRA_Y, BARRA_SEG, col))
    return o


def coppia_html(ago, nov):
    o = ('  <div style="position: absolute; left: 64px; right: 64px; top: %dpx; height: %dpx; '
         'background: %s; border-radius: 22px; padding: 26px 34px;">'
         '<div style="font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 0.18em; '
         'text-transform: uppercase; color: %s;">Agosto</div>'
         '<div style="font-family: %s; font-weight: 800; font-size: 50px; line-height: 1.2; '
         'letter-spacing: -0.6px; color: %s; margin-top: 10px; white-space: nowrap;">%s</div>'
         '</div>\n' % (Y_AGO, H_AGO, GROUND_A, MA, T3, AR, T2, ago))
    righe = ''.join('<div style="white-space: nowrap;">%s</div>' % r for r in nov)
    o += ('  <div style="position: absolute; left: 136px; right: 64px; top: %dpx; height: %dpx; '
          'background: %s; border-left: 3px solid %s; border-radius: 16px 0 0 16px; '
          'padding: 28px 34px 28px 27px;">'
          '<div style="font-family: %s; font-weight: 600; font-size: 17px; letter-spacing: 0.18em; '
          'text-transform: uppercase; color: %s;">Novembre</div>'
          '<div style="font-family: %s; font-weight: 900; font-size: 62px; line-height: 1.26; '
          'letter-spacing: -1px; color: %s; margin-top: 10px;">%s</div>'
          '</div>\n' % (Y_NOV, H_NOV, GROUND_N, ORO, MA, ORO, AR, BIANCO, righe))
    return o


def scena_artboard(num, t0, t1, tipo, dati):
    su_foto = tipo in ('foto', 'loop')
    o = frame(1080, 1920, FUME_DEEP if su_foto else FUME)
    if su_foto:
        o += foto(CUCINA_916)
        o += velo(*VELO_REEL)
    else:
        o += strato(RAD_C3)
    o += marchio(y=112, ombra=su_foto)

    if tipo in ('coppia', 'fermo', 'kicker'):
        o += barra({'kicker': 0}.get(tipo, num - 5))
        o += kicker('Cosa cambia davvero', 300, size=31)

    if tipo in ('foto', 'pieno'):
        o += blocco(dati, 840, 70, 900, BIANCO, lh=1.18, ombra=su_foto)
    elif tipo == 'svolta':
        o += blocco(dati, 890, 70, 900, ORO, lh=1.18, allinea='center')
    elif tipo in ('coppia', 'fermo'):
        o += coppia_html(dati[0], dati[1])
    elif tipo == 'dato':
        o += blocco(['Roma, gennaio-marzo 2026:'], 790, 50, 800, T1, lh=1.2)
        o += blocco(['61,5%'], 866, 70, 900, ORO, lh=1.0)
        o += blocco(['di occupazione alberghiera.'], 966, 50, 800, BIANCO, lh=1.2)
        o += fonte('Federalberghi Roma su dati STR', 1048, size=31, colore=T4)
    elif tipo == 'chiusa':
        o += blocco([dati[0]], 820, 50, 800, T1, lh=1.24)
        o += ('  <div style="position: absolute; left: 64px; top: 916px; width: 856px; '
              'height: 140px; background: %s; border-radius: 8px;"></div>\n' % ORO)
        o += blocco(['Da ottobre guadagniamo', 'solo se guadagni tu.'], 926, 50, 900,
                    FUME_DEEP, left=78, right=160, lh=1.3)
    elif tipo == 'cta':
        o += cta_pillola(1400, dati[0], h=88)

    return o


# --------------------------------------------------- reel/scene.json
def _el(eid, nome, **kw):
    d = {'id': eid, 'nome': nome, 'tipo': kw.pop('tipo', 'testo')}
    d.update(kw)
    return d


def scene_json():
    D = 24.6
    velo = ('radial-gradient(ellipse 90% 28% at 50% 46%, rgba(26,23,19,0.62), transparent 64%), '
            'linear-gradient(180deg, rgba(63,58,51,0.86) 0%, rgba(63,58,51,0.10) 34%, '
            'rgba(63,58,51,0.88) 100%)')
    els = [
        _el('foto_apertura', 'Foto interno &middot; apertura', tipo='immagine',
            src='../grafiche/' + CUCINA_916, x=0, y=0, w=1080, h=1920, fit='cover',
            t_in=0.0, t_out=1.8, anim_in='nessuna', anim_out='taglio'),
        _el('velo_apertura', 'Velo sulla foto &middot; apertura', tipo='fascia',
            x=0, y=0, w=1080, h=1920, fondo=velo, raggio=0,
            t_in=0.0, t_out=1.8, anim_in='nessuna', anim_out='taglio'),
        _el('foto_loop', 'Foto interno &middot; ritorno per il loop', tipo='immagine',
            src='../grafiche/' + CUCINA_916, x=0, y=0, w=1080, h=1920, fit='cover',
            t_in=24.4, t_out=D, anim_in='sfuma', anim_out='nessuna', dur_in=0.2),
        _el('velo_loop', 'Velo sulla foto &middot; ritorno', tipo='fascia',
            x=0, y=0, w=1080, h=1920, fondo=velo, raggio=0,
            t_in=24.4, t_out=D, anim_in='sfuma', anim_out='nessuna', dur_in=0.2),
        _el('marchio', 'Marchio Hadrianus', testo='HADRIANUS', x=64, y=112, w=952,
            font='Archivo', peso=800, size=33, colore='#FFFFFF', tracking=9,
            t_in=0.0, t_out=D, anim_in='sfuma', anim_out='nessuna', dur_in=0.4),
        _el('sottomarchio', 'Sottotitolo marchio', testo='MULTISERVICE', x=64, y=160, w=952,
            font='Manrope', peso=600, size=17, colore='rgba(255,255,255,0.72)', tracking=7,
            t_in=0.0, t_out=D, anim_in='sfuma', anim_out='nessuna', dur_in=0.4),
    ]

    # --- barra di avanzamento (reel oltre i 10 s)
    for i in range(5):
        x = 64 + i * (BARRA_SEG + BARRA_GAP)
        els.append(_el('barra_bin%d' % (i + 1), 'Binario barra %d' % (i + 1), tipo='fascia',
                       x=x, y=BARRA_Y, w=BARRA_SEG, h=6, fondo='rgba(255,255,255,0.18)',
                       raggio=3, t_in=6.5, t_out=15.4, anim_in='sfuma', anim_out='sfuma'))
        els.append(_el('barra_seg%d' % (i + 1), 'Segmento barra %d' % (i + 1), tipo='fascia',
                       x=x, y=BARRA_Y, w=BARRA_SEG, h=6, fondo=ORO, raggio=3,
                       t_in=7.0 + i * 1.6, t_out=15.4,
                       anim_in='maschera-sinistra', anim_out='sfuma', dur_in=0.3))

    els.append(_el('kicker', 'Kicker COSA CAMBIA DAVVERO', testo='COSA CAMBIA DAVVERO',
                   x=64, y=300, w=952, font='Manrope', peso=600, size=31, tracking=5.6,
                   colore=ORO, t_in=6.5, t_out=15.4,
                   anim_in='scatto', anim_out='esce-alto', dur_in=0.3))

    for num, t0, t1, tipo, dati in SCENE:
        if tipo in ('foto', 'pieno'):
            els.append(_el('s%02d_testo' % num, 'Scena %d' % num,
                           testo='<br>'.join(dati), x=64, y=840, w=952,
                           font='Archivo', peso=900, size=70, lh=1.18, colore='#FFFFFF',
                           t_in=t0, t_out=t1,
                           anim_in='maschera-basso', anim_out='esce-alto', dur_in=0.2))
        elif tipo == 'svolta':
            els.append(_el('s%02d_svolta' % num, 'Scena %d &middot; la parola di svolta' % num,
                           testo=dati[0], x=64, y=890, w=952, allinea='center',
                           font='Archivo', peso=900, size=70, colore=ORO,
                           t_in=t0, t_out=t1, anim_in='scatto', anim_out='sfuma',
                           dur_in=0.18))
        elif tipo in ('coppia', 'fermo'):
            ago, nov = dati
            # La scena 11 e' l'immobilita' dopo il picco: la coppia 5 resta in
            # campo, non si ridisegna. Quindi niente elementi nuovi.
            if tipo == 'fermo':
                continue
            fine = 15.4 if num == 10 else t1     # la 5ª coppia tiene fino al fermo
            els += [
                _el('s%02d_ago_f' % num, 'Coppia %d &middot; fondo agosto' % (num - 5),
                    tipo='fascia', x=64, y=Y_AGO, w=952, h=H_AGO, fondo=GROUND_A, raggio=22,
                    t_in=t0, t_out=fine, anim_in='entra-sinistra', anim_out='esce-alto',
                    dur_in=0.4),
                _el('s%02d_ago_t' % num, 'Coppia %d &middot; etichetta AGOSTO' % (num - 5),
                    testo='AGOSTO', x=98, y=Y_AGO + 26, w=400, font='Manrope', peso=600,
                    size=17, tracking=3, colore=T3, t_in=t0, t_out=fine,
                    anim_in='entra-sinistra', anim_out='esce-alto', dur_in=0.4),
                _el('s%02d_ago_r' % num, 'Coppia %d &middot; riga agosto' % (num - 5),
                    testo=ago, x=98, y=Y_AGO + 72, w=884, font='Archivo', peso=800,
                    size=50, colore=T2, t_in=t0, t_out=fine,
                    anim_in='entra-sinistra', anim_out='esce-alto', dur_in=0.4),
                _el('s%02d_nov_f' % num, 'Coppia %d &middot; fondo novembre' % (num - 5),
                    tipo='fascia', x=136, y=Y_NOV, w=880, h=H_NOV, fondo=GROUND_N, raggio=16,
                    t_in=t0 + 0.25, t_out=fine, anim_in='entra-destra', anim_out='esce-alto',
                    dur_in=0.4),
                _el('s%02d_nov_s' % num, 'Coppia %d &middot; stecca oro' % (num - 5),
                    tipo='fascia', x=136, y=Y_NOV, w=3, h=H_NOV, fondo=ORO, raggio=0,
                    t_in=t0 + 0.25, t_out=fine, anim_in='entra-destra', anim_out='esce-alto',
                    dur_in=0.4),
                _el('s%02d_nov_t' % num, 'Coppia %d &middot; etichetta NOVEMBRE' % (num - 5),
                    testo='NOVEMBRE', x=166, y=Y_NOV + 28, w=400, font='Manrope', peso=600,
                    size=17, tracking=3, colore=ORO, t_in=t0 + 0.25, t_out=fine,
                    anim_in='entra-destra', anim_out='esce-alto', dur_in=0.4),
                _el('s%02d_nov_r' % num, 'Coppia %d &middot; righe novembre' % (num - 5),
                    testo='<br>'.join(nov), x=166, y=Y_NOV + 74, w=816, font='Archivo',
                    peso=900, size=62, lh=1.26, colore='#FFFFFF',
                    t_in=t0 + 0.25, t_out=fine, anim_in='entra-destra', anim_out='esce-alto',
                    dur_in=0.4),
            ]
        elif tipo == 'dato':
            els += [
                _el('s14_riga', 'Scena 14 &middot; il territorio',
                    testo='Roma, gennaio-marzo 2026:',
                    x=64, y=790, w=952, font='Archivo', peso=800, size=50, colore=T1,
                    t_in=t0, t_out=t1, anim_in='maschera-basso', anim_out='esce-alto',
                    dur_in=0.2),
                _el('s14_num', 'Scena 14 &middot; il dato', testo='61,5%',
                    x=64, y=866, w=952, font='Archivo', peso=900, size=70, lh=1.0, colore=ORO,
                    t_in=t0 + 0.2, t_out=t1, anim_in='scatto', anim_out='esce-alto',
                    dur_in=0.45),
                _el('s14_voce', 'Scena 14 &middot; di che cosa',
                    testo='di occupazione alberghiera.',
                    x=64, y=966, w=952, font='Archivo', peso=800, size=50, colore='#FFFFFF',
                    t_in=t0 + 0.3, t_out=t1, anim_in='maschera-basso', anim_out='esce-alto',
                    dur_in=0.2),
                _el('s14_fonte', 'Scena 14 &middot; la fonte', testo='Federalberghi Roma su dati STR',
                    x=64, y=1048, w=952, font='Manrope', peso=500, size=31, colore=T4,
                    t_in=t0 + 0.4, t_out=t1, anim_in='sfuma', anim_out='esce-alto'),
            ]
        elif tipo == 'chiusa':
            els += [
                _el('s15_a', 'Scena 15 &middot; agosto', testo=dati[0],
                    x=64, y=820, w=952, font='Archivo', peso=800, size=50, colore=T1,
                    t_in=t0, t_out=t1, anim_in='maschera-basso', anim_out='esce-alto',
                    dur_in=0.2),
                _el('s15_evid', 'Scena 15 &middot; evidenziatore oro', tipo='fascia',
                    x=64, y=916, w=856, h=140, fondo=ORO, raggio=8,
                    t_in=t0 + 0.4, t_out=t1, anim_in='maschera-sinistra',
                    anim_out='esce-alto', dur_in=0.26),
                _el('s15_b', 'Scena 15 &middot; da ottobre', testo='Da ottobre guadagniamo<br>solo se guadagni tu.',
                    x=78, y=926, w=880, font='Archivo', peso=900, size=50, lh=1.3,
                    colore=FUME_DEEP, t_in=t0 + 0.4, t_out=t1,
                    anim_in='maschera-sinistra', anim_out='esce-alto', dur_in=0.26),
            ]
        elif tipo == 'cta':
            els.append(_el('s16_cta', 'Scena 16 &middot; CTA', testo=CTA.upper(),
                           x=64, y=1400, w=952, h=88, fondo=ORO, raggio=999,
                           padding='0px', allinea='center', font='Manrope', peso=600,
                           size=31, tracking=4.3, colore=FUME_DEEP,
                           t_in=t0, t_out=24.4, anim_in='entra-basso',
                           anim_out='esce-basso', dur_in=0.26, dur_out=0.2))

    return {
        'versione': 1,
        'titolo': 'Ad agosto sei pieno come tutti',
        'data': '2026-09-17',
        'durata': D,
        'fondo': FUME,
        'sfondo_immagine': None,
        'elementi': els,
    }


# ================================================================ MAIN
ARTBOARD = [
    ('C1.dc.html', c1, 1080, 1350, 'Carosello 1/5 &middot; il gancio'),
    ('C2.dc.html', c2, 1080, 1350, 'Carosello 2/5 &middot; il sollievo'),
    ('C3.dc.html', c3, 1080, 1350, 'Carosello 3/5 &middot; tre scalini'),
    ('C4.dc.html', c4, 1080, 1350, 'Carosello 4/5 &middot; il lavoro che non si vede'),
    ('C5.dc.html', c5, 1080, 1350, 'Carosello 5/5 &middot; offerta e CTA'),
    ('F1.dc.html', f1, 1080, 1920, 'Facebook 1/3 &middot; verticale 9:16'),
    ('F2.dc.html', f2, 1080, 1080, 'Facebook 2/3 &middot; cosa cambia da ottobre'),
    ('F3.dc.html', f3, 1080, 1080, 'Facebook 3/3 &middot; offerta'),
    ('S1.dc.html', s1, 1080, 1920, 'Storia 1 &middot; il metro'),
    ('S2.dc.html', s2, 1080, 1920, 'Storia 2 &middot; agosto non fa testo'),
]


def main():
    tavola = []
    x = y = 0
    for i, (nome, fn, w, h, titolo) in enumerate(ARTBOARD):
        scrivi(os.path.join(HERE, nome), fn())
        tavola.append({'file': nome, 'x': (i % 5) * 1240, 'y': (i // 5) * 2120,
                       'w': w, 'h': h, 'title': titolo, 'print': 'fixed'})

    for j, (num, t0, t1, tipo, dati) in enumerate(SCENE):
        nome = 'R%02d.dc.html' % num
        scrivi(os.path.join(HERE, nome), scena_artboard(num, t0, t1, tipo, dati))
        tavola.append({'file': nome, 'x': (j % 6) * 1240, 'y': 4300 + (j // 6) * 2120,
                       'w': 1080, 'h': 1920,
                       'title': 'Reel scena %d &middot; %.1f-%.1f s' % (num, t0, t1),
                       'print': 'fixed'})

    with open(os.path.join(HERE, 'canvas.json'), 'w') as f:
        json.dump({'artboards': tavola}, f, indent=2, ensure_ascii=False)

    reel = os.path.join(GIORNO, 'reel')
    os.makedirs(reel, exist_ok=True)
    with open(os.path.join(reel, 'scene.json'), 'w') as f:
        json.dump(scene_json(), f, indent=2, ensure_ascii=False)

    print('%d artboard + canvas.json + reel/scene.json' % len(tavola))


if __name__ == '__main__':
    main()
