# Revisione marketing & design — Giornaliero 14/09/2026 · "La casella dimenticata"

**Materiale visto:** `brief-mercato.md`, `copy.md`, `direzione-artistica.md`, `checklist-compliance.md`, i 19 PNG (guardati a dimensione telefono, uno per uno), `grafiche/build.py`, `reel/battute.json` + `reel/scene.txt`, `PUBBLICAZIONE.md`.
**Riferimenti di giudizio:** `riferimenti/riferimento-1.md` (tono e forma della CTA), `.claude/reference/lessico-brand.md`, tabella "Pattern di layout già usati" di `.claude/reference/design-system.md`, `campagne/giornaliero/PIANO.md`.

## Giudizio complessivo

**PRONTA CON RITOCCHI** — l'argomento è il migliore che il brand abbia prodotto finora (angolo nuovo, meccanismo concreto, frase onesta che nessun concorrente dice), ma il pezzo che deve portare il reach — il reel — è oggi una sequenza di immagini ferme, e le CTA chiedono un DM senza offrire niente in cambio. Sono due ritocchi, non una rilavorazione: il resto è materiale da tenere come metro dei giorni successivi.

### Correzioni di compliance: verificate, tutte e cinque applicate

| Rilievo bloccante | Stato |
|---|---|
| "Nessun costo fisso" fuori dalla caption `F3` | ✅ `copy.md` riga 562 e `PUBBLICAZIONE.md` riga 58 portano solo "15% sul fatturato generato" |
| Stessa riga fuori dalla tabella LAYOUT di `F3` | ✅ `copy.md` riga 577: "15% sul fatturato." |
| "quattro mesi fa" tolto | ✅ `copy.md` riga 521 e caption pronta: resta solo la data |
| "consecutive" sulle 10 notti | ✅ `copy.md` riga 540 e `PUBBLICAZIONE.md` riga 48 |
| Apostrofo curvo di `F2` | ✅ nessun `’` residuo in `build.py` (grep pulito), `F2.png` riesportato |
| Arco di avanzamento incoerente | ✅ rimosso dall'artboard `F2` — ma la specifica non è stata aggiornata (vedi intervento 7) |

Nessun claim bloccato viene riaperto in questa revisione.

## Punteggio per dimensione

| Dimensione | Giudizio | Nota chiave |
|---|---|---|
| Impaginazione/layout | ⚠️ | Carosello e storie tengono benissimo sul telefono; la chiusura del reel (`R1b9`) è l'unico artboard con un difetto visibile, e `C1`/`C2` hanno vuoti centrali che le fanno leggere non finite |
| Contenuti/struttura | 👍 | Anti-sovrapposizione perfetta: tempo / catena / data / due estremi. Manca solo il pezzo "e se passo a voi, devo rifare tutto?" — è il contenuto naturale di domani, non un buco di oggi |
| Grafiche/foto | ⚠️ | Palette, oro e tipografia impeccabili. Il problema sono le immagini: il reel è fermo, e la stessa scena stock (ingresso) regge 5 dei 19 pezzi |
| Testi | 👍 | Gancio, frase onesta e riga di perimetro sono il meglio prodotto finora. Unico punto debole: le CTA |
| Efficacia commerciale | ⚠️ | Il proprietario capisce il problema e crede al meccanismo, ma non sa cosa succede se scrive. Cinque CTA, zero promesse |

## Interventi prioritari (in ordine di impatto commerciale)

### 1. Il reel è una sequenza di immagini ferme — rimontarlo prima di pubblicare (18:00)

`reel/scene.txt` è una concat di 9 PNG con durate fisse e stacchi netti: nessun movimento, nessuna dissolvenza (la "dissolvenza 0,3 s" dichiarata a `copy.md` riga 65 non esiste nel montato), nessuna traccia audio tra gli input. Effetti pratici:
- **battute 1 e 2 (0,0 → 4,0 s): la stessa identica foto** (`r-balcone.jpg` per entrambe, `build.py` righe 204-205). I primi 4 secondi del reel, cioè quelli che decidono la ritenzione, sono un fermo immagine in cui cambia solo una riga di testo.
- **battute 5-7 (6,8 → 11,0 s)** sono tre fotogrammi quasi neri della stessa scena: su un telefono alla luce del giorno `R1b7` ("E non suona.") legge come schermo spento.
- **niente audio** = niente audio di tendenza, e Instagram mostra il reel muto.

Da fare, in ordine di costo crescente: (a) usare davvero le clip di `brand-assets/video/clean/` sotto gli overlay — sono 1080×1920 30 fps e la ricetta è documentata in `design-system.md` riga 118; (b) in subordine, push-in lento per battuta + dissolvenze da 0,3 s e schiarire di uno stop le battute 5-7; (c) in ogni caso, aggiungere un letto audio (anche solo in app al caricamento) e annotarlo in `PUBBLICAZIONE.md`. È l'intervento che vale più di tutti gli altri messi insieme: il reel è l'unico pezzo del pacchetto che deve portare pubblico nuovo.

### 2. Cinque CTA, nessuna dice cosa succede dopo

`R1b9` "Ne parliamo in DM" · `C5` "Scrivi CATENA in DM" · `F3` "Commenta CATENA o scrivici in privato" · `S1`/`S2` "Scrivi in DM". Nessuna abbassa il rischio del primo passo. Il riferimento del brand lo fa (`riferimento-1.md`: *"Scrivi CALCOLO in DM per una simulazione gratuita"*): lì il proprietario sa cosa riceve. Qui, dopo tre minuti di contenuto che gli ha appena ricordato che è esposto, gli si chiede di alzare la mano a vuoto.

Aggiungere una riga di promessa sulle due CTA che convertono (`C5` e `F3`) — senza claim nuovi, è un'offerta di conversazione:

> **Scrivi CATENA in DM: ti diciamo quali di questi sei anelli, sulla tua casa, oggi stai eseguendo tu.**

Su `C5` la riga sta sotto la pill (spazio libero c'è: la pill chiude a y 1344 nel layout dichiarato e l'artboard ha margine). Su `F3` può sostituire la riga oro o entrare in caption come ultima frase al posto di "commenta CATENA o scrivici in privato" secco. Sul reel basta la caption.

### 3. `F3` aperta da sola promette delega totale

Nel collage Facebook la terza immagine si apre singolarmente, ed è la superficie più assertiva del pacchetto: "Sei anelli. Tutti eseguiti." + "Il proprietario riceve solo il bonifico netto a fine mese." + pill. La frase che rende credibile tutto il resto — *La responsabilità resta tua. Il lavoro no.* — non c'è: sta su `C5` (altro canale) e in caption (che in un gruppo si legge a metà). Davanti a proprietari competenti e diffidenti, `F3` da sola è esattamente il post aziendale che fiutano.

Sostituire il titolo **"Sei anelli. Tutti eseguiti."** con **"La responsabilità resta tua. Il lavoro no."** e spostare "Sei anelli. Tutti eseguiti." nella marca temporale in alto (dove oggi c'è `FINE MESE`, che è l'informazione meno utile dell'artboard). Gerarchia e altezze restano identiche: è un cambio di testo, non di layout. Compliance lo aveva già suggerito come opzione; commercialmente non è un'opzione, è ciò che differenzia il post.

### 4. Il carosello promette sei anelli e poi ne conta quattro

`C1` dice "Sei anelli. Ognuno con la sua scadenza.", poi le marche temporali contano `01 · 02 · 03 · 04`. Chi salva un contenuto lo conta: la promessa numerica non torna e il carosello perde credibilità proprio nel pezzo costruito per essere salvato. Due righe da cambiare, a scelta:
- sottotitolo `C1` → **"Sei anelli. Tre momenti."** (e la formula regge anche il rilievo di compliance su "scadenza" come termine troppo preciso per due dei sei anelli), oppure
- togliere i numeri dalle marche (`PRIMA CHE L'ANNUNCIO SIA ONLINE`, `QUANDO L'OSPITE ARRIVA`, `DURANTE E DOPO IL SOGGIORNO`, `CHI ESEGUE LA CATENA`).

La prima è migliore: mantiene la scansione numerica, che è il ritmo della catena.

### 5. `C2`-`C4` parlano al fai-da-te come se non sapesse le regole

Le slide interne dicono *cosa* si deve fare ("Il CIN deve essere nell'annuncio", "L'imposta di soggiorno la incassi tu. E la versi tu."). Il target primario queste cose le sa già: è il motivo per cui le fa da solo. Il brief lo dice esplicitamente ("non è uno sprovveduto che non sa le regole, è uno che ha un altro lavoro"), ma il *quando* — l'unica cosa che sposta il suo giudizio — vive solo nella caption e nel sottotitolo di `C1`, mai sulle slide.

Aggiungere l'orario su una sola slide interna, `C3`, in coda alla nota sotto il chip `+24:00`: **"Anche se l'ospite arriva alle 23:40."** Una riga: sposta la slide da lezione a riconoscimento, e cuce il carosello al reel e alla storia 2 senza che si citino a vicenda.

### 6. `R1b9` — la chiusura del reel è l'artboard più debole dei 19

Tre difetti nello stesso fotogramma, ed è quello su cui il reel si ferma 2,4 s:
- la riga "Gestione completa." (y 960, `build.py` riga 241) **copre la parola del logo bronzo**, che occupa 420-960 px (riga 227-228): il lockup del marchio si legge mozzato;
- il logo è un JPG mascherato in radiale su fondo scuro: a dimensione telefono si vede l'alone ellittico, legge come adesivo incollato;
- la CTA "NE PARLIAMO IN DM" è Manrope 31 px in sabbia (riga 245-249), senza pill: è **la CTA più piccola e meno contrastata di tutto il pacchetto**, proprio dove serve di più. `C5`, `S1`, `S2` e `F3` usano la pill oro.

Alzare il logo a top ~330, portare la riga oro e la CTA in pill oro come negli altri quattro artboard, e scendere di un gradino la riga "Gestione completa. / 15% sul fatturato." se serve spazio.

### 7. `F1` — la foto combatte con il testo, ed è la stessa scena di altri 4 pezzi

`d-ingresso-giorno.jpg` è l'unica immagine chiara e "nordica" del pacchetto (pareti bianche, infisso nero, lampada in vimini): non dice Roma, non dice standard alberghiero, e la fascia centrale in cui cade il gancio resta a medio tono, quindi il testo bianco ci sta appoggiato invece che appoggiato su un fondo. La stessa scena, ri-gradata di notte, regge anche `R1b5`, `R1b6`, `R1b7` e `S2`: **5 pezzi su 19 sono la stessa stanza**. Oggi passa; se diventa l'abitudine, in una settimana il feed è una casa sola.

Per oggi basta rinforzare il velo nella fascia y 700-1400 di `F1` (stesso trattamento già applicato a `C1`). Per i giorni successivi: `F1` è la prima immagine di Facebook, merita uno scatto reale di `brand-assets/immobili/` o `ambientazione/`.

### 8. Ritmo verticale di `C1` e `C2` (ritocco minore, ma è il giorno 1 di uno standard)

- `C1`: i primi 600 px — il 44% della slide — portano solo marchio e `T ZERO`, e il velo è così forte che la foto del salotto non si legge. Nel feed la prima cosa che si vede è un rettangolo scuro. Alzare il blocco gancio a y ~480, o alleggerire il velo di 6-8 punti nella fascia alta così la foto esiste.
- `C2`: tra il corpo (chiude a y 800) e la nota (y 1080) ci sono 280 px di nulla, mentre `C3` e `C4` sono piene. Portare la nota a y ~880: la slide smette di sembrare incompiuta accanto alle altre.

### 9. La specifica e gli artboard hanno iniziato a divergere

Non impatta la pubblicazione di oggi, impatta il giorno 30. `build.py` è la fonte di verità, ma chi rigenerasse dal Master Template otterrebbe altro:
- `copy.md` riga 486 e riga 779 dichiarano ancora l'arco Facebook `1/3 → 3/3`, che dopo la correzione non esiste su nessuna delle tre immagini;
- `C5`: la tabella LAYOUT dà frase onesta 700-850 / claim 890-1010 / offerta 1050-1130 / CTA 1170-1286; l'artboard costruisce a 775 / 950 / 1090 / 1228;
- `R1b8` e `S1`: la specifica dichiara 2 righe, gli artboard ne stampano 3 (già rilevato da compliance).

Allineare oggi le tre voci, e da domani far generare la tabella LAYOUT dallo stesso dizionario che costruisce l'artboard, così la deriva non può ripetersi.

## Rischio di tono: nessuna deriva allarmistica, un solo punto di paternalismo

Sul contenuto più pericoloso del brand — le sanzioni — il registro tiene. Nessun importo, nessun rosso, nessun punto esclamativo, nessun "stanno arrivando i controlli"; *"Non è una stretta. È un cambio di meccanismo."* su `F1` è la riga che disinnesca l'accusa di terrorismo commerciale, e la riga di perimetro sul commercialista stampata **in grafica** su `F3` è ciò che un proprietario diffidente cerca prima di credere al resto. Il proprietario fai-da-te non si sente preso per sprovveduto **nel reel, nelle storie e in `C5`**; si sente un po' spiegato in `C2`-`C4` — è esattamente il motivo dell'intervento 5, e si chiude con una riga.

Un punto da tenere d'occhio nei commenti, non da cambiare: *"Il tuo commercialista lavora una volta l'anno"* (caption `F3`) è la frase più attaccabile del pacchetto in un gruppo di proprietari. La risposta pronta in `PUBBLICAZIONE.md` c'è e regge; non toccare la frase, è vera e distingue.

## Tenuta come primo giorno di un sistema quotidiano

**L'impianto è ripetibile, la firma no — ed è giusto così, purché sia esplicito.** Il telaio che va tenuto ogni giorno è: `build.py` → 19 artboard → export PNG → sei controlli a dimensione telefono → `PUBBLICAZIONE.md` con orari, file e caption incollabili. Funziona: oggi ha prodotto 19 pezzi coerenti e un referto di compliance verificabile riga per riga.

Quello che **non** va ripetuto domani è la *firma grafica*: "marca temporale + arco che si chiude" nasce dall'argomento di oggi (il tempo). Se resta anche domani diventa la cornice del brand e la regola fissa 5 ("varia il design") salta entro mercoledì. Domani il pilastro è il metodo: serve un dispositivo suo, e la marca temporale va archiviata nella tabella dei pattern usati di `design-system.md` insieme a questa giornata.

Due cose che oggi passano e tra una settimana stancano:
1. **La pill oro a piena larghezza compare 4 volte in 19 pezzi** (`C5`, `F3`, `S1`, `S2`). Su un solo giorno è coerenza; su sette giorni è un tic. Regola proposta: una sola pill piena per pacchetto (la CTA del carosello), le altre in outline o in riga oro.
2. **Le due storie hanno la stessa struttura** (marca in alto a destra → gancio 70 px → corpo → risposta oro → pill). Oggi si differenziano per il chip `+24:00` e per il colore del gancio; domani serve che almeno una delle due inverta l'ordine (risposta in apertura, problema sotto) o cambi taglio del testo, altrimenti le storie diventano un modulo.

Infine, il pezzo che manca al funnel non è di oggi ma è il primo che il target chiederà dopo aver visto tutto: **"e se passo a voi, devo rifare l'annuncio? il CIN resta lo stesso? quanto ci vuole?"**. `S1` lo sfiora ("il codice ci sta dentro dal primo giorno") e basta. È il contenuto naturale di martedì (pilastro metodo): il passaggio senza attrito.

## Cosa funziona già bene (da non toccare, e da tenere come standard)

- **La frase onesta come meccanismo, non come slogan.** *"La responsabilità resta tua. Il lavoro no."* + *"Non smetti di essere il titolare. Smetti di essere l'esecutore."* + la riga di perimetro sul commercialista: è la cosa che nessun concorrente dice e l'unico motivo per cui un diffidente legge fino in fondo. Deve sopravvivere a ogni revisione futura, e va usata **in grafica**, non solo in caption.
- **La regola di anti-sovrapposizione** (reel = il tempo · carosello = la catena · Facebook = la data · storie = i due estremi). È l'architettura che rende un pacchetto quotidiano un sistema invece di cinque post sullo stesso tema. Da riusare così com'è ogni giorno.
- **`C4` e `C5` sono i due benchmark di impaginazione.** `C4`: la superficie chiara come respiro tra due sequenze scure, con la riga chiave in oro scuro che è l'unica cosa che si legge da lontano. `C5`: elenco → frase onesta → claim oro → offerta → pill, gerarchia perfetta in cinque livelli senza una card.
- **La disciplina dell'oro** (solo marca temporale e frase che chiude l'obiezione). È il motivo per cui il pacchetto sembra costoso invece che decorato.
- **`F2` come "documento consultabile"**: fondo sabbia, tre marche temporali, zero retorica. È il pezzo che in un gruppo viene screenshottato. Tenere il formato per tutti i contenuti di puro servizio.
- **La compliance progettata a monte** (niente importi, niente aliquote, niente TULPS, ordine identificazione→accesso stampato in grafica): è ciò che ha permesso di fare un contenuto sulle sanzioni senza allarmismo. Il metodo, non solo il risultato, va replicato.
- **`PUBBLICAZIONE.md` con le risposte pronte ai commenti.** Prodotto dopo compliance, ed è materiale operativo vero: va reso obbligatorio ogni giorno, con la sezione "se ti rispondono nei commenti" sempre presente.

## Suggerimenti opzionali (nice-to-have)

- **`R1b2` "Per una casella."**: senza verbo regge solo per chi ha letto la battuta 1. Con un reel che parte in mute e in scroll, **"Per una casella dimenticata."** costa 1,4 s uguali e chiude la frase (già proposto da compliance, lo confermo dal lato ritenzione).
- **`S2` gancio**: "L'ospite entra alle 23:40" seguito da "Lo identifichi. Poi entra." crea una micro-contraddizione di sequenza. **"Alle 23:40 l'ospite è alla porta."** la elimina e rende il gancio più teso.
- **`C3` titolo**: "Prima lo riconosci" → **"Prima lo identifichi"**, che è il verbo usato in `F2`, `S2` e nel corpo della stessa slide. Uniformità di lessico su un termine tecnico.
- **Storie — `PUBBLICAZIONE.md`**: la fascia sotto y 1600 è volutamente vuota su `S1` e `S2`. È il posto giusto per lo sticker "Fai una domanda"/link DM: dirlo esplicitamente nel file, altrimenti la pill oro resta un bottone che non si può premere.
- **Caption `F3`**: il blocco PRIMA / ALL'ARRIVO / DURANTE E DOPO ripete parola per parola l'immagine `F2` che sta accanto. Ridurlo a due righe e lasciare il lavoro all'immagine riporta la caption dentro la voce del brand invece che in quella dei software di settore.
- **`F1`** non ha CTA né rimando: una riga piccola in coda ("La catena completa, nella seconda immagine.") aumenta la probabilità che si aprano anche `F2` e `F3` nel collage.

---

**Sintesi operativa:** interventi 1, 2 e 3 prima della pubblicazione (il reel prima delle 18:00, `F3` prima delle 15:00). Interventi 4, 5, 6 nello stesso giro di `build.py`, sono cinque righe in tutto. Interventi 7, 8, 9 prima della giornata di domani, perché è lì che diventano debito.
