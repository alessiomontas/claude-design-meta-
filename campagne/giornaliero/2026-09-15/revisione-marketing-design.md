# Revisione marketing & design — Giornaliero 2026-09-15 (martedì · IL METODO)

## Giudizio complessivo
**PRONTA CON RITOCCHI** — angolo forte, salvabile e mai usato; si perde nell'ultimo metro: le due storie non portano l'offerta, tre artboard hanno vuoti/contrasti fuori standard e il reel dice di cosa parla solo dopo 1,1 s.

## Punteggio per dimensione
| Dimensione | Giudizio | Nota chiave |
|---|---|---|
| Impaginazione/layout | ⚠️ | Main e F1 falliscono il controllo 3 (vuoti > 260 px) e il 4 (contrasto in fondo) |
| Contenuti/struttura | 👍 | Progressione gancio → date → metodo → buco → offerta regge; manca solo l'urgenza datata |
| Grafiche/foto | ⚠️ | Firma "riga di calendario" nuova ma illeggibile come calendario; foto di Main slavata sotto il testo |
| Testi | 👍 | Tono giusto, CTA unica; da rinforzare cosa si ottiene scrivendo CALCOLO |
| Efficacia commerciale | ⚠️ | Le due storie chiudono senza 15% né simulazione gratuita: rischio percepito non abbassato |

## Interventi prioritari (in ordine di impatto)

1. **S1 e S2 — rimettere l'offerta prima della CTA.** `grafiche/build.py`, artboard S1 e S2: nei PNG manca il blocco 4 previsto da `copy.md` ("è dentro il 15%…"). Le storie sono il formato che porta più DM e oggi chiedono di scrivere senza dire cosa si riceve. Inserire una riga sopra la CTA: `Dentro il 15%, con check-in smart H24 e pulizie in standard alberghiero.` (Manrope 600, 33, `#E6DFD4`).
2. **CTA — dire cosa si ottiene, ovunque compaia.** C5, F3, S1, S2: sotto la banda oro sostituire/affiancare alla firma la riga `Simulazione gratuita del rendimento.` La firma "Guadagniamo solo se guadagni tu." resta, ma sopra la CTA, non sotto.
3. **Urgenza datata (oggi manca del tutto il "perché ora").** Su C5 e S2, una riga fattuale sopra la CTA: `La prima data è fra cinque settimane.` Nessun claim, solo calendario: è la leva che trasforma il salvataggio in DM.
4. **Main (C1) — vuoto e contrasto.** Fascia vuota di ~330 px fra il corpo (y 900) e `→ SCORRI` (y 1230): fallisce il controllo 3. E `→ SCORRI` è oro su pavimento chiaro: fallisce il 4. Alzare gancio+corpo di 60 px, portare la riga di calendario sotto il corpo come conferma visiva, e chiudere il velo in basso (ultimo stop da `.90` a `.96`).
5. **F1 — 350 px morti sotto "SALVA QUESTO POST" e nessuna CTA.** È la prima immagine del collage Facebook, quella che viene guardata per intera: allungare la card date di 40 px per riga e chiudere con una banda oro `SCRIVI CALCOLO IN DM` a y 1600-1690 (dentro safe area).
6. **La firma del giorno non si legge come calendario.** Le sette celle sono quadrati astratti. Aggiungere le iniziali dei giorni (`L M M G V S D`, Manrope 700, 24, `#9A8A63`) sopra la riga e i numeri sulle celle piene: su S2 `23 24 25`, su S1 `7 8`, su Main le due celle devono corrispondere a `23 ottobre` e `3 novembre` citate nel corpo — oggi sono in posizione 3 e 6, scollegate dal testo. È l'intervento che rende la slide screenshottabile.
7. **F2 è diventato un elenco di titoli, contro la trappola del martedì.** Quattro righe senza riga di dettaglio = elenco di servizi. Rimettere sotto ogni titolo la riga corta di C3 (`Fiere, festival, ponti, feste.` ecc., Manrope 600, 28): riempie anche i ~200 px vuoti sopra il filo oro.
8. **C5 — allineare al copy approvato.** Nel PNG mancano il badge `15% sul fatturato generato` e le spunte oro: i 5 servizi sono una riga corrente con i `·`, difficile da leggere in 2 secondi. Ripristinare badge + elenco a spunte come da `copy.md` §C5, e portare "Guadagniamo solo se guadagni tu." da oro spento (illeggibile al 30%) a `#E6DFD4`.
9. **Reel — il gancio arriva tardi.** `reel/build_reel.py`: `gancio` parte a 1,099 s. Anticiparlo a **0,55 s** (subito dopo la seconda notifica) e spostare la terza notifica a 1,0 s: i primi due secondi restano pieni, ma lo spettatore sa di cosa si parla al primo.
10. **Reel — il blocco fasi non accelera.** `FASI` a 5,0/6,6/8,2/9,8 = 1,6 s fisso per 6,4 s, il tratto più lento del video dopo un'apertura che accelera. Portare a 5,0 / 6,5 / 7,9 / 9,2 e anticipare di 0,6 s tutto ciò che segue: il reel chiude a ~17,4 s, più asciutto.
11. **C3 — gerarchia del numero.** Le righe di dettaglio vanno a capo e il numero oro `01` resta disallineato rispetto al titolo. Allineare il numero alla prima riga del titolo (`align-items:flex-start`) e accorciare i dettagli a riga unica (es. 01 → `Fiere, festival, ponti. Prima della casa, la città.`).
12. **Caption del reel — togliere l'elenco dei cinque servizi.** Il pilastro di oggi è il metodo: lasciare l'elenco completo solo sul carosello e su Facebook, nel reel tenere `Dentro il 15%, e a fine mese ricevi il bonifico netto.`

## Cosa funziona già bene (da non toccare)
- C2: è la slide che si salva. Gerarchia, card, contrasto e ritmo delle quattro date sono giusti così.
- C4: la notte-buco è il pezzo di metodo meglio raccontato del pacchetto, e la cella con `?` fa il lavoro da sola.
- La scelta di non mettere tariffe a schermo: rende il contenuto credibile e citabile.
- La CTA a commento sulla zona nella caption Facebook: è il motore di micro-viralità del pacchetto.
- Firma visiva diversa da tutti i pattern in `design-system.md` (binario, tendina, scontrino, 12 caselle, blocchi invertiti): regola "varia il design" rispettata.

## Suggerimenti opzionali (nice-to-have)
- Copertina reel dedicata: C2 con il titolo "Le date da segnare" funziona meglio del frame 0 nel feed.
- In C2, marcare `1° novembre` con un micro-tag oro `DOMENICA`: il dettaglio controintuitivo è ciò che fa commentare.
- Aggiungere il pattern del giorno alla tabella di `design-system.md` come "riga-settimana con celle accese".
