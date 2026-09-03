# SKILLS — elenco, cosa fanno, quando si attivano

Due categorie diverse, da non confondere:

- **A. Skill di Claude Code usate dall'assistente in questa sessione** per produrre il lavoro (strumenti esterni al progetto, forniti dalla piattaforma).
- **B. Skill/agenti che fanno parte del progetto stesso** (`.claude/skills/`, `.claude/agents/`), cioè il prodotto consegnato, pensati per essere richiamati da chi userà questo repository con Claude Code in futuro.

---

## A. Skill di piattaforma usate in questa sessione

### `design`
**Cosa fa:** crea una canvas multi-artboard (design "Claude Design"), scritta come file `.dc.html` (uno per ogni artboard: storia, slide di carosello, post) più un `canvas.json` che ne definisce il layout sulla canvas. Il risultato viene "seedato" in un payload HTML autonomo e pubblicato come Artifact: chi lo apre può modificarlo visivamente (spostare, ridimensionare, cambiare font, editare testo inline) se il salvataggio è abilitato, altrimenti può solo vederlo ed esportare PNG/PDF.
**Quando si è attivata:** ogni volta che è stato prodotto un kit grafico per una campagna — sempre, in questa sessione, perché "genera sempre anche la grafica" è una regola fissa (vedi REGOLE.md). Usata per: il kit della Campagna 1 (10 poi 13 artboard, incluse le revisioni "hotel-style"→"standard alberghiero" e la sostituzione del case study), il kit della Campagna 2 (13 artboard).
**Meccanica concreta:** l'assistente scrive i file `.dc.html` a mano (HTML/CSS inline, palette e font del brand), poi esegue `seed-canvas.mjs` (script della skill, fuori dal repository del progetto, in `/tmp/claude-0/bundled-skills/.../design/`) per assemblare il payload, poi pubblica con lo strumento Artifact.
**Limite noto:** il file HTML "seedato" (`social-kit-*.html`, ~2.4 MB) non è versionato in git (vedi `.gitignore` e DECISIONI.md) — vive come Artifact online e viene rigenerato dai sorgenti `.dc.html` quando serve.

### `artifact-capabilities`
**Cosa fa:** restituisce l'elenco delle "capability" runtime disponibili per l'utente corrente (in particolare: la capability che abilita il salvataggio/editing collaborativo di un Artifact, e quella che abilita l'export PNG/PDF).
**Quando si è attivata:** una volta, prima della prima pubblicazione di un canvas editabile, per sapere quali `capabilities` dichiarare nella chiamata di pubblicazione (altrimenti il canvas risulterebbe sola-lettura senza che l'utente lo sappia).

### `WebSearch` (strumento, non skill in senso stretto)
**Cosa fa:** ricerca web con sintesi e fonti.
**Quando si è attivata:** due volte, su richiesta esplicita dell'utente (B.7 in REGOLE.md), per fondare su dati reali il nuovo gancio del post Facebook dopo il divieto di citare singole strutture come prova. Query usate: pain point dei proprietari di affitti brevi/gestione immobiliare (fonti in lingua inglese) e problemi reali di morosità/case sfitte in Italia (fonti in italiano). Risultato salvato in `campagne/gestione-case-vacanza-proprietari/ricerca-pain-points-proprietari.md` con le fonti citate.

### Skill NON usate ma disponibili nell'ambiente (elencate dal sistema, mai invocate)
`framework-vendita` e `nuova-campagna` (skill di **progetto**, vedi sezione B) comparivano nell'elenco delle skill disponibili ma non risultano invocate esplicitamente come comando `/` in questa sessione — il lavoro è stato guidato manualmente dall'assistente seguendo lo stesso schema concettuale. Altre skill di piattaforma elencate come disponibili (`dataviz`, `pptx`, `docx`, `pdf`, `xlsx`, `code-review`, ecc.) non sono mai state pertinenti al lavoro richiesto e non sono state usate.

---

## B. Skill/agenti del progetto (il prodotto consegnato)

Questi vivono nel repository e sono pensati per essere usati da chi continuerà il lavoro con Claude Code.

### Skill `.claude/skills/framework-vendita/SKILL.md`
**Cosa fa:** codifica il metodo di copywriting persuasivo di Hadrianus: struttura in 8 blocchi (Hook → Problema → Agitazione → Soluzione → Prova → Offerta → Urgenza → CTA), principi di scrittura, checklist di qualità.
**Quando si attiva:** va richiamata da qualunque agente scriva o valuti un testo di vendita — di fatto dagli agenti `copywriter` e `compliance-checker`. Non è mai stata eseguita come comando standalone in questa sessione; il suo contenuto è stato seguito "a memoria" dall'assistente nello scrivere i copy delle due campagne.
**Stato:** scritta come "punto di partenza strutturato... va raffinata via via che si aggiungono riferimenti reali" — non ancora raffinata oltre la sua stesura iniziale.

### Skill `.claude/skills/nuova-campagna/SKILL.md`
**Cosa fa:** dovrebbe orchestrare in sequenza i 5 agenti (ricerca → copy → art-director/grafiche → compliance → revisione) per produrre una campagna completa, salvando tutto in `campagne/<nome-campagna>/`.
**Quando si attiva:** in teoria, invocando `/nuova-campagna` con prodotto/target/canale. **Non è mai stata invocata come comando reale in questa sessione**: le due campagne sono state prodotte simulando manualmente la stessa sequenza (l'assistente ha scritto brief, copy, grafiche, compliance e revisione uno dopo l'altro, senza passare dal meccanismo di orchestrazione degli agenti). Questo è un punto aperto — vedi APERTI.md.

### Agente `.claude/agents/ricercatore-mercato.md`
**Cosa fa:** produce un brief di mercato (offerta, target, concorrenza, angoli di vendita proposti) leggendo `riferimenti/` e facendo ricerca quando utile.
**Quando si attiva:** sempre per primo in una nuova campagna. Nella pratica di questa sessione, il suo output (`brief-mercato.md`) è stato scritto direttamente dall'assistente nello stile che l'agente dovrebbe produrre, non tramite invocazione dell'agente come subagent.

### Agente `.claude/agents/copywriter.md`
**Cosa fa:** scrive i testi seguendo `framework-vendita` e il brief di mercato, calibrandosi su `riferimenti/`.
**Quando si attiva:** dopo il brief di mercato. Stesso discorso del punto precedente: eseguito concettualmente, non come subagent reale.

### Agente `.claude/agents/art-director.md`
**Cosa fa:** definisce la direzione visiva e produce le grafiche editabili (richiama la skill `design` o Canva se collegato).
**Quando si attiva:** dopo che il copy è stabile. In pratica, il suo ruolo è quello effettivamente svolto dall'assistente ogni volta che ha costruito i file `.dc.html`.

### Agente `.claude/agents/compliance-checker.md`
**Cosa fa:** controlla claim verificabili, coerenza di tono, refusi, formattazione; blocca qualunque claim non verificato.
**Quando si attiva:** sempre come penultimo step, anche per un singolo contenuto fuori da una campagna completa. Nella pratica, il suo output (`checklist-compliance.md` nella Campagna 1) è stato scritto manualmente dall'assistente; per la Campagna 2 non esiste un file di compliance dedicato — è stato dichiarato conforme solo nel corpo della chat (punto aperto, vedi APERTI.md).

### Agente `.claude/agents/revisore-marketing-design.md`
**Cosa fa:** revisione esperta finale su 5 dimensioni (impaginazione/layout, contenuti/struttura, grafiche/foto, testi, efficacia commerciale), con giudizio complessivo e interventi prioritari.
**Quando si attiva:** sempre per ultimo, dopo compliance, prima della consegna al cliente. Eseguito manualmente per la Campagna 1 (`revisione-marketing-design.md`, oggi parzialmente superato dalle correzioni successive); non eseguito per la Campagna 2.
