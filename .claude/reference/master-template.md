# Master Template — formato fisso di ogni contenuto

Da oggi **ogni** contenuto (post, storia, carosello, scena di reel, annuncio) si consegna in questo formato.
Nessuna variante, nessuna aggiunta discorsiva. Se un blocco non si applica, si scrive `—`, non si elimina.

---

## Il template

```
### [ID] · [canale] · [formato px] · [ruolo nel funnel]

**COPY**
Gancio      | <max 50 caratteri>
Corpo       | <max 2 righe, max 40 caratteri per riga>
CTA         | <max 25 caratteri>
Caption     | <solo per post; 4-6 righe>

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| ... | ... | ... | ... | ... | ... |
Griglia: margine 64 px · colonna utile 952 px · safe area 180 px alto, 320 px basso
Velo: <formula CSS esatta>

**PROMPT GRAFICO (EN)**
<blocco unico copiabile, 5 blocchi del framework in fila>

**NEGATIVE**
<blocco standard + esclusioni della scena>

**PARAMETRI**
--ar <x:y> --v 6.1 --style raw --s <n> --seed <n campagna>

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | ... | CONFERMATO / DA VERIFICARE / lessico di brand |
```

---

## Esempio compilato

```
### P1a · Facebook · 1080×1920 · gancio freddo

**COPY**
Gancio      | Il valore di casa tua lo sai.
Corpo       | Quanto rende ogni mese
            | non te lo dice nessuno.
CTA         | Scrivi "STIMA" nei commenti
Caption     | —

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| gancio | 860-1010 | riga 1 | Archivo 900 | 70 | #FFF |
| corpo | 1050-1200 | righe 2-3 | Archivo 800 | 62 | #FFF |
| CTA | 1290-1350 | banda oro | Manrope 600 maiusc. | 31 | #2E2A25 su #C8A24B |
Griglia: margine 64 px · colonna utile 952 px · safe area 180/320
Velo: radial-gradient(ellipse 88% 25% at 50% 50%, rgba(26,23,19,.60), transparent 62%),
      linear-gradient(180deg, rgba(38,34,29,.80) 0%, rgba(38,34,29,.08) 33%, rgba(38,34,29,.82) 100%)

**PROMPT GRAFICO (EN)**
Interior of a lived-in Roman apartment, mid-century furniture, travertine floor, olive linen
sofa, brass details, a balcony door open onto a quiet street --
composition follows the rule of thirds, camera perfectly level, vertical lines straight,
the central horizontal band of the frame is empty negative space with no objects at eye level,
generous headroom --
warm smoky-grey and sand colour palette, muted olive and brass accents, golden hour light,
soft directional sunlight from a side window, warm neutral white balance, low saturation,
gentle film-like contrast --
shot on Canon EOS R5, 16-35mm at 20mm, f/8, ISO 200, architectural interior photography,
natural light only, photorealistic, real estate listing photography, no CGI look

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, captions, distorted furniture, warped
perspective, bent walls, tilted horizon, oversaturated colours, HDR halos, blue tones, navy,
teal and orange grading, cluttered surfaces, visible brand appliances, TV screens with content,
3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
--ar 9:16 --v 6.1 --style raw --s 150 --seed 774120

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "quanto rende non te lo dice nessuno" | opinione di posizionamento, nessun dato |
| 2 | stima gratuita in commento | CONFERMATO |
```

---

## Griglia unica (vale per ogni artboard 1080×1920)

| Parametro | Valore |
|---|---|
| Margine laterale | 64 px (colonna utile 952 px) |
| Safe area alto | 180 px (interfaccia Instagram/Facebook) |
| Safe area basso | 320 px |
| Passo verticale | 20 px — ogni `top` è multiplo di 20 |
| Blocco testo centrato | centro ottico a y 960, mai più di 2 righe per blocco |

**Scala tipografica** (1080 px di larghezza): 70 · 62 · 50 · 45 · 40 · 33 · 31 · 17.
Fuori scala non si va. Se una riga non entra, si accorcia il testo, non si riduce il corpo.

Per 1080×1080: margine 64, safe area 0, centro ottico y 540, scala massima 62.

---

## Controllo qualità — prima di consegnare, non dopo

Nessun contenuto esce senza che questi sei punti siano verificati **sul PNG renderizzato**, guardato alla
larghezza di un telefono. Se anche uno solo fallisce, si corregge prima di mostrare.

| # | Controllo | Fallisce se |
|---|---|---|
| 1 | Centratura | un blocco è fuori asse di più di 8 px rispetto alla colonna utile |
| 2 | Troncature | una card, una banda o una riga tocca il bordo o esce dal frame |
| 3 | Vuoti | esiste una fascia vuota alta più di 260 px che non sia voluta |
| 4 | Contrasto | il testo non si legge su schermo ridotto al 30% — serve più velo, non più ombra |
| 5 | Safe area | qualcosa di leggibile sta sopra y 180 o sotto y 1600 |
| 6 | Marchi di terzi | elettrodomestici, schermi, loghi riconoscibili nell'inquadratura |

Storico dei rifiuti del titolare, da non ripetere: slide decentrata · card tagliata in basso ·
grafiche "smunte" (velo assente, foto slavata) · struttura senza gerarchia · proporzioni sbagliate.

---

## Contratto di output in chat

| Regola | |
|---|---|
| Formato | liste e tabelle. Mai paragrafi discorsivi |
| Preamboli | zero. Si parte dal contenuto |
| Spiegazioni di processo | solo se cambiano una decisione del titolare |
| Modifiche | si tocca **solo** l'elemento richiesto. Mai rigenerare una campagna intera per una riga |
| Consegna | file + link. Il ragionamento sta nei documenti della campagna, non in chat |
| Domande | raggruppate in fondo, max 3, solo quelle che bloccano |
