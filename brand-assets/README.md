# Brand assets — Hadrianus

Asset visivi reali del brand e degli immobili gestiti, da usare nelle grafiche (post, storie, reel) al posto/accanto agli elementi tipografici usati finora.

## Struttura

```
brand-assets/
├── logo/                              → busto di Adriano davanti al tempio, 4 varianti
│   ├── logo-marmo-frontale.png        → marmo, frontale, scritta "HADRIANUS" incisa alla base, sfondo pavimento marmo (alta risoluzione)
│   ├── logo-marmo-profilo-stretto.jpg → marmo, profilo, inquadratura stretta (cupola tagliata a destra), sfondo chiaro
│   ├── logo-marmo-profilo-largo.jpg   → marmo, profilo, inquadratura larga (cupola intera visibile), sfondo chiaro
│   └── logo-bronzo-frontale.jpg       → bronzo con dettagli oro, scritta "HADRIANUS" in oro, sfondo scuro/marmo notturno
├── ambientazione/
│   └── tramonto-litorale-romano.jpg   → tramonto sul mare, scoglio in controluce, cielo arancione — per contenuti ambientati "Roma · Ostia"
└── immobili/                          → foto reali di un immobile in gestione (interni + esterno)
    ├── salotto-divano-azzurro.jpg     → soggiorno, divano blu-fumo, boiserie in legno
    ├── smart-tv-streaming-mockup.jpg  → parete TV con mockup Netflix/Prime Video/Disney+ — ⚠️ vedi nota compliance sotto
    ├── cucina-soggiorno-open-space.png → cucina open space con isola e tavolo da pranzo
    └── balcone-terrazzo.jpeg          → balcone/terrazzo con poltrona sospesa e piante
```

## Stato

✅ **File reali presenti e organizzati** (9 file, spostati da `.claude/` e dalla root dove erano stati caricati, e rinominati con nomi descrittivi).

⚠️ **Varianti "senza sfondo" del logo non ancora disponibili.** L'utente ha chiesto esplicitamente di salvare anche varianti trasparenti (PNG con alpha channel) di ogni angolazione del logo. Le 4 immagini in `logo/` hanno tutte uno sfondo pieno (parete grigia o marmo scuro): **non ho uno strumento di rimozione sfondo / editing immagini in questo ambiente**, quindi non posso generarle io stesso. Per averle serve una di queste strade:
- l'utente le crea con uno strumento esterno (Remove.bg, Photoshop, ecc.) e le carica qui in `logo/trasparenti/`;
- oppure si chiede esplicitamente di provare a generarle con uno strumento di immagini se/quando disponibile in questo ambiente.

## ⚠️ Nota compliance — `smart-tv-streaming-mockup.jpg`

Questa foto mostra sulla TV un **mockup con i loghi Netflix, Prime Video e Disney+** (marchi registrati di terzi). Prima di usarla in contenuti pubblicati (post, storie, ads):
- **non lasciar intendere una partnership/affiliazione** con questi servizi che non esiste;
- valutare se sostituire il mockup con un frame neutro della TV, o descrivere il servizio a parole ("smart TV con le principali piattaforme di streaming") invece di mostrare i loghi;
- se si vuole comunque usarla, farlo solo come foto illustrativa dell'immobile (es. sito/scheda struttura), non come claim commerciale enfatizzato.
Il `compliance-checker` deve controllare questo punto ogni volta che questa foto (o il suo contenuto) viene usata in un contenuto di acquisizione clienti.

## Come vengono usati (regola in `CLAUDE.md` §"Asset di brand reali")

- **Logo**: in copertine/aperture dove serve un momento "brand" pulito (intro carosello, cover reel), o come badge in un angolo (quando disponibile la versione trasparente).
- **Tramonto Litorale**: sfondo fotografico reale per grafiche a tema "Roma · Ostia" (storie, cover reel), con overlay scuro/gradiente fumè sopra per leggibilità del testo.
- **Foto immobili**: prova visiva reale dello standard alberghiero promesso nel copy (es. nei post/caroselli "come funziona", "gestione completa") — coerenti con la regola di brand "niente esempi su singole strutture nominate come prova sociale nei contenuti di acquisizione clienti": usarle come illustrazione di stile/standard, senza nominare l'indirizzo o la struttura specifica.
