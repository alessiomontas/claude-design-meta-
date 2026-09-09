# Direzione artistica — reel "Cosa cerca davvero un proprietario"

**Sei scene editabili (canvas Claude Design):** https://claude.ai/code/artifact/d42e38d2-10a2-4608-ab97-6f8ef30377ea
Ogni scena è un artboard 1080×1920 con sfondo, velo, marchio e testi separati: si sposta, si ridimensiona e si
riscrive tutto, come in Canva. `grafiche/Main.dc.html` è la scena 1, poi `S2` … `S6`.

## Il riferimento e cosa ne abbiamo preso

Il modello indicato dal titolare è un reel di un team immobiliare americano: interni scuri, camera lentissima,
una frase bianca al centro esatto, stacchi netti al secondo. Funziona perché **non mostra niente da vendere**:
mostra desideri, uno per inquadratura.

Preso dal modello: il centraggio assoluto del testo, il ritmo (2 s di gancio, poi una battuta al secondo, poi
due secondi di chiusura), il marchio fisso in alto, gli stacchi senza dissolvenza.
Cambiato: la palette (fumè caldo + oro, non il grigio-blu del riferimento), il corpo del testo (+20%, il
riferimento è troppo piccolo per un pubblico di proprietari over 45), e il finale, che nel modello resta un
desiderio mentre qui diventa la firma commerciale.

## Palette e tipografia

| Elemento | Valore |
|---|---|
| Testo principale | `#FFFFFF`, Archivo 800/900, 70-72 px, interlinea 1,13 |
| Riga di apertura | Manrope 600, 45 px, `rgba(255,255,255,.94)` |
| Riga di chiusura | `#E2BE6C` (oro brand schiarito per reggere sul video), Archivo 800, 47 px |
| CTA | Manrope 600, 31 px, maiuscolo, spaziatura 6 px |
| Marchio in alto | Archivo 800 33 px spaziato 10 px + filo 1 px + Manrope 600 17 px spaziato 7 px |
| Velo | fumè `rgba(38,34,29,…)` a tre strati (vedi sotto) |

Nessun blu navy. Nessun elemento tipografico decorativo: qui il protagonista è la fotografia reale.

## Il velo — la ricetta che risolve le grafiche "smunte"

Il problema delle grafiche precedenti era il contrario di questo: fondo pieno e foto assente. Qui la foto c'è
sempre e sotto il testo passano **tre strati sovrapposti**, tutti ricalcabili negli artboard:

1. `radial-gradient(ellipse 88% 25% at 50% 50%, rgba(26,23,19,.60) → trasparente)` — scurisce la fascia centrale
2. `linear-gradient(180deg, rgba(38,34,29,.80) in alto → .08 al centro → .82 in basso)` — chiude alto e basso
3. `rgba(63,58,51,.15)` piatto — unisce cromaticamente scene diverse (balcone verde, cucina bianca, marmo)

più, sul video, una gradazione `contrasto 1.07 · luminosità −0.05 · saturazione 0.90`: è quello che toglie
l'aria da catalogo alle riprese e le porta sul caldo del brand.

Sotto ogni riga di testo, tre ombre stratificate (`0 3px 10px .68`, `0 12px 44px .55`, `0 1px 2px .85`):
è la parte che rende il bianco leggibile anche sul legno chiaro del balcone.

## Le fonti visive, scena per scena

| Scena | Sorgente | Nota |
|---|---|---|
| 1-2 | `brand-assets/video/clean/interno-cucina.mp4` | interno reale, movimento appena percettibile |
| 3 | `brand-assets/video/clean/balcone.mp4` | balcone reale con poltrona sospesa |
| 4 | `brand-assets/immobili/salotto-divano-azzurro.jpg` | ritaglio sul divano, avvicinamento lento |
| 5 | `brand-assets/immobili/cucina-soggiorno-open-space.png` | ritaglio spostato a sinistra per tenere il tavolo |
| 6 | `brand-assets/video/clean/busto-frontale.mp4` | il marchio come immagine, non come logo |

Alternanza voluta: video, video, foto, foto, video. Due foto di fila spezzano la ripetizione dei movimenti
generati delle clip e alzano la nitidezza a metà video, dove l'attenzione cala.

## Pattern grafico (per non ripeterlo)

**Pattern "una frase al centro sul reale"**: nessun blocco, nessuna card, nessun numero grande. Solo fotografia
+ velo + una riga. È il primo contenuto Hadrianus costruito così — tutti i precedenti avevano struttura
(scontrino, blocchi invertiti, calendario, card recensione, planimetria). Da non riusare nella prossima
campagna: registrato in `.claude/reference/design-system.md`.
