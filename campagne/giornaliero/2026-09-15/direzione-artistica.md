# Direzione artistica — 15 settembre 2026

Pilastro **Il metodo** · angolo **Il calendario di Roma**.

## Firma visiva del giorno: la riga di calendario

Una fila di sette celle quadrate (una settimana) con le **date calde piene d'oro** e le
altre in fumè. È l'unico elemento grafico nuovo del giorno e torna su ogni artboard con
un numero diverso di celle piene, così il carosello ha una progressione leggibile anche
senza leggere il testo:

| Artboard | Celle piene | Che cosa dice |
|---|---|---|
| C1 Main | 2 su 7 | non tutte le notti valgono uguale |
| C4 | 6 su 7, una con `?` | il buco fra due prenotazioni |
| C5 | 7 su 7 | il calendario pieno, tenuto da noi |
| S1 | 2 al centro | i due giorni del ponte |
| S2 | 3 consecutive | i tre giorni di fiera |

Deliberatamente **diversa** dai pattern già usati (binario delle scadenze, tendina che
attraversa, scontrino, blocchi invertiti, step numerati, card Q&A) — preferenza fissa 5.

## Palette e tipografia

Fumè `#2E2A25` / `#3F3A33`, oro `#C8A24B`, sabbia `#F5F0E6`. Archivo per i titoli e i
numeri di passaggio, Manrope per il corpo. Nessun blu navy.

## Foto

Tre scatti di case vacanza **senza oggetti personali né disordine**, come richiesto dal
titolare: camera con letto rifatto e asciugamani, cucina/pranzo, camera con vista mare.
Ritagliati in 9:16, 4:5, 1:1 e in fascia.

**Velo, non ombra.** Le grafiche su foto usano due veli sovrapposti. Le storie hanno un
velo dedicato (`VELO_STORIA`), più piatto e più denso di quello del carosello: sono alte
1920 e portano testo su quasi tutta l'altezza, quindi la fascia chiara a metà del velo
del carosello lasciava il corpo bianco su parete e lenzuola chiare.

## Formati

- Carosello 5 slide 1080×1350 (4:5)
- Facebook: F1 **1080×1920 (9:16)**, F2 e F3 1080×1080 — la prima è 9:16 perché nel
  collage Facebook un 4:5 viene tagliato ai lati (preferenza fissa 6)
- Storie 1080×1920, autoconclusive: ognuna ha problema, soluzione e CTA

## Reel

18,0 s · 1080×1920 · H.264 30fps. Struttura C di `.claude/reference/reel-virali.md`:
frame 0 già in movimento, tre interrupt nei primi due secondi, cadenza delle notifiche
che accelera (600 → 500 → 400 → 320 ms), stacchi a taglio secco, micro-pausa dopo il
picco, onda diagonale che riempie il calendario a 12,2 s, evidenziatore oro che corre su
"lo teniamo noi", loop di stato verificato (frame 0 ≡ frame 17,95).
