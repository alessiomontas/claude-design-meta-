# Copy v2 — Giornaliero lunedì 14 settembre 2026 · "TI HANNO SCATTATO LE FOTO COL TELEFONO"

> **Riscrittura integrale.** Sostituisce il pacchetto di `copy.md` (angolo burocrazia/CIN), **bocciato dal titolare**.
> `copy.md` resta come storico e **non va toccato**. Le storie `S1` e `S2` del pacchetto precedente **restano come sono**: questo file ne aggiunge due nuove, `S3` e `S4`.

**Angolo:** *"Ti hanno scattato le foto col telefono."* — la prima foto dell'annuncio decide se cliccano o scorrono.
**Meccanismo:** il confronto secco fra la foto amatoriale e la foto professionale. Il difetto è del fai-da-te, la soluzione è di Hadrianus: **il servizio fotografico è incluso nella gestione, non si paga a parte.**
**Registro:** commerciale e assertivo. Le cose che dipendono da noi si affermano come certe — *ti garantiamo, ti assicuriamo, con noi la tua casa…*
**Chiusura obbligatoria:** ogni contenuto finisce sul **valore che dà Hadrianus**. Mai sul peso che resta al proprietario.

### Le tre correzioni rispetto al pacchetto bocciato (non riaprirle in revisione)

| # | Cosa è stato bocciato | Cosa fa questo pacchetto |
|---|---|---|
| 1 | La burocrazia come gancio: parla di rogne, non di guadagno | Gancio su ciò che fa cliccare l'annuncio. Zero CIN, zero adempimenti, zero sanzioni: **la parola "burocrazia" non compare mai** |
| 2 | Registro troppo prudente | Assertivo: *"ti garantiamo"*, *"ti assicuriamo"*, *"con noi la tua casa"*. I limiti restano solo su ciò che non dipende da noi |
| 3 | Note di demerito in chiusura (*"la responsabilità resta tua, il lavoro no"*) | **Bandite.** Quella frase e ogni sua variante sono fuori da questo pacchetto. Ogni pezzo chiude su cosa fa Hadrianus |

### Anti-ripetizione

`campagne/facebook-campagna-virale/` ha già usato "sei errori che fanno perdere prenotazioni", e il primo dei sei era **le foto** — ma come **una riga in un elenco testuale**. Qui il trattamento è opposto: **un solo punto, tutto un confronto visivo prima/dopo**, con una firma grafica nuova (la tendina). Nessun elenco di sei errori, in nessun contenuto.
I sei errori bruciati — **foto, prezzo fermo, risposte lente, calendario non aggiornato, descrizione, pulizia non standardizzata** — non compaiono in `S3` e `S4`, che usano due errori liberi: **minimo notti** e **orari di check-in**.

### Regola di onestà sul "prima" (vincolante, non negoziabile)

Il "prima" **non è la casa di un cliente vero**. È una **versione volutamente degradata di una foto reale** (`brand-assets/immobili/`), degradata da noi in post-produzione e **dichiarata come simulazione dentro il contenuto stesso**, con il chip oro `SIMULAZIONE` sempre visibile sulla metà "prima".
Precedente già in produzione nel brand: `campagne/reel-standard-alberghiero/` apre con *"Questa casa non esiste. Lo standard, sì."*
**Prima e dopo sono lo stesso file sorgente**: così la riga "Stessa stanza" è letteralmente vera, non una figura retorica.

---

## Canali e divisione dell'argomento

| ID | Canale | Formato | Pezzo dell'argomento |
|---|---|---|---|
| `R2` | Reel Instagram/Facebook | 1080×1920 · 15,6 s | **Il momento della scelta** — la tendina che scopre il prima/dopo |
| `K1`-`K5` | Carosello Instagram | 5× 1080×1350 | **Cosa rende una foto capace di vendere** — contenuto da salvare |
| `FB1`-`FB3` | Post Facebook | 1080×1920 + 2× 1080×1080 | **L'annuncio di valore** — utile anche a chi non chiamerà mai |
| `S3` | Storia Instagram (autoconclusiva) | 1080×1920 | **Errore: il minimo di notti troppo alto** |
| `S4` | Storia Instagram (autoconclusiva) | 1080×1920 | **Errore: il check-in a orari rigidi** |

**Convenzione ID:** volutamente diversa da quella di `copy.md` (`R1`, `C1-C5`, `F1-F3`, `S1-S2`) per non sovrascrivere né confondere i file grafici già prodotti per il pacchetto bocciato.

**Deviazioni dichiarate dal Master Template** (consapevoli, come nel file precedente):
1. il campo `Gancio` è sdoppiato in **Gancio A / Gancio B** — regola di progetto: sempre 2 varianti d'apertura;
2. nelle storie autoconclusive il campo `Corpo` porta **fino a 4 righe** (problema + consiglio), sempre entro 40 caratteri per riga: una storia deve chiudere da sola, mai su una seconda storia;
3. la caption di `FB3` supera le 6 righe: è un annuncio di valore per la community, il formato lo richiede. Caption del carosello e del reel restano brevi.

**Griglia 1080×1350** (non normata nel Master Template, dichiarata qui): margine 64 px · colonna utile 952 px · safe area 0 · centro ottico y 675 · passo 20 px · scala massima 70 (solo `K1`) e 62 (slide interne).

**Firma grafica della giornata — "la tendina che attraversa"** (pattern nuovo, non presente in `design-system.md` §"Pattern già usati"):
linea verticale oro da 6 px a tutta altezza con **maniglia circolare Ø 44 px** all'altezza del centro ottico. A **sinistra** della linea la foto corretta, a **destra** la simulazione degradata (velo `rgba(26,23,19,.26)` in più sulla metà destra). Nel carosello la linea **avanza di slide in slide** — x 216 → 432 → 648 → 864 → fuori bordo su `K5`, dove la maniglia si integra nella pill CTA. Nel reel la stessa linea è il movimento clou della scena 4. Dove la linea attraversa un blocco di testo, passa **sotto** e si attenua a `rgba(200,162,75,.35)`.

---

### R2 · Reel Instagram/Facebook · 1080×1920 · 15,6 s · gancio freddo → prova visiva → offerta

**COPY**
```
Gancio A    | Foto col telefono.
Gancio B    | Il tuo annuncio si gioca in una foto.
Corpo       | Stessa stanza. Altro annuncio.
            | Cambia chi tiene la macchina.
CTA         | Scrivi CALCOLO in DM
Caption     | Stessa stanza, due foto. La prima è una simulazione: una foto reale
            | rovinata apposta da noi. Non è la casa di nessun cliente.
            | Con noi il servizio fotografico è incluso nella gestione: la casa la
            | fotografiamo noi, l'annuncio lo scriviamo noi. Non lo paghi a parte.
            | Gestione completa, 15% sul fatturato generato.
            | Guadagniamo solo se guadagni tu.
            | Scrivi CALCOLO in DM per una simulazione gratuita.
```

**LAYOUT**

Zone fisse (valgono per tutte le scene):

| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| binario | 220-223 | filo orizzontale 322 px, centrato | — | — | rgba(245,240,230,.24) |
| barra avanzamento | 220-223 | barra oro che si riempie sui 15,6 s | — | — | #C8A24B |
| chip simulazione (scene 1-4) | 1500-1556 | SIMULAZIONE (x 700-1016, allineato a destra) | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B su rgba(26,23,19,.55) |
| testo 1 riga | 920-1000 | riga della scena | Archivo 900 | 70 | #FFF |
| testo 2 righe | 860-1060 | righe della scena | Archivo 900 | 70 | #FFF |
| tendina (scena 4) | 0-1920 | linea verticale 6 px + maniglia Ø 44 a y 960 | — | — | #C8A24B |
| riga oro (scena 9) | 1180-1240 | GUADAGNIAMO SOLO SE GUADAGNI TU | Archivo 800 maiusc. | 31 | #C8A24B |
| CTA (scena 9) | 1300-1360 | SCRIVI CALCOLO IN DM | Manrope 600 maiusc. | 31 | #F5F0E6 |

Griglia: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso · testo al centro esatto, mai allineato a sinistra
Velo: `radial-gradient(ellipse 92% 30% at 50% 48%, rgba(26,23,19,.62), transparent 64%), linear-gradient(180deg, rgba(46,42,37,.86) 0%, rgba(46,42,37,.20) 34%, rgba(46,42,37,.88) 100%), rgba(63,58,51,.28)`
Scala: 70 px, gradino alto del Master Template. Fuori scala non si va.

**SCENE — durata, testo, movimento** *(il movimento è obbligatorio in ogni scena: il reel precedente è stato bocciato perché era una sequenza di immagini ferme)*

| # | In → Out | Durata | Testo a schermo | Cosa si vede e **come si muove** |
|---|---|---|---|---|
| 1 · gancio | 0,0 → 1,6 | 1,6 s | **"Foto col telefono."** | La foto degradata è **già a schermo al fotogramma 1**: storta di 3,5°, scura, tagliata male. **Movimento:** micro-tremolio a mano libera (±6 px, 2 Hz) + la foto prova a raddrizzarsi e ricade. Il testo entra a 0,35 s da sotto, in 0,18 s. **Nei primi 0,8 s non c'è niente da capire: c'è da vedere una foto sbagliata che si muove.** |
| 2 | 1,6 → 3,2 | 1,6 s | **"È la prima cosa / che vede chi cerca."** | Stessa foto degradata, **push-in lento del 4%**. Le due righe entrano sfalsate (riga 1, riga 2 a +0,3 s). Tremolio ridotto a ±3 px |
| 3 | 3,2 → 4,8 | 1,6 s | **"E decide lì."** | **Scroll:** una colonna di riquadri fotografici scorre verticalmente veloce (900 px/s) e si **ferma di colpo** sulla foto storta, che rimbalza di 12 px. Nessuna interfaccia, nessun pulsante, nessun logo di piattaforma |
| 4 · clou | 4,8 → 7,0 | 2,2 s | **"Guarda."** (esce a 5,4 s) | **LA TENDINA.** A 5,4 s la linea oro da 6 px con maniglia circolare parte dal bordo sinistro e attraversa il fotogramma in **1,2 s** (curva ease-in-out), scoprendo **la stessa stanza fotografata bene**. Il chip `SIMULAZIONE` resta sulla metà destra e scompare con essa |
| 5 | 7,0 → 8,6 | 1,6 s | **"Stessa stanza. / Altro annuncio."** | Foto professionale piena, push-in lentissimo (2%). Le due righe entrano sfalsate di 0,25 s |
| 6 | 8,6 → 10,2 | 1,6 s | **"Cambia solo / chi tiene la macchina."** | **Pan orizzontale lentissimo** (3% della larghezza) sulla foto professionale |
| 7 · presa in carico | 10,2 → 12,0 | 1,8 s | **"Ti garantiamo / il servizio fotografico."** | Stacco netto su un **secondo ambiente** professionale che entra dal basso (slide-up 40 px, 0,3 s) |
| 8 | 12,0 → 13,6 | 1,6 s | **"Dentro la gestione. / Non lo paghi a parte."** | Stesso ambiente, fermo; **filo oro 3 px** che si allunga da sinistra a destra sotto la seconda riga in 0,5 s |
| 9 · chiusura | 13,6 → 15,6 | 2,0 s | **"Gestione completa. / 15% sul fatturato."** + riga oro + CTA | Fondo fumè pieno + logo bronzo. **Banda oro che sale** da sotto (0,35 s) e porta la CTA. Il video finisce di colpo: in loop riparte pulito sulla foto storta |

Totale **15,6 s** (dentro la finestra 12-18 s). Barra di avanzamento oro attiva: sopra i 10 s è prevista dal modello.

**PROMPT GRAFICO (EN)**
```
— per le scene 1-6: NESSUNA immagine generata.
  Sorgente unica: brand-assets/immobili/salotto-divano-azzurro.jpg (foto reale).
  "DOPO" = stessa foto, corretta: auto-tone, raddrizzamento, crop 9:16 sul soggetto.
  "PRIMA" = stessa foto, degradata da noi (ricetta nel blocco NEGATIVE).

— per le scene 7-8, se la foto reale non regge il 9:16, piano di sfondo generato (tipo B):

Second room of the same lived-in Roman apartment, walnut sideboard, olive linen armchair,
travertine floor, a balcony door open onto a quiet street, nobody in the room --
composition follows the rule of thirds, camera perfectly level on a tripod, vertical lines
straight, the central horizontal band of the frame is empty negative space with no objects
at eye level, generous headroom, lower third free of furniture --
warm smoky-grey and sand colour palette, muted olive and brass accents, golden hour light,
soft directional sunlight from a side window, warm neutral white balance, low saturation,
gentle film-like contrast --
shot on Canon EOS R5, 16-35mm at 20mm, f/8, ISO 200, architectural interior photography,
natural light only, photorealistic, real estate listing photography, no CGI look
```

**NEGATIVE**
```
--no text, letters, words, numbers, watermark, logo, signage, captions, subtitles,
app interfaces, buttons, search bars, platform UI, star ratings, price tags,
phone screens with interface, phone frames, hands holding a phone,
distorted furniture, warped perspective, bent walls, tilted horizon, people in frame,
extra limbs, deformed hands, mannequin faces, plastic skin,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
house numbers, street names, doorplates,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting

RICETTA DI DEGRADO del "PRIMA" (post-produzione su foto reale, Adobe):
rotazione -3,5° · esposizione -1,2 EV · bilanciamento del bianco spinto sul giallo (+900 K)
· crop volutamente sbagliato (soffitto tagliato, mobile tagliato a metà sul bordo destro)
· leggera sfocatura di movimento (2 px) · contrasto piatto.

COSA IL DEGRADO NON DEVE MAI FARE:
non aggiungere persone, non aggiungere disordine che nella casa reale non c'era,
non rendere la stanza irriconoscibile (prima e dopo devono leggersi come lo stesso ambiente),
non mostrare targhe, numeri civici, insegne o marchi di terzi,
non far sembrare che sia la casa di un cliente: il chip SIMULAZIONE resta sempre visibile.
```

**PARAMETRI**
`--ar 9:16 --v 6.1 --style raw --s 100 --seed 914026`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "È la prima cosa che vede chi cerca. E decide lì." | posizionamento, **nessun numero, nessuna statistica, nessun riferimento ad algoritmi** |
| 2 | "Stessa stanza" | **letteralmente vero**: prima e dopo sono lo stesso file sorgente |
| 3 | Il "prima" è una simulazione | **dichiarato in grafica** (chip oro per 4 scene su 9) e in caption. Vincolo di onestà, non rimovibile |
| 4 | "Ti garantiamo il servizio fotografico. Dentro la gestione. Non lo paghi a parte." | **CONFERMATO dal titolare 14/09/2026** |
| 5 | "Gestione completa. 15% sul fatturato." | CONFERMATO |
| 6 | "Guadagniamo solo se guadagni tu" | lessico di brand — alla lettera, solo in chiusura |
| 7 | "più prenotazioni", "annuncio sempre pieno", percentuali di clic | **assenti per scelta**: sono risultati di mercato, non li garantiamo |

---

### K1 · Carosello Instagram · 1080×1350 · gancio / il confronto

**COPY**
```
Gancio A    | Ti hanno scattato le foto
            | col telefono.
Gancio B    | La prima foto è tutto
            | quello che vedono del tuo annuncio.
Corpo       | Quattro cose rendono una foto
            | capace di vendere la casa.
CTA         | Scorri →
Caption     | (unica per il carosello — vedi blocco K5)
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| chip simulazione | 200-256 | SIMULAZIONE (x 700-1016, sulla metà destra) | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B su rgba(26,23,19,.55) |
| gancio | 640-900 | 3 righe | Archivo 900 | 70 | #FFF |
| sottotitolo | 940-1020 | 2 righe | Manrope 500 | 40 | #d8d2c4 |
| CTA scorri | 1100-1180 | pill outline (x 64-420) | Archivo 700 | 33 | #C8A24B |
| tendina | 0-1350 (x 216) | linea 6 px + maniglia Ø 44 a y 675 | — | — | #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · centro ottico y 675 · passo 20 px
Velo: `radial-gradient(ellipse 90% 34% at 50% 58%, rgba(26,23,19,.62), transparent 64%), linear-gradient(180deg, rgba(46,42,37,.86) 0%, rgba(46,42,37,.22) 34%, rgba(46,42,37,.90) 100%)` + velo aggiuntivo `rgba(26,23,19,.26)` sulla sola metà destra
**Vuoto dichiarato:** la fascia y 256-640 resta libera di proposito. È lì che si legge il confronto fra le due metà: non è un buco di impaginazione (controllo 3 del Master Template — deroga motivata).

**PROMPT GRAFICO (EN)**
```
— (nessuna immagine generata: foto reale brand-assets/immobili/salotto-divano-azzurro.jpg,
   metà sinistra corretta e metà destra degradata secondo la ricetta del blocco R2)
```

**NEGATIVE**
```
— (vale integralmente il blocco NEGATIVE di R2, ricetta di degrado inclusa)
```

**PARAMETRI**
`--ar 4:5 --v 6.1 --style raw --s 150 --seed 914026`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "La prima foto è tutto quello che vedono del tuo annuncio" | posizionamento, nessun dato |
| 2 | "Quattro cose rendono una foto capace di vendere la casa" | promessa di contenuto, mantenuta nelle slide `K2`-`K5` |
| 3 | Il "prima" è una simulazione | dichiarato in grafica col chip oro |

---

### K2 · Carosello Instagram · 1080×1350 · 01 · la luce

**COPY**
```
Gancio A    | Una sola luce alla volta.
Gancio B    | Metà gialla e metà grigia.
Corpo       | Lampade accese e finestra aperta
            | insieme danno una foto di due colori.
            | Spegni tutto. Apri tutto.
            | Scatta a metà mattina.
CTA         | —
Caption     | —
```
Riga oro (chiusura della slide): **"La casa torna del colore che ha davvero."**

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #F5F0E6 |
| kicker | 200-240 | 01 · LA LUCE | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| titolo | 380-560 | 2 righe | Archivo 800 | 62 | #F5F0E6 |
| corpo | 620-800 | 4 righe | Manrope 500 | 40 | #d8d2c4 |
| riga oro | 860-920 | 1 riga | Archivo 700 | 40 | #C8A24B |
| inserto fotografico | 980-1286 (x 64-1016) | banda foto reale corretta, angoli 20 px | — | — | — |
| tendina | 0-1350 (x 432) | linea 6 px + maniglia Ø 44 a y 675 | — | — | #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · passo 20 px · margine inferiore 64 px
Velo: — (artboard pieno, `radial-gradient(120% 80% at 50% 10%, #4a443a 0%, #3F3A33 55%, #2E2A25 100%)`; metà destra della linea +`rgba(26,23,19,.16)`)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C + inserto da foto reale `brand-assets/immobili/cucina-soggiorno-open-space.png`)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1350)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Luce artificiale e luce di finestra insieme producono due dominanti diverse nella stessa foto | **fatto tecnico di fotografia** (temperatura colore), non un dato di mercato |
| 2 | "Scatta a metà mattina" | consiglio operativo, nessun dato |

---

### K3 · Carosello Instagram · 1080×1350 · 02 · l'ordine

**COPY**
```
Gancio A    | Fotografi la casa finita,
            | non la casa in pausa.
Gancio B    | Nella foto si vede tutto quello
            | che hai lasciato sul tavolo.
Corpo       | Via telecomandi, cavi, ciabatte,
            | detersivi, scolapiatti.
            | Letto teso, cuscini battuti,
            | lavabo libero, tende tirate uguali.
CTA         | —
Caption     | —
```
Riga oro (chiusura della slide): **"Chi guarda vede una casa pronta, non una da sistemare."**

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #26241F |
| kicker | 200-240 | 02 · L'ORDINE | Manrope 600 maiusc. tracking 8 | 17 | #b3892f |
| titolo | 380-560 | 2 righe | Archivo 800 | 62 | #26241F |
| corpo | 620-800 | 4 righe | Manrope 500 | 40 | #46423a |
| riga oro | 860-920 | 1 riga | Archivo 700 | 40 | #b3892f |
| inserto fotografico | 980-1286 (x 64-1016) | banda foto reale corretta, angoli 20 px | — | — | — |
| tendina | 0-1350 (x 648) | linea 6 px + maniglia Ø 44 a y 675 | — | — | #b3892f |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · passo 20 px · margine inferiore 64 px
Velo: — (artboard pieno chiaro `#F5F0E6` — **unica slide chiara** del carosello, fa da respiro a metà sequenza)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C + inserto da foto reale `brand-assets/immobili/balcone-terrazzo.jpeg`)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1350)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Elenco di oggetti da togliere prima dello scatto | consiglio operativo, nessun dato |
| 2 | inserto fotografico | **vietato** usare `smart-tv-streaming-mockup.jpg`: marchi di terzi (vedi `brand-assets/README.md`) |

---

### K4 · Carosello Instagram · 1080×1350 · 03 · l'inquadratura

**COPY**
```
Gancio A    | Le verticali devono
            | restare verticali.
Gancio B    | Se la stanza pende, sembra più piccola.
Corpo       | Macchina all'altezza del petto e dritta:
            | stipiti e spigoli non devono pendere.
            | Scatta da un angolo, mai dal centro.
            | E tieni il telefono in orizzontale.
CTA         | —
Caption     | —
```
Riga oro (chiusura della slide): **"La stanza sembra grande quanto è."**

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #F5F0E6 |
| kicker | 200-240 | 03 · L'INQUADRATURA | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| titolo | 380-560 | 2 righe | Archivo 800 | 62 | #F5F0E6 |
| corpo | 620-800 | 4 righe | Manrope 500 | 40 | #d8d2c4 |
| riga oro | 860-920 | 1 riga | Archivo 700 | 40 | #C8A24B |
| inserto fotografico | 980-1286 (x 64-1016) | banda foto reale corretta + **due fili oro verticali** da 2 px sugli stipiti, a dimostrare le verticali dritte | — | — | #C8A24B |
| tendina | 0-1350 (x 864) | linea 6 px + maniglia Ø 44 a y 675 | — | — | #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · passo 20 px · margine inferiore 64 px
Velo: — (artboard pieno, `radial-gradient(120% 80% at 50% 10%, #4a443a 0%, #3F3A33 55%, #2E2A25 100%)`)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C + inserto da foto reale `brand-assets/immobili/salotto-divano-azzurro.jpg`, versione corretta)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1350)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Macchina a mezza altezza e livellata, scatto da un angolo, orizzontale | **regole standard di fotografia d'interni**, nessun dato di mercato |
| 2 | "Se la stanza pende, sembra più piccola" | osservazione percettiva, nessun numero |

---

### K5 · Carosello Instagram · 1080×1350 · 04 · la sequenza + chiusura

**COPY**
```
Gancio A    | L'ordine delle foto
            | è mezzo annuncio.
Gancio B    | La copertina vende. Le altre confermano.
Corpo       | Con noi non le scatti tu.
            | Il servizio fotografico è incluso
            | nella gestione.
CTA         | Scrivi CALCOLO in DM
Caption     | Ti hanno scattato le foto col telefono. Succede, e si corregge.
            | Qui ci sono le quattro cose che rendono una foto capace di vendere
            | la casa: la luce, l'ordine, l'inquadratura, la sequenza. Valgono
            | anche se fai da solo — salvale e usale al prossimo scatto.
            | Con noi non le scatti tu: il servizio fotografico è incluso nella
            | gestione, la casa la fotografiamo noi e l'annuncio lo scriviamo noi.
            | Non lo paghi a parte.
            | Ti garantiamo la gestione completa: foto e annuncio, pricing dinamico,
            | check-in smart H24, gestione ospiti, pulizie in standard alberghiero.
            | Tu ricevi il bonifico netto a fine mese.
            | 15% sul fatturato generato. Guadagniamo solo se guadagni tu.
            | Scrivi CALCOLO in DM per una simulazione gratuita.
```

Elenco della sequenza (voci della slide, numerazione oro):
```
01  Copertina: l'ambiente migliore, in orizzontale
02  Il resto del giorno: soggiorno e cucina
03  Le camere, una per volta
04  Bagno, esterno, vista
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #F5F0E6 |
| kicker | 200-240 | 04 · LA SEQUENZA | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| titolo | 280-400 | 2 righe | Archivo 800 | 62 | #F5F0E6 |
| elenco sequenza | 440-680 | 4 righe, passo 60 px, numero oro 31 | Manrope 600 | 31 | #d8d2c4 |
| filo oro | 720-723 | filo orizzontale 952 px | — | — | #C8A24B |
| riga garanzia | 760-900 | 2 righe | Archivo 900 | 50 | #F5F0E6 |
| riga offerta | 940-1000 | Gestione completa, 15% sul fatturato generato. | Manrope 600 | 31 | #b7ad9a |
| riga oro | 1030-1080 | Guadagniamo solo se guadagni tu. | Archivo 800 | 33 | #C8A24B |
| CTA | 1120-1286 | pill oro piena larghezza | Archivo 800 | 40 | #2E2A25 su #C8A24B |
| tendina | — | linea uscita dal bordo destro: resta **solo la maniglia**, integrata nel bordo sinistro della pill CTA | — | — | #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · passo 20 px · margine inferiore 64 px rispettato
Velo: — (artboard pieno, `radial-gradient(120% 80% at 50% 10%, #4a443a 0%, #3F3A33 55%, #2E2A25 100%)`)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C: nessuna immagine generata, solo HTML/CSS su fondo fumè)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1350)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Il servizio fotografico è incluso nella gestione. Non lo paghi a parte." | **CONFERMATO dal titolare 14/09/2026** |
| 2 | "La casa la fotografiamo noi e l'annuncio lo scriviamo noi" | CONFERMATO (servizio fotografico + ottimizzazione annuncio) |
| 3 | "Pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero" | CONFERMATO |
| 4 | "Tu ricevi il bonifico netto a fine mese" | **CONFERMATO — frase del titolare, utilizzabile alla lettera** |
| 5 | "15% sul fatturato generato" | CONFERMATO |
| 6 | "Guadagniamo solo se guadagni tu" | lessico di brand — alla lettera, solo in chiusura |
| 7 | "nessun costo fisso" | **non scritto**: il claim generale resta aperto (vedi riepilogo). Qui si afferma **solo** che il servizio fotografico è incluso, che è confermato |
| 8 | fotografo professionista esterno, attrezzatura, servizio "editoriale" | **[DATO DA VERIFICARE]** — vedi riepilogo. Il copy dice "il servizio fotografico", mai "un fotografo professionista" |

---

### FB1 · Facebook · 1080×1920 · gancio + problema

**COPY**
```
Gancio A    | Ti hanno scattato le foto
            | col telefono.
Gancio B    | Il tuo annuncio si gioca
            | prima che qualcuno lo apra.
Corpo       | La prima foto è l'unica cosa
            | che vede chi sta scorrendo.
CTA         | —
Caption     | (unica per le 3 immagini — vedi blocco FB3)
```
Riga oro: **"Il resto lo legge solo chi si è già fermato."**
Nota in basso: **"La foto qui sopra è una simulazione: una foto reale rovinata apposta da noi."**

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| chip simulazione | 260-316 | SIMULAZIONE (x 700-1016) | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B su rgba(26,23,19,.55) |
| gancio | 760-1100 | 4 righe | Archivo 900 | 70 | #FFF |
| corpo | 1140-1300 | 2 righe | Archivo 800 | 62 | #FFF |
| riga oro | 1350-1410 | 1 riga | Archivo 800 | 50 | #C8A24B |
| nota | 1480-1560 | 2 righe | Manrope 500 | 33 | #d8d2c4 |

Griglia: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso (nulla di leggibile sotto y 1600)
Velo: `radial-gradient(ellipse 92% 32% at 50% 56%, rgba(26,23,19,.62), transparent 64%), linear-gradient(180deg, rgba(46,42,37,.86) 0%, rgba(46,42,37,.20) 32%, rgba(46,42,37,.90) 100%)`
**Formato:** 9:16 obbligatorio. Nel collage Facebook la prima immagine in 4:5 viene tagliata ai lati (preferenza fissa 6 di `CLAUDE.md`).

**PROMPT GRAFICO (EN)**
```
— (nessuna immagine generata: foto reale brand-assets/immobili/salotto-divano-azzurro.jpg
   nella versione degradata, ricetta nel blocco NEGATIVE di R2)
```

**NEGATIVE**
```
— (vale integralmente il blocco NEGATIVE di R2, ricetta di degrado inclusa)
```

**PARAMETRI**
`--ar 9:16 --v 6.1 --style raw --s 150 --seed 914026`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "La prima foto è l'unica cosa che vede chi sta scorrendo" | posizionamento, **nessun numero, nessun riferimento agli algoritmi delle piattaforme** |
| 2 | Dichiarazione di simulazione in grafica | **obbligatoria**, non rimovibile in impaginazione |
| 3 | percentuali di clic, di visualizzazioni, di prenotazioni | **assenti** |

---

### FB2 · Facebook · 1080×1080 · soluzione (cosa cambia davvero)

**COPY**
```
Gancio A    | Stessa stanza. Quattro differenze.
Gancio B    | Non serve un'altra casa. Serve un'altra foto.
Corpo       | LUCE · una sola alla volta: o le lampade, o la finestra
            | ORDINE · niente cavi, niente detersivi, letto teso
            | INQUADRATURA · dritta, da un angolo, in orizzontale
            | SEQUENZA · copertina, giorno, camere, bagno ed esterno
CTA         | —
Caption     | (unica per le 3 immagini — vedi blocco FB3)
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 72-140 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #26241F |
| titolo | 200-280 | Stessa stanza. Quattro differenze. | Archivo 800 | 50 | #26241F |
| riga 1 | 340-420 | LUCE + testo (kicker oro 17 + Manrope 500 40) | Manrope | 17 / 40 | #b3892f / #26241F |
| riga 2 | 460-540 | ORDINE + testo | Manrope | 17 / 40 | #b3892f / #26241F |
| riga 3 | 580-660 | INQUADRATURA + testo | Manrope | 17 / 40 | #b3892f / #26241F |
| riga 4 | 700-780 | SEQUENZA + testo | Manrope | 17 / 40 | #b3892f / #26241F |
| banda chiusura | 860-1016 | banda oro piena: **"Con noi la tua casa la fotografiamo noi."** | Archivo 800 | 40 | #2E2A25 su #C8A24B |
| tendina | 0-1080 (x 540) | linea 6 px + maniglia Ø 44 a y 540, **sotto** il testo, attenuata a rgba(200,162,75,.35) | — | — | #b3892f |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · centro ottico y 540 · scala massima 62 · margine inferiore 64 px
Velo: — (artboard pieno chiaro `#F5F0E6`, filo oro 3 px a sinistra di ogni kicker)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1080)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Le quattro leve (luce, ordine, inquadratura, sequenza) | consigli operativi di fotografia, nessun dato di mercato |
| 2 | "Con noi la tua casa la fotografiamo noi" | **CONFERMATO dal titolare 14/09/2026** |
| 3 | "Non serve un'altra casa. Serve un'altra foto." | posizionamento. **Non promette prenotazioni** |

---

### FB3 · Facebook · 1080×1080 · offerta / CTA

**COPY**
```
Gancio A    | Il servizio fotografico è incluso.
Gancio B    | Non è un extra. È dentro la gestione.
Corpo       | La casa la fotografiamo noi.
            | L'annuncio lo scriviamo noi.
            | Tu ricevi il bonifico netto a fine mese.
CTA         | Scrivi CALCOLO in DM
Caption     | Ti hanno scattato le foto col telefono.
            |
            | Lo diciamo senza giri di parole, perché è l'errore più diffuso ed è
            | anche il più facile da correggere. La prima foto dell'annuncio è
            | l'unica cosa che vede chi sta scorrendo. Il resto lo legge solo chi si
            | è già fermato.
            |
            | Nelle immagini qui sopra c'è la stessa stanza, due volte. La prima è
            | una simulazione: abbiamo preso una foto reale e l'abbiamo rovinata
            | apposta — storta, scura, tagliata male, con le lampade accese e la
            | finestra aperta insieme. Non è la casa di nessun cliente, e volevamo
            | dirlo prima che lo chiedesse qualcuno.
            |
            | Quattro cose rendono una foto capace di vendere la casa. Valgono
            | anche se fai tutto da solo:
            |
            | 1) LA LUCE. Una sola alla volta. Lampade accese e luce di finestra
            | insieme danno una foto metà gialla e metà grigia. Spegni tutto, apri
            | tutto, scatta a metà mattina.
            |
            | 2) L'ORDINE. Via telecomandi, cavi, ciabatte, detersivi, scolapiatti.
            | Letto teso, cuscini battuti, lavabo libero, tende tirate uguali su
            | tutte le finestre. Si fotografa la casa finita, non la casa in pausa.
            |
            | 3) L'INQUADRATURA. Macchina all'altezza del petto e dritta: stipiti e
            | spigoli non devono pendere. Scatta da un angolo della stanza, mai dal
            | centro. E tieni il telefono in orizzontale.
            |
            | 4) LA SEQUENZA. Copertina con l'ambiente migliore. Poi soggiorno e
            | cucina, poi le camere una per volta, poi bagno, esterno e vista.
            |
            | Con noi non devi farne nessuna. Il servizio fotografico è incluso
            | nella gestione: la casa la fotografiamo noi, l'annuncio lo scriviamo
            | noi. Non è un extra e non lo paghi a parte.
            |
            | Ti garantiamo la gestione completa: foto e annuncio, pricing dinamico,
            | check-in smart H24, gestione ospiti, pulizie in standard alberghiero.
            | Tu ricevi il bonifico netto a fine mese.
            |
            | 15% sul fatturato generato. Guadagniamo solo se guadagni tu.
            |
            | Hai una casa a Roma o a Ostia? Scrivi CALCOLO in DM per una
            | simulazione gratuita.
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 72-140 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #F5F0E6 |
| kicker | 200-230 | GESTIONE COMPLETA | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| titolo | 260-420 | 2 righe | Archivo 900 | 62 | #C8A24B |
| corpo | 460-620 | 3 righe | Archivo 700 | 40 | #F5F0E6 |
| riga offerta | 660-720 | 15% sul fatturato generato. | Archivo 800 | 45 | #F5F0E6 |
| riga oro | 760-810 | Guadagniamo solo se guadagni tu. | Archivo 800 | 33 | #C8A24B |
| CTA | 900-1016 | pill oro piena larghezza | Archivo 800 | 40 | #2E2A25 su #C8A24B |
| tendina | — | maniglia oro Ø 44 integrata nel bordo sinistro della pill CTA (chiude la sequenza delle 3 immagini) | — | — | #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · scala massima 62 · margine inferiore 64 px
Velo: — (artboard pieno, `radial-gradient(120% 80% at 50% 10%, #4a443a 0%, #3F3A33 55%, #2E2A25 100%)`)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1080)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Il servizio fotografico è incluso nella gestione. Non lo paghi a parte." | **CONFERMATO dal titolare 14/09/2026** |
| 2 | "Tu ricevi il bonifico netto a fine mese" | **CONFERMATO — frase del titolare** |
| 3 | Elenco servizi: foto e annuncio, pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero | CONFERMATO |
| 4 | "15% sul fatturato generato" | CONFERMATO |
| 5 | "Guadagniamo solo se guadagni tu" | lessico di brand — alla lettera, solo in chiusura |
| 6 | Dichiarazione di simulazione dentro la caption | **obbligatoria**, non rimovibile in revisione |
| 7 | "nessun costo fisso" / "zero costi iniziali" | **assenti**: claim ancora aperto, vedi riepilogo |
| 8 | "più prenotazioni", "annuncio sempre pieno" | **assenti**: risultati di mercato, non garantiti |

---

### S3 · Storia Instagram · 1080×1920 · autoconclusiva — il minimo di notti troppo alto

**COPY**
```
Gancio A    | Hai messo minimo 3 notti.
Gancio B    | A Roma si arriva venerdì
            | e si riparte domenica.
Corpo       | Roma si visita in due giorni.
            | Con il minimo a tre notti,
            | chi ne cerca due non ti trova.
CTA         | Scrivi CALCOLO in DM
Caption     | —
```
Etichetta oro: **IL CONSIGLIO**
Consiglio: **"Tieni il minimo alto solo in alta stagione e sui ponti. Nei periodi bassi e in settimana scendi a una o due notti, e alza un po' la tariffa per coprire il riassetto."**
Riga di garanzia (chiusura della storia): **"Con noi prezzo e minimo notti si muovono insieme, data per data. Ci pensiamo noi."**

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| chip errore | 260-316 | ERRORE · MINIMO NOTTI (allineato a destra) | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B su rgba(26,23,19,.55) |
| gancio | 560-720 | 2 righe | Archivo 900 | 70 | #FFF |
| corpo problema | 770-890 | 3 righe | Manrope 500 | 40 | #d8d2c4 |
| etichetta consiglio | 940-970 | IL CONSIGLIO | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| consiglio | 990-1130 | 3 righe | Archivo 700 | 45 | #F5F0E6 |
| riga garanzia | 1180-1300 | 2 righe | Archivo 800 | 50 | #C8A24B |
| CTA | 1420-1540 | pill oro piena larghezza | Archivo 800 | 40 | #2E2A25 su #C8A24B |
| tendina | 0-1920 (x 108) | linea 6 px a filo del margine sinistro, senza maniglia (firma della giornata, ridotta) | — | — | rgba(200,162,75,.55) |

Griglia: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso (nulla di leggibile sotto y 1600)
Velo: `radial-gradient(ellipse 90% 32% at 50% 52%, rgba(26,23,19,.62), transparent 64%), linear-gradient(180deg, rgba(46,42,37,.86) 0%, rgba(46,42,37,.20) 34%, rgba(46,42,37,.90) 100%)`

**PROMPT GRAFICO (EN)**
```
Entrance hall of a lived-in Roman apartment in the morning, a small weekend cabin bag resting
on the travertine floor beside a walnut console, a linen jacket on a brass hook, the front
door closed, nobody in the room --
composition follows the rule of thirds, camera perfectly level on a tripod, vertical lines
straight, the central horizontal band of the frame is empty negative space with no objects
at eye level, generous headroom, lower third free of furniture --
warm smoky-grey and sand colour palette, muted olive and brass accents, golden hour light,
soft directional sunlight from a side window, warm neutral white balance, low saturation,
gentle film-like contrast --
shot on Canon EOS R5, 16-35mm at 20mm, f/8, ISO 200, architectural interior photography,
natural light only, photorealistic, real estate listing photography, no CGI look
```

**NEGATIVE**
```
--no text, letters, words, numbers, watermark, logo, signage, captions,
calendars, clock faces with readable dials, printed documents,
phone screens with interface, app interfaces, booking platform UI, luggage tags with writing,
brand logos on the bag, distorted furniture, warped perspective, bent walls, tilted horizon,
people in frame, extra limbs, deformed hands, mannequin faces, plastic skin,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
house numbers, street names, doorplates,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting
```

**PARAMETRI**
`--ar 9:16 --v 6.1 --style raw --s 150 --seed 914026`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Con il minimo a tre notti, chi ne cerca due non ti trova" | **meccanica del filtro di ricerca** (un soggiorno di 2 notti non è compatibile con un minimo di 3), non una statistica e non un'affermazione sugli algoritmi. *Formulazione di ripiego se in revisione sembra troppo netta:* "chi ne cerca due non può prenotarti" |
| 2 | "Roma si visita in due giorni" · "si arriva venerdì e si riparte domenica" | descrizione del comportamento del turismo breve, **senza alcuna quantificazione**. Nessuna percentuale sul peso dei soggiorni di 1-2 notti (vedi riepilogo) |
| 3 | "Alza un po' la tariffa per coprire il riassetto" | consiglio operativo, nessun importo |
| 4 | "Con noi prezzo e minimo notti si muovono insieme, data per data" | CONFERMATO nella sostanza (pricing dinamico). **Conferma puntuale sul minimo notti da chiudere** — vedi riepilogo, con formulazione di ripiego |
| 5 | "più prenotazioni", "calendario sempre pieno", "+X% di occupazione" | **assenti**: risultati di mercato, non garantiti |
| 6 | errori già bruciati dalla campagna virale (prezzo fermo, risposte lente, calendario, descrizione, pulizia, foto) | **non citati**: la storia parla solo del minimo notti |

---

### S4 · Storia Instagram · 1080×1920 · autoconclusiva — il check-in a orari rigidi

**COPY**
```
Gancio A    | Check-in dalle 15 alle 19.
Gancio B    | L'aereo atterra alle 23.
            | Tu ricevi fino alle 19.
Corpo       | Chi atterra a Fiumicino la sera
            | e chi arriva col treno tardi
            | cerca una casa che lo aspetti.
CTA         | Scrivi CALCOLO in DM
Caption     | —
```
Etichetta oro: **IL CONSIGLIO**
Consiglio: **"Allarga la finestra di arrivo e scrivilo nell'annuncio. E a qualunque ora sia, l'ospite va identificato prima di entrare: di persona o in videochiamata."**
Riga di garanzia (chiusura della storia): **"Ti assicuriamo il check-in smart H24: l'ospite ricevuto a qualsiasi ora, identificato prima di entrare."**

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| chip errore | 260-316 | ERRORE · ORARI DI ARRIVO (allineato a destra) | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B su rgba(26,23,19,.55) |
| gancio | 560-720 | 2 righe | Archivo 900 | 70 | #FFF |
| corpo problema | 770-890 | 3 righe | Manrope 500 | 40 | #d8d2c4 |
| etichetta consiglio | 940-970 | IL CONSIGLIO | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| consiglio | 990-1130 | 3 righe | Archivo 700 | 45 | #F5F0E6 |
| riga garanzia | 1180-1300 | 2 righe | Archivo 800 | 50 | #C8A24B |
| CTA | 1420-1540 | pill oro piena larghezza | Archivo 800 | 40 | #2E2A25 su #C8A24B |
| tendina | 0-1920 (x 108) | linea 6 px a filo del margine sinistro, senza maniglia | — | — | rgba(200,162,75,.55) |

Griglia: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso (nulla di leggibile sotto y 1600)
Velo: `radial-gradient(ellipse 90% 30% at 50% 50%, rgba(26,23,19,.64), transparent 62%), linear-gradient(180deg, rgba(46,42,37,.88) 0%, rgba(46,42,37,.24) 36%, rgba(46,42,37,.92) 100%)`

**PROMPT GRAFICO (EN)**
```
Hallway of a lived-in Roman apartment late at night seen from inside, a single warm floor
lamp switched on, travertine floor, the closed front door at the end of the corridor, a
folded towel on a walnut bench, nobody in the room --
composition follows the rule of thirds, camera perfectly level on a tripod, vertical lines
straight, the central horizontal band of the frame is empty negative space with no objects
at eye level, generous headroom --
warm smoky-grey and sand colour palette, muted olive and brass accents, warm tungsten
lamplight as the only source, deep warm shadows, warm neutral white balance, low saturation,
gentle film-like contrast, no cool tones anywhere --
shot on Canon EOS R5, 16-35mm at 20mm, f/8, ISO 800, architectural interior photography,
available light only, photorealistic, real estate listing photography, no CGI look
```

**NEGATIVE**
```
--no text, letters, words, numbers, watermark, logo, signage, captions,
clock faces with readable dials, digital clock displays, calendars, printed documents,
phone screens with interface, keyboxes, lockboxes, keys hanging outside the door,
distorted furniture, warped perspective, bent walls, tilted horizon, people in frame,
extra limbs, deformed hands, mannequin faces, plastic skin,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows, moonlight blue,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
house numbers, street names, doorplates,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting
```

**PARAMETRI**
`--ar 9:16 --v 6.1 --style raw --s 150 --seed 914026`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Chi atterra a Fiumicino la sera e chi arriva col treno tardi" | descrizione del fenomeno, **nessun numero di voli, treni o passeggeri** |
| 2 | "Ti assicuriamo il check-in smart H24" | **CONFERMATO** (servizio del brand) |
| 3 | "L'ospite va identificato prima di entrare: di persona o in videochiamata" | CONFERMATO nella sostanza. **Riga non rimovibile**: senza di essa la storia descriverebbe un ingresso non conforme (vincolo ereditato dal pacchetto precedente e tuttora valido) |
| 4 | "prenotazioni in più", "nessun arrivo perso" | **assenti**: risultati di mercato, non garantiti |
| 5 | numero di keybox, sentenze, circolari, articoli di legge | **assenti**: questo pacchetto non parla di norme |

---

## Claim da verificare — riepilogo per `compliance-checker`

| # | Claim | Dove compare | Nota |
|---|---|---|---|
| 1 | **Chi scatta le foto** | `R2` (scena 7), `K5`, `FB2`, `FB3` | **[DATO DA VERIFICARE: il servizio fotografico è affidato a un fotografo professionista esterno o eseguito dal team interno? Con che attrezzatura?]** Finché è aperto, il copy dice **"il servizio fotografico"** e **"la fotografiamo noi"**, mai "un fotografo professionista" e mai "servizio fotografico editoriale". Se il titolare conferma, si può alzare il claim in tutti e quattro i punti. |
| 2 | **Il minimo notti dentro il pricing dinamico** | `S3` (riga di garanzia) | **[DATO DA VERIFICARE: Hadrianus gestisce anche il minimo di notti, o solo la tariffa?]** Il pricing dinamico è confermato; il minimo notti è una leva dello stesso strumento ma non è stato confermato esplicitamente. **Se non chiuso prima della pubblicazione**, la riga diventa: *"Con noi le tariffe si muovono data per data. Ci pensiamo noi."* |
| 3 | **Consenso sulla foto reale degradata** | `R2`, `K1`, `FB1` | **[DATO DA VERIFICARE: il proprietario dell'immobile reale in `brand-assets/immobili/` autorizza la pubblicazione di una versione volutamente peggiorata del suo appartamento?]** È il vero rischio di questo pacchetto: la casa è reale e riconoscibile. **Bloccante.** Alternative se il consenso non c'è: (a) degradare una foto di un immobile non più in gestione, (b) usare come sorgente un'immagine generata — in quel caso *entrambe* le versioni vanno dichiarate come non reali. |
| 4 | **"Nessun costo fisso"** | **nessun contenuto** | Claim ereditato e ancora aperto da `facebook-stagionalita-reel-proprietari` e da `copy.md`. **Deliberatamente non usato qui.** Si afferma solo che *il servizio fotografico è incluso e non si paga a parte*, che il titolare ha confermato. Non trasformarlo in "nessun costo iniziale" in impaginazione. |
| 5 | **Peso del turismo di 1-2 notti a Roma** | `S3` (alluso, mai quantificato) | Nessuna fonte in questo pacchetto. **[DATO DA VERIFICARE: quota di soggiorni di 1-2 notti sulle strutture ricettive di Roma]** — serve solo se un giorno si vorrà scrivere un numero. Oggi la storia funziona senza. |
| 6 | **Comportamento delle piattaforme sulla prima foto** | `R2`, `FB1` | Nessun dato citato, di proposito: mai "l'algoritmo premia", mai percentuali di clic. Se in revisione qualcuno propone un numero, va rifiutato o marcato. |

### Regole rispettate nel testo (da non rompere in revisione)

- **Nessuna nota di demerito.** *"La responsabilità resta tua. Il lavoro no."* e ogni variante sono **fuori da questo pacchetto**. Ogni contenuto chiude sul valore che dà Hadrianus.
- **Nessuna burocrazia.** Niente CIN, adempimenti, sanzioni, scadenze, Regolamento UE. Quel materiale resta in `copy.md`, che è storico.
- **Registro assertivo dove possiamo:** *ti garantiamo*, *ti assicuriamo*, *con noi la tua casa*, *ci pensiamo noi*. Non ammorbidire in "potremmo", "cercheremo di", "ti aiutiamo a".
- **Nessuna garanzia di risultato di mercato:** mai "prenotazioni garantite", "guadagno garantito", "sempre pieno", "zero multe". Garantiamo il lavoro e lo standard.
- **Nessuna percentuale o statistica inventata:** nessun +X%, nessun dato su algoritmi, clic, visualizzazioni.
- **La dichiarazione di simulazione non si toglie mai:** chip oro in grafica su `R2`, `K1`, `FB1` e frase esplicita nelle caption di `R2` e `FB3`.
- **Il "prima" e il "dopo" sono lo stesso ambiente reale.** Se in produzione diventano due case diverse, il confronto è disonesto e il contenuto va rifatto.
- **"Standard alberghiero"**, mai "hotel-style". **"Guadagniamo solo se guadagni tu"**, mai "guadagni solo se guadagni tu", e sempre in chiusura.
- **CTA unica e concreta in tutti i contenuti: "Scrivi CALCOLO in DM"** (con "per una simulazione gratuita" dove c'è spazio). Mai "scrivici in DM" a vuoto: nella revisione precedente è stato segnalato come lo spreco principale.
- **Nessuna struttura nominata** come prova. Nessun "Rome Smart Sea". **"Templum Purum" non esiste**: non compare e `riferimenti/riferimento-3.md` non è stato usato.
- **Nessun marchio di terzi:** niente interfacce di piattaforme di prenotazione nel reel (scena 3), niente `smart-tv-streaming-mockup.jpg` negli inserti del carosello.
- **In `S4` l'ordine è vincolante:** prima l'identificazione, poi l'accesso. Mai descrivere un ingresso senza riconoscimento.
- **Anti-sovrapposizione interna:** il reel mostra il confronto e non spiega le quattro leve; il carosello spiega le quattro leve e non rifà il confronto a pieno schermo; Facebook le riassume per la community; le storie parlano di due errori che nessun altro contenuto tocca.
- **Anti-sovrapposizione con `facebook-campagna-virale`:** nessun elenco di sei errori, nessuna riga "foto fatte di sera". Il consiglio sulla luce qui è diverso e più tecnico (**una sola temperatura di luce alla volta**), non "rifalle di giorno".

---

## Nota per `art-director`

**Pattern visivo nuovo, obbligatorio: "la tendina che attraversa".** Non riprendere nessuno dei layout registrati in `design-system.md` §"Pattern già usati": niente blocchi invertiti a piena larghezza, niente scontrino/ledger, niente calendario a 12 caselle, niente step numerati giganti, niente box con bordo sinistro oro, niente device mockup, niente marca temporale + arco (è la firma di ieri, `copy.md`).

1. **La tendina** — linea verticale oro 6 px con maniglia circolare Ø 44 px al centro ottico. A sinistra la foto corretta, a destra la simulazione degradata (velo `rgba(26,23,19,.26)` in più sulla metà destra). Nel carosello avanza: x 216 → 432 → 648 → 864 → fuori bordo su `K5`, dove resta solo la maniglia integrata nella pill CTA. Nelle storie si riduce a un filo oro al margine sinistro (x 108), senza maniglia.
2. **Il chip `SIMULAZIONE`** — oro su fondo scuro traslucido, sempre sulla metà "prima", in ogni artboard e in ogni scena del reel in cui la foto degradata è visibile. Non è un dettaglio grafico: è il vincolo di onestà.
3. **Il reel deve muoversi davvero.** Il precedente è stato bocciato perché era una sequenza di immagini ferme: qui ogni scena ha un movimento dichiarato in tabella (tremolio a mano libera, push-in, scroll con arresto secco, tendina, pan, slide-up, filo che si allunga, banda che sale). Se una scena resta ferma, va rifatta.
4. **Prima e dopo dallo stesso file sorgente.** Il "dopo" è la foto reale corretta (auto-tone, raddrizzamento, crop); il "prima" è la stessa foto degradata con la ricetta del blocco `NEGATIVE` di `R2`. Adobe fa la post-produzione, Claude Design monta l'artboard. **Non generare due immagini diverse.**
5. `K3` e `FB2` sono le **uniche superfici chiare** (sabbia `#F5F0E6`): servono da respiro. Non aggiungerne altre.
6. Base scura **grigio fumè caldo** (`#3F3A33`), **mai blu navy**. Tipografia Archivo/Manrope. Tutti i file consegnati come **artboard editabili** (`.dc.html` su canvas Claude Design), PNG solo come export aggiuntivo.
7. **Nomi file:** usare i nuovi ID (`R2`, `K1`-`K5`, `FB1`-`FB3`, `S3`, `S4`). **Non sovrascrivere** i file di `png/` e `grafiche/` del pacchetto bocciato, e **non toccare `S1` e `S2`**.
8. **Blocco:** niente va impaginato come definitivo finché il claim 3 del riepilogo (consenso sulla foto reale degradata) non è chiuso.
9. I sei controlli di qualità di `master-template.md` vanno fatti sul PNG renderizzato, a dimensione telefono, **prima** di mostrare qualcosa. Deroga già dichiarata e motivata: il vuoto y 256-640 di `K1`.

---

**Prossimo passo obbligatorio:** `compliance-checker`. Questo materiale non va consegnato al cliente né pubblicato prima di quel passaggio. Dopo la revisione, aggiornare la riga del 14/09 in `campagne/giornaliero/PIANO.md` con il nuovo angolo e aggiungere il gancio ("la prima foto dell'annuncio — foto col telefono vs servizio fotografico incluso") a `campagne/INDEX.md`.
