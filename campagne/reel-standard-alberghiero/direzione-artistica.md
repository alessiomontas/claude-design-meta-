# Direzione artistica — reel "Lo standard alberghiero"

**Sei scene editabili:** https://claude.ai/code/artifact/fb199a63-fd44-421c-99a3-0ee89c443c20
`grafiche/Main.dc.html` è la scena 1, poi `S2` … `S6`. Ogni artboard ha sfondo, velo, marchio con barra e testi
separati e modificabili.

## Come sono state scelte le posizioni dei testi

Il video di partenza è già un pezzo di design finito: interni curati, luce calda, transizioni proprie. Scrivere
sopra "a occhio" avrebbe coperto quello che lo rende bello. Quindi il posizionamento è stato **misurato**, non
deciso a sentimento:

1. **Mappa del movimento.** Differenza media fra fotogrammi consecutivi su tutta la durata, per separare le
   finestre ferme dalle transizioni. Risultato: sei inquadrature ferme
   (0,4-4,1 · 5,0-8,7 · 9,9-13,6 · 15,0-18,6 · 20,0-24,1 · 27,7-29,2) separate da transizioni a pannelli lunghe
   fra 0,4 e 1,1 s. **Nessun testo cade su una transizione**: entrerebbe e uscirebbe mentre l'immagine slitta.
2. **Mappa del dettaglio.** Per ogni inquadratura, energia dei bordi e luminanza media divise in otto fasce
   orizzontali. Le fasce con dettaglio sotto il 75% della media sono quelle dove il testo non copre niente.

Quello che ne è uscito, fascia per fascia:

| Inquadratura | Fascia più vuota | Dove è finito il testo | Perché |
|---|---|---|---|
| 1 · mosaico | dettaglio uniforme, immagine scura (lum 82) | **centro**, y 735-1130 | l'unica scura abbastanza da reggere il testo al centro; è anche il gancio, e il centro è la posizione che ferma lo scroll |
| 2 · salotto | y 240-480 (det 14,1 · media 19,5) | **alto**, y 350-620 | sotto ci sono divano, tavolino e la veduta della cupola: intoccabili |
| 3 · cucina | y 240-480 (det 10,7 · media 18,4) | **alto** | la fascia y 720-960 è la più piena del video (det 27,6): lampade e piano |
| 4 · camera | y 240-480 (det 15,0) | **alto** | il letto occupa y 1200-1440 (det 26,7) |
| 5 · bagno | y 1440-1680 (det 13,6) e y 240-480 (det 15,3) | **alto** | la fascia bassa è più vuota ma finisce sotto l'interfaccia di Instagram: scartata |
| 6 · busto | y 1440-1680 (det 6,1, la più vuota di tutto il video) | **basso**, y 1235-1660 | il volto sta in alto e non va coperto: il testo sta sul petto |

Il testo in alto per quattro inquadrature di fila non è pigrizia: è la scelta che tiene **il volto del video —
divano, cucina, letto, vasca — sempre libero**, e dà all'occhio un punto fisso dove tornare a leggere.

## I tre veli

Tre soli, ciascuno costruito per la posizione del testo che deve reggere:

| Velo | Dove | Costruzione |
|---|---|---|
| **alto** | 4,6 → 24,7 s | `linear-gradient(180deg, rgba(38,34,29,.90) 0%, .80 18%, .58 34%, .26 50%, .06 62%, 0 72%)` — scuro sopra, sparito prima della metà: la parte bella dell'immagine resta pulita |
| **centro** | 0 → 5,1 s | radiale al centro (`rgba(24,21,17,.70)`) + una velatura verticale leggera: serve solo al gancio |
| **basso** | 24,7 → fine | lo stesso gradiente del velo alto, ribaltato |

I veli si incrociano in dissolvenza (0,4-0,9 s) sulle transizioni del video, così non si vede mai un velo
comparire su un'immagine ferma.

## Tipografia

Identica alla serie: Archivo 900 a 70 px per il gancio e la chiusura, Archivo 800 a 66 px per le battute
centrali, Manrope 600 a 42 px per la riga secondaria, oro `#E2BE6C` a 58/44 px. Sotto ogni riga tre ombre
sovrapposte. Massimo due righe per battuta.

**Il ritmo a due tempi** è la novità di questo reel: ogni inquadratura dura 3,4-4,2 s, troppo per una riga sola.
Quindi la riga grande entra subito e **la riga secondaria entra 1,8 s dopo**, dentro la stessa inquadratura. Si
leggono due volte invece di una, e l'attenzione non cala nel mezzo.

## Barra di avanzamento

Il filo sotto `HADRIANUS` è il binario; una barra oro lo riempie **a sei scatti**, uno per inquadratura (14% →
29% → 46% → 63% → 82% → 100%). Su 29 secondi serve più che sui 15: dice quanto manca.

## Audio

**Il video arriva con la sua musica e l'audio è stato conservato così com'è.** Il montaggio ricostruisce solo la
traccia video e poi rimonta l'audio originale senza ricodificarlo: nessuna giuntura, nessun click.

## Nota sul materiale

Gli interni sono **immagini generate**, non immobili in gestione. Non compaiono marchi di terzi. L'unico modo
onesto di usarli in un contenuto di acquisizione era dichiararlo, ed è esattamente quello che fa il gancio —
vedi `copy.md`, sezione "Il problema che questo video poneva". Se un domani questo reel viene rimontato con altri
testi, **quella dichiarazione va tenuta**.

## Pattern grafico

**"Testo nello spazio vuoto misurato" + ritmo a due tempi.** Terzo pattern della serie reel, distinto dagli altri
due: il primo mette la frase al centro esatto, il secondo aggiunge la barra su 15 secondi, questo posiziona il
testo **dove l'immagine lo consente** e raddoppia le entrate. Da usare quando il video di partenza è già un
lavoro di design finito e non va coperto. Registrato in `.claude/reference/design-system.md`.
