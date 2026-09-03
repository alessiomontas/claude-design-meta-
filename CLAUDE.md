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
