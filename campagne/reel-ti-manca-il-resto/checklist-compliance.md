# Checklist compliance — reel "Ti manca il resto" (15 s)

Verifica del 9 settembre 2026 su `copy.md`, `direzione-artistica.md`, `montaggio.md`, `README.md`, i nove
artboard in `grafiche/` (`Main`, `S2`…`S9`) e `reel/copertina.jpg`. Confronto con
`.claude/reference/brand-identity.md`, `.claude/reference/lessico-brand.md`, `riferimenti/riferimento-1.md` e
`-2.md`, le tabelle claim di `campagne/facebook-lungo-vs-breve-proprietari/copy.md` (righe 108-138) e la
verifica del primo reel della serie (`campagne/reel-cosa-cerca-un-proprietario/checklist-compliance.md`).

## Esito

> **AGGIORNAMENTO — correzioni applicate il 9 settembre 2026.** Tutti e tre i rilievi sono stati chiusi con le
> sostituzioni consigliate: scena 4 → *"Il prezzo che segue la domanda."*, scena 5 → *"Il check-in, a qualsiasi
> ora."* (scelta l'opzione 2: la conferma scritta del titolare sulla messaggistica H24 non c'è, ed è ora
> segnata come [DA VERIFICARE] nella tabella claim), scena 7 → *"Il controllo, a ogni check-out."*
> Rigenerati `S4`, `S5`, `S7`, il canvas online e i secondi 5,4-11,0 del video.
>
> Chiuse anche le due verifiche lasciate aperte: **marchi di terzi** — guardati i fotogrammi dell'MP4 a 5,6 ·
> 6,4 · 7,0 · 7,6 · 8,0 s, né il tostapane né la macchina a capsule entrano in inquadratura, e la nota di
> `direzione-artistica.md` è stata estesa alle scene 4 e 5; **barra di avanzamento** — il sospetto era fondato,
> la barra era piena dal primo fotogramma perché ffmpeg valuta l'espressione di `drawbox` una volta sola. Ora il
> riempimento è dentro i nove PNG del velo e avanza a scatti, uno per scena. Copertina riestratta a 3,5 s.
> **Il testo qui sotto è la verifica originale, lasciata com'era.**

**DA CORREGGERE — blocca.** Due bloccanti pieni (scena 7 e scena 4) e uno che si chiude con una risposta scritta
del titolare (scena 5). Tutti e tre stanno nella lista centrale, tutti e tre nella stessa categoria di errore già
bloccata nel reel precedente: **una battuta che descrive un risultato invece di un lavoro, dentro una lista che
la scena 8 (*"Il resto lo facciamo noi."*) trasforma in promessa di servizio.**

Il resto passa, e passa bene: lessico di brand alla lettera, nessun numero inventato, nessun
`[DATO DA VERIFICARE]` residuo, nessuna testimonianza, nessuna struttura nominata, nessun superlativo, nessun
confronto con concorrenti, caption interamente dentro il perimetro confermato dal titolare, seconda persona
coerente, zero refusi negli artboard.

**L'MP4 è già esportato**: le correzioni toccano i secondi **4,0-11,0**, quindi vanno rifatti `S4`, `S7`
(e `S5` se non arriva la conferma), il canvas online e il rimontaggio di quel tratto.
`reel/copertina.jpg` **non** è interessata (è la scena 1-2).
La riga 16 di `campagne/INDEX.md` è già 🟡 *"In verifica compliance"*: **va lasciata 🟡** finché le correzioni non
sono applicate.

## Bloccanti (da correggere prima della consegna)

### 1. "Le recensioni che reggono tutto." — è l'unico elemento della lista che non è un lavoro, ed è un risultato che Hadrianus non può erogare

**Dove:** `grafiche/S7.dc.html` riga 25 · `copy.md` righe 38 (tabella), 56 (voce fuori campo), 69-70 (caption),
90 (tabella claim).

Le altre quattro voci sono servizi dichiarati in `.claude/reference/brand-identity.md` riga 13 (ottimizzazione
annuncio, pricing dinamico, gestione ospiti/check-in H24, pulizie) e nel perimetro confermato dal titolare
(`facebook-lungo-vs-breve-proprietari/copy.md` claim 7 e nota 111 su pulizie e biancheria). **Le recensioni no.**
Le recensioni le scrivono gli ospiti: sono l'*effetto* del lavoro, non una delle sue componenti. Tre conseguenze:

- **La difesa scritta in `copy.md` riga 90 non regge.** Dice *"descrive il peso delle recensioni nel meccanismo,
  non un risultato ottenuto"*. Sarebbe vero in un contenuto descrittivo; qui, 1,4 secondi dopo, la scena 8 dice
  *"Il resto lo facciamo noi."* — cioè prende in carico esattamente le cinque voci appena elencate. Da quel
  momento la battuta promette che ce ne occupiamo noi. È **la stessa identica meccanica** già bloccata nel reel
  precedente (`reel-cosa-cerca-un-proprietario/checklist-compliance.md`, bloccante 2: la difesa *"non è un claim,
  è il desiderio del proprietario"* cadeva davanti a *"Questo è il nostro lavoro."*). Secondo contenuto della
  serie, stesso errore, stessa posizione nella struttura: qui va chiuso alla radice.
- **"Reggono tutto" implica recensioni positive.** Non c'è modo di leggere la frase come neutra: nel contesto di
  vendita significa "recensioni buone, che tengono su l'annuncio". È una promessa di risultato su una variabile
  che dipende dagli ospiti — la categoria che `lessico-brand.md` riga 14 vieta senza appello.
- **"Le recensioni le facciamo noi" è la frase peggiore che un gestore di affitti brevi possa dire.** Anche solo
  come implicatura, sposta il contenuto su un terreno (recensioni prodotte/gestite dal professionista) su cui
  nessuno vuole essere frainteso in un commento pubblico. Il rischio non vale la battuta.

Nota di coerenza interna: `copy.md` riga 17-18 descrive la lista come *"i cinque pezzi che gli mancano — e sono
tutti pezzi di **lavoro**"*. La quinta voce smentisce la definizione che il documento stesso dà della lista.

**Sostituzione consigliata** (è il lavoro che *produce* le recensioni, ed è confermato dal titolare alla lettera —
`facebook-lungo-vs-breve-proprietari/copy.md` claim 7: *"Casa in ordine e controllata a ogni check-out secondo lo
standard alberghiero — CONFERMATO DAL CLIENTE"*; stessa forma nominale delle scene 4-6, due righe corte, regge il
corpo 72 px senza toccare il layout):

> `Il controllo,<br>a ogni check-out.`

**Alternativa** se si vuole tenere il lessico di brand esplicito (verificare la prima riga a 72 px: 24 caratteri
sono al limite dei 960 px utili, semmai scendere a 62 px):

> `Lo standard alberghiero,<br>a ogni check-out.`

**Da NON usare** come ripiego: qualsiasi variante che mantenga "recensioni" come oggetto del "lo facciamo noi"
(*"Le recensioni, curate una per una"*, *"Le recensioni che tengono"*): il problema non è l'avverbio, è il
soggetto.

**Caption, `copy.md` righe 69-70** — sostituire l'ultima voce dell'elenco:
> ~~E le recensioni, che reggono tutto il resto.~~
> **E il controllo della casa a ogni check-out — che è poi quello che le recensioni misurano.**

(in caption la formulazione lunga è consentita e tiene la parola "recensioni" in funzione descrittiva, non
promissoria.)

### 2. "Il prezzo giusto, ogni giorno." — due claim in quattro parole, e nessuno dei due è quello confermato

**Dove:** `grafiche/S4.dc.html` riga 25 · `copy.md` righe 35, 53, 87.

Il servizio confermato è **"pricing dinamico"** (`brand-identity.md` riga 13; `riferimenti/riferimento-1.md`
riga 12, parole del cliente). La battuta a schermo dice altre due cose che nessuno ha confermato:

- **"giusto"** è un giudizio di esito, non una descrizione di attività: afferma che il prezzo applicato *è quello
  corretto*. `copy.md` riga 87 lo glossa come *"adeguato alla domanda, non il più alto"* — ma quella glossa sta
  nel documento interno, non a schermo, e nessuno spettatore legge "giusto" come "adeguato alla domanda".
- **"ogni giorno"** è una frequenza operativa: dichiara un riprezzamento quotidiano. Non è scritto da nessuna
  parte, in nessun `riferimenti/` e in nessuna tabella claim. È un assoluto della stessa famiglia di *"sempre"* e
  *"mai"*, entrambi bloccati nel reel precedente e già in precedenza in
  `facebook-lungo-vs-breve-proprietari/checklist-compliance.md`.

Elemento che rende la correzione facile: **la caption ha già la versione difendibile.** `copy.md` riga 68 scrive
*"Il prezzo che cambia con la domanda invece di restare fermo"* — esatta, verificabile, e descrive il servizio
confermato. È il testo a schermo che è andato oltre, non il ragionamento.

**Sostituzione consigliata** (allinea lo schermo alla caption; due righe corte, stesso ritmo della lista):

> `Il prezzo che<br>segue la domanda.`

**Alternativa:** `Il prezzo,<br>mai fermo.` — **no**: reintroduce un assoluto. Se serve una seconda opzione:
`Il prezzo<br>che cambia con la domanda.` (seconda riga lunga, verificare a 72 px).

**Da allineare:** `copy.md` riga 35 (tabella struttura), riga 53 (voce fuori campo), riga 87 (tabella claim, che
oggi certifica come "servizio dichiarato" una formulazione che il servizio dichiarato non copre).

### 3. "Le risposte, a qualsiasi ora." — si chiude con un sì scritto del titolare, oppure si cambia

**Dove:** `grafiche/S5.dc.html` riga 25 · `copy.md` righe 36, 54, 68-69 (caption), 88.

È il più leggero dei tre, ma non è a posto. Quello che il cliente dichiara con parole sue è **"check-in smart
H24"** (`riferimenti/riferimento-1.md` riga 12) e **"gestione ospiti"** (`brand-identity.md` riga 13). Da lì a
*"le risposte, a qualsiasi ora"* c'è un passo: la disponibilità H24 sul **check-in** diventa disponibilità H24
sulla **messaggistica**. Può essere vero — non è scritto da nessuna parte, ed è il terzo assoluto del reel.

**Due modi di chiuderlo, uno basta:**

1. **Conferma scritta del titolare** su una domanda sola: *"rispondiamo ai messaggi degli ospiti a qualsiasi ora,
   o l'H24 riguarda il check-in?"*. Se la risposta è la prima, la battuta resta com'è e questa riga si chiude
   (aggiungere la conferma alla tabella claim di `copy.md` con la data, non lasciarla in chat).
2. **Sostituzione**, che resta dentro la formula già pubblicata dal cliente e tiene identico il beat ritmico
   ("a qualsiasi ora" è la parte che fa la battuta):

> `Il check-in,<br>a qualsiasi ora.`

Se si sceglie la 2, allineare anche la caption riga 68-69 (*"Le risposte agli ospiti a qualsiasi ora"* →
*"Il check-in degli ospiti a qualsiasi ora"*) e le righe 36, 54, 88.

### File da rigenerare dopo le correzioni

`grafiche/S4.dc.html`, `grafiche/S7.dc.html` (+ `S5.dc.html` se non arriva la conferma), `grafiche/canvas.json`,
il canvas online (link in `README.md` riga 16, `copy.md` riga 9, `direzione-artistica.md` riga 3),
`reel/reel-ti-manca-il-resto.mp4` limitatamente ai **secondi 4,0-11,0**, e le occorrenze in `copy.md`
(tabella struttura righe 35-38, voce fuori campo righe 53-56, caption righe 68-70, tabella claim righe 87-90).
Attenzione a non alterare la barra oro: la sua corsa è calcolata sul tempo assoluto (`322*min((t+offset)/15,1)`),
quindi il rimontaggio del tratto centrale deve conservare gli stessi `offset` per scena.
`reel/copertina.jpg` **non** va rifatta.

## Verifiche che non ho potuto chiudere da qui (nessun accesso ai fotogrammi dell'MP4)

**Marchi di terzi — la documentazione dice il vero, ma è incompleta su una scena.** Verificato che
`brand-assets/immobili/smart-tv-streaming-mockup.jpg` (loghi Netflix / Prime Video / Disney+, nota di compliance
in `brand-assets/README.md` righe 29-35) **non è tra le fonti**: le otto sorgenti elencate in
`direzione-artistica.md` righe 41-48 sono altre, e la nota alle righe 56-60 la dichiara correttamente
inutilizzabile in qualsiasi ritaglio. Anche il cambio della scena 8 è documentato correttamente: la scena non usa
più l'open space ma `salotto-divano-azzurro.jpg` (ritaglio tenda), coerente con la riga 47 della tabella fonti.

**Quello che la documentazione non dice**: il tostapane e la macchina a capsule non sono spariti dalla campagna,
sono ancora **nella foto sorgente della scena 4** (`cucina-soggiorno-open-space.png`, ritaglio "zona pranzo") e
nel video della **scena 5** (`brand-assets/video/clean/interno-cucina.mp4`, stesso interno ingrandito del 50%).
Ho guardato la foto sorgente: i due apparecchi stanno nel terzo destro dell'inquadratura, quindi un ritaglio 9:16
centrato sul tavolo li esclude quasi certamente — ma "quasi certamente" non è una verifica, e in questo ambiente
non posso estrarre fotogrammi dall'MP4.

Da fare prima della consegna, sul video esportato, non sugli artboard:
1. guardare i secondi **5,4-8,2** a schermo intero e confermare che nessuno dei due apparecchi (né altri marchi
   leggibili) entri nell'inquadratura;
2. scrivere l'esito in `direzione-artistica.md`, estendendo la nota delle righe 56-60 anche alle scene 4 e 5 —
   oggi certifica solo la scena 8, e chi rileggerà il file fra un mese crederà che il tema sia chiuso.
   È lo stesso punto lasciato aperto dalla verifica del primo reel (osservazione "Marchi di terzi", righe
   135-143): se resta aperto due volte di fila, alla terza nessuno lo controllerà più.

**Barra di avanzamento nella copertina.** In `reel/copertina.jpg` il filo sotto "HADRIANUS" appare **oro per
tutta la sua lunghezza**, mentre la copertina è il fotogramma del gancio completo (~2,6-4,0 s), dove il
riempimento dovrebbe essere circa un terzo del binario (`S2.dc.html` riga 23: 86 px su 322). Può essere un effetto
del binario bianco al 28% letto sopra un cielo arancione — o può essere una copertina renderizzata con la barra al
100%. Da controllare a occhio ingrandendo l'immagine: se è piena, la copertina dice "il video è finito" nel
fotogramma che deve fermare lo scroll, e va riestratta dall'MP4 a ~3,5 s. Non è un problema di conformità, è un
difetto di qualità sull'unico fotogramma che tutti vedono.

## Osservazioni (non bloccanti, ma da considerare)

**Il gancio "Per guadagnare di più non ti serve un'altra casa" è difendibile — ma è difendibile *perché* la lista
è tutta di lavoro.** Verdetto sul punto su cui è stato chiesto il giudizio più severo: **non implica un
rendimento**, e per tre ragioni. (a) Non contiene numeri, percentuali né orizzonti temporali: `lessico-brand.md`
riga 14 vieta il rendimento "garantito" e prescrive *"una simulazione gratuita" / "quanto potrebbe rendere"* — e
la caption chiude esattamente così (riga 79). (b) La frase è costruita come **negazione di una spesa** ("non ti
serve comprare"), non come affermazione di un guadagno: il complemento "per guadagnare di più" è il fine che il
proprietario già ha, non un esito promesso da Hadrianus. (c) È lo stesso movimento di `riferimento-1.md` riga 14
(*"Vuoi scoprire quanto potrebbe rendere davvero il tuo appartamento?"*): potenziale, mai quantificato.

Con una condizione, però, che vale la pena scrivere qui perché è il punto fragile: **il gancio regge solo finché
tutto ciò che segue è lavoro e non risultato.** Ogni voce della lista che promette un esito (le recensioni,
il prezzo "giusto") retroagisce sul gancio e lo trasforma in *"con noi guadagni di più"*. È la seconda ragione,
indipendente dalla prima, per cui i bloccanti 1 e 2 vanno chiusi. E per lo stesso motivo: se un domani a questo
reel si affianca una cifra (in caption, in un commento, in una risposta in DM), scatta la regola vincolante di
`facebook-lungo-vs-breve-proprietari/copy.md` riga 111 — *"media, non una promessa: ogni casa fa storia a sé"* —
che qui oggi non serve solo perché di cifre non ce n'è nessuna.

**"15% solo sulle prenotazioni che generiamo" e "Nessun costo fisso": confermati, nessuna azione.**

| Dato | Dove è confermato |
|---|---|
| 15% solo sulle prenotazioni che generiamo | `facebook-lungo-vs-breve-proprietari/copy.md` claim 8 (*CONFERMATO DAL CLIENTE, formula esatta obbligatoria*) e claim 4; `riferimenti/riferimento-1.md` riga 13; `brand-identity.md` riga 11 |
| Nessun costo fisso | idem, claim 8 (*"senza costi fissi"*) e claim 4 (*"nessun canone fisso"*) |
| Nessun deposito cauzionale (caption) | claim 4, introdotto da direttiva del titolare |
| Pagamento il 10 di ogni mese (caption) | claim 6, *confermato come prassi effettiva*, e non presentato come esclusiva |
| Simulazione gratuita (caption) | formula prescritta da `lessico-brand.md` riga 14 |

Due precisazioni che **non** richiedono modifiche ma che è bene restino a verbale. (1) *"Nessun costo fisso"*
occupa da sola tutta la scena 9 a 70 px: è la formula confermata alla lettera e arriva 2 secondi dopo il 15%,
quindi il perimetro (è la **nostra** struttura di compenso) si legge. Resta però vietato, qui come altrove,
allargarla a *"nessun altro costo" / "tutto incluso" / "l'unica spesa"*: TARI, oneri condominiali e utenze
restano del proprietario (regola vincolante, `facebook-lungo-vs-breve-proprietari/copy.md` righe 114-118). Il
reel non la viola: la nomina soltanto insieme al 15%. (2) *"Le pulizie e la biancheria"* è dentro il perimetro
(la biancheria è elencata fra le voci coperte, riga 111 dello stesso file), e la battuta dice che il servizio
esiste, non che è gratuito — il che la tiene fuori dal `[DATO DA VERIFICARE]` ancora aperto sui costi una tantum
di avvio (set biancheria iniziale, riga 112). Se un giorno quel dato si chiude in negativo, questa battuta non va
comunque toccata: va toccata solo un'eventuale formula "senza anticipi".

**Caption: "Ti serve il resto" contro "Ti manca il resto" della copertina.** `copy.md` riga 65 apre la caption con
*"Ti serve il resto."*, mentre il fotogramma che le sta accanto nel feed — e il titolo stesso della campagna —
dicono *"Ti manca il resto."*. L'antitesi *non ti serve X / ti serve Y* è più bella, e sospetto sia voluta; ma
nel feed le due righe si leggono insieme all'immagine, e la mezza incoerenza si nota. Se non è una scelta
consapevole, allineare a **"Ti manca il resto."**; se lo è, va bene così — l'importante è che sia una decisione,
non una svista.

**`copy.md` riga 97-99 e `direzione-artistica.md` riga 53: "tutte reali, nessuna immagine generata" è impreciso.**
Tre scene su nove (5, 7, 9) sono clip video, e `brand-assets/video/README.md` riga 28 dice che le clip del busto e
l'interno **hanno movimento generato, non ripreso** (l'interno è una casa vera con animazione artificiale; il
balcone di `clean/balcone.mp4` corrisponde a un immobile reale). Nessuna conseguenza pubblica — nessuna delle tre
è presentata come "il nostro immobile", che è il vincolo posto da quel README — ma la scheda di compliance del
reel deve dire il vero, altrimenti la prossima volta ci si fida di una riga sbagliata. Riformulare in:
*"Fotografie reali; tre clip video di brand con movimento generato, usate come sfondo e mai presentate come
immobili in gestione."*

**Tabella claim di `copy.md` (righe 83-92): va riscritta insieme alle correzioni.** Le righe 87 e 90 contengono
due autocertificazioni che questa verifica smentisce (*"servizio dichiarato"* per un prezzo "giusto ogni giorno"
che il servizio dichiarato non copre; *"non un risultato ottenuto"* per le recensioni). È lo stesso rilievo mosso
al primo reel: se restano così, il prossimo che apre il file crede che quei due punti siano stati controllati e
approvati.

**Lessico di brand: pulito su tutta la riga.** *"Guadagniamo solo se guadagni tu."* è alla lettera in
`S9.dc.html` riga 25 (in oro, in chiusura — l'uso corretto secondo `campagne/INDEX.md` riga 30), in caption
(riga 77) e nella voce fuori campo (riga 58); mai la variante sbagliata *"guadagni solo se…"*. Zero occorrenze di
"hotel-style" in tutta la cartella. Nessuna struttura nominata: la campagna evita per intero il registro di
`riferimenti/riferimento-2.md` (Rome Smart Sea, ADR 183 €, Superhost), che è esattamente ciò che
`lessico-brand.md` riga 12 vieta nei contenuti di acquisizione. Nessun `[DATO DA VERIFICARE]` residuo, nessun
superlativo assoluto, nessun paragone con concorrenti nominati, nessuna testimonianza, nessun punteggio.

**Refusi, accenti, apostrofi: puliti in tutti e nove gli artboard.** Entità corrette dove servono —
`pi&ugrave;` (Main, S2), `un&rsquo;altra` (Main, S2), `L&rsquo;annuncio` (S3): apostrofo tipografico ’, mai il
dritto. Punteggiatura coerente (tutte le battute chiuse dal punto fermo), nessun doppio spazio, nessuna riga
orfana. Nei `.md` gli apostrofi sono dritti: irrilevante, non si pubblicano.

**Seconda persona singolare: coerente in tutte e nove le battute.** Scene 1-3 con il "tu" esplicito (*"non **ti**
serve"*, *"**Ti** manca"*, *"che **ti** fa trovare"*), scene 4-7 sintagmi nominali senza soggetto (compatibili),
scena 8 il passaggio a "noi" (*"lo facciamo noi"*, *"che generiamo"*), scena 9 il ritorno al "tu" nella formula di
brand. Nessun "voi", nessuna terza persona, nessun impersonale — è l'errore corretto in caption nel reel
precedente (*"Si desidera non pensarci"*) e qui non si ripresenta: la caption è in seconda persona dalla prima
riga all'ultima. Le sostituzioni proposte ai bloccanti 1-3 sono tutte sintagmi nominali e non introducono nuove
persone grammaticali.

**CTA: chiara e allineata.** *"SCRIVICI IN PRIVATO"* a schermo (S9, maiuscolo tipografico via
`text-transform`, non testo urlato nel sorgente) e *"Scrivici in privato: simulazione gratuita sul tuo immobile"*
in caption. La geografia c'è (caption riga 72: *"case vacanza a Roma e sul litorale"*) — era un'osservazione
aperta sul primo reel, qui è stata recepita.

**Completezza della campagna: coerente.** Non c'è un `brief-mercato.md`, ma la motivazione dell'angolo, il target
e il confronto con `campagne/INDEX.md` stanno in `copy.md` §"L'angolo" (righe 11-26): è la convenzione già seguita
dagli altri due reel, non una dimenticanza. Copy, direzione artistica e montaggio raccontano lo **stesso** angolo,
lo **stesso** target e le **stesse** nove scene, senza scarti; l'angolo è effettivamente nuovo rispetto ai
quattordici già registrati in `INDEX.md` righe 25-40. `montaggio.md` non promette nulla e resta operativo.

## Coerenza col tono Hadrianus

**In linea.** Il registro — frasi brevi, nessun avverbio di enfasi, nessun punto esclamativo, la lista che conta
invece di gridare — è la stessa cosa che `riferimenti/riferimento-1.md` riga 13 fa con *"È il 15% che paghi, per
il 100% di stress che non paghi più"*: si vende **la sottrazione di fatica**, non la performance. Il salto
"capitale che hai già / lavoro che manca" è il modo più economico di dire quello che il riferimento dice in
quattro righe di elenco (*"Chiamate notturne, burocrazia infinita, check-in da incastrare…"*).

Un solo punto di attenzione, ed è di sostanza più che di tono: **il reel è tutto posizionamento e zero prova**, e
lo dichiara (`copy.md` righe 94-95, che tengono fuori Superhost, recensioni, medie e occupazione). È una scelta
legittima e coerente con la serie, a patto che valga la sequenza di pubblicazione di `montaggio.md` righe 28-30:
questo reel argomenta, ma è `reel-superhost-acquisizione` a dimostrare. Se il piano cambia e questo reel gira da
solo per settimane, il proprietario freddo riceve tre volte una promessa di lavoro senza mai una prova — e il
gancio "guadagnare di più" comincia a pesare più di quanto il contenuto sostenga.

Nessuno scostamento nella caption, che nel primo reel era il punto debole: qui è in seconda persona dall'inizio
alla fine, ha la geografia, ha la formula di brand in chiusura e non contiene un solo numero fuori perimetro.
