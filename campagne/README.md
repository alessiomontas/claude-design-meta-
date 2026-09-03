# Campagne

Questa cartella raccoglie l'output tracciabile di ogni campagna generata dal sistema. Ogni campagna vive in una sottocartella con uno slug descrittivo (es. `gestione-case-vacanza-proprietari/`).

**Prima di crearne una nuova, guarda `INDEX.md`** in questa cartella: elenca angoli/ganci già usati (da non ripetere) e lo stato di ogni campagna esistente.

## Struttura standard di una campagna

```
campagne/<nome-campagna>/
├── brief-mercato.md            → output di ricercatore-mercato
├── copy.md                     → output di copywriter (tutti i testi)
├── direzione-artistica.md      → output di art-director (mood, palette, formati)
├── grafiche/                   → grafiche editabili (.dc.html per canvas Claude Design, o export)
├── checklist-compliance.md     → output di compliance-checker
└── revisione-marketing-design.md → output di revisore-marketing-design (revisione esperta finale)
```

Non tutte le campagne avranno tutti i file (dipende dal canale e dal tipo di contenuto), ma l'ordine di produzione è sempre lo stesso: brief → copy → direzione artistica → grafiche → compliance → revisione esperta.

## Grafiche editabili

Le grafiche vanno prodotte in un formato **modificabile dall'utente**, non come immagini piatte:

- **Claude Design canvas** (`.dc.html`): artboard multiple su un'unica canvas, modificabili visivamente (testo inline, proprietà, export PNG/PDF). Sempre disponibile, è il formato di default — non richiede alcun connettore.
- **Canva**: se il connettore è collegato ed esplicitamente richiesto, l'art-director può generare le bozze nel workspace Canva come alternativa.

Palette, tipografia, formati esatti e componenti riutilizzabili sono in `.claude/reference/design-system.md` — è la fonte unica, non ridefinirli campagna per campagna.

I file sorgente delle grafiche (o i link agli artefatti/design pubblicati) vanno riferiti in `direzione-artistica.md` così la campagna resta tracciabile.
