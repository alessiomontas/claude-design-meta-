# Reel virali — manuale operativo di montaggio (senza volto, senza voce)

Riferimento stabile del progetto. Si legge **prima** di costruire qualsiasi reel Hadrianus, insieme a
`modello-reel-8-secondi.md` (che resta il telaio della serie breve) e a `design-system.md` (palette e font).
Qui non ci sono principi generici: ci sono **meccaniche di montaggio al secondo**, implementabili in HTML/CSS
e catturabili a 30 fps.

**Vincolo di produzione dato**: pagina HTML animata in CSS → cattura fotogramma per fotogramma a 30 fps →
MP4 1080×1920. Niente riprese di persone, niente voce, niente musica in fase di export (si aggiunge dopo su
Instagram), niente 3D reale, niente generazione immagini IA. Tutto ciò che segue è scritto dentro questo vincolo:
se una tecnica non è realizzabile così, non è in questo manuale.

**Come leggere le fonti.** Dove c'è un numero misurato è indicato lo studio. Dove è opinione di creator o prassi
di settore è scritto `[opinione di settore]`. Non aggiungere numeri non presenti qui: valgono le regole non
negoziabili di `CLAUDE.md`.

---

## 0. I tre numeri che decidono il montaggio

1. **Watch time / completion rate è il segnale n.1 per i Reels**, insieme a **sends per reach** (quante volte il
   video viene inoltrato in DM) e likes per reach. I sends sono il segnale più forte per arrivare a chi **non**
   ti segue; vengono riportati come pesati diverse volte più dei like. (Sintesi di più guide che citano
   dichiarazioni di Adam Mosseri, 2026 — Buffer, Later, Hootsuite, Dataslayer. Il peso esatto "3-5×" circola nelle
   guide ma **non è un dato ufficiale verificabile**: trattalo come `[opinione di settore]`.)
2. **Durata**: un test creator di aprile 2026 su 50 reel (CreatorHouse) riporta completion medio **94% a 7 s,
   78% a 15 s, 56% a 30 s**, ma il gruppo da 15 s ha vinto sulla *reach* perché il 7 s produce troppo poco
   watch-time per impression. Lettura operativa: **8-15 s è la fascia da usare di default**, 30-45 s solo quando
   c'è davvero qualcosa da spiegare. (È un test di un singolo creator, non uno studio indipendente:
   `[dato di parte, indicativo]`.)
3. **Ritmo**: la prassi convergente è **un cambiamento visivo ogni 1,5-3 s**, e **oltre i 4 s di inquadratura
   ferma si perde il pubblico**. Per i formati senza volto la forchetta si allarga a 3-5 s *solo se* dentro
   quell'intervallo succede comunque qualcosa (un testo che atterra, uno zoom che si risolve). `[prassi di settore]`

Conseguenza per Hadrianus: **l'85% circa dei video social viene guardato senza audio** (cifra citata ovunque nel
settore, `[dato di settore ripetuto, origine non tracciabile]`). Nel nostro caso l'audio non esiste proprio in
export: **la tipografia è il parlato**. Ogni decisione di montaggio va giudicata come se fosse doppiaggio.

---

## 0-bis. Aggiornamento dati 21/09/2026 — cosa cambia e cosa no

Fonte: le analisi OpusClip 2026 (campione dichiarato: **34.635 clip** per i tipi di gancio,
**13,5 M clip** per l'anatomia complessiva, **10.598** per il registro; metrica = visualizzazioni
TikTok a 7 giorni, clip promosse a pagamento escluse). **Non ho potuto leggere le pagine intere**:
l'egress di rete blocca `opus.pro` (`CONNECT tunnel failed, 403`), quindi quanto segue viene dai
riassunti dei motori di ricerca. Trattali come `[web]`, non come misure verificate da noi.

**1. Il gancio più forte è il risultato, non il problema.** Il tipo di gancio con la resa più alta
è il **product/outcome showcase** — mostrare il risultato finito, la trasformazione o l'esito nei
**primi 2 secondi**: media **6.037 visualizzazioni** per clip, circa **2×** il tipo peggiore `[web]`.
**Questo contraddice il nostro impianto.** Quasi tutti i reel Hadrianus aprono su un *problema* o
su una *negazione*. Non va buttato — la negazione è il nostro telaio riconoscibile — ma va affiancato:
vedi la struttura D in `modelli-e-ganci.md` §6, che apre sul risultato e poi torna indietro.

**2. Il registro che va di più è già il nostro.** L'impronta tonale più comune nel campione virale
è **«serious and professional + thought-provoking»**, presente nel **25,7%** `[web]`. È esattamente
il registro Hadrianus. **Nessuna modifica**: è una conferma, e va usata per resistere alla tentazione
di fare reel "simpatici" con musica trend e testi ammiccanti.

**3. Le didascalie impresse e animate sono fra i segnali più forti** `[web]`. Noi non abbiamo voce,
quindi il testo *è* già il contenuto: la conferma è che la tipografia cinetica **dentro** un formato
è un moltiplicatore, e che la regola 1.8 (mai kinetic type da solo) resta giusta. Nessuna modifica.

**4. Sulla durata c'è una tensione aperta, non la risolvo d'ufficio.** Quelle analisi danno
**30-45 s** come fascia ottimale e **41 s** come mediana della fascia virale `[web]`. Il §0 qui
sopra e la nostra serie da 8-15 s dicono il contrario. Tre ragioni per non allungare tutto domani:
è **TikTok**, non Reels; la metrica è **visualizzazioni a 7 giorni**, non il completion che noi
ottimizziamo; e il nostro pubblico è B2B locale, non intrattenimento. **Decisione: un test, non una
riforma.** Un contenuto al mese sopra i 35 s, confrontato sulla stessa metrica con i corti.
Finché il test non dice altro, la fascia resta 8-30 s.

**5. Hashtag: 8-12, mischiando di nicchia e generici** `[web]`. Oggi non abbiamo una regola scritta;
questa diventa la regola per le caption.

**6. Orari: non applicabili.** Le analisi indicano 7:00 e 16:00 ET nei giorni feriali: è un dato
statunitense su un altro fuso e un altro pubblico. Per Ostia e Roma valgono gli orari in
`campagne/giornaliero/PIANO.md`, non questi.

---

## 1. I formati che funzionano senza volto e senza voce

Ordinati per efficacia *per un property manager che vende gestione a proprietari di casa*, non per popolarità
assoluta. Per ognuno: perché funziona, obiettivo primario, struttura al secondo, come si rende in CSS.

### 1.1 Lista negata / "non è quello che pensi" — il telaio già nostro
**Obiettivo**: salvataggi e condivisioni (il proprietario inoltra al socio/coniuge).
**Perché funziona**: apre negando l'aspettativa ("i proprietari non ci chiedono X"), quindi il cervello deve
restare per sapere cosa è vero. Ogni riga successiva è un'occasione di riconoscersi. È il formato con il
rapporto più alto tra semplicità di montaggio e tenuta.
**Struttura**: è `modello-reel-8-secondi.md`, non riscriverla qui. 2 s gancio → 1 s svolta → 3×1 s desideri → 2 s firma.
**CSS**: una sola scena, testi che si sostituiscono a taglio netto. Il più economico da produrre.
**Limite**: posiziona, non dimostra. Se serve prova, usa 1.3 o 1.5.

### 1.2 Prima / dopo a tendina (before-after wipe)
**Obiettivo**: condivisioni. È il formato faceless con l'engagement più alto riportato dalle guide `[opinione di settore]`.
**Perché funziona**: trasformazione visibile in meno di 2 secondi, zero testo necessario per capirla. Chi guarda
completa il video per vedere "quanto" cambia, e lo rivede per confrontare.
**Errore che lo rende povero**: **una sola tendina** su una sola coppia di foto. Il formato regge se le coppie
sono **tre**, incalzanti, con la tendina che ogni volta arriva **più veloce** dell'altra.
**Struttura 12 s**:
- 0,0-1,2 — foto "prima" già in movimento (zoom lento in corso, non partito ora), etichetta piccola in alto a sinistra.
- 1,2-1,5 — tendina 1 (300 ms, `clip-path: inset()` con `cubic-bezier(.16,1,.3,1)`), atterra il dato: `+X% in più`.
- 1,5-3,0 — la scena "dopo" continua lo zoom: **non si ferma mai**.
- 3,0-3,3 — stacco netto su coppia 2. Tendina più corta (240 ms) a 4,2 s.
- 6,0-6,2 — coppia 3, tendina 200 ms a 7,0 s.
- 8,0-10,0 — le tre "dopo" si affiancano in griglia 3 colonne (scala da 1 a 0,33 in 400 ms).
- 10,0-12,0 — CTA oro a tutta larghezza.
**Adattamento Hadrianus**: annuncio scritto male → annuncio nostro; casa non preparata → casa in standard
alberghiero; calendario bucato → calendario pieno. Il "prima" **non deve mai essere una casa reale di un cliente
riconoscibile**: usa mock disegnati in HTML (vedi 1.4).

### 1.3 Documento / checklist che si compila da sola
**Obiettivo**: **salvataggi** — è il formato che si salva, perché è utile fuori dal momento.
**Perché funziona**: promette un elenco finito ("le 7 cose che controlliamo prima di ogni check-in") e il
contatore visibile crea la compulsione a arrivare alla fine. Il formato listicle è quello con il tasso di
visione completa più alto tra i faceless `[opinione di settore]`.
**Struttura 15 s**:
- 0,0-1,5 — la riga del titolo entra già "battuta": `7 CONTROLLI` grande, `PRIMA DI OGNI CHECK-IN` piccola sotto.
  In alto appare subito la barra di avanzamento oro a 0%.
- 1,5-13,0 — **7 righe × ~1,6 s**. Ogni riga: entra da sinistra in 180 ms con un leggero overshoot, il segno di
  spunta oro si disegna (`stroke-dashoffset`) in 220 ms, la barra avanza di 1/7.
  Le righe già passate **restano a schermo** scalate a 0,86 e opacità 0,45: la lista si accumula, non si sostituisce.
- 13,0-15,0 — la lista intera si comprime in alto, sotto entra la CTA.
**Perché la lista deve accumularsi**: se ogni riga sostituisce la precedente il video sembra una presentazione.
Se si accumula, chi guarda vede "quanto manca" e vede il lavoro come volume. È la differenza tra povero e denso.

### 1.4 Finta interfaccia (notifica, calendario, chat, dashboard) disegnata in HTML
**Obiettivo**: contatti in DM. È il formato più forte per far scattare "voglio quel numero anche io".
**Perché funziona**: un'interfaccia familiare è letta in mezzo secondo senza istruzioni, e sembra *prova* anche
quando è chiaramente un mock. Le notifiche che si accumulano hanno un ritmo naturale.
**Struttura 10 s**:
- 0,0-0,6 — schermo scuro, **una notifica entra** dal bordo alto (traslazione + scala 0,94→1 in 220 ms).
- 0,6-4,0 — altre 5 notifiche entrano a cadenza accelerata (600, 500, 400, 320, 260 ms): le precedenti scendono
  e sfumano. Il ritmo che accelera è il cuore del formato.
- 4,0-4,2 — stacco su un **calendario mensile**: le caselle si riempiono d'oro a ondata diagonale (`animation-delay`
  calcolato per riga+colonna), 900 ms in tutto.
- 4,2-7,0 — sopra il calendario sale il **contatore** dell'occupazione o dell'incasso.
- 7,0-10,0 — il calendario si sfoca (`filter: blur(10px)` in 300 ms), entra la CTA a fuoco.
**Regola di onestà, non negoziabile**: ogni numero mostrato in una finta interfaccia è un claim. O è verificato,
o è marcato `[DATO DA VERIFICARE]` e **non si pubblica**. In alternativa mostra il *meccanismo* senza cifre
(caselle che si riempiono, notifiche senza importi).

### 1.5 Confronto a schermo diviso (split screen permanente)
**Obiettivo**: condivisioni (è il formato "hai ragione tu" da inoltrare).
**Perché funziona**: il confronto è leggibile da fermo, in qualsiasi fotogramma. Un utente che apre il video a
metà capisce lo stesso — e questo alza il completion.
**Struttura 12 s**:
- 0,0-0,8 — le due metà entrano **una contro l'altra** (sinistra da sinistra, destra da destra, 400 ms, stop
  netto con rimbalzo di 8 px). Al centro resta un filo verticale oro di 3 px.
- 0,8-9,6 — **6 righe alternate**, 1,4 s l'una: prima la riga a sinistra (grigia, con ✕), 300 ms dopo la riga a
  destra (chiara, con ✓). Lo sfasamento di 300 ms è la cosa che rende il formato vivo; senza, sembra una tabella.
- 9,6-10,4 — la metà sinistra collassa (larghezza 50%→0 in 500 ms), la destra occupa tutto.
- 10,4-12,0 — CTA.
**Adattamento**: "da solo" vs "con Hadrianus" · "chi prende il 25%" vs "15% allineato" · "fai da te" vs
"standard alberghiero". Mai nomi di concorrenti.

### 1.6 Contatore / numero che sale su una sola immagine
**Obiettivo**: attenzione e completion su formati cortissimi (6-8 s), buon riempitivo di serie.
**Perché funziona**: un numero in movimento è l'unico elemento che non si può guardare "a metà": si aspetta che
si fermi. Zero comprensione richiesta.
**Struttura 7 s**: 0-0,4 il numero parte già a metà corsa (non da zero: partire da zero spreca un secondo) →
0,4-3,0 sale con easing che decelera → 3,0-3,3 **scatto in scala 1,12 e ritorno** quando si ferma → 3,3-5,0
entra sotto la riga che spiega cosa era il numero → 5,0-7,0 CTA.
**Uso Hadrianus**: giorni di calendario coperti, numero di controlli, ore di risposta. Mai un incasso non verificato.

### 1.7 Micro-tour di una stanza a parallasse
**Obiettivo**: desiderabilità, non conversione. Serve a variare la serie, non a portare contatti.
**Perché funziona**: il movimento continuo su foto ferme legge come "video vero" anche senza riprese.
**Meccanica**: la foto viene tagliata in 2-3 livelli (fondo, oggetto medio, oggetto in primo piano) e ogni livello
trasla a velocità diversa (fondo 1×, medio 1,6×, primo piano 2,4×) mentre l'insieme fa uno zoom lentissimo (scala
1,00→1,06 in 3 s). **La differenza tra un parallasse ricco e uno povero è il terzo livello**: con due livelli
sembra uno scorrimento, con tre sembra profondità.
**Regola**: durata massima **3 s per stanza**, poi stacco netto. Un parallasse che dura 6 s è la definizione di
reel povero.

### 1.8 Testo su fondo pieno a ritmo (kinetic type puro)
**Obiettivo**: nessuno, da solo. **Da usare solo come ponte di 1-2 s dentro un altro formato.**
Funziona nei reel motivazionali, non nei reel di vendita B2B: senza musica e senza volto è il formato che
degrada più in fretta verso il "povero". Se un reel Hadrianus è *interamente* testo su fondo, è sbagliato.

---

## 2. La meccanica dei primi 2 secondi

Non "cattura l'attenzione". Ecco cosa deve succedere **materialmente** sui primi 60 fotogrammi.

**Regola madre: il primo fotogramma non è mai uno stato di riposo.** Il video deve aprirsi *dentro* un movimento
già iniziato. In pratica: quando renderizzi, calcola le animazioni come se fossero partite 400 ms **prima** del
fotogramma 0 (offset negativo su `animation-delay`), così il frame 0 mostra uno zoom già al 3%, una notifica già
a metà corsa, una tendina già scoperta per un decimo. Chi scorre vede movimento, non una copertina.

**I quattro interrupt sovrapposti nei primi 2 s** (devono essercene almeno **tre**):
1. **Movimento già in corso** (zoom/pan/parallasse), frame 0-60.
2. **Testo che atterra con impatto**, non che sfuma: entra in 140-180 ms con overshoot e si **ferma di colpo**.
   Una dissolvenza di 600 ms sul titolo è il difetto n.1 dei reel poveri.
3. **Rottura cromatica** entro il primo mezzo secondo: su base fumè `#3F3A33`, un blocco oro `#C8A24B` che
   compare o una parola che passa da chiaro a oro. L'occhio periferico registra il contrasto prima di leggere.
4. **Cambio di stato a ~1,0-1,3 s**: un secondo micro-evento prima che finisca il gancio (una parola che si
   sostituisce, un badge che scatta, la barra che parte). Se nei primi 2 s succede **una cosa sola**, il video
   è già perso.

**Il testo del gancio**: massimo **5-7 parole per schermata** — è la soglia di leggibilità citata dalle guide
italiane ed estere `[prassi di settore]`. Su 1080×1920 la riga grande sta a ~72 px (regola già fissata in
`modello-reel-8-secondi.md`, pubblico più anziano della media).

**Ganci che funzionano per un property manager** (adattati dalle formule "specifico, contrario o numerico nei
primi 3 secondi" riportate per il real estate 2026):
- negazione: `Nessun proprietario ci chiede quanto guadagna.`
- costo nascosto: `Ogni notte vuota costa due volte.`
- numerico + finito: `7 controlli prima di ogni check-in.`
- contrario: `Il prezzo più alto non riempie il calendario.`
Evita il gancio-domanda generico ("Vuoi guadagnare di più con la tua casa?"): è la forma più vista e la più saltata.

---

## 3. Ritmo

| Elemento | Valore operativo | Note |
|---|---|---|
| Cambiamento visivo | ogni **1,5-3 s** | mai superare 4 s senza che succeda nulla |
| Battuta di testo breve (elenco) | **1,0-1,4 s** | sotto 0,8 s non si legge in italiano |
| Battuta di testo lunga (2 righe) | **1,8-2,2 s** | la chiusura può arrivare a 2,5 s |
| Entrata di un testo | **140-200 ms** | oltre i 300 ms sembra lento |
| Uscita di un testo | **0 ms (taglio) o 120 ms** | le uscite lente sono la morte del ritmo |
| Tendina / wipe | **200-320 ms** | accorciala a ogni ripetizione |
| Stacco di scena | **0 ms** | nessuna dissolvenza incrociata, mai |
| Movimento di camera continuo | **2,5-3,5 s per scena** | oltre diventa sonnolento |

**Accelerazione**: la curva giusta non è costante. Reel da 15 s: prime due battute più lunghe (gancio che si
deve leggere), poi **il centro accelera** (battute che si accorciano di 100-150 ms l'una dall'altra), poi
**l'ultima battuta raddoppia**. È l'unico punto in cui si rallenta: la chiusura. Il rallentamento finale serve
perché la CTA va letta e perché un finale secco senza respiro non fa scrivere in DM.

**Micro-pause**: dopo un dato importante (un numero, il 15%) lascia **300-400 ms di immobilità totale** prima
dell'elemento successivo. La pausa breve dopo il picco è ciò che distingue un montaggio ritmato da un montaggio
frettoloso. Non confondere "pausa dopo il picco" con "scena ferma": 400 ms, non 2 s.

**Pattern interrupt ogni 2-4 s**: alternanza di *tipo* di evento, non solo di contenuto. Se tre eventi di fila
sono "entra una riga di testo", il quarto deve essere di natura diversa (uno stacco, uno zoom che si risolve,
una barra che avanza, un blur). La varietà è di **grammatica**, non di parole.

---

## 4. Tipografia cinetica — i pattern da implementare

Tutti realizzabili in CSS puro. Fonti: Archivo 800/900 per le parole battute, Manrope per il corpo.

1. **Parola per parola (RSVP battuta)** — ogni parola appare da sola al centro, 160-220 ms l'una, il resto dello
   schermo vuoto. Deriva dalla *Rapid Serial Visual Presentation*: si legge più in fretta di una frase intera.
   Usalo **solo sul gancio o su una frase-chiave**, mai su un paragrafo. CSS: `span` per parola +
   `animation-delay` progressivo su opacità e `translateY(12px)`.
2. **Accumulo di parole** — variante opposta: le parole restano e la frase si costruisce. Più adatta alle frasi
   che devono essere *lette insieme* (una promessa, un claim). 120 ms per parola.
3. **Evidenziatore che corre** — un blocco oro si allarga da sinistra a destra **dietro** una parola già presente
   (`background-size: 0% 100%` → `100% 100%`, 260 ms, `transform-origin: left`). La parola evidenziata cambia
   colore in `#2E2A25` a metà corsa. È il pattern più riconoscibile del 2025-26 e il più economico per marcare il
   concetto che vuoi far ricordare. **Una sola parola evidenziata per reel**, altrimenti perde forza.
4. **Testo che sostituisce se stesso** — stessa posizione, la parola vecchia esce in alto e la nuova entra dal
   basso dentro una maschera (`overflow: hidden` sul contenitore, 200 ms). Serve per le sequenze
   "non X · non Y · ma Z". La maschera è ciò che lo fa sembrare fatto bene: senza `overflow:hidden` è un
   cambio di testo, con, è un rullo.
5. **Numeri che salgono** — contatore con decelerazione forte negli ultimi 30% e **scatto di scala** all'arrivo
   (1→1,12→1 in 180 ms). Se il numero ha un'unità (%, €, notti), l'unità **non** deve salire: sta ferma accanto.
6. **Riga che si cancella e si riscrive** — una linea oro attraversa una parola (strikethrough animato,
   `width: 0→100%` in 200 ms) e subito sotto entra la parola corretta. Perfetto per il lessico di brand:
   ~~hotel-style~~ → **standard alberghiero**.
7. **Maschera di rivelazione dal basso** — il testo esce da sotto una linea invisibile (`clip-path: inset(100% 0 0 0)`
   → `inset(0)`), 220 ms. È l'entrata "premium" di default: usala per i titoli quando non vuoi l'overshoot.
8. **Scala da grande a piccolo (compressione)** — un titolo a piena pagina si riduce e va a incastrarsi in alto
   diventando l'etichetta della scena successiva. È una transizione **e** una gerarchia: fa sembrare il video
   progettato, non montato.
9. **Kerning che si chiude** — `letter-spacing` da 0,4em a 0,02em in 400 ms su un kicker maiuscolo. Piccolo,
   costa nulla, aggiunge la sensazione di "motion design" che manca ai reel poveri.

**Regole tipografiche trasversali**: mai più di **due dimensioni** di testo nello stesso fotogramma più il
kicker; mai testo sotto i 44 px su 1080×1920; ombra stratificata sotto ogni riga bianca su foto; le righe si
spezzano **a mano**, mai a caso.

---

## 5. Il loop

**Perché conta**: il watch time è il segnale principale. Un video di 10 s guardato 3 volte vale 30 s di visione su
una sola impression. Le guide sul looping lo indicano come la leva più economica per moltiplicare il watch time,
e il meccanismo psicologico è la chiusura mancata: se il video riparte senza che si percepisca lo stacco, lo
spettatore resta dentro qualche secondo per capire se ha già visto quel pezzo. `[prassi di settore, meccanismo
documentato in modo aneddotico]`

**Le tre costruzioni, in ordine di forza:**

1. **Loop di stato (il migliore per noi)** — l'ultimo fotogramma è **identico** al primo per composizione,
   colore e posizione degli elementi. Concretamente: se apri su fondo fumè con il marchio in alto e una foto in
   zoom al 3%, chiudi sullo stesso fondo, stesso marchio, stessa foto alla stessa scala. La CTA si è già ritirata
   negli ultimi 200 ms. In cattura: renderizza il frame 0 e l'ultimo frame e **confrontali**; se non sono quasi
   sovrapponibili, il loop non c'è.
2. **Loop di movimento** — il movimento di camera non si ferma mai: la scena finale sta traslando nella stessa
   direzione e alla stessa velocità della scena iniziale. Anche con contenuti diversi, l'occhio non registra il
   salto perché la velocità è continua. È il loop più facile da ottenere con zoom lenti.
3. **Loop di domanda** — la chiusura pone la domanda a cui il gancio risponde ("e la tua casa a che punto è?" →
   taglio → "Nessun proprietario ci chiede quanto guadagna"). Non è invisibile, ma crea la seconda visione.

**Regole esecutive del loop:**
- **Nessun fade to black finale.** Mai. Un nero finale chiude il loop e uccide il replay.
- Il video finisce **su un taglio netto**, non su un elemento in movimento a metà transizione.
- Non lasciare l'ultimo fotogramma vuoto o con la sola CTA ferma per più di 1,5 s: è tempo morto che azzera
  la probabilità di replay.
- Nei formati con accumulo (checklist, split screen) il loop di stato richiede che gli elementi accumulati
  **escano** negli ultimi 300 ms, così il frame finale torna pulito come il primo.
- Durata e loop vanno insieme: **sotto i 12 s il loop rende molto**, sopra i 25 s quasi nulla. Se il contenuto
  richiede 30 s, non sprecare struttura per il loop: investi tutto nella chiusura e nella CTA.

---

## 6. Cosa fa sembrare un reel "povero" — la diagnosi

Lista di difetti **concreti e verificabili sul file**. Se un reel ne ha 3, il titolare lo boccerà, e avrà ragione.

**A. Difetti di movimento**
1. Un solo tipo di movimento per tutto il video (solo zoom, o solo pan). Ricchezza = **almeno tre grammatiche
   diverse** di movimento nello stesso reel (es. parallasse + tendina + compressione di scala).
2. Movimento costante e lineare (`linear` o `ease`). Il movimento di qualità **decelera**: `cubic-bezier(.16,1,.3,1)`.
   L'easing lineare è la firma sonora dell'amatoriale.
3. Zoom troppo forte: oltre il 10-12% di scala su una foto in 3 s si vede la sfocatura e sembra un salvaschermo.
4. Movimento che si ferma e poi riparte: se il moto ha un punto morto a metà scena, l'occhio lo legge come errore.
5. Un solo livello di parallasse. Vedi 1.7: il terzo livello è la differenza tra profondità e scorrimento.

**B. Difetti di ritmo**
6. Inquadratura ferma sopra i 4 s.
7. Tutte le battute della stessa durata esatta: la regolarità perfetta è monotona. Serve la curva di
   accelerazione del §3.
8. Dissolvenze incrociate tra le scene. Uno stacco netto è sempre più professionale di un dissolve da 400 ms.
9. Uscite di testo lente. Il testo esce **a taglio**.
10. Nessuna micro-pausa dopo il dato importante: tutto scorre uguale, niente viene ricordato.

**C. Difetti di tipografia**
11. Testo che entra e esce con la sola opacità (`fade`). Senza traslazione, scala o maschera sembra PowerPoint.
12. Troppe dimensioni di testo nello stesso fotogramma (più di due + kicker).
13. Frasi da leggere: più di 7 parole su una schermata.
14. Testo sempre nella stessa posizione per tutto il video senza variazione di gerarchia.
15. Testo bianco appoggiato su foto senza velo o ombra: si legge male e legge "fatto in fretta".

**D. Difetti di composizione**
16. **Fotogrammi vuoti**: un testo al centro e basta. Un fotogramma ricco ha almeno **tre livelli**: fondo in
    movimento, elemento di brand fisso (marchio, filo oro, barra), contenuto.
17. Nessun elemento persistente: se ogni scena è un mondo a sé, il video sembra una raccolta di immagini.
    Il marchio in alto e la barra di avanzamento sono la colla.
18. Margini incoerenti tra una scena e l'altra: il testo sta a 120 px dal bordo in una scena e a 180 px in
    quella dopo. È il difetto che si sente senza saperlo nominare.
19. Bordi netti su tutto e nessuna profondità: nessun blur, nessun velo, nessuna sovrapposizione. Un unico
    piano visivo = povero.
20. Palette piatta: solo fumè e bianco. **L'oro deve comparire in ogni scena**, anche solo come filo di 3 px.

**E. Difetti di struttura**
21. Nessuna progressione: al secondo 8 non si sa quanto manca. Rimedio: barra di avanzamento (già regola nostra
    sopra i 10 s) o numerazione visibile.
22. Il video finisce in nero o su una CTA ferma per 2 s. Niente loop, niente replay.
23. Un solo evento nei primi 2 secondi.
24. Tutto il video è testo su fondo pieno (vedi 1.8).
25. **Nessuna variazione rispetto al reel precedente**: stessa struttura due volte di fila è povertà a livello di
    serie anche se il singolo file è ben fatto (preferenza fissa n.5 di `CLAUDE.md`).

**Autodiagnosi rapida** (da fare sul MP4 renderizzato, guardato a dimensione telefono, prima di mostrarlo):
- metti in pausa a caso 5 volte: **ogni fermo immagine ha almeno tre livelli e l'oro?**
- guarda senza leggere: **si capisce che succede qualcosa ogni 2 secondi?**
- confronta primo e ultimo fotogramma: **si sovrappongono?**
- conta le grammatiche di movimento: **sono almeno tre?**
- conta gli eventi nei primi 2 s: **sono almeno tre?**

---

## 7. Tre strutture complete, secondo per secondo

Formato di tutte: 1080×1920, 30 fps, fondo fumè `#3F3A33` o gradient radiale standard, oro `#C8A24B`,
Archivo 800/900 + Manrope. Marchio fisso in alto per tutta la durata. Nessun nero finale.
I numeri tra parentesi quadre sono da sostituire con dati verificati o vanno rimossi.

### Struttura A — "I 7 controlli" (checklist che si compila) · 15,0 s · obiettivo SALVATAGGI

| t (s) | Cosa succede sullo schermo | Meccanica CSS |
|---|---|---|
| 0,0-0,5 | Foto di interno **già in zoom** (scala 1,03 in corso). Velo scuro al 55%. La parola `PRIMA` entra dal basso in maschera. | `clip-path: inset(100% 0 0 0)`→`inset(0)`, 200 ms; zoom con `animation-delay: -0.4s` |
| 0,5-1,0 | `PRIMA` si comprime in alto a sinistra e diventa kicker; al centro atterra `7 CONTROLLI` (Archivo 900, 132 px) con overshoot e stop netto | scala 1→0,32 + traslazione, 260 ms, `cubic-bezier(.16,1,.3,1)` |
| 1,0-1,4 | Sotto entra `PRIMA DI OGNI CHECK-IN` (Manrope 600, 48 px). Parte la barra oro in alto (0%) | fade+`translateY(10px)`, 160 ms |
| 1,4-1,6 | **Stacco netto**. Fondo fumè pieno. La lista comincia | nessuna transizione |
| 1,6-3,0 | Riga 1: entra da sinistra, spunta oro si disegna, barra a 1/7 | `stroke-dashoffset` 220 ms |
| 3,0-4,3 | Riga 2 (la 1 scala a 0,86, opacità 0,45) | |
| 4,3-5,5 | Riga 3 — le battute si accorciano di ~100 ms l'una | |
| 5,5-6,6 | Riga 4 | |
| 6,6-7,6 | Riga 5 | |
| 7,6-8,5 | Riga 6 | |
| 8,5-9,4 | Riga 7 + barra al 100% con scatto di scala | scala 1,08→1, 180 ms |
| 9,4-9,8 | **Immobilità totale** sulla lista completa | pausa dopo il picco |
| 9,8-10,2 | La lista si comprime in alto (scala 0,7) e sfuma al 30% | 400 ms |
| 10,2-12,4 | Al centro: `Ogni casa. Ogni volta. Senza che tu debba controllare.` — tre frasi che entrano in accumulo, 700 ms l'una | |
| 12,4-14,0 | CTA oro a pillola a tutta larghezza che entra dal basso: `Scrivi "CONTROLLI" in DM` | 260 ms |
| 14,0-14,7 | La CTA **si ritira** verso il basso, la lista sfuma via, resta la foto iniziale in zoom | preparazione del loop |
| 14,7-15,0 | Fotogramma identico a 0,0 | loop di stato |

### Struttura B — "Prima / dopo ×3" (tendine incalzanti) · 12,0 s · obiettivo CONDIVISIONI

| t (s) | Cosa succede | Meccanica |
|---|---|---|
| 0,0-1,2 | Mock di annuncio scritto male (disegnato in HTML), già in pan lento verso sinistra. Etichetta piccola `PRIMA` in alto a sinistra | pan con delay negativo 400 ms |
| 0,6 | Micro-evento: una riga del mock si evidenzia in rosso-neutro/grigio e trema di 4 px | secondo interrupt nei 2 s |
| 1,2-1,5 | **Tendina 1** da destra: scopre l'annuncio nostro. Il pan continua senza interruzione | `clip-path: inset(0 X% 0 0)`, 300 ms |
| 1,5-3,0 | La scena "dopo" prosegue; entra in basso una riga breve (`Titolo, foto, prezzo: tre cose.`) | maschera dal basso 200 ms |
| 3,0-3,2 | **Stacco netto**. Coppia 2: calendario bucato, caselle vuote | |
| 3,2-4,2 | Le caselle vuote pulsano appena (opacità 0,6↔0,9, 1,2 s) | |
| 4,2-4,44 | **Tendina 2** (240 ms): calendario che si riempie d'oro a ondata diagonale | `animation-delay` per riga+colonna |
| 4,44-6,0 | Riga breve in basso | |
| 6,0-6,2 | Stacco. Coppia 3: stanza non preparata → stanza in standard alberghiero | |
| 6,2-7,0 | Zoom lento sulla "prima" | |
| 7,0-7,2 | **Tendina 3** (200 ms) — la più rapida delle tre | |
| 7,2-8,0 | Riga breve | |
| 8,0-8,5 | Le tre scene "dopo" si rimpiccioliscono e si affiancano in tre colonne | scala 1→0,33, 400 ms |
| 8,5-9,0 | Pausa sulla griglia, un filo oro le unisce disegnandosi | 300 ms |
| 9,0-10,6 | Sopra la griglia: `Annuncio. Calendario. Casa.` in accumulo di parole, 220 ms l'una, poi `Tre cose, un unico lavoro.` | |
| 10,6-11,6 | CTA oro | |
| 11,6-12,0 | La griglia si ricompone sulla prima scena "prima", il pan riparte alla stessa velocità del frame 0 | loop di movimento |

### Struttura C — "Il metodo" (finta interfaccia + checklist, per raccontare come lavoriamo) · 18,0 s · obiettivo CONTATTI

Il formato più adatto al "metodo di lavoro" di un property manager: mostra **processo**, non risultati (e resta
quindi dentro la regola "niente case study su strutture nominate").

| t (s) | Cosa succede | Meccanica |
|---|---|---|
| 0,0-0,5 | Schermo fumè. **Una notifica entra** dall'alto, già a metà corsa al frame 0: `Richiesta di prenotazione` | `translateY` + scala 0,94→1, 220 ms, delay negativo |
| 0,5-1,1 | Seconda notifica (`Domanda dell'ospite`), la prima scende e sfuma | 600 ms di cadenza |
| 1,1-1,6 | Terza notifica. Sopra tutto atterra il gancio in maschera: `Questo succede mentre dormi.` | 180 ms |
| 1,6-3,0 | Quarta e quinta notifica a cadenza accelerata (500, 400 ms) — il ritmo che accelera è il punto del blocco | |
| 3,0-3,2 | **Stacco netto**. Tutto sparisce. Fondo pulito | |
| 3,2-4,0 | Al centro: `Noi lo gestiamo prima che tu te ne accorga.` entra parola per parola, 170 ms l'una | RSVP in accumulo |
| 4,0-4,4 | **Immobilità 400 ms** | pausa dopo il picco |
| 4,4-4,6 | Stacco. Compare la parola `IL METODO` come kicker in alto, `letter-spacing` che si chiude | 400 ms |
| 4,6-11,0 | **Quattro fasi**, 1,6 s l'una, ognuna con: numero gigante oro a sinistra (`01`…`04`, Archivo 900, 240 px), titolo e una riga di dettaglio a destra, che entrano sfasati di 250 ms. Il numero della fase precedente **esce verso l'alto in maschera** mentre entra il nuovo. Barra di avanzamento oro in alto che avanza a scatti di 1/4 | maschera `overflow:hidden`, 200 ms per lo scorrimento del numero |
| | Fasi suggerite: `01 Preparazione` · `02 Annuncio e prezzo` · `03 Ospiti, 24 ore su 24` · `04 Pulizie e controlli` | |
| 11,0-11,4 | Le quattro fasi si affiancano in una riga compressa in alto (scala 0,25) | 400 ms |
| 11,4-12,0 | Sotto compare il **calendario mensile** vuoto | |
| 12,0-13,2 | Le caselle si riempiono d'oro a ondata diagonale | 900 ms + 300 ms di respiro |
| 13,2-14,6 | Sopra il calendario entra la riga che vale l'intero reel: `Tu non fai niente. Noi guadagniamo solo se guadagni tu.` — le ultime cinque parole con **evidenziatore oro che corre** | `background-size: 0%→100%`, 260 ms |
| 14,6-15,0 | Immobilità | |
| 15,0-15,3 | Il calendario va in blur (`blur(10px)`) | 300 ms |
| 15,3-16,8 | CTA oro a pillola: `Scrivi "METODO" in DM` | entra dal basso, 260 ms |
| 16,8-17,5 | CTA si ritira, blur si scioglie, il calendario torna a fuoco e **sfuma via** | |
| 17,5-18,0 | Fondo fumè pulito con il marchio: una notifica **ricomincia a entrare** dall'alto, alla stessa velocità del frame 0 | loop di stato + movimento |

> Nota di compliance su C: `Guadagniamo solo se guadagni tu` è la forma corretta (mai "guadagni solo se
> guadagni tu"). Il calendario che si riempie è un **simbolo di processo**, non una promessa di occupazione:
> non affiancargli percentuali non verificate.

---

## 8. Checklist prima dell'export

1. Almeno **tre eventi** nei primi 2 secondi, e il frame 0 è già in movimento.
2. Almeno **tre grammatiche di movimento** diverse nel video.
3. Nessuna inquadratura ferma sopra i 4 s; nessuna dissolvenza incrociata; nessun fade to black.
4. Massimo 7 parole per schermata; massimo due dimensioni di testo + kicker per fotogramma.
5. Oro presente in **ogni** scena; marchio fisso per tutta la durata.
6. Margini identici in tutte le scene.
7. Una micro-pausa di 300-400 ms dopo ogni picco.
8. Primo e ultimo fotogramma sovrapponibili (loop di stato) o velocità di movimento continua (loop di movimento).
9. Durata 8-15 s salvo necessità di spiegazione (max 20-25 s); barra di avanzamento se sopra i 10 s.
10. Struttura **diversa** dall'ultimo reel pubblicato (controlla `campagne/INDEX.md` e `PIANO.md`).
11. Ogni numero a schermo è verificato, oppure non c'è.
12. Passaggio da `compliance-checker` prima della consegna.

---

## Fonti

Ranking e segnali: [Buffer — Instagram algorithm](https://buffer.com/resources/instagram-algorithms/) ·
[Later](https://later.com/blog/how-instagram-algorithm-works/) ·
[Hootsuite](https://blog.hootsuite.com/instagram-algorithm/) ·
[Dataslayer — 5 ranking signals Mosseri confirmed](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers) ·
[Socialync — Mosseri on shares](https://www.socialync.io/blog/adam-mosseri-shares-instagram-algorithm-2026)

Durata e retention: [CreatorHouse — test su 50 reel, aprile 2026](https://creatorhouse.app/blog/instagram-reel-length-2026-test) ·
[OpusClip — ideal reels length](https://www.opus.pro/blog/ideal-instagram-reels-length) ·
[Blitzcut](https://blitzcutai.com/blog/best-reels-length-reach)

Ritmo, hook e pattern interrupt: [Async — how to edit Instagram Reels](https://async.com/blog/how-to-edit-instagram-reels/) ·
[CreatorScope — pattern interrupts](https://www.creatorscope.io/blog/pattern-interrupts-keep-viewers-watching-your-reels-longer-1) ·
[Green Frog Labs — video hooks 2026](https://greenfroglabs.com/blog/video-hooks-scroll-stopping-2026) ·
[OpusClip — hook formulas](https://www.opus.pro/blog/instagram-reels-hook-formulas) ·
[Marketing Espresso (IT)](https://blog.marketing-espresso.com/come-creare-un-reel-efficace/) ·
[Canthiere — reel immobiliari (IT)](https://www.canthiere.it/blog/reel-immobiliari-instagram-tiktok) ·
[Loomen Studio — script reel in 3 atti (IT)](https://www.loomenstudio.com/agency-script-reel-struttura/)

Formati faceless e immobiliari: [SHhots — 10 real estate reel formats 2026](https://shhots.ai/blog/real-estate-reels-ideas/) ·
[Houfy — Instagram for vacation rentals 2026](https://www.houfy.com/blog/instagram-for-vacation-rentals-whats-working-in-2026) ·
[Houfy — reels ideas for rental hosts](https://www.houfy.com/blog/instagram-reels-ideas-for-rental-hosts) ·
[Coffee & Contracts — viral listing reels](https://coffeecontracts.com/blog/the-ultimate-guide-to-viral-listing-reels-what-to-post-as-a-realtor-instead-of-just-sold) ·
[Captivateur — 7 formats faceless](https://captivateur.com/en/blogs/the-keys-to-digital-products-and-plr/faceless-reels-7-formats-pour-creer-du-contenu-viral-sans-se-montrer) ·
[Korpi AI — faceless reels guide 2026](https://korpi.ai/blog/faceless-instagram-reels-guide) ·
[Multi-Housing News — reels per property management](https://www.multihousingnews.com/5-effective-instagram-reels-and-tiktok-strategies-for-property-management/)

Tipografia cinetica: [SVGator — 50 kinetic typography examples](https://www.svgator.com/blog/50-kinetic-typography-examples/) ·
[Linearity — kinetic typography](https://www.linearity.io/blog/kinetic-typography/) ·
[Upskillist — kinetic typography trends](https://www.upskillist.com/blog/top-7-kinetic-typography-trends-2025/)

Loop: [Radarr — looping reels](https://www.radarr.com/blog/ultimate-guide-to-create-instagram-looping-reels/) ·
[Vistaar WebX — the art of looping](https://vistaarwebx.com/the-art-of-looping-creating-seamless-reels-that-keep-viewers-watching/) ·
[Digital Blacksmiths — loopable videos](https://digitalblacksmiths.io/youtube-shorts-algorithm-secret-loopable-videos-increase-watch-time/)

Difetti da amatoriale: [OUI Creatives — 7 reel editing mistakes](https://www.ouicreatives.com/blog/7-reel-editing-mistakes-that-make-your-content-look-amateur-and-what-to-do-instead) ·
[Media à la Carte](https://www.mediaalacarte.com/post/mistakes-that-make-your-reels-look-amateur-and-how-to-fix-them) ·
[Storyblocks — 8 editing mistakes](https://www.storyblocks.com/resources/blog/editing-mistakes-beginners-make-with-video) ·
[Editors Keys](https://www.editorskeys.com/blogs/news/5-editing-mistakes-that-make-your-videos-look-amateur-and-how-to-avoid-them)

---

## Errori di animazione trovati sul campo (aggiornato 16/09/2026)

Tre difetti che il titolare ha visto guardando il reel a velocità reale, e che i frame
estratti uno per uno **non** avevano fatto emergere. Vanno controllati su ogni reel.

### 1. L'accumulo che sbiadisce si legge come un bug

Nel formato "checklist che si accumula" è tentante far sbiadire le righe già entrate
(opacità 0,45, scala 0,86) per tenere l'attenzione sull'ultima. **Non farlo.** A schermo,
a velocità reale, il risultato è che una riga è scura e le altre pallide: chi guarda non
vede una gerarchia, vede *elementi disegnati in modi diversi*. Stessa cosa per le spunte,
che sbiadiscono insieme alla riga e sembrano comparire su alcune voci e non su altre.

**Regola.** In una lista che si accumula, una riga che entra **resta identica alle altre**:
stesso fondo, stesso colore, stessa scala, stessa spunta piena. L'attenzione si porta col
**movimento di entrata**, non togliendo colore a quello che è già a schermo.

Il principio vale oltre le liste: **elementi della stessa famiglia si comportano tutti allo
stesso modo.** Se una forma compare su un elemento, compare su tutti; se ne resta uno senza,
sembra un errore di montaggio.

### 2. Ogni testo ha un tempo minimo di lettura

Una battuta di 0,9 s su una riga di due righe non si legge: si intravede. Tempi minimi
misurati su questo progetto:

| Elemento | Tempo fermo minimo |
|---|---|
| Riga di lista (titolo + dettaglio) | **1,2 s** |
| Frase di due righe | **1,8 s** |
| Parola singola di svolta (`Falso.`) | **1,1 s** |
| Confronto a due fasce, prima che una collassi | **1,2 s** |
| CTA finale | **2,0 s** |

Meglio un reel di 25 s che si legge di uno di 17 s che si intravede. Se il conto non torna,
**si tagliano le scene, non i tempi di lettura.**

### 3. Le posizioni ereditate restano quando l'elemento accanto sparisce

Una frase ancorata a `left: 430px` perché a sinistra c'era la lista compressa resta a 430
anche dopo che quella lista è stata tolta dal montaggio: va a capo in una colonna stretta
per nessun motivo. **A ogni modifica della sequenza, ricontrolla le posizioni delle scene
vicine**, non solo quella che hai cambiato.
