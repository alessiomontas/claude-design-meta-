# Hadrianus Content Engine

Sistema di generazione contenuti di vendita per Hadrianus, basato su Claude Code: un team di agenti specializzati che porta un'idea di campagna dal brief al contenuto pronto per la consegna, sempre nello stesso ordine e con lo stesso metodo.

## Avvio rapido

1. Apri questa cartella con Claude Code (in locale o su claude.ai/code).
2. Al primo utilizzo, popola `riferimenti/` con 2-3 contenuti reali di Hadrianus (vedi `riferimenti/README.md`) — è da lì che gli agenti imparano il tono di voce.
3. Lancia una nuova campagna:

   ```
   /nuova-campagna
   ```

   e rispondi alle domande su prodotto/servizio, target e canale. In alternativa puoi passare le informazioni direttamente:

   ```
   /nuova-campagna Consulenza fiscale per PMI, target: piccoli imprenditori, canale: email
   ```

4. Il risultato viene salvato in `campagne/<nome-campagna>/`: brief di mercato, copy, direzione artistica, grafiche editabili e checklist di compliance. La campagna viene aggiunta a `campagne/INDEX.md`.

## Cosa fa ogni agente

| Agente | Quando entra in gioco | Cosa produce |
|---|---|---|
| `ricercatore-mercato` | Sempre per primo | Brief: target, dolori/desideri, concorrenza, angolo di vendita consigliato |
| `copywriter` | Dopo il brief | Bozze di testo (ads, email, landing, script) secondo il metodo Hadrianus |
| `art-director` | Dopo che il copy è stabile | Direzione visiva (mood, palette, formati) + grafiche editabili (Claude Design / Canva) |
| `compliance-checker` | Dopo le grafiche | Verifica claim, tono, refusi; approva o segnala cosa correggere |
| `revisore-marketing-design` | Sempre per ultimo | Revisione esperta: layout, contenuti, grafiche/foto, testi, efficacia commerciale |

Puoi anche richiamare un singolo agente fuori dal flusso completo, ad esempio:

```
Usa l'agente compliance-checker su questo testo: [...]
```

## Le due skill

- **`framework-vendita`** — il metodo di scrittura persuasiva usato da tutti gli agenti che producono o valutano testo. È il "manuale interno": aggiornalo man mano che capisci cosa funziona davvero per Hadrianus.
- **`nuova-campagna`** — il comando che orchestra i cinque agenti in sequenza per produrre una campagna completa.

## Struttura cartelle

```
CLAUDE.md                      nucleo sempre caricato: identità minima, flusso, regole fisse, lessico
README.md                      questo file
riferimenti/                   contenuti reali di esempio, per calibrare il tono
brand-assets/                  logo, foto ambientazione, foto immobili reali (asset veri, non placeholder)
campagne/
├── INDEX.md                   indice campagne: angoli/ganci già usati, da controllare prima di una nuova
└── <nome-campagna>/           output di ogni campagna generata
_handover/                     snapshot per un revisore esterno (stato, decisioni, regole, inventario, aperti)
.claude/agents/                i 5 agenti specializzati
.claude/skills/                framework-vendita e nuova-campagna
.claude/reference/             approfondimenti on-demand (NON caricati a ogni avvio):
├── brand-identity.md              chi è Hadrianus, target/pain-point, cosa si può usare come prova
├── design-system.md               palette hex, tipografia, formati, componenti .dc.html riutilizzabili
└── lessico-brand.md               glossario esteso corretto/vietato, con esempi
```

`CLAUDE.md` contiene solo ciò che deve essere sempre in memoria (regole fisse, lessico core, flusso). Il contesto più esteso — identità di brand dettagliata, palette esatta con snippet di codice, glossario con esempi — vive in `.claude/reference/` e viene letto solo quando serve, dagli agenti che ne hanno bisogno in quel passaggio. Se una nuova regola deve valere *sempre e comunque*, va in `CLAUDE.md`; se è un dettaglio che serve solo in certi passaggi, va in `.claude/reference/`.

## Strumenti grafici collegabili (Canva e Adobe for creativity, opzionali)

Lo strumento di default per le grafiche editabili è il **canvas Claude Design** (sempre disponibile, nessuna connessione richiesta) — costruisce ogni artboard testo+layout. Due connettori opzionali affiancano compiti specifici, dettagliati in `.claude/reference/design-system.md` §"I 3 strumenti grafici":

- **Canva** — se collegato, l'`art-director` può generare le bozze direttamente nel tuo workspace Canva in alternativa, se lo richiedi esplicitamente.
- **Adobe for creativity** — se collegato, gestisce la post-produzione delle foto/video reali in `brand-assets/` (ritocco, crop sul formato esatto, rimozione sfondo per i loghi trasparenti, montaggio video per i Reel) prima che entrino negli artboard Claude Design.

Le grafiche editabili non sono mai opzionali: si producono comunque, con Claude Design come base, gli altri due strumenti solo dove aggiungono valore reale.

## Manutenzione del sistema

- Aggiungi nuovi `riferimenti/` ogni volta che un contenuto performa particolarmente bene: è il segnale più forte per affinare il metodo.
- Se noti che il copy prodotto si allontana dal tono Hadrianus, il problema quasi sempre è in `riferimenti/` (pochi esempi, o non rappresentativi) più che negli agenti stessi.
- Ogni volta che correggi un termine o una formula (es. "si dice così, non cosà"), aggiungila alla tabella in `.claude/reference/lessico-brand.md` — non lasciarla solo detta a voce, altrimenti si riperde e va ricorretta di nuovo.
- Dopo ogni campagna, verifica che `campagne/INDEX.md` sia aggiornato con l'angolo usato: è quello che permette di non ripetere lo stesso gancio due volte.
- Le regole "dure" (mai inventare claim, sempre passare da compliance) sono in `CLAUDE.md` e valgono per tutti gli agenti: non vanno duplicate né contraddette nei singoli file agente/skill/reference.
