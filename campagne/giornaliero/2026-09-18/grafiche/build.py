# -*- coding: utf-8 -*-
"""Artboard della giornata 18/09/2026 — «Le recensioni non sono un complimento».

Firma del giorno: LA CATENA AD ANELLI (vedi base.py).
Tutti i testi vengono da copy.md. Qui non si riscrive nulla, si impagina.
Le uniche liberta' prese sono le spezzature di riga e i tagli con «…» sulle
recensioni, e sono documentate in direzione-artistica.md.
"""
import json
import os

from base import *   # noqa: F401,F403

HERE = os.path.dirname(os.path.abspath(__file__))
GIORNO = os.path.dirname(HERE)

CTA = 'Scrivi "PUNTEGGIO" in DM'


def indice(testo, y=1250):
    return ('  <div style="position: absolute; left: 64px; top: %dpx; font-family: %s; '
            'font-weight: 600; font-size: 17px; letter-spacing: 5px; color: %s;">%s</div>\n'
            % (y, MA, ORO, testo))


def scorri(y=1010):
    """Affordance del carosello. Sostituisce la freccia isolata in basso a
    destra: riempie il vuoto di coda e non lascia un glifo orfano."""
    return ('  <div style="position: absolute; left: 64px; top: %dpx; display: flex; '
            'align-items: center; gap: 16px; background: rgba(200,162,75,0.16); '
            'border: 2px solid %s; border-radius: 999px; padding: 18px 34px;">'
            '<span style="font-family: %s; font-weight: 700; font-size: 34px; color: %s;">Scorri</span>'
            '<span style="font-size: 36px; color: %s; line-height: 1;">&#8594;</span></div>\n'
            % (y, ORO, AR, BIANCO, ORO))


def voce_anello(y, testo, coda, acceso=True, left=64, right=64, d=22, size=40):
    """Riga dell'elenco delle sei voci (S2): ogni voce e' un micro-anello.

    Non e' una colonna di voci con leader tratteggiati (pattern 16 e 17/09):
    e' lo stesso vocabolario della catena, ridotto. Le cinque voci di lavoro
    sono anelli pieni, «Posizione» e' l'unico anello spento del pacchetto.
    """
    if acceso:
        cerchio = 'background: %s;' % ORO
        col_coda = ORO
        col_testo = BIANCO
    else:
        cerchio = 'background: transparent; border: 2px solid %s;' % VUOTO
        col_coda = T5
        col_testo = T5
    return ('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
            'display: flex; align-items: baseline; gap: 26px;">'
            '<span style="flex: 0 0 auto; width: %dpx; height: %dpx; border-radius: 999px; '
            'transform: translateY(-4px); %s"></span>'
            '<span style="flex: 1; min-width: 0; font-family: %s; font-weight: 600; '
            'font-size: %dpx; line-height: 1.1; letter-spacing: -0.3px; color: %s;">%s</span>'
            '<span style="flex: 0 0 auto; font-family: %s; font-weight: 600; font-size: 33px; '
            'letter-spacing: 0.04em; color: %s;">%s</span></div>\n'
            % (left, right, y, d, d, cerchio, MA, size, col_testo, testo, MA, col_coda, coda))


def catena_verticale(y, righe, accesi=4, left=64, right=64, passo=70, size=40):
    """La catena ruotata: e' il ritmo del quadrato Facebook (F2).

    Filo oro verticale a sinistra, un anello per riga, numero in oro.
    """
    out = []
    n = len(righe)
    cx = left + 13
    out.append('  <div style="position: absolute; left: %dpx; top: %dpx; width: 3px; '
               'height: %dpx; background: %s; border-radius: 2px;"></div>\n'
               % (cx - 1, y + 13, passo * (n - 1), ORO))
    for i, (num, testo) in enumerate(righe):
        yy = y + passo * i
        pieno = i < accesi
        stile = ('background: %s;' % ORO if pieno
                 else 'background: %s; border: 2px solid %s;' % (FUME_DEEP, VUOTO))
        out.append('  <div style="position: absolute; left: %dpx; top: %dpx; width: 26px; '
                   'height: 26px; border-radius: 999px; %s"></div>\n' % (left, yy, stile))
        out.append('  <div style="position: absolute; left: %dpx; right: %dpx; top: %dpx; '
                   'font-family: %s; font-weight: 800; font-size: %dpx; line-height: 1.1; '
                   'letter-spacing: -0.4px; color: %s;">'
                   '<span style="color: %s; font-weight: 900;">%s</span>'
                   '<span style="color: %s;"> · </span>%s</div>\n'
                   % (left + 56, right, yy - 8, AR, size, BIANCO, ORO, num, T5, testo))
    return ''.join(out)


# =====================================================================
# CAROSELLO — 1080x1350. Lockup centrato (marchio 80 + catena 210),
# colonna di testo a sinistra sotto. Indice = anelli accesi.
# =====================================================================
def carosello():
    W, H = 1080, 1350

    # ---- C1 · gancio · 1 anello acceso
    c = frame(W, H)
    c += marchio(80)
    c += catena(210, 1, d=26, etichette=True)
    c += blocco(['Le recensioni non sono', 'un complimento.'], 510, 70, 900)
    c += filo_oro(712, 180)
    c += blocco(['Sono un prezzo.', 'Ti spiego dove si incassa.'], 752, 50, 800, T1)
    c += scorri(1000)
    c += indice('1 / 5')
    scrivi(os.path.join(HERE, 'C1.dc.html'), c)

    # ---- C2 · anello 1 — la visibilita' · 2 anelli
    c = frame(W, H)
    c += marchio(80)
    c += catena(210, 2, d=26, etichette=True)
    c += kicker('Anello 01 &mdash; Visibilità', 340)
    c += blocco(['Primo: dove ti trovano.'], 400, 62, 900)
    c += blocco(['Il punteggio pesa in come esci',
                 'quando qualcuno cerca una casa.'], 500, 45, 800, T1)
    c += fascia_sabbia(760, ['La tua casa non la trova chi passa per strada.',
                             'La trova chi scorre un portale.'],
                       size=40, peso=600, pad_v=40, lh=1.34)
    c += scorri(1010)
    c += indice('2 / 5')
    scrivi(os.path.join(HERE, 'C2.dc.html'), c)

    # ---- C3 · anello 2 — il prezzo · SLIDE DEL NUMERO · 3 anelli
    c = frame(W, H)
    c += marchio(80)
    c += catena(210, 3, d=26, etichette=True)
    c += kicker('Anello 02 &mdash; Prezzo', 340)
    c += blocco(['Secondo: quanto puoi chiedere.'], 400, 50, 900)
    c += ('  <div style="position: absolute; left: 64px; top: 500px; font-family: %s; '
          'font-weight: 900; font-size: 200px; line-height: 1; letter-spacing: -8px; '
          'color: %s;">+11%%</div>\n' % (AR, ORO))
    c += blocco(['+1 punto di valutazione su 5 = circa +11% di prezzo,',
                 'a occupazione invariata.'], 760, 33, 600, BIANCO, font=MA, lh=1.36)
    c += fonte(['Cornell Center for Hospitality Research &mdash; Anderson, 2012.',
                'Studio sul settore alberghiero, non su case vacanza.'], 870)
    c += filo_oro(960, 180)
    c += blocco(['Nell&rsquo;hotellerie questo legame &egrave; misurato da anni.'],
                1000, 33, 600, T2, font=MA, lh=1.3)
    c += blocco(['Sulla tua casa non &egrave; una promessa.', '&Egrave; la direzione.'],
                1060, 40, 800, BIANCO, lh=1.2)
    c += indice('3 / 5', 1250)
    scrivi(os.path.join(HERE, 'C3.dc.html'), c)

    # ---- C4 · anello 3 — chi prenota · 4 anelli · CARD RECENSIONE
    c = frame(W, H)
    c += marchio(80)
    c += catena(210, 4, d=26, etichette=True)
    c += kicker('Anello 03 &mdash; Chi prenota', 340)
    c += blocco(['Terzo: chi prenota.'], 400, 50, 900)
    c += blocco(['Chi ha poco tempo non compra',
                 'il risparmio. Compra la certezza.'], 470, 45, 800, T1)
    c += stelle(648, size=31)
    c += card_recensione(
        690,
        ['&laquo; &hellip; L&rsquo;appartamento era in ordine sotto',
         'ogni aspetto, splendidamente pulito,',
         'ordinato e confortevole&hellip; &raquo;'],
        'Attila &middot; 3 settimane fa')
    c += blocco(['Guarda di cosa parlano: pulizia, arrivo preparato,',
                 'risposte. Non parlano del mare.'], 1030, 33, 600, BIANCO, font=MA, lh=1.32)
    c += blocco(['Non &egrave; il prezzo a educare l&rsquo;ospite: &egrave; il',
                 'posizionamento a filtrare chi prenota.'], 1130, 33, 600, T3, font=MA, lh=1.32)
    c += indice('4 / 5')
    scrivi(os.path.join(HERE, 'C4.dc.html'), c)

    # ---- C5 · chi fa il lavoro + CTA · catena completa, senza etichette
    c = frame(W, H)
    c += marchio(80)
    c += catena(210, 4, d=26)
    c += blocco(['Quel punteggio &egrave; lavoro.'], 330, 62, 900)
    c += blocco(['Pulizia, accuratezza, check-in,',
                 'comunicazione: li fa qualcuno.'], 430, 45, 800, T1)
    c += blocco(['E non &egrave; un&rsquo;eredit&agrave;: il livello Superhost',
                 'l&rsquo;abbiamo raggiunto in due mesi, da un profilo nuovo.'],
                580, 33, 600, T2, font=MA, lh=1.34)
    c += fascia_sabbia(700, ['Gestione completa in standard alberghiero.',
                             'Commissione <b style="color:%s">15%%</b> sul fatturato generato.' % ORO_TESTO,
                             'Guadagniamo solo se guadagni tu.'],
                       size=33, peso=600, pad_v=36, lh=1.52)
    # Spezzatura a mano: la riga del copy a 70 battute andava a capo da sola e
    # lasciava «distribuire,» orfano addosso alla CTA.
    c += blocco(['A settembre il litorale rallenta. Con meno prenotazioni',
                 'da distribuire, il punteggio pesa di pi&ugrave;, non di meno.'],
                950, 31, 600, T4, font=MA, lh=1.34)
    c += cta_pillola(1080, 'Scrivi &laquo;PUNTEGGIO&raquo; in DM', h=90, size=40)
    c += indice('5 / 5')
    scrivi(os.path.join(HERE, 'C5.dc.html'), c)


# =====================================================================
# FACEBOOK — F1 9:16 + F2/F3 1:1
# =====================================================================
def facebook():
    # ---- F1 · 1080x1920 · gancio + problema · catena ancora spenta
    c = frame(1080, 1920)
    c += marchio(112)
    c += catena(420, 1, d=64, etichette=True, spessore=4)
    c += blocco(['Hai il punteggio alto.'], 780, 70, 900, allinea='center')
    c += ('  <div style="position: absolute; left: 0; right: 0; top: 920px; '
          'text-align: center;"><span style="display: inline-block; width: 180px; '
          'height: 3px; background: %s; border-radius: 2px;"></span></div>\n' % ORO)
    c += blocco(['E in banca', 'non &egrave; cambiato niente.'], 970, 62, 800, T1,
                allinea='center')
    c += kicker('Le recensioni non sono un complimento', 1330, colore=ORO, size=31,
                allinea='center')
    scrivi(os.path.join(HERE, 'F1.dc.html'), c)

    # ---- F2 · 1080x1080 · la catena + CARD RECENSIONE
    c = frame(1080, 1080)
    c += marchio(56)
    c += blocco(['Dove si incassa un punteggio.'], 170, 50, 900)
    c += catena_verticale(268, [
        ('01', 'Il punteggio pesa nel posizionamento'),
        ('02', 'Ti trova chi scorre un portale'),
        ('03', 'Il prezzo non lo devi abbassare'),
        ('04', 'Prenota chi cerca tranquillità'),
    ], passo=72, size=36)
    c += stelle(590, size=31)
    c += card_recensione(
        632,
        ['&laquo;L&rsquo;appartamento &egrave; dotato di accessori da cucina,',
         'lavatrice e letti confortevoli. Ottima comunicazione',
         'con l&rsquo;host. Consigliato&raquo;'],
        'Katarzyna', size=34, size_meta=31, pad_v=30, lh=1.32)
    c += kicker('Non &egrave; fortuna. &Egrave; lavoro.', 990, colore=ORO, size=31)
    scrivi(os.path.join(HERE, 'F2.dc.html'), c)

    # ---- F3 · 1080x1080 · offerta + CTA
    c = frame(1080, 1080)
    c += marchio(56)
    c += catena(160, 4, d=22)
    c += blocco(['Quel punteggio', 'lo fa qualcuno.'], 214, 62, 900)
    c += blocco(['Pulizia, check-in, risposte.', 'Tutti i giorni.'], 372, 45, 800, T1)
    c += fascia_sabbia(510, ['Gestione completa in standard alberghiero.',
                             'Commissione <b style="color:%s">15%%</b> sul fatturato generato.' % ORO_TESTO,
                             'Guadagniamo solo se guadagni tu.'],
                       size=33, peso=600, pad_v=34, lh=1.52)
    c += cta_pillola(808, 'Scrivi &laquo;PUNTEGGIO&raquo;', h=96, size=44)
    c += kicker('Roma &middot; Ostia &middot; Litorale', 954, colore=T4, size=17)
    scrivi(os.path.join(HERE, 'F3.dc.html'), c)


# =====================================================================
# STORIE — 1080x1920. Terzo ritmo: UN SOLO anello, grande.
# =====================================================================
def storie():
    # ---- S1 · anello 02 (prezzo) + CARD RECENSIONE
    c = frame(1080, 1920)
    c += marchio(112)
    c += anello_grande(232, '02', 'Anello 02 &mdash; Prezzo', d=104)
    c += blocco(['Non abbassare il prezzo.', 'Ancora.'], 440, 62, 900)
    c += blocco(['Le prenotazioni calano e la prima cosa',
                 'che si tocca &egrave; la tariffa.'], 620, 40, 600, T2, font=MA, lh=1.36)
    c += filo_oro(760, 180)
    c += blocco(['Il punteggio &egrave; la ragione per cui puoi',
                 'non farlo: chi ti trova ha gi&agrave;',
                 'un motivo per fidarsi.'], 800, 50, 800, BIANCO, lh=1.2)
    c += stelle(1010, size=31)
    c += card_recensione(
        1052,
        ['&laquo;&hellip; L&rsquo;appartamento era pulito, confortevole e',
         'preparato per il nostro arrivo&hellip; Consiglio',
         'vivamente questo posto!&raquo;'],
        'Paweł &middot; giugno 2026')
    c += blocco(['Non &egrave; fortuna. &Egrave; lavoro fatto tutti i giorni.'],
                1380, 33, 600, T3, font=MA)
    c += cta_pillola(1460, 'Scrivi &laquo;PUNTEGGIO&raquo; in DM', h=90, size=40)
    scrivi(os.path.join(HERE, 'S1.dc.html'), c)

    # ---- S2 · anello 01 (la recensione: da dove viene) + sei voci
    c = frame(1080, 1920)
    c += marchio(112)
    c += anello_grande(232, '01', 'Anello 01 &mdash; Recensione', d=104)
    c += blocco(['&ldquo;Tanto il punteggio', 'dipende dall&rsquo;ospite.&rdquo;'],
                440, 62, 900, T4)
    c += blocco(['L&rsquo;ospite valuta sei voci.', 'Una sola non dipende da te.'],
                610, 50, 800, BIANCO, lh=1.2)
    c += filo_oro(770, 180)
    voci = [('Pulizia', 'lavoro', True),
            ('Accuratezza', 'lavoro', True),
            ('Check-in', 'lavoro', True),
            ('Comunicazione', 'lavoro', True),
            ('Rapporto qualit&agrave;-prezzo', 'lavoro', True),
            ('Posizione', 'non dipende da nessuno', False)]
    for i, (testo, coda, acceso) in enumerate(voci):
        c += voce_anello(820 + i * 84, testo, coda, acceso, size=40)
    c += blocco(['Cinque su sei sono esecuzione. E l&rsquo;esecuzione si affida.'],
                1380, 33, 600, T3, font=MA)
    c += cta_pillola(1460, 'Scrivi &laquo;PUNTEGGIO&raquo; in DM', h=90, size=40)
    scrivi(os.path.join(HERE, 'S2.dc.html'), c)


# =====================================================================
# REEL — cover + 12 scene 1080x1920. Testo CENTRATO (quarto ritmo, e
# soprattutto: nessun blocco di testo a sinistra a meta' altezza).
# La catena e' l'unico indicatore di avanzamento: la barra a 4 tacche
# prevista dal copy e' TOLTA su veto esplicito del titolare.
# =====================================================================
SCENE = [
    # (id, accesi, kicker, righe, nota)
    ('R01', None, None, ['Le recensioni', 'non sono un complimento.']),
    ('R02', None, None, ['Sono un prezzo.']),
    ('R03', 0, 'Funziona così', []),
    ('R04', 1, 'Funziona così', ['Il punteggio conta', 'in come esci nelle ricerche.']),
    ('R05', 2, 'Funziona così', ['E la tua casa', 'la trova chi scorre un portale.']),
    ('R06', 3, 'Funziona così', ['Chi ti trova', 'ha gi&agrave; un motivo per fidarsi.']),
    ('R07', 4, 'Funziona così', ['Quindi il prezzo', '@non lo devi abbassare.']),
    ('R08', 4, 'Funziona così', []),
    ('R09', None, None, ['Un punteggio alto', 'non &egrave; fortuna.']),
    ('R10', None, None, ['&Egrave; pulizia, risposte,', 'check-in. Tutti i giorni.']),
    ('R11', None, None, ['Guadagniamo solo', 'se guadagni tu.']),
    ('R12', None, None, ['Le recensioni', 'non sono un complimento.']),
]


def reel():
    # ---- copertina
    c = frame(1080, 1920)
    c += marchio(112)
    c += catena(430, 4, d=64, etichette=True, spessore=4)
    c += blocco(['Le recensioni', 'non sono', 'un complimento.'], 780, 70, 900,
                allinea='center', lh=1.14)
    c += ('  <div style="position: absolute; left: 0; right: 0; top: 1090px; '
          'text-align: center;"><span style="display: inline-block; width: 180px; '
          'height: 3px; background: %s; border-radius: 2px;"></span></div>\n' % ORO)
    c += blocco(['Sono un prezzo.'], 1140, 62, 800, T1, allinea='center')
    c += kicker('Dove si incassa un punteggio', 1300, colore=ORO, size=31,
                allinea='center')
    scrivi(os.path.join(HERE, 'R00.dc.html'), c)

    for sid, accesi, kick, righe in SCENE:
        c = frame(1080, 1920)
        c += marchio(112)
        if accesi is not None:
            c += catena(430, accesi, d=64, etichette=True, spessore=4)
        if kick:
            c += kicker(kick, 300, colore=ORO, size=31, allinea='center')
        if righe:
            evid = [r for r in righe if r.startswith('@')]
            normali = [r for r in righe if not r.startswith('@')]
            if len(righe) == 1:
                c += blocco(righe, 880, 70, 900, allinea='center')
                c += ('  <div style="position: absolute; left: 0; right: 0; top: 1010px; '
                      'text-align: center;"><span style="display: inline-block; width: 180px; '
                      'height: 3px; background: %s; border-radius: 2px;"></span></div>\n' % ORO)
            elif evid:
                c += blocco(normali, 820, 70, 900, allinea='center')
                c += evidenziatore([e[1:] for e in evid], 930, 62, 900, left=64, right=64)
            else:
                c += blocco([righe[0]], 820, 70, 900, allinea='center')
                c += blocco(righe[1:], 930, 62, 800, T1, allinea='center')
        if sid == 'R11':
            c += cta_pillola(1400, 'Scrivi &laquo;PUNTEGGIO&raquo; in DM', h=90, size=40)
        scrivi(os.path.join(HERE, '%s.dc.html' % sid), c)


# =====================================================================
# canvas.json + reel/scene.json
# =====================================================================
TAVOLA = [
    ('C1.dc.html', 1080, 1350, 'Carosello 1/5 &middot; il gancio'),
    ('C2.dc.html', 1080, 1350, 'Carosello 2/5 &middot; anello 01 visibilità'),
    ('C3.dc.html', 1080, 1350, 'Carosello 3/5 &middot; anello 02 prezzo (+11%)'),
    ('C4.dc.html', 1080, 1350, 'Carosello 4/5 &middot; anello 03 chi prenota'),
    ('C5.dc.html', 1080, 1350, 'Carosello 5/5 &middot; il lavoro + CTA'),
    ('F1.dc.html', 1080, 1920, 'Facebook 1 &middot; gancio 9:16'),
    ('F2.dc.html', 1080, 1080, 'Facebook 2 &middot; la catena + recensione'),
    ('F3.dc.html', 1080, 1080, 'Facebook 3 &middot; offerta + CTA'),
    ('S1.dc.html', 1080, 1920, 'Storia 1 &middot; anello 02 + recensione'),
    ('S2.dc.html', 1080, 1920, 'Storia 2 &middot; anello 01 + sei voci'),
    ('R00.dc.html', 1080, 1920, 'Reel &middot; copertina'),
] + [('%s.dc.html' % s[0], 1080, 1920, 'Reel &middot; scena %s' % s[0][1:])
     for s in SCENE]


def tavolo():
    x = y = 0
    out = []
    for i, (f, w, h, t) in enumerate(TAVOLA):
        out.append({'file': f, 'x': x, 'y': y, 'w': w, 'h': h, 'title': t,
                    'print': 'fixed'})
        x += w + 160
        if (i + 1) % 6 == 0:
            x = 0
            y += 2080
    with open(os.path.join(HERE, 'canvas.json'), 'w') as fh:
        json.dump({'artboards': out}, fh, indent=2, ensure_ascii=False)
    return out


# --------------------------------------------------------------- scene.json
DUR = [(1, 0.0, 2.0), (2, 2.0, 3.4), (3, 3.4, 5.2), (4, 5.2, 7.2), (5, 7.2, 9.2),
       (6, 9.2, 11.4), (7, 11.4, 13.6), (8, 13.6, 14.2), (9, 14.2, 16.2),
       (10, 16.2, 18.4), (11, 18.4, 21.0), (12, 21.0, 21.0)]

TESTI = {
    1: ['Le recensioni', 'non sono un complimento.'],
    2: ['Sono un prezzo.'],
    3: [],
    4: ['Il punteggio conta', 'in come esci nelle ricerche.'],
    5: ['E la tua casa', 'la trova chi scorre un portale.'],
    6: ['Chi ti trova', 'ha già un motivo per fidarsi.'],
    7: ['Quindi il prezzo', 'non lo devi abbassare.'],
    8: [],
    9: ['Un punteggio alto', 'non è fortuna.'],
    10: ['È pulizia, risposte,', 'check-in. Tutti i giorni.'],
    11: ['Guadagniamo solo', 'se guadagni tu.'],
}
ACCESI = {3: 0, 4: 1, 5: 2, 6: 3, 7: 4, 8: 4}


def scene_json():
    el = []
    dur = 21.6

    def add(**kw):
        el.append(kw)

    # marchio fisso
    add(id='marchio', nome='Marchio &middot; HADRIANUS', tipo='testo',
        testo='HADRIANUS', x=0, y=112, w=1080, allinea='center',
        font='Archivo', peso=800, size=33, tracking=9, colore='#FFFFFF',
        t_in=0.0, t_out=dur, anim_in='sfuma', anim_out='sfuma', dur_in=0.3)
    add(id='marchio_sub', nome='Marchio &middot; MULTISERVICE', tipo='testo',
        testo='MULTISERVICE', x=0, y=156, w=1080, allinea='center',
        font='Manrope', peso=600, size=17, tracking=7, colore='rgba(255,255,255,0.72)',
        t_in=0.0, t_out=dur, anim_in='sfuma', anim_out='sfuma', dur_in=0.3)

    util = 1080 - 128
    d = 64
    passo = util - d
    cx = [64 + d / 2.0 + passo * i / 3.0 for i in range(4)]

    for n, t0, t1 in DUR:
        p = 's%02d_' % n
        if n in ACCESI:
            acc = ACCESI[n]
            # filo spento
            add(id=p + 'filo', nome='Scena %d &middot; filo catena' % n, tipo='fascia',
                x=int(cx[0]), y=460, w=int(cx[3] - cx[0]), h=4,
                fondo='rgba(255,255,255,0.18)', raggio=2,
                t_in=t0, t_out=t1, anim_in='nessuna', anim_out='taglio')
            if acc >= 2:
                add(id=p + 'filo_oro', nome='Scena %d &middot; filo acceso' % n,
                    tipo='fascia', x=int(cx[0]), y=460,
                    w=int(cx[acc - 1] - cx[0]), h=4, fondo='#C8A24B', raggio=2,
                    t_in=t0, t_out=t1, anim_in='maschera-sinistra', anim_out='taglio',
                    dur_in=0.26)
            for i in range(4):
                pieno = i < acc
                add(id=p + 'anello%d' % (i + 1),
                    nome='Scena %d &middot; anello %d%s' % (n, i + 1, ' acceso' if pieno else ''),
                    tipo='fascia', x=int(cx[i] - d / 2), y=430, w=d, h=d,
                    fondo='#C8A24B' if pieno else 'rgba(46,42,37,1)', raggio=999,
                    bordo=None if pieno else '3px solid rgba(255,255,255,0.22)',
                    t_in=t0, t_out=t1,
                    anim_in='scatto' if (pieno and i == acc - 1) else 'nessuna',
                    anim_out='taglio', dur_in=0.22)
                add(id=p + 'etichetta%d' % (i + 1),
                    nome='Scena %d &middot; etichetta %d' % (n, i + 1), tipo='testo',
                    testo=['RECENSIONE', 'VISIBILITÀ', 'PREZZO', 'CHI PRENOTA'][i],
                    x=int(cx[i] - 130) if 0 < i < 3 else (64 if i == 0 else 1080 - 64 - 260),
                    y=512, w=260,
                    allinea='center' if 0 < i < 3 else ('left' if i == 0 else 'right'),
                    font='Manrope', peso=600, size=17, tracking=2.7,
                    colore='#C8A24B' if pieno else 'rgba(255,255,255,0.55)',
                    t_in=t0, t_out=t1, anim_in='nessuna', anim_out='taglio')
            add(id=p + 'kicker', nome='Scena %d &middot; kicker' % n, tipo='testo',
                testo='FUNZIONA COSÌ', x=0, y=300, w=1080, allinea='center',
                font='Manrope', peso=600, size=31, tracking=5.6, colore='#C8A24B',
                t_in=t0, t_out=t1, anim_in='sfuma', anim_out='taglio', dur_in=0.2)

        righe = TESTI.get(n, [])
        if len(righe) == 1:
            add(id=p + 'riga1', nome='Scena %d &middot; riga unica' % n, tipo='testo',
                testo=righe[0], x=64, y=880, w=952, allinea='center',
                font='Archivo', peso=900, size=70, colore='#FFFFFF',
                t_in=t0, t_out=t1, anim_in='scatto', anim_out='taglio', dur_in=0.18)
            add(id=p + 'filo_sotto', nome='Scena %d &middot; filo sotto la frase' % n,
                tipo='fascia', x=450, y=1010, w=180, h=3, fondo='#C8A24B', raggio=2,
                t_in=t0 + 0.18, t_out=t1, anim_in='maschera-sinistra', anim_out='taglio',
                dur_in=0.26)
        elif righe:
            add(id=p + 'riga1', nome='Scena %d &middot; riga 1' % n, tipo='testo',
                testo=righe[0], x=64, y=820, w=952, allinea='center',
                font='Archivo', peso=900, size=70, colore='#FFFFFF',
                t_in=t0, t_out=t1, anim_in='maschera-basso', anim_out='esce-alto',
                dur_in=0.2)
            evid = (n == 7)
            add(id=p + 'riga2', nome='Scena %d &middot; riga 2' % n, tipo='testo',
                testo=righe[1], x=64, y=930, w=952, allinea='center',
                font='Archivo', peso=900 if evid else 800, size=62,
                colore='#2E2A25' if evid else 'rgba(255,255,255,0.88)',
                fondo='#C8A24B' if evid else None,
                t_in=t0 + (0.4 if n in (6, 7) else 0.28), t_out=t1,
                anim_in='maschera-sinistra' if evid else 'maschera-basso',
                anim_out='esce-alto', dur_in=0.26)

        if n == 11:
            add(id=p + 'cta', nome='Scena 11 &middot; CTA', tipo='fascia',
                x=64, y=1400, w=952, h=90, fondo='#C8A24B', raggio=999,
                testo='SCRIVI «PUNTEGGIO» IN DM', font='Archivo', peso=800,
                size=40, colore='#2E2A25',
                t_in=t0 + 1.2, t_out=dur, anim_in='entra-basso', anim_out='esce-basso',
                dur_in=0.26)

    dati = {'versione': 1,
            'titolo': 'Le recensioni non sono un complimento',
            'data': '2026-09-18', 'durata': dur, 'fondo': '#3F3A33',
            'sfondo_immagine': None, 'elementi': el}
    reel_dir = os.path.join(GIORNO, 'reel')
    os.makedirs(reel_dir, exist_ok=True)
    with open(os.path.join(reel_dir, 'scene.json'), 'w') as fh:
        json.dump(dati, fh, indent=2, ensure_ascii=False)
    return dati


def main():
    carosello()
    facebook()
    storie()
    reel()
    t = tavolo()
    s = scene_json()
    print('%d artboard + canvas.json + reel/scene.json (%d elementi)'
          % (len(t), len(s['elementi'])))


if __name__ == '__main__':
    main()
