# Revisione marketing & design — Giornaliero 14/09/2026 v2 · "Ti hanno scattato le foto col telefono"

**Materiale visto:** `copy-v2-foto.md`; le 12 artboard in `png/` guardate una per una a dimensione telefono (`Main`, `K2`-`K5`, `FB1`-`FB3`, `S1`-`S4`); le foto sorgente in `grafiche/` (`salone-telefono.jpg`, `salone-pro.jpg`, `salotto-caldo-banda.jpg`, `c-openspace.jpg`, `c-salotto.jpg`); `grafiche/build_v2.py` e `grafiche/build.py`; `reel/build_reel.py` e `reel/reel.html`; `checklist-compliance-v2.md`; `PUBBLICAZIONE.md`; `riferimenti/riferimento-1.md`; `.claude/reference/design-system.md` §"Pattern già usati".

**Limite dichiarato:** `reel/reel-foto-col-telefono.mp4` non è ispezionabile fotogramma per fotogramma in questo ambiente (nessuno strumento di estrazione frame disponibile). Il giudizio sul reel è costruito sul sorgente che lo genera — `build_reel.py` è deterministico e ricalcolabile a mano istante per istante — più le due foto che il reel monta a pieno schermo. Dove il giudizio dipende da un pixel che non posso vedere, lo dico esplicitamente e lo marco **[DA GUARDARE PRIMA DELLE 18:00]**.

---

## Giudizio complessivo

**PRONTA CON RITOCCHI** — l'angolo è giusto, il registro è giusto, il copy è il migliore delle ultime giornate e la coppia prima/dopo è il miglior asset visivo che il brand abbia prodotto finora. Ma quella coppia si vede **solo nel reel**: il carosello e il post Facebook promettono un confronto e mostrano metà confronto, e tre superfici su dieci illustrano la lezione sulla luce con una foto che quella lezione la sbaglia. Sono ritocchi chirurgici — tre sostituzioni di file, quattro valori di coordinata, cinque stringhe — non un ripensamento. Fatti quelli, è il pacchetto più forte del mese.

**Le tre bocciature del titolare sono rispettate.** L'angolo non è la burocrazia (la parola non compare in nessuna superficie v2). Il registro è commerciale e assertivo dove deve esserlo. La frase *"La responsabilità resta tua. Il lavoro no."* **non rientra da nessuna parte nel pacchetto v2** — verificato con ricerca su tutta la cartella: compare solo in `copy.md`, `brief-mercato.md`, `grafiche/build.py` e nella revisione v1, tutti file del pacchetto bocciato. Su questo punto però c'è una mina, vedi intervento 8.

---

## Punteggio per dimensione

| Dimensione | Giudizio | Nota chiave |
|---|---|---|
| Impaginazione/layout | ⚠️ | `K5`, `FB2`, `FB3` e `S4` sono impaginazione vera e pulita. Ma la firma della giornata — "la tendina" — su 6 artboard non firma niente: è una linea sbiadita con un anello oro che galleggia in mezzo a una parola. E nel reel il testo cade su foto non velate e il chip `SIMULAZIONE` finisce dove Instagram mette la caption |
| Contenuti/struttura | ⚠️ | I quattro pezzi sull'angolo foto (reel, carosello, 3 immagini FB) sono un sistema vero, ben diviso, senza sovrapposizioni. `S1` e `S2` però aprono e chiudono la giornata parlando la lingua che il titolare ha bocciato |
| Grafiche/foto | ❌ | Il "dopo" (`salone-pro.jpg`) è bellissimo e **non compare in nessuna delle 10 artboard come termine di paragone**. In compenso la foto con la piantana accesa — l'errore esatto della slide `01 · LA LUCE` — è il fondo di `S3`, l'inserto di `K3` e le scene 7-8 del reel, cioè proprio quelle che dicono "ti garantiamo il servizio fotografico". Tre sostituzioni di file, non un ridisegno |
| Testi | 👍 | Angolo, registro, lessico, CTA, chiusure: tutto in ordine e in voce. Quattro righe possono diventare più assertive senza spostare di un millimetro il perimetro dei claim (intervento 6) |
| Efficacia commerciale | ⚠️ | L'offerta è chiara e il rischio è abbassato bene (15% sul fatturato, bonifico netto, guadagniamo solo se guadagni tu). Restano due frizioni: la prova visiva manca proprio sulle superfici che vendono, e nessuna grafica dice cosa succede **dopo** che scrivi CALCOLO |

---

## Interventi prioritari (in ordine di impatto commerciale)

### 1 · Metti il "dopo" sulla copertina del carosello — `png/Main.png` · prima delle 12:30

**Dov'è il problema.** `build_v2.py` riga 180: `Main` monta `k-tel-45.jpg` a pieno formato. Tutta la slide è la foto rovinata. La tendina a x 216 non scopre niente, perché a sinistra e a destra della linea c'è la stessa identica foto: l'anello oro finisce sopra la "T" di "Ti hanno" e si legge come un difetto di stampa, non come una firma.

**Perché sposta l'ago.** La slide 1 di un carosello decide se le altre quattro vengono viste. Oggi la copertina dà solo il problema, in un'immagine marrone e scura che a dimensione feed legge come "foto d'atmosfera", non come "foto sbagliata". Il confronto — che è l'unica cosa che nessun concorrente sta facendo — resta chiuso dentro il reel, che esce sei ore dopo.

**Cosa fare.** Il file ti serve, esiste già: `grafiche/k-pro-45.jpg`. Monta `Main` a due metà con la tendina come taglio reale — a sinistra `k-pro-45.jpg`, a destra `k-tel-45.jpg` con il velo `rgba(26,23,19,.26)` in più, chip `SIMULAZIONE` sulla metà destra (dov'è già). La linea oro a x 540, non a 216: deve stare dove il taglio ha senso, e il passo 216→432→648→864 delle slide interne resta com'è. È esattamente ciò che il copy descrive alle righe 52 e 198-199: l'artboard non l'ha mai eseguito.

*Se non si vuole toccare la composizione:* allora togli la tendina da `Main` e dichiaralo nel copy. Una linea che non taglia niente è peggio che nessuna linea.

---

### 2 · Fai vedere che `FB3` è la foto bella — `png/FB3.png` · prima delle 15:00

**Dov'è il problema.** `build_v2.py` righe 308-310. `FB3` monta `salone-pro.jpg` (giusto, la correzione di compliance B2 è applicata) ma sotto un velo da `rgba(26,23,19,0.82)` al centro e `rgba(46,42,37,0.92)` in alto / `0.94` in basso. Risultato: il "dopo" esce **scuro quanto il "prima"**. Ho messo `FB1` e `FB3` uno accanto all'altro a dimensione telefono: sono due rettangoli marroni della stessa densità.

**Perché sposta l'ago.** La caption del post dice *"Nelle immagini qui sopra c'è la stessa stanza, due volte: nella prima e nell'ultima."* Se il lettore non vede la differenza, la frase si ritorce: davanti a proprietari competenti e diffidenti — che è esattamente il pubblico dei gruppi Facebook — una prova che non si vede vale meno di nessuna prova. Compliance aveva bloccato questo punto (B2) e la correzione ha spostato il problema dalla caption alla resa: il "dopo" adesso c'è ma non si legge.

**Cosa fare.** Abbassa il velo di `FB3` e basta: radiale `0.82 → 0.55`, lineare `0.92 → 0.70` in alto e `0.70 → 0.34` a metà. Il testo è tutto Archivo grassetto con `text-shadow` già attivo (`ombra=True` su ogni blocco), regge senza problemi. Se il titolo oro perde contrasto sulla parete chiara, alza l'ombra invece del velo. La stanza deve leggersi **pulita, dritta e luminosa**: è la dimostrazione della frase che le sta sopra.

---

### 3 · Togli la foto con la piantana accesa dalle superfici che insegnano la luce — `K3`, `S3`, reel scene 7-8

**Dov'è il problema.** `salotto-caldo-banda.jpg` / `k-banda-caldo.jpg` / `salotto-caldo-9x16.jpg` sono la stessa scena: divano in pelle cuoio, piantana accesa che spara un alone giallo sulla parete, parete di sinistra grigia e fredda. È **letteralmente** "metà gialla e metà grigia" — la foto che la slide `01 · LA LUCE` insegna a non fare. E sta:
- in `K3`, **una slide dopo** la lezione (`build_v2.py` riga 218);
- come fondo di `S3` (riga 331);
- nel reel, scene 7-8 (`build_reel.py` righe 231 e 241), cioè sotto le parole **"Ti garantiamo il servizio fotografico"** e **"Dentro la gestione. Non lo paghi a parte."**

**Perché sposta l'ago.** È l'unico errore del pacchetto che un proprietario esperto può usare per liquidarti in un commento, e lo farà sotto il post Facebook. Il giorno in cui il brand dichiara "le foto le facciamo noi", la foto che accompagna la promessa non può contenere l'errore che il brand ha appena spiegato. Compliance l'aveva già segnalato (O5) come non bloccante: commercialmente non è un'osservazione, è la credibilità dell'intero angolo.

**Cosa fare** (i file sono già nella cartella, nessuno scatto nuovo):
- **reel scene 7-8** → `c-openspace.jpg`: open space chiaro, neutro, verticali dritte, nessun marchio visibile. È la foto che dimostra lo standard mentre lo si promette. *Verifica solo che nel crop 9:16 il frigorifero non mostri il marchio.*
- **`K3` (l'ordine)** → `c-openspace.jpg` o un crop di `salone-pro.jpg` diverso da quello di `K2`: serve una superficie **in ordine**, non un divano con un quadro sopra. Oggi l'inserto di `K3` non illustra l'ordine, illustra un salotto.
- **`S3`** → un fondo neutro qualsiasi (`c-salotto.jpg` va benissimo). Oggi il fondo di `S3` è la foto più "sbagliata" delle dodici, ed è la prima cosa che esce alle 11:00.

---

### 4 · Il reel: anticipa la tendina e libera il testo — `reel/build_reel.py` · prima delle 18:00

**Il reel regge, e la tendina è un pagamento vero.** Questo va detto per primo, perché è il pezzo migliore della giornata. La meccanica funziona davvero: `.banda` è montata **sopra** `.velo`, quindi le due foto vanno a schermo a piena luminosità, e a 5,4 s la linea oro attraversa il fotogramma in 1,2 s scoprendo `salone-pro.jpg` con un `clip-path: inset(0 100% 0 0) → inset(0)`. Il salto dal marrone storto e sfocato al beige dritto e nitido è netto e fisico. Non è un effetto decorativo: è il momento in cui l'argomento si dimostra da solo, senza una parola. **Questa è la firma da tenere.**

Quattro cose la indeboliscono, tutte risolvibili con numeri:

**a) Il pagamento arriva tardi.** Tre scene su una sola immagine ferma prima della tendina: 0→4,8 s, il 31% del reel. Il "movimento" delle scene 1-3 è tremolio ±6 px e push-in — a dimensione telefono si legge come un'immagine quasi ferma. La scena 3 in particolare è dichiarata nel copy come *"una colonna di riquadri fotografici scorre verticalmente veloce e si ferma di colpo"*: nel build (`kf('scatto')`, righe 198-200) non c'è nessuna colonna, c'è la **stessa foto** che fa un sobbalzo di 12 px fra 3,2 e 3,82 s. Sono 1,6 secondi in cui non succede niente, piazzati esattamente prima del climax.
→ **Comprimi**: fondi la scena 2 e la 3 in una sola da 1,6 s (*"È la prima cosa che vede chi cerca. E decide lì."* sta su due righe) e porta `TENDINA_IN` da 5,4 a **3,4 s**. Il reel resta 15,6 s e i due secondi guadagnati vanno alle scene 7-8, che oggi sono le più compresse e sono quelle che vendono. In alternativa, se la colonna di provini si riesce a montare davvero, la scena 3 si giustifica: ma allora deve muoversi come dichiarato.

**b) Il testo bianco cade su foto chiare.** `.testo` è a `top: 1360px` e `.velo` sta sotto `.banda` nel DOM, quindi non arriva mai sullo schermo: il velo dichiarato nel copy (riga 91) non protegge niente. Nelle scene 5-6 le righe *"Stessa stanza. / Altro annuncio."* e *"Cambia solo / chi tiene la macchina."* cadono sul terzo inferiore di `salone-pro.jpg`, che è **tappeto crema e divano panna**. Bianco su crema, tenuto in piedi solo da un `text-shadow`: si legge, ma si legge male, ed è il tipo di dettaglio che fa sembrare fatto in casa un reel che per il resto non lo è.
→ Aggiungi uno scrim **sopra** `.banda` e sotto `.testo`: `linear-gradient(180deg, transparent 52%, rgba(26,23,19,.78) 100%)`. Due righe di CSS, zero impatto sul resto.

**c) Il chip `SIMULAZIONE` è dove Instagram mette la caption.** `chip_y=1500` (riga 158): il chip vive a y 1500-1556 su 1920. Nelle artboard statiche lo stesso chip sta in alto (y 200 su `Main`, y 260 su `FB1`), che è la scelta giusta. Nel reel è in basso a destra, cioè nella fascia che Instagram occupa con nome utente, caption e audio. Il chip non è un vezzo grafico: è il vincolo di onestà che regge tutto l'angolo. Se l'interfaccia lo copre, la dichiarazione sparisce proprio nel pezzo che girerà di più.
→ Portalo a **`chip_y = 260`**, allineato a `FB1`. Costo zero, e guadagni anche aria nel terzo inferiore.

**d) Il finale è a filo di collisione. [DA GUARDARE PRIMA DELLE 18:00]** Il logo mascherato (`.logo`, righe 148-150) ha il centro a y 832 e la maschera sfuma a zero intorno a y 998; il blocco testo del finale parte a `top: 1000px`. Sono **2 px di margine**. Compliance aveva segnalato (O9) che è lo stesso accoppiamento che nella v1 aveva prodotto il testo sopra la scritta del logo. Non posso verificarlo sul montato: guarda il fotogramma a 14,5 s, e in ogni caso porta il testo da `top: 1000` a **`top: 1060`** — il finale respira e la CTA a 1290 resta dov'è.

**Il finale converte?** Sì, la struttura è quella giusta: offerta → riga oro del lessico → pill CTA che sale da sotto, 2 secondi pieni, e il loop riparte pulito sulla foto storta. Manca una cosa sola, vedi intervento 7.

---

### 5 · Riallinea la giornata: `S1` e `S2` parlano ancora la lingua bocciata — `PUBBLICAZIONE.md`

**Dov'è il problema.** Alle 09:00 esce `S1` (*"Il CIN nell'annuncio è quello giusto?"*) e alle 21:30 `S2` (*"L'ospite entra alle 23:40"*). Sono la prima e l'ultima cosa che il profilo dice oggi, e sono **burocrazia pura**: CIN, verifica dell'annuncio, comunicazione entro 24 ore, imposta di soggiorno. Compliance l'aveva registrato come non bloccante (O11). Commercialmente è il punto in cui la giornata si contraddice: il titolare ha bocciato un pacchetto intero perché *"la burocrazia non è un gancio"*, e la giornata si apre e si chiude su quel gancio.

**C'è di peggio, ed è il motivo per cui questo intervento sta così in alto.** `S2` contiene, in corpo: *"E l'imposta di soggiorno la versi tu, anche se l'ospite non la paga."* (`grafiche/build.py` righe 492-493). È una **nota di demerito**: dice al proprietario che il peso resta suo, e la storia non lo risolve — la riga di chiusura *"Da noi succede mentre dormi. È già dentro la gestione."* si riferisce alla comunicazione delle generalità, non al versamento dell'imposta. Non è la frase bandita alla lettera, ma è la stessa meccanica, e oggi esce alle 21:30 come ultimo messaggio del giorno. Il criterio del titolare — *"è sempre merito dell'impresa"* — qui non è rispettato.

**Cosa fare, in ordine di preferenza:**
1. **Togli `S1` e `S2` dal palinsesto di oggi** e parcheggiale. Sono due artboard buone, riusabili in una giornata a pilastro "adempimenti" dove il gancio è dichiarato. Poi ricomponi: 09:00 → `S3`, 12:30 carosello, 15:00 Facebook, 18:00 reel, 20:00 → `S4`.
2. Se devono uscire per riempire il palinsesto, **almeno non in apertura e chiusura**: spostale a 13:30 e 16:30, e fai aprire la giornata alle 09:00 con **il fotogramma della tendina a 6,6 s esportato come storia**. Costo: un export. Effetto: la giornata si apre sull'immagine più forte che hai, e chi la vede alle 09:00 arriva preparato al carosello delle 12:30. È il pezzo che oggi manca al funnel.
3. In ogni caso, **riscrivi la riga dell'imposta di soggiorno di `S2`** perché chiuda sul valore e non sul peso.

---

### 6 · Alza quattro righe che sono rimaste tiepide (il registro è giusto, non ovunque)

Il registro commerciale è applicato bene e senza sbandare: *ti garantiamo*, *ti assicuriamo*, *con noi la tua casa*, *ci pensiamo noi* stanno sempre su ciò che Hadrianus esegue, mai sul risultato di mercato. Su questo non c'è niente da ammorbidire e niente da segnalare. Ma in quattro punti la frase scivola nell'impersonale o nell'amministrativo, e sono quattro punti che contano. Nessuna di queste modifiche tocca il perimetro dei claim: sono tutte già confermate.

| Dove | Oggi | Proposta | Perché |
|---|---|---|---|
| `K5`, riga di garanzia (`build_v2.py` r. 255) | "Con noi non le scatti tu. / Il servizio fotografico è incluso." | **"Le foto te le facciamo noi. / Non le paghi a parte."** | "è incluso" è la lingua di un listino. La slide che chiude il carosello deve dire chi fa la cosa e togliere di mezzo l'obiezione sul prezzo. Oggi *"Non lo paghi a parte"* sta solo in caption, cioè fuori dall'immagine che viene salvata |
| `FB3`, titolo (r. 313) | "Il servizio fotografico / è incluso." | **"Il servizio fotografico / te lo garantiamo noi."** | Stesso motivo, e usa il verbo che il titolare ha confermato il 14/09. Due righe, stesso corpo 62, stessa scatola |
| `S3`, riga di garanzia (r. 336) | "Con noi le tariffe si muovono / data per data. Ci pensiamo noi." | **"Le tariffe le muoviamo noi, / data per data. Ci pensiamo noi."** | Le tariffe non si muovono da sole. Voce attiva, soggetto Hadrianus. **Non riapre B1**: resta solo sulle tariffe, il minimo notti non viene nominato |
| `S4`, gancio (r. 338) | "Check-in / dalle 15 alle 19." | **"L'aereo atterra alle 23. / Tu ricevi fino alle 19."** (è già il Gancio B del copy, r. 714-715) | Oggi il gancio è un'etichetta, non un conflitto. La variante B mette in collisione due orari nella stessa frase: è quella che ferma il pollice. Il Gancio A può scendere nel corpo |

Due righe **tipografiche**, non di registro: su `Main` e `FB1` il titolo va a capo in tre righe con l'orfana *"le foto"* al centro, che lascia un buco a destra e spezza la lettura. Portalo a due: **"Ti hanno scattato / le foto col telefono."** Stesso corpo 70, una riga in meno, blocco più compatto e più aggressivo.

---

### 7 · Dì cosa succede dopo la CTA

Tutte le grafiche portano la stessa pill: **"Scrivi CALCOLO in DM"**. È la CTA giusta, unica, concreta, ed è il miglioramento più grosso rispetto alle giornate passate (nella revisione v1 il DM generico era il rilievo principale). Ma **nessuna artboard dice cosa arriva in risposta.** "Simulazione gratuita" vive solo nelle caption, cioè nel punto in cui il lettore arriva se si è già convinto.

Il proprietario target sta valutando se scrivere a un'azienda che non conosce. Il passo intermedio che gli abbassa il rischio — *ti mando un numero, gratis, senza impegno* — è già confermato e già scritto in `riferimenti/riferimento-1.md`. Portalo in grafica:

- **`S3` e `S4`**: una riga Manrope 500 da 24 px sotto la pill, y 1590 — dentro la safe area dichiarata (nulla di leggibile sotto y 1600): *"Simulazione gratuita, senza impegno."*
- **Reel, fotogramma finale**: stessa riga a y 1460, sotto la `.banda-cta` che finisce a 1406. Lì lo spazio è libero (il `.filo` a 1500 è già sparito a 13,6 s).
- **`K5` e `FB3`**: non c'è aria sotto la pill senza rompere il margine inferiore di 64 px. Mettila **sopra**, al posto di niente, o lasciale come sono: hanno la caption vicina.

**Nota di coerenza da sistemare a costo zero:** `PUBBLICAZIONE.md` chiude le caption con *"Scrivi CALCOLO in DM e ti diciamo quanto può rendere la tua casa"*, il copy con *"per una simulazione gratuita"*. Scegline una. La seconda è la formula dei `riferimenti/` ed è quella che abbassa di più il rischio percepito: "simulazione" dice che non stai chiamando un venditore.

---

### 8 · Chiudi la cartella prima di consegnarla (rischio operativo, non creativo)

Tre cose che non si vedono nelle grafiche ma che possono far uscire il pezzo sbagliato:

1. **Due reel nella stessa cartella.** `reel/reel.mp4` è quello **bocciato** della v1 e ha il nome più corto e più ovvio; `reel/reel-foto-col-telefono.mp4` è quello buono. Alle 18:00, di fretta, si prende il primo. Sposta i file v1 in `_bocciato/` o rinominali `v1-BOCCIATO-*`. Vale anche per `copy.md`, `checklist-compliance.md`, `brief-mercato.md`, `direzione-artistica.md`, `revisione-marketing-design.md`, `grafiche/build.py`.
2. **`reel/scene.txt` è la lista di montaggio della v1** e comincia con `file 'png/Main.png'` — che oggi è la slide 1 del carosello nuovo. Chi lo rieseguisse otterrebbe un ibrido fra i due pacchetti. Va cancellato o spostato con gli altri file v1.
3. **`brief-mercato.md` istruisce a usare la frase bandita.** Riga 78: *"la cosa onesta che nessun competitor ha il coraggio di dire: la responsabilità resta tua, il lavoro no. Quella frase è il territorio libero."* E `grafiche/build.py` riga 363 la stampa in un artboard. Oggi non esce niente di tutto questo — ma è il documento da cui un domani si riparte, e `direzione-artistica.md` descrive ancora la firma "marca temporale + arco" di un pacchetto che non esiste più. Metti in testa a entrambi i file una riga sola: **"PACCHETTO BOCCIATO DAL TITOLARE 14/09/2026 — angolo burocrazia e frase 'la responsabilità resta tua, il lavoro no' vietati. Non riusare."** Poi scrivi la nota d'angolo v2 e la direzione artistica v2 ("la tendina che attraversa"), come chiede compliance in O10: senza, la cartella di oggi non è tracciabile.

---

### 9 · Ritocchi minori, tutti da 30 secondi

- **La "maniglia" dentro le pill CTA** di `K5` e `FB3` (`build_v2.py` r. 114-116, `maniglia=True`): è un anello scuro a sinistra dentro il bottone oro. A dimensione telefono non si legge come la fine della tendina, si legge come un elemento rotto o un pallino di elenco rimasto lì. Toglila: `maniglia=False`. Sono le due superfici che convertono, non possono avere un dettaglio che sembra un errore.
- **`K2` e `K4` usano lo stesso identico inserto** `k-banda-pro.jpg` (r. 205 e 232). Scorrendo il carosello si vede due volte lo stesso divano a due slide di distanza, e sembra un copia-incolla. Cambia crop almeno su uno dei due.
- **I due fili oro di `K4` cadono sul divano e sul plaid** (r. 154: `fx` fissi a 238 e 714, su una foto che non ha né stipiti né infissi). La slide che spiega le verticali sta dimostrando il contrario di quello che dice — compliance l'aveva segnalato (O4) e non è stato applicato. **Soluzione pulita già in cartella:** usa `c-salotto.jpg` come inserto — parete a doghe verticali, perfettamente dritte, colore neutro. I fili oro cadono su vere verticali e la slide dimostra se stessa. È il singolo ritocco con il miglior rapporto fatica/effetto di tutto l'elenco.
- **`S3` e `S4`, gancio e corpo si toccano.** `build_v2.py` r. 351-352: gancio ancorato a y 640 (2 righe da 70 px → occupa 560-720), corpo ancorato a y 810 (3 righe da 40 px → occupa 731-889). Restano **11 px** fra i due blocchi: a schermo titolo e testo sembrano un unico paragrafo e la gerarchia si appiattisce. Porta il corpo a **y 850**. Sotto c'è aria (il kicker è a 955), non si tocca nient'altro.
- **La linea verticale di `FB2`** (r. 289-290) attraversa in mezzo tutte e quattro le righe di testo su fondo sabbia, senza maniglia e senza scoprire niente: su superficie chiara si legge come una piega o un difetto di stampa. `FB2` è l'immagine pensata per essere salvata e rimandata. Toglila da qui: la tendina si giustifica dove c'è un confronto, e in `FB2` non c'è.
- **`FB2` promette una stanza che non mostra.** Il titolo è *"Stessa stanza. Quattro differenze."* su un artboard tipografico senza nessuna stanza. Dopo lo spostamento del "dopo" su `FB3`, questo titolo è rimasto orfano. Cambialo in qualcosa che stia in piedi da solo — *"Quattro cose cambiano la foto."* — perché nel collage Facebook `FB2` può essere aperta singolarmente.
- **Nota sulla simulazione, parola giusta.** Su `Main` e `FB1` la nota dice *"una foto reale rovinata apposta da noi"*. In `PUBBLICAZIONE.md` la risposta pronta ai commenti dice già *"è una foto comprata da Adobe Stock"*. Portalo nel testo pubblicato: **"una foto d'archivio rovinata apposta da noi"**. Toglie in partenza il sospetto che sia la casa di qualcuno, che è la prima domanda che arriverà. Compliance lo suggeriva in O8.
- **Caption del carosello:** la correzione B6 è stata applicata **in grafica** (la nota sotto il sottotitolo di `Main`) invece che in caption. Va benissimo così, anzi è più visibile. Aggiungila comunque in caption in `PUBBLICAZIONE.md`: costa una riga e copre il caso in cui l'immagine venga riproposta senza contesto.

---

## Le correzioni di compliance: verificate

| # | Rilievo | Stato |
|---|---|---|
| B1 | `S3`, claim non verificato sul minimo notti | ✅ **Applicato in grafica.** `png/S3.png` porta *"Con noi le tariffe si muovono data per data. Ci pensiamo noi."* Il minimo notti non è più affermato. ⚠️ `copy-v2-foto.md` riga 646 porta ancora la vecchia formulazione: allinea il documento |
| B2 | Caption FB che dichiarava un confronto assente | ✅ **Applicato**, con la strada (b): `FB3` monta ora `salone-pro.jpg` e la caption dice *"nella prima e nell'ultima"*. Il confronto però non si **vede** — vedi intervento 2 |
| B3 | Fonte del "prima" documentata come immobile in gestione | ⚠️ **Applicato a metà.** Riga 26 e claim 3 del riepilogo (r. 792) sono corretti e chiusi: Adobe Stock, `grafiche/stock-salone.jpg`. Ma le righe 113, 203, 254, 302, 349 e 470 indicano ancora `brand-assets/immobili/...` come sorgente. Il rischio che compliance voleva eliminare — che qualcuno rigeneri degradando la casa vera di un cliente — è ancora scritto nero su bianco in sei punti del documento da cui si riparte. Da chiudere |
| B4 | Marcatori `[DATO DA VERIFICARE]` aperti | ⚠️ **Parziale.** I claim 3 e 5 sono chiusi. I claim 1 (chi scatta le foto, r. 434 e 790), 2 (minimo notti, r. 791) e 4 (nessun costo fisso, r. 793) sono ancora aperti nel file. Nessuno di loro tocca una superficie pubblicata — la regola di `CLAUDE.md` chiede però che siano chiusi **per iscritto** prima della consegna |
| B5 | `FB2`, etichette tagliate ("UCE", "RDINE") | ✅ **Risolto.** `kicker(..., left=86)` alla riga 301, filo a `left: 64`. Nel PNG si leggono LUCE, ORDINE, INQUADRATURA, SEQUENZA per intero |
| B6 | Carosello senza dichiarazione di simulazione in chiaro | ✅ **Risolto in grafica** (nota sotto il sottotitolo di `Main`), più il chip. Meglio della correzione proposta. Vedi il minore in intervento 9 |
| O2 | "finestra aperta" → "tende" | ✅ Corretto su `K2` (*"Spegni le lampade. Scosta le tende."*) e nella caption FB. Resta *"la finestra aperta"* in `PUBBLICAZIONE.md` r. 53, ma lì descrive il degrado, non dà un consiglio: non blocca |
| O3 | `K4`, "sembra più piccola" | ✅ Corretto: la riga oro dice *"La stanza sembra grande quanto è."* La tabella CLAIM del copy (r. 361) porta ancora la vecchia frase: allinea |
| O4 | `K4`, fili oro fuori bersaglio | ❌ **Non applicato.** Vedi intervento 9 |
| O5 | `K3`, inserto con dominante arancione | ❌ **Non applicato.** Vedi intervento 3 |
| O6 | Divergenze copy ↔ artboard | ❌ **Non applicate**, e se ne sono aggiunte: le y di `Main` (770/980/1130/1245 nel render contro 640-900/940-1020/1100-1180 nella tabella), la posizione del testo del reel (`top: 1360` contro y 860-1060 dichiarate), il chip del reel (1500 contro 1500-1556 ma in una griglia diversa). Il copy è il documento da cui si rigenera: allinealo dopo i ritocchi, non prima |
| O7 | `S4`, identificazione fuori dalla riga oro | ❌ Non applicato, ma il vincolo è rispettato (la condizione sta nel consiglio, in chiaro). Non blocca |

**Niente di quanto propongo qui riapre un claim bloccato.** Le formulazioni dell'intervento 6 restano dentro il perimetro confermato dal titolare il 14/09; l'intervento 3 sostituisce foto, non affermazioni; l'intervento 7 usa "simulazione gratuita", che è già nelle caption approvate.

---

## Cosa funziona già bene (da non toccare)

- **L'angolo.** *"Ti hanno scattato le foto col telefono"* è un gancio vero: è specifico, è accusatorio senza essere offensivo, riguarda una cosa che il proprietario ha fatto davvero e che può correggere oggi. E soprattutto non parla di rogne, parla di **quello che fa cliccare l'annuncio** — che è esattamente la correzione chiesta dal titolare. Questo angolo va messo in `INDEX.md` come territorio del brand e ripreso.
- **La coppia `salone-telefono.jpg` / `salone-pro.jpg`.** Il degrado è fatto bene: storta, sottoesposta, virata gialla, tagliata male, con la sfocatura da mosso — e resta riconoscibilmente la stessa stanza, quindi *"Stessa stanza"* è letteralmente vero. Il "dopo" è una foto che qualunque proprietario vorrebbe avere del proprio salotto. È il miglior asset visivo del brand: va usato **tre volte di più** di quanto lo si stia usando oggi.
- **La tendina, nel reel.** Come movimento di rivelazione funziona: è un taglio che scopre, non una transizione decorativa. Tienila come firma dei reel. Nelle artboard statiche, invece, o taglia davvero il fotogramma (intervento 1) o va tolta.
- **Il carosello come contenuto da salvare.** Quattro consigli veri, corretti nel merito, utili anche a chi non diventerà mai cliente, dati **prima** di chiedere qualcosa. *"Valgono anche se fai da solo — salvale e usale al prossimo scatto"* è il tono adulto dei `riferimenti/`: nessun paternalismo, nessuna pressione. È il pezzo che merita di essere salvato e rimandato, ed è il motivo per cui il carosello merita il ritocco della copertina invece del cestino.
- **`K5` e `FB3` come superfici di conversione.** Gerarchia impeccabile: kicker → titolo → elenco → filo oro → garanzia → offerta → lessico → pill a piena larghezza. L'occhio scende dritto fino alla CTA senza un'esitazione, e la pill oro su fumè è visibile a colpo d'occhio anche in miniatura. Questa struttura è uno standard: riusala.
- **`K3` come respiro.** Una sola superficie chiara a metà carosello, ed è quella giusta (la 3 su 5). Il ritmo scuro-scuro-chiaro-scuro-scuro funziona allo scorrimento.
- **Il registro assertivo, come è stato interpretato.** *Ti garantiamo / ti assicuriamo / con noi la tua casa / ci pensiamo noi* stanno sempre su ciò che Hadrianus **esegue** — il servizio fotografico, la gestione, il check-in H24 — e mai sul risultato di mercato. Nessuna prenotazione promessa, nessuna percentuale, nessun "sempre pieno". È la linea esatta fra commerciale e millantato, e il pacchetto la tiene in tutti e dieci i pezzi. Questo è il modo giusto di applicare l'istruzione del titolare.
- **La chiusura di brand.** *15% sul fatturato generato · Guadagniamo solo se guadagni tu · Scrivi CALCOLO in DM* riprodotta alla lettera da `riferimento-1.md` in tutte le caption e su tutte le superfici di chiusura. È il punto in cui il pacchetto suona più di casa.
- **La divisione del lavoro fra i pezzi.** Il reel mostra il confronto e non spiega le leve; il carosello spiega le leve e non rifà il confronto; Facebook riassume per la community; le storie portano due errori che nessun altro pezzo tocca. Nessuna sovrapposizione, nessuna ripetizione. Questo è un sistema, non quattro contenuti messi in fila.

---

## Suggerimenti opzionali (nice-to-have)

- **La storia di apertura dal fotogramma della tendina.** Già detto nell'intervento 5: esporta il frame a 6,6 s (metà sinistra pro, metà destra degradata, linea oro a metà) e mandala alle 09:00. Costo zero, ed è l'unica cosa che manca al funnel di oggi — un'apertura che prepara il carosello.
- **Il carosello ha un quinto consiglio già scritto e non usato:** *"tieni il telefono in orizzontale"* sta dentro `K4` come quarta riga, schiacciata in fondo a un blocco. È il consiglio più immediato e più facile da applicare di tutti e quattro. In una storia da sola, con un'icona di un telefono che ruota, vale da sé.
- **La griglia del profilo.** `Main` è 1080×1350: nella griglia Instagram viene ritagliata e la pill *"Scorri →"* a y 1205-1285 sparisce. Non è un problema nel feed, ma se la copertina del carosello deve funzionare anche sul profilo, il gancio va tenuto sopra y 1150.
- **Una risposta pronta in più** in `PUBBLICAZIONE.md`: *"E se ho già delle belle foto?"* → *"Meglio: le usiamo e le rimettiamo in sequenza. Il servizio fotografico resta incluso, non lo paghi comunque a parte."* È l'obiezione del proprietario più competente, cioè proprio quello che vuoi.
- **`FB2` è la superficie più "agenzia" del pacchetto** (titolo + elenco a quattro voci + banda). Compliance l'aveva notato. Funziona, ma se deve reggere da sola nel collage, una riga dal registro dei `riferimenti/` la riporta dentro la voce del brand — del tipo *"È il 15% che paghi, per il 100% di stress che non paghi più."* Opzionale, non urgente.

---

## Cosa tenere come standard per i giorni successivi

1. **Un angolo si sceglie su cosa fa guadagnare il proprietario, non su cosa gli fa paura.** La differenza fra il pacchetto bocciato e questo è tutta qui, e si sente in ogni riga. Quando un angolo comincia con un adempimento, fermarsi e cercare la versione che comincia con una decisione del cliente finale.
2. **Ogni chiusura è merito dell'impresa.** Nessun contenuto finisce sul peso che resta al proprietario, in nessuna forma e in nessuna posizione — nemmeno a metà corpo, come in `S2`. Se una frase descrive una responsabilità che resta sua, o la risolve la riga dopo o non entra.
3. **Assertivo su ciò che eseguiamo, muto su ciò che non dipende da noi.** *Ti garantiamo il servizio fotografico* sì; *ti garantiamo più prenotazioni* mai. È la regola che ha retto tutti e dieci i pezzi di oggi e va copiata così com'è nei prossimi.
4. **Voce attiva, soggetto Hadrianus.** "Le foto te le facciamo noi" batte "il servizio fotografico è incluso" a parità assoluta di claim. Quando una frase descrive un servizio senza nominare chi lo fa, riscriverla.
5. **Se il contenuto insegna una regola, le immagini di quel contenuto devono rispettarla.** Vale oltre la fotografia: il giorno in cui si parla di ordine, non si pubblica un tavolo ingombro. È il controllo che è mancato oggi ed è quello che costa di più in credibilità.
6. **Il confronto prima/dopo è un formato del brand, non di questa giornata.** Ha una meccanica riusabile (stesso file sorgente, degrado dichiarato, chip `SIMULAZIONE`, tendina che scopre) e un vincolo di onestà già scritto. Riusare la meccanica su: annuncio scritto male / scritto bene, calendario fermo / calendario mosso, casa riassettata da un proprietario / in standard alberghiero.
7. **Mai degradare la foto di un immobile in gestione.** Il "prima" viene sempre da archivio licenziato. Il vincolo è chiuso e vale per sempre: va scritto nella direzione artistica di ogni giornata che usi un confronto, non solo qui.
8. **CTA sempre "Scrivi CALCOLO in DM", mai "Scrivi in DM"**, su tutte le superfici della stessa giornata, storie comprese. E accanto alla pill, sempre, cosa arriva in risposta: *simulazione gratuita, senza impegno*.
9. **I sei controlli di qualità si fanno sul PNG a dimensione telefono, prima di mostrare qualcosa** (preferenza fissa 9). Oggi ci sono arrivate fino alla revisione finale: una parola tagliata su `FB2`, un anello oro sopra un titolo, due fili oro su un divano, un velo che annulla la foto che doveva dimostrare la promessa. Sono tutti difetti che si vedono in tre secondi guardando l'immagine — nessuno si vede leggendo la specifica.
10. **La specifica è il documento da cui si rigenera: va allineata al render, sempre.** Due giornate di fila hanno prodotto un copy che descrive artboard diverse da quelle consegnate. Il giorno in cui qualcuno ripartirà dal copy, ricostruirà il pacchetto sbagliato.
11. **Un pacchetto bocciato si archivia, non si lascia accanto a quello buono.** Nomi distinti, cartella `_bocciato/`, e una riga in testa ai documenti che dica cosa è vietato riusare.

---

**Prossimo passo:** interventi 1, 2, 3 e 5 **prima delle rispettive fasce orarie**; l'intervento 4 **prima delle 18:00**, con il controllo a occhio sul fotogramma finale. Gli interventi 6, 7 e 9 si fanno nello stesso giro di riesportazione. L'intervento 8 prima di chiudere la cartella. Dopo i ritocchi, riesportare `png/Main.png`, `K3`, `K4`, `K5`, `FB2`, `FB3`, `S3`, `S4` e il reel, e allineare `copy-v2-foto.md` e `PUBBLICAZIONE.md`.
