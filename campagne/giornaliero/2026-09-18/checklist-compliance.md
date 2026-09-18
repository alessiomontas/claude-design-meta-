# Checklist compliance — Giornaliero 18/09/2026 · «Le recensioni non sono un complimento»

## Esito

**DA CORREGGERE** — 7 bloccanti. Nessuno riguarda un claim inventato: l'impianto di claim è solido e
i divieti chiusi dal titolare (punteggio aggregato, Cornell fuori posto, anello 5, Superhost come gancio)
sono **tutti rispettati**. I bloccanti sono su riuso delle recensioni, integrità di una citazione,
leggibilità di un caveat, una parafrasi su fonte non verificata e tre incoerenze interne al pacchetto.

Controllato: `brief-mercato.md`, `copy.md`, `direzione-artistica.md`, 23 `.dc.html`, 23 PNG
(C1-C5, F1-F3, S1-S2, R00-R12), `reel/scene.json`, incrocio con
`campagne/facebook-recensioni-superhost/recensioni-reali.md`.

---

## Bloccanti (da correggere prima della consegna)

### 1. Le cinque recensioni **sono le stesse** già usate in `facebook-recensioni-superhost`
Verifica richiesta esplicitamente, e l'esito è negativo. Tutte e cinque — **Paweł, Attila, Katarzyna,
Aline, Martin** — sono già nell'elenco delle nove in
`campagne/facebook-recensioni-superhost/recensioni-reali.md` (righe 9-32). Non una parte: tutte.
Tre di esse (Paweł in S1, Attila in C4, Katarzyna in F2) vanno **a schermo**, cioè nel formato più
memorabile, sullo stesso pubblico.
Il brief lo aveva posto come condizione (`brief-mercato.md`, riga 138: «non riusare le stesse già
pubblicate in quella campagna senza variarle») e `copy.md` lo lascia aperto (riga 687).

→ **Come si risolve.** Due strade, entrambe accettabili, nessun'altra:
- **(a)** chiedere al titolare cinque recensioni **non ancora pubblicate** (dallo stesso screenshot o da
  uno nuovo) e sostituire almeno le **tre a schermo**. Le quattro rimaste inutilizzate nel file storico
  (**Anne Loes**, **Maïwenn**, **Stefania**, **Fanny**) sono anch'esse già archiviate ma **mai pubblicate**:
  se il titolare conferma che non sono mai uscite, bastano per coprire i tre slot a schermo, con
  **Stefania** (italiana, niente riga di traduzione, parla di pulizia + host attento) come sostituta
  naturale di Paweł in S1.
- **(b)** ok esplicito del titolare al riuso, annotato in `PUBBLICAZIONE.md` e nel registro di
  `campagne/giornaliero/PIANO.md`. In assenza di questo ok, non si pubblica.

### 2. Citazione di Katarzyna tagliata **senza** i puntini di sospensione
Regola: tagli con `…` ammessi, testo presentato come integrale quando non lo è **no**.
Originale (`recensioni-reali.md`, righe 29-31) comincia con: «Un appartamento in ottima posizione,
vicino alla spiaggia, alla stazione ferroviaria, a negozi e caffetterie.» — quella frase è stata tolta,
ma la citazione a schermo apre con le virgolette secche.
Dove: `grafiche/F2.dc.html` riga 32 (e `png/F2.png`), più il testo del post Facebook (`copy.md` riga 402)
e la tabella slot (riga 37).

→ **Correzione esatta**, identica nei tre punti:
`«… L'appartamento è dotato di accessori da cucina, lavatrice e letti confortevoli. Ottima comunicazione con l'host. Consigliato»`
Sono 2 battute in più su 130 di capienza: rigenerare F2 e ricontrollare che la card resti su 3 righe.
*(Le altre quattro citazioni sono verbatim e correttamente segnate: Attila e Paweł con `…` in apertura
e in mezzo, Aline e Martin integrali/troncati con `…` nel testo FB. Nessuna parola riscritta da nessuna
parte — verificato parola per parola contro l'originale.)*

### 3. I caveat Cornell in C3 **non sono leggibili** a dimensione telefono
Ci sono, e sono i due giusti («settore alberghiero», «2012») — ma sono a **corpo 17 su 1080 px**:
su un telefono da ~390 px di larghezza diventano ~6 px reali. Il `+11%` è a corpo 200. Il numero si
legge dall'altra parte della stanza, la condizione che lo rende citabile no. È esattamente lo squilibrio
che rende un claim indifendibile: a schermo resta solo «+11%».

→ **Correzione esatta.** In `grafiche/C3.dc.html` riga 35: `font-size: 17px` → **`26px`**,
`color: rgba(255,255,255,0.62)` → **`rgba(255,255,255,0.80)`**. Il blocco cresce di ~26 px: c'è spazio,
tra la fonte (y 870) e il filo oro (y 1010) ci sono 140 px. Rigenerare e ricontrollare sul PNG.
*(La riga `traduzione di Airbnb` a corpo 17 nelle card resta com'è: è una nota di provenienza, non un
caveat che regge un claim, e sta su fondo sabbia con contrasto molto più alto.)*

### 4. Il pacchetto dice **due numeri diversi** sulle sei voci
- Testo Facebook (`copy.md` riga 394): «**quattro** delle sei voci che l'ospite valuta sono esecuzione».
- Storia S2, a schermo (`png/S2.png`): «**Cinque** su sei sono esecuzione», con cinque micro-anelli pieni.
Stesso giorno, stesso pubblico, due conteggi. Chi vede entrambi nota l'aggiustamento e smette di fidarsi
del resto del ragionamento — che è la cosa che questo contenuto vende.

→ **Correzione esatta.** Allineare sul **cinque**, che è quello a schermo e quello disegnato:
in `copy.md` riga 394 sostituire «quattro delle sei voci che l'ospite valuta sono esecuzione» con
«**cinque delle sei voci che l'ospite valuta dipendono da come la casa è gestita**».
(Una sola parola nel testo del post, contro un ridisegno di S2.)

### 5. La parafrasi Booking, nella forma attuale, **non è difendibile**
Questione lasciata aperta dall'art-director: la chiudo come **da ammorbidire**.
Il problema non è l'esistenza del meccanismo — quello è dichiarato e regge. Il problema è il **secondo
dettaglio**: «e precisa che le recensioni recenti pesano più di quelle vecchie» (`copy.md` riga 386).
È una frase specifica, **attribuita a Booking in prima persona**, ricavata da indicizzazione e non da
pagina aperta (il brief stesso lo scrive alla riga 44: «verificare il testo esatto prima di citarlo»).
Metterla in bocca a una piattaforma terza senza aver letto la fonte è il tipo di dettaglio che, se
sbagliato, si ritorce. Il primo dettaglio (punteggio fra i fattori di visibilità) è invece coperto
anche da Airbnb, che è verificata: quello resta.

→ **Correzione esatta.** Nel punto 1 del post Facebook sostituire:
> «Booking indica il punteggio recensioni tra i fattori su cui il partner può agire per migliorare la propria visibilità, e precisa che le recensioni recenti pesano più di quelle vecchie.»

con:
> «Booking e Airbnb dicono entrambe, nelle guide che pubblicano per chi ospita, che il punteggio delle recensioni è fra gli elementi che incidono sulla visibilità di un annuncio.»

Il resto del paragrafo (Airbnb, categorie, Guest Favorite nei risultati, «il funzionamento esatto resta
riservato: nessuno può prometterti una posizione») **non si tocca**: è documentato ed è la riga che
protegge dal claim di risultato. Se il titolare apre la pagina Booking e verifica il dettaglio sulla
recency, si può rimettere **virgolettato**; finché non è verificato, fuori.

### 6. Nel reel l'etichetta accesa **non corrisponde alla frase a schermo**
Non è un dettaglio estetico: è un errore di lettura, e il reel è il formato dove testo ed etichetta si
leggono nello stesso istante. Off-by-one sistematico:

| Scena | Frase a schermo | Anello acceso |
|---|---|---|
| R04 | «Il punteggio conta in come esci nelle ricerche» (= visibilità) | `RECENSIONE` |
| R06 | «Chi ti trova ha già un motivo per fidarsi» (= chi prenota) | `PREZZO` |
| R07 | «Quindi il prezzo non lo devi abbassare» (= prezzo) | `CHI PRENOTA` |

La causa: l'ordine di racconto del reel è **1→3→2** (visibilità → fiducia → prezzo, come prescrive il
brief alla riga 117), mentre la striscia porta le etichette del **carosello**, che ha un altro ordine.

→ **Correzione minima** (una riga, nessun testo da riscrivere, nessuna scena da rigirare): nel reel
usare le sue etichette, `RECENSIONE · VISIBILITÀ · FIDUCIA · PREZZO`. Così R04 accende `VISIBILITÀ`,
R05 resta su `VISIBILITÀ`, R06 accende `FIDUCIA`, R07 accende `PREZZO` — e l'evidenziatore oro, unico
accento del pacchetto, cade sull'ultimo anello, dove serve. Da aggiornare in `grafiche/base.py`
(etichette catena del reel), `reel/scene.json` e la tabella di `direzione-artistica.md` (righe 91-92 e 95-108).

### 7. Tre numerazioni diverse della stessa catena — **è il punto che avevi notato, e crea attrito**
Confermo la tua lettura, e il problema è più largo di quanto sembrasse. Oggi nel pacchetto convivono:

- **Carosello:** quattro pallini (`RECENSIONE · VISIBILITÀ · PREZZO · CHI PRENOTA`) ma kicker
  `ANELLO 01 — VISIBILITÀ` / `02 — PREZZO` / `03 — CHI PRENOTA`. Su C2 si vedono **due pallini accesi
  sopra la scritta «ANELLO 01»**; su C4 **quattro accesi sopra «ANELLO 03»**. L'occhio conta i pallini
  prima di leggere il numero, e i due dati si contraddicono a mezzo secondo di distanza.
- **F2:** la stessa catena numerata **01→04**, con `01 · Il punteggio pesa nel posizionamento` (che nel
  carosello è l'anello 01 = visibilità, ma qui è il primo dei quattro).
- **Storie:** medaglione `01 — ANELLO 01 — RECENSIONE` in S2 e `02 — ANELLO 02 — PREZZO` in S1. In S2
  «anello 01 = recensione», nel carosello «anello 01 = visibilità»: contraddizione secca fra due
  contenuti dello stesso giorno. In più S2 non è un passaggio della catena, è l'obiezione sulle sei voci:
  il numero lì non significa niente.

Non è un caso limite: è **la premessa contata una volta sì e una volta no**. E l'attrito è peggiore in
C2, che è la slide in cui il lettore sta imparando a leggere lo schema.

→ **Correzione minima, e la più economica delle tre possibili** (vedi nota sotto): **togliere il numero
dai kicker, tenere l'etichetta.** I pallini accesi dicono già dove siamo, con più precisione di un numero.
- C2: `ANELLO 01 — VISIBILITÀ` → **`VISIBILITÀ`**
- C3: `ANELLO 02 — PREZZO` → **`PREZZO`**
- C4: `ANELLO 03 — CHI PRENOTA` → **`CHI PRENOTA`**
- S1: medaglione `02` + `ANELLO 02 — PREZZO` → medaglione tolto, resta **`PREZZO`** (il filo oro sotto
  il lockup basta come firma grafica)
- S2: medaglione `01` + `ANELLO 01 — RECENSIONE` → **`LE SEI VOCI`**, che è di cosa parla davvero la storia
- **F2 resta com'è**: i suoi `01→04` sono gli unici numeri coerenti coi quattro pallini, ed è l'unico
  posto dove la catena è scritta per esteso invece che accennata.

*(Le altre due strade, scartate: rinumerare tutto 01→04 includendo la recensione obbliga a inventare
una slide «anello 01 = recensione» che il carosello non ha; etichettare il primo pallino «PREMESSA»
aggiunge una parola tecnica su un elemento che deve essere letto in un colpo d'occhio.)*

---

## Osservazioni (non bloccanti, ma da considerare)

- **`copy.md` non è più allineato ai PNG.** L'art-director ha accorciato le citazioni di Paweł (S1) e
  Attila (C4) — legittimamente, e lo dichiara nella sezione *Deviazioni* — ma `copy.md` porta ancora i
  testi lunghi (righe 35-36, 264, 582), e il gancio di S2 è `"Il punteggio dipende dall'ospite."` nel
  blocco COPY e `"Tanto il punteggio dipende dall'ospite."` (quello renderizzato) nel blocco sotto.
  Se il Master Template è la fonte, va riallineato ai file consegnati, altrimenti alla prossima modifica
  qualcuno rigenera la versione sbagliata.
- **«Attila · 3 settimane fa».** Data relativa: fra un mese sarà falsa, e nell'archivio della campagna
  precedente la stessa recensione risultava «1 settimana fa». Meglio un mese fisso («agosto 2026», se il
  titolare lo conferma dallo screenshot) — le altre card usano già il mese.
- **C2, vuoto di ~160 px** fra il corpo e la fascia sabbia. Passa il controllo 3, ma è l'unica slide del
  carosello in cui si sente un buco a metà.
- **CTA doppia formulazione:** «Scrivi "PUNTEGGIO" in DM» (Instagram) e «Scrivi "PUNTEGGIO"» (F3),
  mentre il testo del post dice «nei commenti o in privato». È coerente col canale, lo segnalo solo
  perché F3 da solo non dice dove scrivere.
- **S2, ~350 px vuoti sotto la CTA.** Dentro safe area, ma la storia si chiude alta: se serve, l'elenco
  può respirare 40 px in più.

---

## Verifiche puntuali richieste — esito

| # | Controllo | Esito |
|---|---|---|
| 1 | Recensioni verbatim, nessuna parola riscritta | **OK** su 5/5, confronto parola per parola con `recensioni-reali.md` |
| 1b | Tagli segnati con `…` | **NO** su Katarzyna → bloccante 2 |
| 1c | Riga «traduzione di Airbnb» dove il testo è tradotto | **OK** — presente su Paweł (S1), Attila (C4), Katarzyna (F2) e sui tre tradotti nel testo FB; correttamente **assente** su Aline, che è in italiano |
| 1d | Niente nome casa, indirizzo, foto, avatar, logo/interfaccia Airbnb, finti screenshot | **OK** su tutti e 23 i PNG. Zero fotografie nel pacchetto; le stelle sono fuori dalla card, in oro su fumè; «Airbnb» compare solo come parola |
| 2 | Nessun punteggio aggregato, n. recensioni, punteggi per categoria | **OK** — nessuna occorrenza in 23 HTML e 23 PNG. S2 elenca le sei voci **senza** valori |
| 3 | Cornell solo in C3 e nel testo FB, con caveat | **OK come collocazione** (assente da reel, storie, F1-F3, C1-C2-C4-C5) · **NON OK come leggibilità** → bloccante 3 |
| 4 | Anello 5 solo come «è il posizionamento a filtrare chi prenota» | **OK** — presente solo in C4 (penultima riga, non in chiusura) e nel §4 del post. Nessun nesso causale, nessun numero, assente da reel e storie |
| 5 | Portali come meccanismo dichiarato, mai algoritmo conosciuto | **OK** — nessun «algoritmo» a schermo, nessuna promessa di posizione, e nel post c'è la riga di protezione «nessuno può prometterti una posizione». Unica riserva sulla parafrasi Booking → bloccante 5 |
| 6 | Superhost solo come riga d'appoggio in formato largo | **OK** — due sole occorrenze (C5 riga 29 dell'HTML, coda del post), mai gancio, nessun confronto con la media, assente da reel e storie |
| 7 | Nessuna struttura nominata, nessun risultato Hadrianus quantificato | **OK** — l'unico numero riferito a noi è la commissione 15%, che è l'offerta |
| 8 | Lessico | **OK** — «Guadagniamo solo se guadagni tu» nella forma corretta in C5, F3 e R11; «standard alberghiero» ovunque; zero occorrenze di «hotel-style» |
| 9 | Marcatori `[DATO DA VERIFICARE]` residui | **OK** — nessuno nei deliverable; compaiono solo nel brief, nell'elenco di ciò che è stato **escluso** |
| 10 | Marchi di terzi nelle immagini | **OK** — nessuna foto, nessun logo, nessuna interfaccia ricostruita |
| 11 | Completezza pacchetto | **OK** — brief, copy e direzione artistica condividono angolo, target e catena; 23/23 artboard presenti in HTML e PNG |

---

## Coerenza col tono Hadrianus

**In linea, e su un punto meglio del solito.**

`riferimenti/riferimento-2.md` chiude con «Non si tratta di fortuna, ma di un metodo alberghiero
applicato agli affitti brevi»: qui la stessa idea diventa «Non è fortuna. È lavoro fatto tutti i giorni»
(S1, F2, R09-R10) — più corta, più parlata, stesso pensiero. L'apertura del post («Hai il punteggio alto.
E in banca non è cambiato niente.») è la voce che i riferimenti usano quando parlano al proprietario:
frase breve, dolore nominato, zero preamboli.

Un merito che vale la pena registrare: il riferimento-2 è l'esempio del tono **giusto** con il contenuto
**sbagliato** — nomina la struttura e sciorina ADR e valutazione media. Questo pacchetto fa lo stesso
discorso (prova sociale, metodo, non-fortuna) **senza** nominare niente e senza un solo numero nostro.
È il riferimento ripulito dalla trappola che contiene.

Unica cosa che si discosta: «Nell'hotellerie questo legame è misurato da anni» (C3, e nel post) è la
frase più da addetto ai lavori del pacchetto. Il brief la vuole così, ed è difendibile — ma su C3 arriva
**dopo** il `+11%`, e da sola non basta a contestualizzarlo. Se applichi il bloccante 3, il caveat
leggibile fa quel lavoro e la frase torna a essere un tocco di autorevolezza invece che l'unico argine.
