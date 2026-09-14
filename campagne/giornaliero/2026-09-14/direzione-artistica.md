# Direzione artistica — giornata 14/09/2026

**Pilastro:** l'obiezione · **Angolo:** l'esposizione amministrativa ("la casella dimenticata")

## Mood

**Calmo, sequenziale, inevitabile.** Non allarmistico: l'angolo parla di sanzioni e scadenze, e la tentazione sarebbe il registro rosso-urgente. Sarebbe l'errore — tradirebbe il tono dei `riferimenti/` e confermerebbe l'obiezione "mi state spaventando per vendere". Il visivo fa il contrario: mostra che il tempo passa **con ordine**, e che qualcuno lo sta contando.

## Impianto: "il binario delle scadenze"

Struttura nuova per il brand, nata dall'angolo stesso — una catena di atti, ognuno con la sua ora.

| Elemento | Cosa fa |
|---|---|
| **Marca temporale** in alto a sinistra: trattino oro 28 px + testo 17 px Manrope 600 maiuscolo, tracking 8 | Dice *quando* siamo nella catena (`T ZERO`, `01 · PRIMA CHE L'ANNUNCIO SIA ONLINE`, `ALL'ARRIVO · +24:00`, `FINE MESE`). È la firma grafica della giornata |
| **Arco di avanzamento** in basso a destra, che si chiude di slide in slide | Rende visibile la progressione senza numerare le slide |
| **Anello chiuso** dentro la pill CTA finale | La catena che si chiude: chiusura visiva dell'argomento |
| **Filo orizzontale** sottile prima della riga di risposta | Separa il problema dalla presa in carico, senza card né box |
| **Binario** del reel: filo 322 px sotto il marchio, con barra oro che si riempie sui 15,4 s | L'orologio del copy, reso senza mai disegnare un orologio |

**Perché è diverso dai precedenti.** I pattern già bruciati sono: scontrino/ledger (`fai-da-te-vs-gestione-professionale`), blocchi invertiti a piena larghezza (`facebook-lungo-vs-breve`), step numerati giganti e card domanda/risposta (`instagram-fiducia`), griglia 2×2 dei servizi (`gestione-case-vacanza`). Qui non c'è nessuna card, nessun numero gigante, nessuna griglia: l'unica costante è **una marca temporale e un arco**. L'informazione è ancorata a sinistra su una colonna sola, e la gerarchia la fa il corpo del testo, non un contenitore.

## Palette

Nessuna deviazione: fumè profondo `#2E2A25`, fumè `#3F3A33`, fumè medio `#4a443a`, oro `#C8A24B`, oro scuro `#b3892f` (solo su fondo chiaro), sabbia `#F5F0E6`. Testi chiari `#d8d2c4` / `#b7ad9a`, testi scuri `#26241F` / `#46423a`.

**L'oro è riservato a due cose sole**: la marca temporale e la frase che chiude l'obiezione. Non decora — segna il tempo e la promessa.

**F2 è l'unica artboard su fondo chiaro** (sabbia pieno): è la slide di puro servizio, quella che spiega la catena in tre momenti. Il cambio di fondo la stacca dalle altre due immagini Facebook e le dà l'aria del documento consultabile, non dell'annuncio.

## Lock di brand sulle foto

Tutte le immagini passano per un filtro prima del velo: `saturate(0.72) sepia(0.14) brightness(0.90) contrast(1.06)`.

Senza, i verdi del balcone e i bianchi freddi degli interni dominano e la grafica legge "smunta" — il difetto già bocciato dal titolare. Il filtro sta nella funzione `foto()` di `grafiche/build.py`, quindi vale per ogni immagine di ogni giornata futura.

I veli sono stati rinforzati **soprattutto nella fascia centrale** (0,44-0,52 di opacità contro gli 0,20 iniziali), perché è lì che cade il testo: più velo, non più ombra.

## Formati prodotti

| Blocco | Artboard | Formato |
|---|---|---|
| `Main`, `R1b2`-`R1b9` | 9 battute del reel | 1080×1920 |
| `C1`-`C5` | carosello | 1080×1350 |
| `F1` | Facebook 1ª immagine | 1080×1920 (mai 4:5: nel collage verrebbe tagliata) |
| `F2`, `F3` | Facebook 2ª e 3ª | 1080×1080 |
| `S1`, `S2` | storie autoconclusive | 1080×1920 |

## Provenienza delle immagini

- **`brand-assets/`** — fotogrammi delle clip reali del brand: balcone, interno cucina, busto di Adriano, logo bronzo.
- **Adobe Stock, licenziate in full resolution** — la scena notturna delle battute 5-7 del reel e della storia 2, e l'ingresso di giorno di `F1`: scene che `brand-assets/` non copre.
- **Nessuna immagine generata da IA.** In questo ambiente la generazione da testo non è disponibile (il connettore Adobe ha la parte generativa disattivata). I `PROMPT GRAFICO` in inglese restano dentro `copy.md` per rigenerare le scene altrove, se il titolare vorrà.

## Elementi chiave

Cosa si nota per primo, in ordine: **la marca temporale** (dice dove sei nella catena) → **la riga grande** (il fatto) → **l'oro** (la presa in carico) → **la CTA**. Nel reel l'ordine è: barra che si riempie → riga unica al centro ottico → chiusura su logo.

## Da evitare

- Orologi disegnati, calendari, documenti, timbri: il tempo si rende con la barra e la marca temporale, mai con l'icona letterale. Sarebbe la grafica da studio legale che il brief vieta.
- Rosso, arancio, semafori, punti esclamativi: allarmismo.
- Importi di sanzione in grafica: confermati solo con riserva sulla singola fattispecie.
- Blu navy, in qualunque forma.

## Controllo qualità

I sei controlli di `master-template.md` sono stati fatti sui PNG renderizzati, a dimensione telefono. Due difetti trovati e corretti prima della consegna:

1. **`F2`** — la marca temporale `DURANTE E DOPO` era appoggiata alla riga sopra (17 px contro i ~50 delle altre sezioni). Causa: lo stacco marca→testo era fissato, ma i blocchi a tre righe sono più alti e, essendo centrati, risalgono. Corretto calcolando lo stacco sull'altezza del blocco.
2. **Reel e artboard con foto** — velo troppo debole proprio nella fascia centrale dove cade il testo, con la foto del balcone che restava verde e luminosa. Corretto con il lock di brand sulle foto e il rinforzo dei veli descritti sopra.

## File

- `grafiche/` — 19 artboard `.dc.html` editabili + `canvas.json` + `build.py` (rigenera tutto) + le foto
- `png/` — i 19 export
- `reel/reel.mp4` — 15,43 s, H.264, 1080×1920, 30 fps, montato dalle 9 battute (`battute.json` tiene i tempi)
