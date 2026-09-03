# REGOLE — copia integrale e verbatim

Questo file contiene due parti:

- **Parte A**: copia integrale, verbatim, del contenuto di `CLAUDE.md` così com'è nel repository — è la "memoria fissa" scritta che ogni agente legge a ogni avvio.
- **Parte B**: istruzioni date dall'utente **a voce nella chat**, mai trascritte integralmente in un file, riportate qui parola per parola (in italiano, con eventuali refusi originali dell'utente lasciati intatti) insieme al contesto di quando sono state date.

Nessun testo di questo file è stato riassunto: dove è tra virgolette, è copia esatta.

---

## PARTE A — Contenuto integrale di `CLAUDE.md`

```markdown
# Hadrianus Content Engine

Questo repository è il motore di generazione contenuti di vendita di **Hadrianus**. Claude Code legge questo file a ogni avvio: contiene il contesto, le regole e il flusso di lavoro che ogni agente deve rispettare.

## Cos'è questo sistema

Un team di agenti specializzati che, dato un prodotto/servizio, un target e un canale, produce contenuti di vendita pronti alla consegna (ads, email, landing page, script) seguendo sempre lo stesso metodo, calibrato sugli esempi reali in `riferimenti/`.

Non si scrive mai copy "a braccio": prima si studia il mercato, poi si scrive seguendo il framework, poi si dà direzione grafica, infine si controlla tutto prima di consegnare.

## Struttura del progetto

```
CLAUDE.md                      → questo file, contesto globale
README.md                      → istruzioni rapide d'uso
riferimenti/                   → contenuti reali di esempio (il "tono di voce" da imitare)
campagne/                      → output tracciabile delle campagne (una cartella per campagna)
.claude/agents/
├── ricercatore-mercato.md     → studia target/angolo prima di scrivere
├── copywriter.md              → scrive i testi seguendo il metodo
├── art-director.md            → direzione grafica + grafiche editabili (Claude Design / Canva)
├── compliance-checker.md      → controllo claim, tono, refusi prima della consegna
└── revisore-marketing-design.md → revisione esperta finale (layout, grafiche, efficacia commerciale)
.claude/skills/
├── framework-vendita/         → il metodo di vendita, richiamato da ogni agente
└── nuova-campagna/            → comando che orchestra gli agenti in sequenza
```

## Flusso di lavoro standard

Per ogni nuova campagna, l'ordine è sempre lo stesso e va rispettato:

1. **`ricercatore-mercato`** — analizza prodotto, target, concorrenza e angolo di vendita. Produce un brief scritto.
2. **`copywriter`** — scrive i testi partendo dal brief, seguendo la skill `framework-vendita` e lo stile di `riferimenti/`.
3. **`art-director`** — definisce la direzione visiva coerente col copy e produce le **grafiche editabili** (canvas Claude Design, o bozze Canva se il connettore è attivo).
4. **`compliance-checker`** — controllo claim verificabili, tono coerente, refusi, formattazione.
5. **`revisore-marketing-design`** — revisione esperta finale: impaginazione, contenuti, grafiche e foto, testi ed efficacia commerciale, prima della consegna al cliente.

Il comando `/nuova-campagna` esegue questi passaggi in sequenza. Non saltare mai un passaggio, anche per contenuti "veloci": è il motivo per cui questo sistema esiste.

## Preferenze fisse di output (memoria — valgono SEMPRE)

Queste tre regole sono decise dall'utente e vanno rispettate in ogni contenuto, senza bisogno che le ripeta:

1. **Ogni grafica deve essere EDITABILE come su Canva.** Non si consegnano mai solo immagini piatte come unica opzione. L'utente deve poter, sul risultato: aggiungere elementi (es. inserire un'immagine sotto le scritte), spostarli, ingrandirli/rimpicciolirli, cambiare font, modificare il testo inline. Strumento di default: **canvas Claude Design** (skill `design`) oppure **Canva** se collegato. I PNG pronti all'upload si possono fornire in aggiunta (export), mai al posto della versione editabile.

2. **Vietato il blu navy.** La base scura del brand è un **grigio fumè caldo** — una miscela di nero, marrone e giallo (grigio-fumo, non freddo). Palette operativa definita in `campagne/<nome>/direzione-artistica.md`; il navy non va più usato in nessun contenuto.

3. **Le storie sono autoconclusive, mai a carosello.** Ogni storia, da sola, dà **problema E soluzione**: testo concentrato in poche frasi impattanti + una risoluzione efficace che mette in evidenza i punti di forza Hadrianus e la CTA. Non spezzare una storia in una sequenza/carosello di più storie. (Il formato carosello resta valido solo per i POST del feed, non per le storie.)

4. **Genera SEMPRE anche la grafica, di default.** Ogni volta che produci un contenuto (post, storia, reel, campagna, annuncio…), oltre al testo generi anche la/le **grafiche editabili** abbinate, senza che l'utente debba chiederlo. È il comportamento standard, non un'aggiunta opzionale. Le grafiche seguono tutte le regole sopra (editabili come Canva, palette fumè, ecc.).

5. **Varia il design tra un contenuto/campagna e l'altro.** Mantieni sempre l'identità di brand (palette fumè + oro, tipografia Archivo/Manrope, tono), ma **cambia layout e composizione** a ogni nuovo comando/campagna, così le grafiche non sembrano tutte uguali: varia gerarchia, disposizione dei blocchi, uso di card/bande/griglie, punti focali. Stessa identità, esecuzione sempre fresca.

6. **Post Facebook — formato fisso (SOLO Facebook).** Un post Facebook si compone sempre di **3 immagini da mostrare tutte e tre**: la 1ª **verticale allungata 1080×1920 (9:16)** (porta il gancio e il problema), la 2ª e la 3ª **quadrate 1080×1080** (soluzione e offerta/CTA). La 1ª deve essere allungata 9:16 perché nel collage di Facebook (1 grande a sinistra + 2 quadrate a destra) la cella sinistra è stretta e alta: un 4:5 verrebbe tagliato ai lati. Vale solo per i post Facebook; gli altri canali mantengono i loro formati.

## Lessico di brand (regole fisse di copy — valgono SEMPRE)

- **Formula corretta:** si scrive sempre **"guadagniamo solo se guadagni tu"**. Mai "guadagni solo se guadagni tu" (errato).
- **Vietata la parola "hotel-style"/"hotel style"**: poco professionale. Usa **"standard alberghiero"** (o "metodo alberghiero", "livello alberghiero").
- **Niente esempi su singole strutture** (es. "Rome Smart Sea") nei contenuti che devono acquisire clienti: non è un dato che porta clienti. La prova si costruisce su serietà, processo, standard alberghiero e allineamento di interessi (15%), non su un singolo case study.

## Regole non negoziabili

- **Mai inventare claim, numeri, risultati o testimonianze.** Se un dato non è verificato, va segnalato come tale (es. "[DATO DA VERIFICARE]"), mai scritto come fatto.
- **Il tono di voce si calibra sempre su `riferimenti/`**, non su preferenze generiche di stile. Se `riferimenti/` è vuoto o incompleto, chiedilo esplicitamente all'utente prima di scrivere copy definitivo.
- **Niente contenuto esce senza passare da `compliance-checker`.** Anche una singola email o un singolo post. Per una campagna completa serve poi la `revisore-marketing-design` prima della consegna al cliente.
- **Le grafiche si consegnano sempre in formato modificabile** (canvas Claude Design o Canva), mai come immagini piatte non editabili.
- **Ogni campagna produce output tracciabile**: salvare brief, copy, direzione artistica e checklist di compliance in `campagne/<nome-campagna>/` (la cartella viene creata al bisogno).
- Se mancano informazioni essenziali (chi è il target, qual è l'offerta, quali claim sono verificati) **fermarsi e chiederle**, non presumerle.

## Come aggiungere/aggiornare i riferimenti

`riferimenti/` deve contenere contenuti reali già scritti (o performanti) da Hadrianus: sono l'unico modo per gli agenti di imparare il vero tono di voce, non un'imitazione generica di "buon copywriting". Vedi `riferimenti/README.md` per il formato.

## Note tecniche

- Gli agenti in `.claude/agents/` sono richiamabili singolarmente (per interventi mirati, es. "usa compliance-checker su questo testo") oppure in sequenza tramite `/nuova-campagna`.
- La skill `framework-vendita` è il "manuale del metodo": è un punto di partenza strutturato, va raffinata via via che si aggiungono riferimenti reali e si osserva cosa funziona meglio per Hadrianus.
- L'integrazione Canva (agente `art-director`) è opzionale: se il connettore Canva non è collegato, l'agente produce comunque un brief visivo testuale dettagliato invece delle bozze grafiche.
```

*(fine copia integrale di `CLAUDE.md`)*

---

## PARTE B — Istruzioni date a voce in chat (mai trascritte integralmente in un file prima d'ora)

Riportate nell'ordine in cui sono state date. Ogni citazione è testo esatto scritto dall'utente nella chat, refusi originali inclusi.

### B.1 — Richiesta iniziale di generare il sistema (contesto: primo messaggio operativo)

> "genera questo team
>
> hadrianus-content-engine/
> ├── CLAUDE.md                    → contesto che Claude Code legge a ogni avvio
> ├── README.md                    → istruzioni rapide
> ├── riferimenti/                 → i tuoi 3 contenuti, come esempio per gli agenti
> ├── .claude/agents/
> │   ├── ricercatore-mercato.md   → studia il nuovo target/angolo prima di scrivere
> │   ├── copywriter.md            → scrive i testi seguendo il tuo metodo
> │   ├── compliance-checker.md    → controllo finale prima della consegna
> │   └── art-director.md          → direzione grafica (+ Canva, se collegato)
> └── .claude/skills/
>     ├── framework-vendita/       → il tuo metodo, richiamato da ogni agente
>     └── nuova-campagna/          → il comando che li fa lavorare in sequenza"

Nota: questa è la struttura *richiesta*; nella realizzazione è stato aggiunto un quinto agente (`revisore-marketing-design`) non presente in questo elenco iniziale, per soddisfare una richiesta successiva (vedi B.2).

### B.2 — Richiesta di generare una campagna completa con revisione esperta (contesto: secondo messaggio operativo)

> "ok ora prova a generare una campagna completa di gestione case vacanza per trovare nuovi proprietari immobiliari che ci affidano il loro immobile, con 5 storie 2 post e 1 real
> genera anche tutti i contenuti grafici che siano modificabili.
> inoltre analizza tutta la truttura e migliora e aggiorna cio che e' da migliorare e una volta generato il prodotto finale fallo analizzare da un esperto in marketing e design che controlla impaginazione, contenuti, grafiche e foto, testi ed efficacia commerciale"

Questa istruzione, non scritta altrove verbatim, è l'origine diretta dell'agente `revisore-marketing-design` e della richiesta di "analizzare e migliorare la struttura" (che ha portato ad aggiungere `campagne/README.md` e lo step grafiche+revisione in `/nuova-campagna`).

### B.3 — Feedback sulla prima campagna e correzione richiesta

> "No voglio che mi crei una campagna con tutte le storie caroselli/post ecc pronti da essere caricati su Instagram"

Questa istruzione (breve, ma decisiva) ha fatto passare il sistema da "brief/copy testuali + grafiche editabili in canvas" a "anche export PNG pronti alle dimensioni esatte del canale", con l'introduzione della pipeline Playwright (`build-and-render.mjs`).

### B.4 — Le tre regole fisse su editabilità, palette e formato storie (contesto: dopo aver visto il primo kit grafico)

> "Sì, mettiti nella tua memoria che tutte le volte che mi generi qualcosa deve essere editabile, perciò io posso aggiungerci un'immagine per esempio sotto le scritte, l'aspetta possa ingrandirla, rimpicciolirla, cambiargli il font, come se fosse su Canva normale. Ok? Ogni immagine che tu mi generi deve essere che questa opzione. Inoltre voglio che togli completamente dalla tua memoria il colore blu navi e metti un grigio, tipo un miscuglio tra nero, marrone e giallo. perciò un grigio tipo quasi fumè diciamo. al posto del Bluenavit. Li generami appunto tutti questi contenuti e più inoltre le storie non voglio che me le fai a Carosello, voglio che mi fai una storia impattante che direttamente nella stessa storia dà il problema e dà la risposta. Cioè chi era il problema è dalla risposta diciamo invece che farlo come carosello in varie storie. Solo nella singola storia tutto il testo concentrato in un paio di frasi impattanti e una risoluzione efficace facendo capire quelli che sono i nostri punti di forza.mettiti questi input nella memoria fissa"

Questa istruzione è la fonte diretta delle regole 1, 2, 3 di CLAUDE.md §"Preferenze fisse di output" (Parte A sopra). Testo trascritto esattamente, incluso il refuso "Bluenavit" per "blu navy".

### B.5 — Richiesta del post Facebook per gruppi locali (contesto: prompt strutturato da "senior copywriter")

> "Ruolo: Agisci come un Senior Copywriter e Stratega di Local Marketing, specializzato in campagne social ad altissima conversione e passaparola virale.
> Obiettivo: Scrivere un post Facebook strategico da pubblicare all'interno di gruppi locali molto popolari. Lo scopo è acquisire nuovi clienti, trasmettere assoluta affidabilità e innescare un forte passaparola tra i membri del gruppo.
> Contesto e Stile: Per scrivere questo post, utilizza tutto il contesto, il tono di voce e lo stile comunicativo del mio brand che hai già elaborato e memorizzato finora.
> Istruzioni per la stesura del post: Costruisci il copy seguendo questa esatta struttura persuasiva:
>
> 1. Gancio Commerciale (Hook) Estremo: Inizia con una frase "pattern interrupt" che fermi immediatamente lo scroll. Deve essere un gancio irresistibile, magari legato a un'offerta forte, a una garanzia unica o alla risoluzione del problema numero uno del nostro target locale.
> 2. Costruzione della Fiducia (Trust): Subito dopo il gancio, spiega perché siamo la scelta più sicura. Usa parole che trasmettano autorità, trasparenza e tranquillità. Chi legge deve pensare: "Finalmente qualcuno di serio e competente di cui potersi fidare nella nostra zona".
> 3. Call to Action (CTA) Primaria: Dì chiaramente cosa devono fare per approfittare dell'opportunità (es. scriverci in privato, cliccare un link, commentare "INFO"). Rendilo semplice e privo di ostacoli.
> 4. Micro-viralità (Il Passaparola): Inserisci una CTA secondaria naturale ma potente, spingendo le persone a taggare chi ne ha bisogno (es. "Conosci qualcuno che sta cercando di risolvere [problema] o che avrebbe proprio bisogno di questo? Taggalo nei commenti, ti ringrazierà!").
>
> Regole di Formattazione e Tono:
>
> * Evita l'effetto "spam aziendale": il tono deve essere quello di un annuncio di estremo valore fatto per la community del gruppo.
> * Usa paragrafi brevi (1-2 frasi massimo) e spazi bianchi per facilitare la lettura da smartphone.
> * Usa le emoji in modo strategico per guidare l'occhio verso i punti chiave e le Call to Action.
>
> Output richiesto: Generami 3 varianti diverse di questo post (con 3 ganci iniziali di natura diversa: uno più incentrato sul problema, uno sull'offerta/opportunità e uno più emotivo), così posso testare quale funziona meglio. Indica dove devo inserire i nomi delle zone o i link con delle parentesi quadre (es. [Nome Città/Quartiere])."

Questo è il brief strutturale usato per la prima versione del post Facebook (poi corretto, vedi B.7). La struttura Hook→Trust→CTA→Micro-viralità NON è stata scritta come regola in CLAUDE.md: vive solo qui e nei file `post-facebook-gruppi-locali.md` delle campagne, che la applicano ma non la ripetono in questi termini.

### B.6 — Comando fisso su grafica sempre generata e variazione del design

> "Sì devi sempre generare anche le grafiche mettito in meroria come comando principale e devono essere sempre modificabili ,con tutti icriteri che avevamo impostato , cerca di non farle sempre tutte uguali a cambiare il design leggermente da comano che ti do a comano di campagne nuove"

Fonte diretta delle regole 4 e 5 di CLAUDE.md §"Preferenze fisse di output" (Parte A). Testo trascritto esattamente, refusi originali inclusi ("mettito in meroria", "icriteri", "comano").

### B.7 — Correzione del formato Facebook (con screenshot) e correzioni di lessico

Contesto: l'utente ha inviato uno screenshot di Facebook con la prima immagine del post (formato 4:5) evidenziata in rosso, tagliata ai lati nel collage.

> "Stavo caricando quello che il post all'interno del gruppo e come vedi la prima immagine che mi hai creato, la f b uno in formato non va bene, perché sì l'hai fatta in formato verticale, però come vedi mi serve che sia più allungata perché così viene tagliata. Perciò io te l'ho cerchiata in rosso e ti ho mandato uno screenshot di come si vede. Vorrei che elabora appunto lo screenshot che ti ho inviato, capisci la dimensione dell'immagine, mi rigeneri soltanto f b uno, però di del formato corretto appunto."

Poi, nello stesso scambio, correzioni di merito sul copy e sul lessico:

> "non va. Allora non va solo ovviamente bene questo post. Il gancio è praticamente inutile. Oltre a questo, hai fatto soltanto un'immagine, invece in questi post è meglio spiegare almeno in tre immagini, da farle vedere tutte e tre. La prima va bene così allungata in verticale, le altre due è meglio farle quadrate. Detto questo, mettitelo in memoria per i post Facebook, ok? E questo sarò parlando del formato delle immagini nella quantità di immagini che devi generare. Detto questo fai una ricerca online, quelle che possono essere campagne per prendere clienti di property manager, perciò per la captazione di proprietà immobiliari che magari lasciano l'appartamento scritto o lo affittano a lungo termine, a lungo tempo o gestiscono loro l'immobile ma senza grandi risultati con le case vacanze. perciò andare umanari a fare una piccola lista iniziale come di impatto, come chiamata, comunque le possono essere problemi reali che hanno loro in queste in queste fasi. Poi, guadagni solo se guadagni tu è completamente errato, perché dovrebbe essere riformulato con guadagniamo solo se guadagni tu. E poi hotel style, non mi piace, è poco professionale con la parola style, perciò magari è meglio standard alberghiero e non fare esempi su singole strutture come rome smart sea non essendo tanto non e' un dato che ci porta clienti."

Fonte diretta di: (a) la regola 6 di CLAUDE.md (formato Facebook a 3 immagini, prima verticale 9:16); (b) le tre regole di CLAUDE.md §"Lessico di brand" (formula "guadagniamo solo se guadagni tu", divieto di "hotel-style", divieto di citare singole strutture); (c) la richiesta di fare una ricerca online sui pain point dei proprietari immobiliari (da cui è nato `ricerca-pain-points-proprietari.md`).

### B.8 — Richiesta della seconda campagna (angolo fiducia)

> "generami una nuova camoagna per instagram con 3 storie nuove e 2 post a carosello con ganci e grafiche differenti che puntano a creare confidenza e prendere nuovi clienti"

Fonte diretta della Campagna 2 (`campagne/instagram-fiducia-proprietari/`): 3 storie + 2 caroselli, esplicitamente con ganci e grafiche "differenti" (applicazione concreta della regola 5) e con l'obiettivo esplicito "creare confidenza" (da cui il nome della campagna e l'angolo scelto, distinto dal rischio/morosità della Campagna 1).

### B.9 — Richiesta dell'handover (questo pacchetto)

> "Prepara un pacchetto di handover completo di questo progetto per un revisore esterno che non ha accesso a questa chat."

con le specifiche sui 6 file richiesti (STATO.md, DECISIONI.md, REGOLE.md, SKILLS.md, INVENTARIO.md, APERTI.md) e la richiesta di comprimere il workspace in uno zip scaricabile — istruzioni eseguite direttamente, non richiedono ulteriore trascrizione qui essendo questo stesso pacchetto la risposta.
