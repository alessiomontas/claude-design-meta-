# Direzione artistica — giornata 14/09/2026, pacchetto v2

**Angolo:** "Ti hanno scattato le foto col telefono"
*(Il pacchetto v1 — angolo burocrazia/CIN — è stato bocciato dal titolare. La sua direzione artistica resta in `direzione-artistica.md` come storico: il pattern "binario delle scadenze" descritto lì **non va riusato**, è legato a quell'angolo.)*

## Mood

**Diretto, dimostrativo, commerciale.** L'angolo non si spiega: si fa vedere. Tutto il peso visivo sta su una sola cosa — due versioni della stessa stanza — e ogni altro elemento è subordinato a quel confronto.

Cambio di registro rispetto al v1, richiesto dal titolare: **il merito è sempre dell'impresa**. Nessuna grafica chiude sul peso che resta al proprietario; ogni pezzo finisce su cosa garantisce Hadrianus.

## Impianto: "la tendina che attraversa"

| Elemento | Cosa fa |
|---|---|
| **Linea verticale oro** da 6 px, attenuata a `rgba(200,162,75,.35)` | La firma della giornata. Attraversa la pagina da cima a fondo, passando **sotto** i blocchi di testo |
| **Maniglia circolare** Ø 44 px sulla linea | La rende un gesto, non una decorazione: si legge come qualcosa da trascinare |
| **Avanzamento nel carosello**: 216 → 432 → 648 → 864 → fuori bordo | La linea cammina di slide in slide. Su `K5` esce e resta **solo la maniglia**, integrata nel bordo sinistro della pill CTA: la sequenza si chiude da sola |
| **Nel reel** la stessa linea è il movimento clou: a 5,4 s attraversa il fotogramma in 1,2 s e scopre la foto corretta | |

**Perché l'attenuazione.** La prima versione aveva la linea a piena intensità con un alone: sui PNG competeva con la lettura invece di firmare la pagina. La regola sta nel copy ed è stata applicata solo dopo averla vista sbagliata.

**Perché è diverso dai precedenti.** Pattern già bruciati: scontrino/ledger, blocchi invertiti a piena larghezza, step numerati giganti, card domanda/risposta, griglia 2×2 dei servizi, e il binario delle scadenze del v1. Qui non c'è nessuna card e nessuna griglia: l'unica costante è una linea che cammina.

## Le due foto, e perché non sono di un cliente

Il confronto nasce da **una sola foto di Adobe Stock regolarmente licenziata** (`grafiche/stock-salone.jpg`, asset 624287619): da quella vengono sia il "prima" sia il "dopo", quindi *"stessa stanza, altro annuncio"* è letteralmente vero.

**Il titolare ha scelto deliberatamente una casa non in gestione.** Una versione volutamente peggiorata di un immobile reale riguarda il suo proprietario, che non è parte della decisione. Regola operativa: **non rigenerare mai il "prima" partendo da `brand-assets/immobili/`**.

La foto è verticale (4480×6720): riempie il 9:16 senza bande e senza sacrificare la stanza. È il motivo per cui è stata scelta fra sei candidate.

**Come è stato costruito il "prima"** — i difetti veri dello scatto col telefono, tutti insieme:
- rotazione −4,6° e inquadratura fuori asse che taglia poltrona e pianta
- curva gamma 2,35: schiaccia ombre e mezzitoni e lascia **bruciata la finestra** — il difetto tipico del controluce
- dominante calda con blu a 0,66, contrasto 0,80
- **perdita di dettaglio reale**: ridotta a 520 px e reingrandita, più sfocatura e rumore concentrato nelle ombre
- vignettatura e JPEG a qualità 42

Il primo tentativo abbassava solo la luminosità e veniva *sbiadito*, non brutto: leggeva come una scelta di stile.

**Secondo ambiente:** `stock-salotto-caldo.jpg` (asset 296826045), divano in pelle cognac. Entra nella scena 7 del reel, su "Ti garantiamo il servizio fotografico", e nell'inserto di `K3`. Serve a non far vedere la stessa stanza per quindici secondi.

## Palette

Invariata: fumè profondo `#2E2A25`, fumè `#3F3A33`, fumè medio `#4a443a`, oro `#C8A24B`, oro scuro `#b3892f` su fondo chiaro, sabbia `#F5F0E6`. Nessun blu, nessun navy.

L'oro è riservato a tre cose: la linea-firma, la riga che chiude ogni slide, la CTA. `K3` è **l'unica slide chiara** del carosello e fa da respiro a metà sequenza.

## Il reel: perché è animato davvero

Il reel del v1 è stato bocciato dal titolare come *"penoso"*: erano nove immagini ferme incollate una dopo l'altra, senza un solo movimento dentro la scena.

Il nuovo nasce da una **pagina HTML con una timeline scrubbabile** (`reel/build_reel.py` → `reel/reel.html`, resa in MP4 da `.claude/skills/giornata/anima_reel.py`). Ogni animazione dura quanto il reel e usa `fill-mode: both`, quindi lo stato a un dato istante è deterministico e ogni fotogramma si cattura esatto.

Movimento in **tutte e nove le scene**: mano libera con due tentativi di raddrizzare che ricadono, push-in, scroll di provini che si inchioda e rimbalza, la tendina, pan lento, stacco dal basso sul secondo ambiente, banda oro che sale sul finale.

**Il reel è muto**: la musica si aggiunge in fase di pubblicazione, dalla libreria di Instagram, per non avere problemi di diritti.

## Formati

| Blocco | Artboard | Formato |
|---|---|---|
| `Main` (slide 1), `K2`-`K5` | carosello | 1080×1350 |
| `FB1` | Facebook 1ª immagine | 1080×1920 — mai 4:5, nel collage verrebbe tagliata |
| `FB2`, `FB3` | Facebook 2ª e 3ª | 1080×1080 |
| `S1`-`S2` | storie già approvate, **non toccate** | 1080×1920 |
| `S3`-`S4` | storie nuove | 1080×1920 |
| reel | video | 1080×1920, 15,6 s, 30 fps, H.264 |

## Da evitare

- Riaprire il pattern "binario delle scadenze" del v1: è legato all'angolo bocciato.
- Mettere la linea-firma a piena intensità: compete col testo.
- Degradare foto di `brand-assets/immobili/` per ottenere un "prima".
- Blu navy, in qualunque forma.

## Controllo qualità

I sei controlli di `master-template.md` sono stati fatti sui PNG renderizzati. Difetti trovati e corretti **prima** della consegna:

1. Linea-firma troppo accesa: competeva con la lettura.
2. Su `Main` lo spicchio di foto corretta largo 216 px non si leggeva come confronto — sembrava un gradiente. Il prima/dopo è rimasto al reel e a Facebook; la slide fa il gancio sulla foto sbagliata.
3. Su `S3` e `S4` due righe superavano la colonna utile, andavano a capo e finivano sopra il blocco successivo.
4. L'etichetta `IL CONSIGLIO` restava incastrata fra due blocchi.
5. Su `FB2` il filo oro tagliava la prima lettera dei kicker: `UCE`, `RDINE`, `NQUADRATURA`.
6. `FB3` non aveva foto: il post prometteva "la stessa stanza, due volte" e mostrava solo il "prima". Ora porta il "dopo".

## File

- `grafiche/build_v2.py` — rigenera le 12 artboard; `grafiche/build.py` resta per `S1`/`S2`
- `grafiche/` — artboard `.dc.html`, `canvas.json`, foto e ritagli
- `png/` — i 12 export
- `reel/` — `build_reel.py`, `reel.html`, `reel-foto-col-telefono.mp4`
- Canvas editabile: https://claude.ai/artifact/3e3Y2yU7j4TNRNPFPga2g6
