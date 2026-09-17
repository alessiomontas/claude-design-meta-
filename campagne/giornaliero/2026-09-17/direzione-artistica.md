# Direzione artistica — giornaliero 17/09/2026

**Pilastro:** il territorio · **Angolo:** «Ad agosto sei pieno come tutti. Non è lì che si vede il gestore.»

## Mood

**Sollievo, fermo, comparativo.** Tre aggettivi, in quest'ordine di importanza.

Il rischio del contenuto è tutto in una parola: il proprietario può leggere «il tuo agosto non
dimostra niente» come un rimprovero. Il visivo deve togliere quella lettura prima che il testo venga
letto. Per questo:

- **niente rosso, niente allarme, niente ✕.** Nessun segno di errore compare in tutto il pacchetto:
  il proprietario non ha sbagliato, ha guardato il mese sbagliato;
- **niente asimmetria di giudizio.** Agosto non viene *barrato* né spento: viene messo alla base, e
  novembre gli sta sopra di un gradino. È una differenza di mestiere, non un voto;
- **fermo.** Nessun elemento inclinato, nessuna ombra morbida, nessun effetto. Tutto poggia su una
  colonna sola a sinistra. L'aria che resta è voluta: un contenuto che rassicura non può essere
  affollato.

## Impianto del giorno: **lo scalino**

Il contenuto mette a confronto due mesi, e il copy vieta esplicitamente la tabella a due colonne.
Allora il confronto non si mette **affianco**: si mette **sotto e rientrato**.

| Elemento | Cosa fa |
|---|---|
| **La base** — fascia `rgba(255,255,255,.06)`, filo a tutta larghezza della colonna | è AGOSTO: il piano di partenza, il minimo sindacale |
| **Lo scalino** — pannello rientrato di **72 px**, fondo `rgba(200,162,75,.10)`, **stecca oro verticale da 3 px** sul bordo sinistro | è NOVEMBRE: la stessa casa, un gradino più dentro |
| **La marca di mese** — `AGOSTO` / `NOVEMBRE`, Manrope 600 a 17 px, tracking .18em, in linea di base col testo | dice di chi è la riga senza disegnare una colonna |
| **L'etichetta del criterio** — `PREZZO`, `DURATA`, `OSPITE`, `CANALI`… in oro sopra ogni blocco | è l'unico oro che *nomina*: tutto il resto dell'oro è superficie |

Lo scalino torna su **ogni** artboard del pacchetto, anche dove non ci sono due mesi da mettere a
fronte: la riga che conta sta sempre un gradino più dentro delle altre (il sollievo in C1 e F1, la
nota in C2, l'offerta in C5 e F3, il criterio di giudizio in S1, il dato in S2, le tre voci in F2).
È questo a tenere insieme dieci artboard e diciassette scene senza ripetere due volte lo stesso
impaginato.

### Perché è un impianto nuovo

Nessuno dei pattern bruciati: calendario a 12 caselle, scontrino/ledger, blocchi invertiti a piena
larghezza, frase al centro sul reale, barra di avanzamento come impianto, testo nello spazio vuoto
misurato, step numerati giganti, card domanda/risposta, riga di calendario a 7 celle (15/09), marca
temporale + arco (14/09), modulo a caselle vuote (16/09). E **nessuna tabella a due colonne**, come
il copy impone.

Rispetto al 14 e al 15/09, che erano anch'essi scuri: lì la gerarchia la facevano una marca temporale
e un arco (14) e una fila di celle quadrate (15), con il marchio **centrato** in alto. Qui il marchio
è **allineato a sinistra**, l'indice di slide sale **in alto a destra** in asse con lui, e tutta la
pagina è una colonna unica che scende a gradini. Non c'è una cella, non c'è un numero grande, non c'è
una griglia.

### La regola di omogeneità, applicata

Tutte le coppie di una stessa artboard — e tutte e cinque le coppie del reel — hanno **identico**
fondo, identica stecca, identico rientro, identica scala, identica entrata e identico sfasamento.
Nessuna coppia sbiadisce, nessuna si comporta diversamente dalle altre.

**Come è garantito, invece che sperato:** ogni riga è un blocco `white-space: nowrap` con la
spezzatura decisa a mano, e la voce «Novembre» sta **sempre su due righe**. Così l'altezza di un
blocco è un fatto di geometria e non di conteggio caratteri. È la risposta al punto lasciato aperto
dal copywriter su C3/C4: i tre blocchi misurano **264 px esatti** su entrambe le slide, verificato sul
rendering (`grafiche/verifica.py`), non a occhio. Il corpo resta a **33**, come da copy.

## Palette

Nessuna deviazione dal design system. Fondo **fumè `#3F3A33`** come da brief, estremo `#2E2A25`,
fumè medio `#4a443a` nel radiale; oro `#C8A24B`; testo `#FFF`, `rgba(255,255,255,.88/.72/.55)`.

Due regole d'uso che valgono per tutta la giornata:

- **l'oro non decora: separa i due mesi.** Fondo oro velato = novembre. Oro pieno = solo azione
  (CTA), dato (la banda 61,5%) ed evidenziatore. Oro come *parola* = solo l'etichetta del criterio e
  le due righe di chiusura;
- **niente filo oro orizzontale, in nessuna artboard.** La stecca oro è sempre verticale, sempre
  nella gronda a sinistra di un pannello. Nei due pacchetti precedenti una riga oro sotto un titolo è
  finita due volte addosso a una parola e si è letta come una cancellatura: qui la funzione
  `filo()` è stata **rimossa** dalla libreria, non solo non usata.

Il contrasto non è stimato, è misurato sui PNG: il punto peggiore di tutto il pacchetto è
**4,5:1** (la domanda in oro di C5, corpo 62). Dove non bastava si è caricato il **velo**, mai
aggiunta ombra — è la regola 4 del controllo qualità.

## Formati per canale

| Blocco | Artboard | Formato |
|---|---|---|
| Carosello | `C1`–`C5` | 1080×1350 (4:5) |
| Facebook 1ª immagine | `F1` | **1080×1920 (9:16)** — mai 4:5, nel collage verrebbe tagliata |
| Facebook 2ª e 3ª | `F2`, `F3` | 1080×1080 (1:1) |
| Storie autoconclusive | `S1`, `S2` | 1080×1920 (9:16) |
| Reel, una per scena | `R01`–`R17` | 1080×1920 (9:16) |

Griglia unica: margine 64 · colonna utile 952 · safe area 180/320 sui 9:16 · scala
70·62·50·45·40·33·31·17, mai fuori scala.

## Elementi chiave — cosa si nota per primo

| Artboard | Ordine di lettura |
|---|---|
| C1, F1 | la riga grande sulla foto → **lo scalino col sollievo** → il kicker di territorio |
| C2 | la riga oro («E non è un tuo errore.») → il metro → la nota sullo scalino |
| C3, C4 | il titolo → **i tre scalini**, letti come tre gradini identici → (C4) la banda oro del dato, in fondo |
| C5, F3 | la domanda in oro → l'offerta sullo scalino → il 15% → la CTA |
| F2 | il kicker `COSA CAMBIA DA OTTOBRE` → le tre voci, tutte allo stesso modo → la chiusura in oro |
| S1, S2 | il gancio → (S2) il **61,5% con la fonte nella stessa card** → lo scalino → la chiusura → la CTA |
| Reel | la barra che si riempie → AGOSTO alla base → **NOVEMBRE che rientra** → l'evidenziatore → la CTA |

La CTA è **sempre l'ultimo elemento** e **sempre oro pieno**: banda rettangolare nel feed, pillola
nelle storie e nel reel. Testo identico ovunque, `Scrivi "NOVEMBRE" in DM`, virgolette dritte.

## Reel

24,6 s · 17 scene · durate esattamente quelle del copy, calcolate sui tempi minimi di lettura.
Sorgente unica: **`reel/scene.json`** (66 elementi su una sola linea del tempo).

- la foto d'interno sta **solo** nelle scene 1 e 17 (`sfondo_immagine: null`, due elementi immagine
  con il loro velo): dalla scena 2 lo stacco è su fumè pieno, come chiede la sceneggiatura;
- barra di avanzamento a 5 segmenti, uno per coppia, presente da 6,5 a 15,4 s (reel oltre i 10 s);
- le cinque coppie entrano **identiche**: base da sinistra, scalino da destra sfasato di 250 ms,
  stessa durata, stessa scala. La scena 11 non ridisegna niente — è l'immobilità dopo il picco, e la
  quinta coppia resta in campo;
- un solo evidenziatore in tutto il reel, alla scena 15, su `Da ottobre guadagniamo solo se guadagni
  tu`: una **banda** oro piena con il testo in fumè, non riquadri inline (che davano un bordo destro
  frastagliato);
- scena 14: il **61,5%** è l'eroe a corpo 70, con `di occupazione alberghiera.` e la fonte
  `Federalberghi Roma su dati STR` nella stessa inquadratura. Il dato non deve mai poter essere letto
  come occupazione di Hadrianus;
- la CTA esce verso il basso a 24,4 s e torna la foto d'apertura: loop di stato, nessun fade to black.

`R01`–`R17` sono i fotogrammi chiave editabili delle stesse scene, e servono anche da riferimento per
ricostruire il reel in Canva (regola fissa 10).

## Foto

| Dove | File | Nota |
|---|---|---|
| C1 | `brand-assets/immobili/balcone-terrazzo.jpeg` → `foto-balcone-4x5.jpg` | terrazzo di fine estate: è esattamente la scena del prompt di C1 |
| C5, F3, reel 1/17 | `brand-assets/immobili/cucina-soggiorno-open-space.png` (ripulita, vedi sotto) | deciso dal titolare |
| F1 | `brand-assets/ambientazione/tramonto-litorale-romano.jpg` → `foto-tramonto-9x16.jpg` | Roma · Ostia · Litorale |
| S1, S2, C2, C3, C4, F2 | — | fondo fumè pieno |

**Escluse come da consegna:** `smart-tv-streaming-mockup.jpg` (loghi di terzi) e
`salotto-divano-azzurro.jpg` (divano blu contro il «no blue tones»).

**Marchi di terzi rimossi (controllo 6).** La foto della cucina porta due diciture leggibili:
**KOENIC** sul tostapane e **PHILIPS** sul bollitore. In un contenuto di acquisizione clienti non ci
vanno. `grafiche/prepara-foto.py` produce una **copia** ripulita (`fonte-cucina-pulita.png`) e da lì
ricava i ritagli; `brand-assets/` resta intatto. Due tecniche diverse perché i due oggetti non hanno
lo stesso intorno: toppa presa dall'acciaio sopra per il tostapane, ricostruzione della fascia per
interpolazione riga-per-riga per il bollitore (sopra c'è il muro con la placca e sotto le foglie:
qualunque toppa avrebbe portato dentro un pezzo di scena).

**Lock di brand sulle foto:** `saturate(0.72) sepia(0.14) brightness(0.90) contrast(1.06)`, più su C1
una tinta calda piatta `rgba(74,68,58,.34)` — senza, il verde del terrazzo litiga col fumè.

Adobe Stock è stato interrogato per una strada romana d'autunno (la scena del prompt di S1): la
ricerca non ha restituito risultati in questo ambiente. S1 resta quindi su **fondo pieno**, e va
bene così: è la storia del sollievo, porta molto testo, e sotto una foto avrebbe richiesto un velo
tale da annullare la foto stessa.

## Da evitare

- **Qualunque segno di errore** su agosto: ✕, barre, testo spento, rosso. Agosto non è sbagliato, è
  facile. Se un giorno si vorrà una variante più dura, non è questa.
- **La tabella a due colonne**, la griglia calendario, il grafico di andamento stagionale: vietati dal
  copy in tutti e tre i punti NEGATIVE.
- **Il filo oro orizzontale** sotto o sopra una riga di testo.
- **Badge aggiunti in fase grafica** — «0 costi fissi», «nessun deposito», «controlli settimanali»,
  «risposte in un'ora» sotto il marchio: sono tutti `[DATO DA VERIFICARE]` o impegni non documentati.
  In nessuna artboard ne compare uno.
- **Il 61,5% separato dalla sua fonte.** Numero, oggetto e fonte stanno sempre nella stessa card o
  nella stessa banda (S2, C4, reel scena 14).
- **Elementi della stessa famiglia trattati diversamente.** A velocità reale si legge come un errore
  di montaggio.

## Controllo qualità — fatto prima di consegnare

Sui PNG renderizzati, guardati a larghezza telefono, più una verifica misurata
(`grafiche/verifica.py`, che si può rieseguire).

| # | Controllo | Esito |
|---|---|---|
| 1 | Centratura | OK — ogni blocco sulla colonna 64/952, misurato |
| 2 | Troncature | OK — nessun trabocco `nowrap`, nessun elemento fuori frame, **nessuna sovrapposizione** (era il difetto della banda 61,5% sopra il terzo blocco di C4: corretto) |
| 3 | Vuoti | OK — nessuna fascia libera oltre 260 px sulle artboard a fondo piatto. Sulle artboard con foto e nelle scene del reel la fascia libera **è** il contenuto |
| 4 | Contrasto | OK — misurato sui PNG, punto peggiore 4,5:1. Corretto alzando il **velo**, mai l'ombra |
| 5 | Safe area | OK — tutto il testo di lettura dentro 180/1600. Il lockup di marca resta a y 112 sui 9:16 per convenzione di brand, come nei pacchetti del 14, 15 e 16/09 |
| 6 | Marchi di terzi | OK — KOENIC e PHILIPS rimossi dalla copia di lavoro; nessuno schermo acceso, nessuna insegna |

Difetti dei giorni scorsi, ricontrollati uno per uno: **nessun filo oro attraversa una parola**
(la funzione è stata tolta dalla libreria); **nessuna card tagliata in basso**; **nessuna grafica
smunta** (lock di brand + veli caricati sulla fascia che porta il testo).

## Grafiche editabili

**Canvas Claude Design** — `grafiche/canvas.json` + 27 artboard `.dc.html`, tutte modificabili
(testo in linea, posizione, corpo, colore, aggiunta di elementi). Non sono immagini piatte: i PNG in
`png/` sono l'export in più, per il caricamento e per il controllo qualità.

```
campagne/giornaliero/2026-09-17/
├── direzione-artistica.md        questo file
├── grafiche/
│   ├── canvas.json               la tavola: 27 artboard con posizione e formato
│   ├── base.py                   libreria fumè + il componente "scalino"
│   ├── build.py                  le artboard e reel/scene.json, da una sorgente sola
│   ├── prepara-foto.py           rimozione marchi di terzi + ritagli sul formato
│   ├── verifica.py               controllo misurato (trabocchi, sovrapposizioni, safe area, altezze)
│   ├── C1–C5, F1–F3, S1–S2 .dc.html
│   ├── R01–R17.dc.html           una per scena del reel
│   └── foto-*.jpg, fonte-cucina-pulita.png
├── png/                          27 export 1:1
└── reel/
    ├── scene.json                il reel come dati — 24,6 s, 66 elementi
    └── reel.html                 pagina animata, generata da scene.json
```

Rigenerazione: `python3 grafiche/prepara-foto.py` → `python3 grafiche/build.py` →
`python3 grafiche/verifica.py` → `python3 .claude/skills/giornata/render.py campagne/giornaliero/2026-09-17`.
Per il reel: `python3 .claude/skills/giornata/scene_to_html.py <cartella>/reel/scene.json <cartella>/reel/reel.html`.
