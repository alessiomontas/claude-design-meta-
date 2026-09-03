# INVENTARIO — albero del workspace

Legenda stato: 🟢 **vivo** (fonte di verità corrente, va mantenuto aggiornato) · 🟡 **storico/superato** (fotografa uno stato passato del progetto, non riflette le ultime correzioni — vedi APERTI.md) · ⚪ **derivato/rigenerabile** (output automatico, si può cancellare e rifare dai sorgenti) · 🔧 **strumento** (script/config, non contenuto).

```
.
├── CLAUDE.md                                    🟢 memoria fissa del progetto: regole, flusso, lessico di brand (copiato integralmente in _handover/REGOLE.md)
├── README.md                                    🟢 istruzioni rapide d'uso del sistema per un nuovo utente
├── .gitignore                                   🔧 esclude da git i file "seedati" della skill design (social-kit-*.html, ~2.4MB, rigenerabili)
│
├── .claude/
│   ├── agents/
│   │   ├── ricercatore-mercato.md               🟢 definizione agente: brief di mercato
│   │   ├── copywriter.md                        🟢 definizione agente: scrittura copy
│   │   ├── art-director.md                      🟢 definizione agente: direzione visiva + grafiche editabili
│   │   ├── compliance-checker.md                🟢 definizione agente: controllo claim/tono/refusi
│   │   └── revisore-marketing-design.md         🟢 definizione agente: revisione esperta finale
│   └── skills/
│       ├── framework-vendita/SKILL.md           🟢 metodo di copywriting (8 blocchi Hook→CTA)
│       └── nuova-campagna/SKILL.md               🟢 orchestrazione dei 5 agenti in sequenza (mai invocata realmente in questa sessione — vedi APERTI.md)
│
├── riferimenti/
│   ├── README.md                                🟢 istruzioni sul formato dei riferimenti
│   ├── riferimento-1.md                         🟢 contenuto reale del cliente: acquisizione proprietari, commissione 15%
│   ├── riferimento-2.md                         🟢 contenuto reale del cliente: case study Rome Smart Sea (NB: il case study qui è materiale di riferimento/tono di voce, non va confuso col divieto — valido solo — di usarlo come prova nei contenuti di acquisizione, vedi REGOLE.md §Lessico di brand)
│   └── riferimento-3.md                         🟢 contenuto reale del cliente: B2B pulizie "Templum Purum"
│
└── campagne/
    ├── README.md                                🟢 spiega la struttura standard di una cartella-campagna
    │
    ├── gestione-case-vacanza-proprietari/       CAMPAGNA 1 — angolo iniziale rendita/anti-stress poi corretto su rischio affitto tradizionale
    │   ├── brief-mercato.md                     🟡 STORICO: brief originale, cita ancora "Rome Smart Sea" come prova e "hotel-style" — superato dalle correzioni successive, mai riscritto
    │   ├── copy.md                               🟡 STORICO: prima bozza di copy (5 storie stile carosello, poi vietato), esplicitamente marcata "bozza iniziale (superata)" in testa al file
    │   ├── direzione-artistica.md                🟢 VIVO: aggiornata con palette fumè e note sulla rimozione del case study
    │   ├── checklist-compliance.md               🟡 STORICO: approva ancora contenuti col vecchio lessico/case study, mai rieseguita dopo le correzioni
    │   ├── revisione-marketing-design.md         🟡 STORICO: revisione della prima versione del kit (navy, 5 storie), oggi non rispecchia il kit attuale
    │   ├── ricerca-pain-points-proprietari.md    🟢 VIVO: ricerca web su morosità/case sfitte, con fonti — base della prova "dati di mercato"
    │   ├── post-facebook-gruppi-locali.md        🟢 VIVO: copy del post Facebook (3 varianti iniziali + gancio riscritto su morosità/casa sfitta, formato 3 immagini)
    │   ├── grafiche/
    │   │   ├── Main.dc.html                     🟢 artboard editabile: Storia A (rendita/anti-stress)
    │   │   ├── StoriaB.dc.html                  🟢 artboard editabile: Storia B (rischio affitto tradizionale → terza strada)
    │   │   ├── StoriaC.dc.html                  🟢 artboard editabile: Storia C (15% / fiducia)
    │   │   ├── Carosello1.dc.html … Carosello5.dc.html   🟢 5 artboard editabili: carosello feed (hook, problema, servizi, differenza, offerta+CTA)
    │   │   ├── PostProva.dc.html                🟢 artboard editabile: post "Due strade per la tua casa" (confronto affitto vs casa vacanza)
    │   │   ├── ReelCover.dc.html                 🟢 artboard editabile: copertina reel
    │   │   ├── FbPost1.dc.html                  🟢 artboard editabile: post Facebook immagine 1/3, verticale 9:16
    │   │   ├── FbPost2.dc.html, FbPost3.dc.html  🟢 artboard editabili: post Facebook immagini 2/3 e 3/3, quadrate
    │   │   ├── canvas.json                       🟢 layout del canvas (posizione/dimensione di ogni artboard + note)
    │   │   ├── README.md                         🟢 istruzioni per rigenerare il canvas dai sorgenti
    │   │   └── social-kit-proprietari.html       ⚪ DERIVATO, non versionato (.gitignore): payload "seedato" ~2.4MB, rigenerabile da seed-canvas.mjs; la copia pubblicata vive come Artifact online
    │   └── instagram-ready/
    │       ├── build-and-render.mjs              🔧 script Playwright: converte i .dc.html in HTML standalone e li fotografa in PNG alle dimensioni esatte
    │       ├── src/*.html                        ⚪ DERIVATO: HTML standalone generato dallo script per ciascun artboard, usato solo per il rendering
    │       ├── out/*.png                         🟢 VIVO (deliverable finale): PNG pronti all'upload — storia-a/b/c, carosello-1..5, post-prova, reel-cover, fb-1/2/3
    │       └── PIANO-PUBBLICAZIONE.md            🟢 VIVO: cosa pubblicare, in che ordine, con quali didascalie
    │
    └── instagram-fiducia-proprietari/           CAMPAGNA 2 — angolo fiducia/trasparenza, layout differenti dalla Campagna 1
        ├── copy-e-piano.md                       🟢 VIVO: copy delle 3 storie + 2 caroselli, caption, note compliance, ordine di pubblicazione
        ├── grafiche/
        │   ├── Main.dc.html                      🟢 artboard editabile: Storia 1 ("a chi do le chiavi")
        │   ├── Storia2.dc.html                   🟢 artboard editabile: Storia 2 (trasparenza costi)
        │   ├── Storia3.dc.html                   🟢 artboard editabile: Storia 3 (la casa resta tua)
        │   ├── CarA1.dc.html … CarA5.dc.html      🟢 5 artboard editabili: Carosello A "Come funziona" (step numerati)
        │   ├── CarB1.dc.html … CarB5.dc.html      🟢 5 artboard editabili: Carosello B "Le domande che ci fanno tutti" (Q&A)
        │   ├── canvas.json                        🟢 layout del canvas
        │   └── social-kit-fiducia.html            ⚪ DERIVATO, non versionato (.gitignore): payload seedato; copia pubblicata come Artifact online (URL separato dalla Campagna 1)
        └── instagram-ready/
            ├── build-and-render.mjs               🔧 script Playwright (copia adattata dello script della Campagna 1, percorsi diversi)
            ├── src/*.html                         ⚪ DERIVATO: HTML standalone per il rendering
            └── out/*.png                          🟢 VIVO (deliverable finale): 13 PNG — storia-1/2/3, carosello-A-1..5, carosello-B-1..5
```

## Cosa NON esiste (e potrebbe sembrare che dovrebbe, leggendo CLAUDE.md)

- **`_handover/`** non esisteva prima di questa richiesta: è stato creato ora, contestualmente a questo pacchetto.
- **Nessun file di compliance/revisione per la Campagna 2** (`instagram-fiducia-proprietari/`): a differenza della Campagna 1, non esistono `checklist-compliance.md` né `revisione-marketing-design.md` dedicati. La conformità è stata dichiarata solo a parole in chat ("Note compliance" dentro `copy-e-piano.md`), non con un documento a parte nello stile degli altri agenti.
- **Nessuna foto reale**: tutte le grafiche di entrambe le campagne sono composizioni tipografiche (testo, forme, icone SVG), non contengono foto di immobili. Non ci sono placeholder-immagine rotti nel kit attuale (sono stati rimossi durante le correzioni), ma nemmeno foto vere.
- **Nessun output per canali diversi da Instagram/Facebook** (no email, no landing page, no annuncio Google/Meta Ads in senso stretto — solo post organici/gruppi).
