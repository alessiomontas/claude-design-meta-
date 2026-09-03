# DECISIONI — Hadrianus Content Engine

Ogni voce: decisione presa, motivo, alternative scartate. In ordine cronologico approssimativo (per come sono emerse in chat).

---

**Struttura del sistema: agenti + skill invece di un unico prompt monolitico.**
Motivo: l'utente voleva un processo ripetibile e sempre uguale (ricerca → copy → grafica → compliance → revisione), non un output "a braccio" diverso ogni volta. Alternative scartate: un singolo comando che genera tutto in un colpo senza fasi distinte (scartato perché non garantisce che ogni step — es. compliance — venga davvero eseguito).

---

**Aggiunta di un quinto agente, `revisore-marketing-design`, oltre ai 4 richiesti inizialmente dall'utente.**
Motivo: la richiesta esplicita dell'utente era "una volta generato il prodotto finale fallo analizzare da un esperto in marketing e design che controlla impaginazione, contenuti, grafiche e foto, testi ed efficacia commerciale" — un ruolo distinto dal `compliance-checker` (che controlla claim/refusi, non efficacia commerciale). Alternative scartate: far fare questo controllo al `compliance-checker` stesso (scartato perché sono compiti concettualmente diversi: uno verifica cosa NON si può dire, l'altro giudica se il contenuto VENDE).

---

**Le grafiche vengono prodotte con la skill `design` (Claude Design canvas), non solo come brief testuale o export statico.**
Motivo: richiesta esplicita e poi resa "memoria fissa": "ogni grafica deve essere EDITABILE come su Canva". Alternative scartate: consegnare solo PNG (rifiutato esplicitamente dall'utente, "mai al posto della versione editabile"); usare Canva come strumento primario (scartato perché il connettore Canva non risultava collegato in questa sessione — resta l'alternativa se collegato in futuro, l'agente `art-director` lo prevede).

---

**Palette di brand: da blu navy a grigio fumè caldo (nero+marrone+giallo).**
Motivo: richiesta esplicita dell'utente ("togli completamente dalla tua memoria il colore blu navy e metti un grigio... tipo un miscuglio tra nero, marrone e giallo"). Applicata retroattivamente a tutte le grafiche già prodotte della Campagna 1. Nessuna alternativa proposta: è un vincolo di brand, non una scelta estetica dell'assistente.

---

**Le storie Instagram sono sempre autoconclusive (problema + soluzione in una sola storia), mai spezzate in un carosello di più storie.**
Motivo: richiesta esplicita dell'utente, con motivazione sua: vuole che ogni singola storia dia da sola problema e soluzione con un paio di frasi impattanti. Il formato "carosello" resta ammesso solo per i POST del feed. Alternativa precedente (scartata): la prima versione del sistema usava 5 storie in sequenza narrativa (hook→agitazione→soluzione→prova→offerta) — esplicitamente corretta dall'utente come non voluta.

---

**Generare sempre anche la grafica per ogni contenuto, senza che l'utente lo chieda ogni volta.**
Motivo: richiesta esplicita ("tutte le volte che mi generi qualcosa deve essere editabile... mettitelo in memoria come comando principale"). Diventata regola fissa in CLAUDE.md. Nessuna alternativa: prima di questa richiesta l'assistente proponeva la grafica come step separato del flusso `/nuova-campagna`, non come default automatico per qualsiasi output testuale.

---

**Variare il design (layout, composizione) tra una campagna/comando e l'altro, mantenendo la stessa identità di brand.**
Motivo: richiesta esplicita ("cerca di non farle sempre tutte uguali... varia leggermente il design"). Applicata concretamente nella Campagna 2 (layout "virgolette/risposta", numeri giganti per gli step, card domanda/risposta) rispetto alla Campagna 1 (layout con box e checklist). Alternativa scartata: riusare lo stesso template di artboard per velocità — esplicitamente vietato dall'utente.

---

**Formato del post Facebook: sempre 3 immagini, la prima verticale 9:16 (non 4:5), le altre due quadrate.**
Motivo: bug reale segnalato dall'utente con screenshot — la prima immagine (inizialmente 1080×1350, cioè 4:5) veniva tagliata ai lati nel collage di Facebook, perché la cella sinistra del collage è stretta e alta (~1:2). La correzione a 1080×1920 (9:16) risolve il problema empiricamente osservato. Alternativa scartata: mantenere 4:5 e accettare il taglio (impossibile, comprometteva la leggibilità del gancio).

---

**Lessico di brand corretto in tre punti, su segnalazione esplicita dell'utente:**
1. `"guadagniamo solo se guadagni tu"` è l'unica formula corretta (non `"guadagni solo se guadagni tu"`, che era un errore presente nei contenuti iniziali copiati dai riferimenti del cliente).
2. `"hotel-style"` → sempre `"standard alberghiero"` (o "metodo/livello alberghiero"): l'utente lo giudica poco professionale.
3. Vietato citare singole strutture (es. "Rome Smart Sea") come prova nei contenuti di acquisizione clienti: secondo l'utente non è un dato che porta clienti.
Motivo di ognuna: istruzione diretta dell'utente, promossa a regola fissa in CLAUDE.md. Alternativa scartata per il punto 3: sostituire il case study con altri dati interni Hadrianus (scartata perché non richiesti/non disponibili) — si è optato per **dati di mercato generali** (morosità, case sfitte in Italia) come nuova leva di prova, scelta esplicitamente dall'utente tramite AskUserQuestion tra 4 opzioni proposte.

---

**Sostituzione della prova sociale "case study Rome Smart Sea" con dati di mercato generali (morosità, case sfitte) reperiti via ricerca web.**
Motivo: conseguenza diretta del divieto sui case study di singole strutture. Prima di agire, è stata fatta una ricerca web esplicita (vedi `campagne/gestione-case-vacanza-proprietari/ricerca-pain-points-proprietari.md`) per fondare il nuovo gancio su dati reali citabili, invece di inventare percentuali. Alternative proposte e scartate dall'utente (tramite AskUserQuestion): "prova = serietà/processo" senza dati di mercato; "solo correzioni testo mantenendo il case study in deroga"; "non toccare il kit IG per ora". L'utente ha scelto esplicitamente "prova = dati di mercato".

---

**Uso di Playwright + Chromium headless (non la skill `design` stessa) per generare gli export PNG "pronti da caricare".**
Motivo: la skill `design` produce un canvas editabile via Artifact, ma l'utente ha chiesto esplicitamente contenuti "pronti da essere caricati su Instagram" in più immagini — serviva un rendering programmatico offline alle dimensioni esatte (1080×1920, 1080×1350, 1080×1080). Si è scelto di derivare l'HTML standalone direttamente dai file sorgente `.dc.html` (stessa fonte di verità del canvas editabile), invece di scrivere il markup due volte, per evitare disallineamento tra "versione editabile" e "versione PNG". Alternativa scartata: mantenere due sorgenti separati (uno per il canvas, uno per il render) — scartata per rischio di disallineamento nel tempo.

---

**Il file HTML "seedato" del canvas (`social-kit-*.html`, ~2.4 MB) non viene versionato in git; è escluso via `.gitignore`.**
Motivo: è un artefatto generato e rigenerabile dai sorgenti `.dc.html` + `canvas.json`, e la versione "vera" vive comunque pubblicata come Artifact online. Tenerlo fuori da git evita di appesantire la storia del repo con file binari-simili di grandi dimensioni ad ogni modifica. Alternativa scartata: versionarlo comunque per avere uno storico visivo — scartata per il peso (2-2.5 MB per file, rigenerato spesso).

---

**Ogni campagna vive nella propria cartella sotto `campagne/<nome-campagna>/`, con una sottostruttura fissa (`grafiche/`, `instagram-ready/`, più i .md di processo).**
Motivo: requisito esplicito iniziale dell'utente ("ogni campagna produce output tracciabile"), poi rispettato in modo automatico anche per la seconda campagna senza bisogno di richiederlo di nuovo. Alternativa scartata: cartella piatta con tutti i contenuti di tutte le campagne mescolati — mai stata un'opzione considerata, contraria all'istruzione originale.

---

**La seconda campagna (fiducia) è stata pubblicata come Artifact SEPARATO (nuovo URL), non come aggiornamento del canvas della prima campagna.**
Motivo: sono due campagne concettualmente distinte (angoli, ganci e layout diversi), non una revisione della stessa. Aggiornare lo stesso Artifact avrebbe sovrascritto la Campagna 1 ancora attiva/pubblicabile. Alternativa scartata: un unico grande canvas con entrambe le campagne — scartata per chiarezza e per rispettare la struttura a cartelle per campagna.
