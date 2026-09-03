# STATO — Hadrianus Content Engine

Ultimo aggiornamento: fine sessione corrente (branch `claude/hadrianus-content-engine-setup-79hbsa`, ultimo commit `f76b050`).

## Obiettivo del progetto

Costruire, dentro questo repository, un **sistema di generazione contenuti di vendita** per **Hadrianus** (property management / gestione case vacanza a Roma e Ostia — brand del cliente, dominio email `hadrianusmultiservice.it`), utilizzabile con Claude Code:

- un team di **agenti** specializzati (ricerca di mercato → copy → direzione artistica/grafiche → compliance → revisione esperta) che lavorano sempre nello stesso ordine;
- una **skill** che orchestra il flusso completo (`/nuova-campagna`);
- una **skill** che codifica il metodo di copywriting (`framework-vendita`);
- una cartella `riferimenti/` con contenuti reali del cliente da cui gli agenti imparano il tono di voce;
- una cartella `campagne/` con l'output tracciabile di ogni campagna generata (brief, copy, grafiche editabili, compliance, revisione).

Il sistema non è mai stato pensato come "genera un post": è pensato come infrastruttura riusabile per produrre più campagne nel tempo, sempre con lo stesso metodo e le stesse regole di brand.

## Cosa è FATTO (stabile, consegnato, verificato)

1. **Impalcatura del sistema** (CLAUDE.md, README.md, 5 agenti in `.claude/agents/`, 2 skill in `.claude/skills/`, `riferimenti/` popolato con 3 contenuti reali del cliente). Vedi INVENTARIO.md per il dettaglio file.
2. **Campagna 1 — `campagne/gestione-case-vacanza-proprietari/`**: acquisizione proprietari per gestione case vacanza (Roma/Ostia). Angolo iniziale = anti-stress/rendita passiva, poi corretto per usare il rischio dell'affitto tradizionale (morosità, casa sfitta) come leva principale, invece del case study "Rome Smart Sea" (rimosso per regola di brand). Include:
   - brief di mercato, copy, direzione artistica, checklist compliance, revisione marketing/design (tutti in stato "storico/superato" tranne dove segnalato — vedi nota su `copy.md`);
   - un kit grafico editabile completo (canvas Claude Design, pubblicato come Artifact) con 3 storie, 5 slide di carosello, 1 post di confronto, 1 cover reel, 3 grafiche per un post Facebook;
   - export PNG pronti all'upload per Instagram in `instagram-ready/out/`;
   - un post Facebook per gruppi locali con 3 varianti di gancio (problema / offerta / emotivo) in `post-facebook-gruppi-locali.md`, poi sostituito da una versione con gancio unico basato su ricerca di mercato reale (morosità/casa sfitta) — vedi DECISIONI.md.
3. **Campagna 2 — `campagne/instagram-fiducia-proprietari/`**: seconda campagna Instagram, angolo "fiducia/trasparenza" (deliberatamente diverso dal rischio della campagna 1), 3 storie autoconclusive + 2 caroselli da 5 slide ("Come funziona" e "Le domande che ci fanno tutti"), layout visivi differenti dalla campagna 1 pur mantenendo l'identità di brand. Canvas editabile pubblicato come Artifact separato, 13 PNG pronti in `instagram-ready/out/`.
4. **Correzioni di lessico/brand** applicate retroattivamente a tutti i contenuti pubblicati: "guadagniamo solo se guadagni tu" (mai "guadagni solo..."), "standard alberghiero" (mai "hotel-style"), nessun riferimento a singole strutture come prova.
5. **Palette di brand** cambiata da blu navy a grigio fumè caldo (nero+marrone+giallo), applicata a entrambe le campagne.
6. **Memoria fissa** (preferenze utente valide sempre) scritta in `CLAUDE.md` §"Preferenze fisse di output" e §"Lessico di brand": editabilità obbligatoria, niente navy, storie autoconclusive, grafica sempre generata di default, variazione del design tra campagne, formato fisso a 3 immagini per i post Facebook (1 verticale 9:16 + 2 quadrate).

## Cosa è IN CORSO / punto esatto in cui siamo ora

L'ultima azione completata prima di questa richiesta di handover era la consegna della Campagna 2 (fiducia), con relativo commit e push. Non ci sono task a metà nel codice: ogni campagna consegnata ha copy + grafiche editabili + PNG + commit.

Subito prima della richiesta di handover, l'assistente aveva proposto due follow-up mai confermati dall'utente:
- generare caption dedicate per ogni singola storia della campagna fiducia (oggi le caption scritte in `copy-e-piano.md` coprono i 2 caroselli, non le 3 storie singolarmente);
- generare un post Facebook a 3 immagini abbinato alla campagna fiducia (oggi esiste un post Facebook solo per la Campagna 1).

Nessuna delle due è stata iniziata.

## Cosa MANCA / non è stato fatto

- Non è stato eseguito nessun ciclo completo tramite il comando `/nuova-campagna` così come descritto in CLAUDE.md/SKILL.md: le due campagne sono state prodotte con una sequenza equivalente ma pilotata manualmente dall'assistente in chat, non invocando gli agenti come subagent veri e propri in un colpo solo. Il flusso concettuale (ricerca → copy → grafica → compliance → revisione) è stato rispettato, ma non c'è la prova diretta che `/nuova-campagna` end-to-end funzioni senza intervento.
- Le foto reali degli immobili non sono mai state fornite dal cliente: tutte le grafiche sono tipografiche (niente foto), quindi il punto "sostituire i placeholder foto" della vecchia `revisione-marketing-design.md` (Campagna 1) è ancora aperto in senso lato, anche se le grafiche attuali non hanno più placeholder foto rotti — semplicemente non usano foto.
- Non esiste ancora contenuto per canali diversi da Instagram/Facebook (no email, no landing page, no script video benché il reel abbia uno storyboard testuale in `copy.md` della Campagna 1).
- I documenti "storici" della Campagna 1 (`brief-mercato.md`, `checklist-compliance.md`, `revisione-marketing-design.md`, `copy.md`) NON sono stati aggiornati per rispecchiare tutte le correzioni successive (lessico, palette, rimozione case study): riportano ancora "hotel-style" e "Rome Smart Sea" in più punti, perché fotografano lo stato del progetto al momento in cui sono stati scritti. Solo i file davvero pubblicati (grafiche `.dc.html`, PNG, `PIANO-PUBBLICAZIONE.md`, `direzione-artistica.md`, `grafiche/README.md`) sono stati corretti. Questo è stato segnalato esplicitamente all'utente e mai risolto (vedi APERTI.md).
- Non è stato mai chiesto/ricevuto un feedback reale del cliente Hadrianus su nessuno dei contenuti prodotti: tutto è stato validato solo internamente (checklist di compliance simulata dall'assistente, non da un umano lato cliente).

## File di riferimento per capire la sessione

- `CLAUDE.md` — memoria fissa e regole (riportate integralmente in REGOLE.md).
- `campagne/*/copy-e-piano.md` o `PIANO-PUBBLICAZIONE.md` — cosa pubblicare e come.
- `_handover/DECISIONI.md` — perché le cose sono state fatte in un modo piuttosto che in un altro.
