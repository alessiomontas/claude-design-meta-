# Framework prompt grafici — Hadrianus

Scopo: generare immagini di livello professionale con Midjourney v6.1+, DALL·E 3, Leonardo, Firefly.
Claude non produce pixel: **produce il prompt**. La qualità dell'immagine è interamente decisa qui.

Regola zero: **un prompt vago produce un'immagine amatoriale.** Ogni prompt esce completo di tutti e cinque i
blocchi sotto. Un prompt senza blocco 2 (composizione) o senza blocco 5 (negative) non si consegna.

---

## I 5 blocchi obbligatori

| # | Blocco | Cosa contiene | Perché |
|---|---|---|---|
| 1 | **Subject** | soggetto, materiali, epoca, contesto geografico | evita il "generico da stock" |
| 2 | **Composition** | inquadratura, obiettivo, regola dei terzi, **zona vuota dichiarata per il testo** | è ciò che rende l'immagine usabile come grafica invece che come fotina |
| 3 | **Aesthetic & Lighting** | ora del giorno, direzione della luce, color grading, palette brand | fa la differenza fra "reso AI" e "servizio fotografico" |
| 4 | **Technical** | corpo macchina, focale, diaframma, pellicola/resa | ancora il realismo |
| 5 | **Negative** | cosa escludere | rimuove i tell dell'AI a basso costo |

Più il **blocco parametri** (aspect ratio, versione, stile, seed).

---

## Blocco 2 — la zona vuota va dichiarata, sempre

Il testo si sovrappone **dopo**, nell'artboard. L'immagine deve nascere con lo spazio già libero. Si scrive
dentro il prompt con formule che i generatori capiscono:

| Posizione testo | Formula da usare nel prompt |
|---|---|
| Alto | `the upper third of the frame is empty negative space: plain wall and ceiling, nothing to read` |
| Centro | `uncluttered horizontal band across the middle of the frame, low detail, no objects at eye level` |
| Basso | `foreground floor area left empty, clean and unobstructed, lower third free of furniture` |
| Laterale | `subject pushed to the right third, left third empty` |

Corredato da: `composition follows the rule of thirds`, `generous headroom`, `shot on a tripod, camera perfectly level, vertical lines straight`.

**Mai** chiedere testo dentro l'immagine. I generatori sbagliano l'italiano (accenti, doppie, apostrofi) e il
risultato è irrecuperabile. In negative va sempre `text, letters, words, watermark, logo, signage, captions`.

---

## Blocco 3 — lock di brand (non negoziabile)

Ogni prompt Hadrianus porta questa riga, adattata al soggetto:

```
warm smoky-grey and sand colour palette, muted olive and brass accents,
golden hour light, soft directional sunlight from a side window,
warm neutral white balance, low saturation, gentle film-like contrast
```

**Vietato**: qualsiasi formula che porti al blu. Niente `cool tones`, `blue hour`, `navy`, `moody blue`,
`teal and orange`. Il navy è escluso per decisione fissa del titolare — va anche in negative.

Riferimenti cromatici da citare quando serve precisione: fumè `#3F3A33`, fumè scuro `#2E2A25`,
oro `#C8A24B`, sabbia `#F5F0E6`.

---

## Blocco 4 — ancore di realismo

Sono ciò che separa un'immagine pubblicabile da una riconoscibilmente artificiale.

| Tipo di scatto | Formula tecnica |
|---|---|
| Interni immobiliari | `shot on Canon EOS R5, 16-35mm at 20mm, f/8, ISO 200, architectural interior photography, natural light only` |
| Dettaglio / still life | `shot on Sony A7RIV, 90mm macro, f/2.8, shallow depth of field` |
| Esterni / territorio | `shot on Leica Q2, 28mm, f/5.6, golden hour` |
| Ritratto (ospite, proprietario) | `85mm portrait lens, f/1.8, natural window light, candid, not looking at camera` |

Aggiungere sempre: `photorealistic, real estate listing photography, no CGI look`.

---

## Blocco 5 — negative prompt standard Hadrianus

Copiare integralmente, poi aggiungere le esclusioni specifiche della scena.

```
--no text, letters, words, watermark, logo, signage, captions, subtitles,
distorted furniture, warped perspective, bent walls, tilted horizon,
extra limbs, deformed hands, mannequin faces, plastic skin,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting
```

Note su due voci:
- `visible brand appliances, TV screens with content` — marchi di terzi dentro una grafica commerciale sono un
  problema di conformità già emerso su `smart-tv-streaming-mockup.jpg`. Si escludono a monte.
- `blue tones, navy` — vedi lock di brand.

---

## Blocco parametri

| Destinazione | Formato | Stringa |
|---|---|---|
| Reel / storia / 1ª immagine Facebook | 9:16 | `--ar 9:16 --v 6.1 --style raw --s 150` |
| Post feed Instagram | 4:5 | `--ar 4:5 --v 6.1 --style raw --s 150` |
| 2ª e 3ª immagine Facebook | 1:1 | `--ar 1:1 --v 6.1 --style raw --s 150` |
| Piano di sfondo per scena reel | 9:16 | `--ar 9:16 --v 6.1 --style raw --s 100` (stile basso: lo sfondo non deve competere col testo) |

**Coerenza dentro una campagna** — obbligatoria, altrimenti le immagini sembrano prese da tre case diverse:
- stessa `--seed` su tutte le immagini della stessa campagna;
- oppure `--sref <url prima immagine approvata>` sulle successive;
- stessa ora del giorno, stessa direzione della luce, stessa focale in tutti i prompt della serie.

DALL·E 3 e Firefly non hanno `--seed`: si replica la coerenza ripetendo **alla lettera** i blocchi 3 e 4 in ogni
prompt della serie.

---

## Tre tipi di output, tre prompt diversi

| Tipo | Cosa serve | Differenza nel prompt |
|---|---|---|
| **A · Grafica singola** (post, storia) | immagine + testo sovrapposto nell'artboard | zona vuota ampia, `--s 150` |
| **B · Piano di sfondo per scena reel** | deve reggere un velo scuro e testo grande | `--s 100`, scena più semplice, meno oggetti, luce più piatta |
| **C · Artboard editabile** | **nessuna immagine generata**: è HTML/CSS | non si usa questo framework, si usa `design-system.md` |

---

## Vincolo di conformità sulle immagini generate

**Un'immagine generata non è mai un immobile in gestione.** Non si presenta, non si didascalizza e non si lascia
intendere come "una casa che gestiamo": chi risponde all'annuncio poi visita le case vere, e la distanza si paga.

Due modi leciti di usarle:
1. come **ambientazione/mood**, senza alcuna affermazione di possesso o gestione;
2. **dichiarandolo nel contenuto stesso** — precedente già in produzione: il reel da 29 secondi apre con
   *"Questa casa non esiste. Lo standard, sì."* (`campagne/reel-standard-alberghiero/`).

Quando esiste una foto reale pertinente in `brand-assets/immobili/`, **la foto reale vince sempre** sulla
generata. Le generate servono dove il reale non c'è.

---

## Dialetto per generatore — il prompt va tradotto, non copiato

I cinque blocchi restano identici. Cambia **la sintassi**, e sbagliarla è il modo più rapido di ottenere
un'immagine mediocre: un `--no` incollato dentro Gemini diventa testo che il modello prova a interpretare.

| | Midjourney / Leonardo | **Gemini (scelto dal titolare)** |
|---|---|---|
| Formato | `--ar 9:16` | a parole: *"Generate a vertical 9:16 image"*, come **prima riga** |
| Negative | `--no x, y, z` | a parole: *"Avoid completely: x, y, z"*, come **ultimo paragrafo** |
| Stile | `--style raw --s 150` | *"photographic, not illustrative; no stylisation"* |
| Seed | `--seed 774120` | non esiste: si ripetono i blocchi 3 e 4 **alla lettera** in ogni prompt della serie |
| Lunghezza | compatta | Gemini regge prompt lunghi e strutturati: **scrivi tutto per esteso, in frasi complete** |

**Struttura del prompt per Gemini** — cinque paragrafi, in quest'ordine:

1. `Generate a vertical 9:16 photograph.` + soggetto e contesto
2. Composizione, con la **zona vuota dichiarata** ("the central horizontal band of the frame must stay empty…")
3. Luce e colore, con il lock di brand
4. Dati tecnici (macchina, focale, diaframma)
5. `Avoid completely:` + tutte le voci del negative standard

Vincolo che vale su Gemini più che altrove: **mai chiedere testo dentro l'immagine.** Gemini *sa* scrivere, e
quindi ci prova — producendo italiano sbagliato dentro una grafica commerciale. Il testo si sovrappone dopo,
nell'artboard.

## Il giro di lavoro con Gemini + Google Drive

Gemini non è collegabile come connettore (verificato nel registro: non esiste). Google Drive sì, ed è già
collegato. Quindi:

1. Claude scrive il prompt nel dialetto Gemini, dentro il Master Template
2. Il titolare lo incolla su **gemini.google.com**, genera, sceglie
3. Salva l'immagine in una cartella Drive dedicata — **`Hadrianus/generate/`**
4. Dice a Claude il nome del file
5. Claude la scarica da Drive, la monta nell'artboard o nella scena del reel, renderizza il PNG e fa i sei
   controlli di qualità prima di mostrarla

Regola già in vigore: **Claude apre Google Drive solo quando gli viene detto esplicitamente.** Il passaggio 4
non è una formalità, è quello che autorizza la lettura.
