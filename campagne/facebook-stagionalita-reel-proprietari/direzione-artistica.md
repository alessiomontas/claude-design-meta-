# Direzione artistica — Stagionalità (post Facebook + reel)

**Canvas editabile (tutte le artboard):** https://claude.ai/code/artifact/4fdbf673-67be-48a8-92d5-01cbc945e06c
**Reel in movimento (anteprima animata, 21 s in loop):** https://claude.ai/code/artifact/b55d8c9b-8305-4024-a0ec-00f45e4c3e82
**Video montato:** `reel/reel-stagionalita.webm` (608×1080, 21,2 s, muto)
**Sorgenti:** `grafiche/*.dc.html` + `grafiche/canvas.json` · **PNG pronti:** `png/`

## Mood

**Freddo che diventa caldo.** L'angolo è l'obiezione "d'inverno non viene nessuno": il visivo la mette in scena e poi la ribalta. La prima schermata è desaturata e fredda, la seconda entra calda e in ordine. Da lì in poi il ritmo è secco: una faccia della domanda invernale per scena, un numero in oro in alto a destra, una riga che compare dal basso.

## Palette

Palette fumè di brand invariata (hex in `.claude/reference/design-system.md`). L'oro `#C8A24B` qui ha un compito preciso e uno solo: **segnare ciò che è acceso** — i mesi bassi del calendario, i numeri delle scene, la CTA. Il freddo della prima scena è ottenuto con `saturate(.35) brightness(.8)` sulla foto, non con un colore nuovo: nessun blu navy, nemmeno come "tinta invernale".

## Pattern visivo — "calendario a 12 caselle"

Firma grafica della campagna, nuova rispetto a tutti i pattern in `design-system.md`: dodici riquadri (i mesi), **i sei di ottobre-marzo accesi in oro**, gli altri spenti in fumè. È l'immagine dell'angolo — l'inverno che si accende — e compare sia nel post (striscia in basso su img 1, griglia grande su img 3) sia nel reel (scena 7, dove le sei caselle si accendono una per battuta).

Nel reel il pattern si combina con: apertura a citazione desaturata, stacco caldo, quattro schede "una tipologia di ospite per scena" con numero in oro e filo che si allunga sotto il titolo, chiusura a fondo pieno con il numero e la banda oro della CTA che sale dal basso.

## Formati

| Contenuto | File | Formato |
|---|---|---|
| FB img 1 — il gancio | `FbGancio.dc.html` | **1080×1920 (9:16)** — obbligatorio: in 4:5 il collage Facebook taglia ai lati |
| FB img 2 — chi ci dorme | `FbOspiti.dc.html` | 1080×1080 |
| FB img 3 — meccanismo + CTA | `FbMeccanismo.dc.html` | 1080×1080 |
| Reel scene 1-8 | `Reel01…Reel08` | 1080×1920 |
| Reel hook alternativo | `Reel01b` | 1080×1920 — per l'A/B test |
| Reel scena 7, accensione | `Reel07_1…Reel07_6` | 1080×1920 — sei stati, uno per casella accesa |

## Movimento del reel (già montato nel video)

- **0:00-2:00** — foto Litorale fredda, zoom lento in avanti, virgolette e titolo che salgono in dissolvenza.
- **2:00** — **stacco secco** sul caldo: "Falso." entra in scala, "Cambia solo l'ospite" sale subito dopo. È il momento di svolta: qui, nel montaggio con audio, va aperto il filtro sulla musica.
- **2:00-14:00** — quattro scene da 2,4 s: filo oro che si allunga, titolo che sale, numero fisso in alto a destra a fare da metronomo.
- **14:00-16:24** — calendario: le sei caselle si accendono a tempo, una ogni 0,31 s con un micro-rimbalzo.
- **16:24-21:12** — numeri e caveat che entrano in cascata, poi la banda oro della CTA che sale dal basso. Stop netto, nessuna dissolvenza: il reel riparte in loop mentre chi guarda sta ancora leggendo.

## Elementi chiave

Cosa si nota per primo: la citazione tra virgolette (img 1 e reel 1), il numero `1.000-1.100 €` in oro (img 3 e reel 8), le caselle accese del calendario. Le formule obbligate — *"su base annua, inverno compreso"*, *"Media, non una promessa: ogni casa fa storia a sé."*, *"Le utenze restano tue."*, *"Guadagniamo solo se guadagni tu."* — sono impaginate alla lettera, perché le immagini circolano da sole.

## Da evitare

- Percentuali di occupazione, tassi di riempimento, grafici stagionali: l'intero angolo è costruito **senza un solo dato di occupazione**, per scelta.
- Formule assolute sui costi ("tutto incluso", "l'unica spesa"): TARI e oneri condominiali restano al proprietario, si possono omettere ma mai negare.
- Blu navy, "hotel-style", strutture nominate, cifre sull'up-sell centro Roma.
- Foto estive luminose nelle scene invernali: il contrasto freddo/caldo funziona solo se il freddo resta freddo.

## Blocchi ancora aperti

Assicurazione danni ospiti e assenza di costi una tantum **non sono impaginati** in `FbMeccanismo` e `Reel08`: lì compare solo il 15% + "Guadagniamo solo se guadagni tu", come prescritto dal copy finché il titolare non chiude i due punti. Se conferma, si aggiungono; se corregge le cinque tipologie di ospite, vanno rifatti `FbOspiti` e `Reel03-06`.

## Nota tecnica sul video

Il file consegnato è **WebM (VP8), muto**: in questo ambiente l'unico encoder video disponibile è VP8, non c'è H.264 e non esiste una traccia audio da usare. Per Instagram e Facebook il video va importato in CapCut (o Canva) e riesportato in MP4 con la musica: la griglia dei tagli è a 100 BPM e i punti esatti sono in `montaggio-capcut.md`. In alternativa, i PNG in `png/` si montano da zero in un paio di minuti, sempre seguendo quella guida.
