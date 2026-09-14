# Copy — Giornaliero lunedì 14 settembre 2026 · L'OBIEZIONE

**Angolo:** "La casella dimenticata" — l'esposizione amministrativa del proprietario.
**Meccanismo:** "la catena di ogni prenotazione" — ogni prenotazione fa partire atti con scadenze, e la catena la esegue Hadrianus dentro il 15%.
**Frase onesta obbligatoria (non eluderla):** *la responsabilità resta tua, il lavoro no.*
**Claim sbloccato oggi dal titolare:** *"Il proprietario riceve solo il bonifico netto a fine mese."*

## Canale e divisione dell'argomento

| ID | Canale | Formato | Pezzo dell'argomento |
|---|---|---|---|
| `R1` | Reel Instagram/Facebook | 1080×1920 · 15,4 s | **Il tempo** — non l'elenco |
| `C1`-`C5` | Carosello Instagram | 5× 1080×1350 | **La catena completa** — contenuto da salvare |
| `F1`-`F3` | Post Facebook | 1080×1920 + 2× 1080×1080 | **La data e il contesto** (20 maggio 2026 · Regolamento UE) |
| `S1` | Storia Instagram (autoconclusiva) | 1080×1920 | **L'estremo "prima"** — l'annuncio e il CIN |
| `S2` | Storia Instagram (autoconclusiva) | 1080×1920 | **L'estremo "dopo"** — le 23:40, le 24 ore, l'imposta di soggiorno |

**Due deviazioni dichiarate dal master template**, entrambe consapevoli:
1. nel blocco COPY il campo `Gancio` è sdoppiato in **Gancio A / Gancio B** (regola di progetto: sempre 2 varianti d'apertura);
2. nelle due storie autoconclusive il campo `Corpo` porta **fino a 4 righe** (2 di problema + 2 di risposta), sempre entro 40 caratteri per riga: una storia deve chiudere da sola problema **e** soluzione, non può essere spezzata su una seconda storia.

**Griglia 1080×1350 (non normata nel master template), dichiarata qui:** margine 64 px · colonna utile 952 px · safe area 0 · centro ottico y 675 · passo 20 px · scala massima 70 (solo slide 1) e 62 (slide interne).

---

### R1 · Reel Instagram/Facebook · 1080×1920 · 15,4 s · gancio freddo + presa in carico

**COPY**
```
Gancio A    | Non ti sanzionano per quanto guadagni.
Gancio B    | Ricevi una prenotazione. Parte un orologio.
Corpo       | Tu domani hai un altro lavoro.
            | L'orologio va avanti lo stesso.
CTA         | Ne parliamo in DM
Caption     | Non ti sanzionano per quanto guadagni. Ti sanzionano per una casella
            | dimenticata.
            | Ogni prenotazione fa partire una catena di atti, ognuno con la sua
            | scadenza. Nessuno di quegli atti è difficile: il problema è la frequenza
            | e l'orario.
            | Li eseguiamo noi, dentro la gestione completa. La responsabilità resta
            | tua. Il lavoro no.
            | 15% sul fatturato. Guadagniamo solo se guadagni tu. Scrivici in DM.
```

**LAYOUT**

Zone fisse (valgono per tutte le battute):

| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| binario | 220-223 | filo orizzontale 322 px, centrato | — | — | rgba(245,240,230,.24) |
| barra avanzamento | 220-223 | barra oro che si riempie sui 15,4 s | — | — | #C8A24B |
| kicker (solo battuta 1) | 800-840 | AFFITTO BREVE | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| testo 1 riga | 920-1000 | riga della battuta | Archivo 900 | 70 | #FFF |
| testo 2 righe | 860-1060 | righe della battuta | Archivo 900 | 70 | #FFF |
| riga oro (solo battuta 9) | 1180-1240 | GUADAGNIAMO SOLO SE GUADAGNI TU | Archivo 800 maiusc. | 31 | #C8A24B |
| CTA (solo battuta 9) | 1300-1360 | Ne parliamo in DM | Manrope 600 maiusc. | 31 | #F5F0E6 |

Battute (telaio "negazione + desideri", versione lunga di `modello-reel-8-secondi.md`):

| # | In → Out | Durata | Testo a schermo | Scena |
|---|---|---|---|---|
| 1 · gancio | 0,0 → 2,6 | 2,6 s | kicker `AFFITTO BREVE` + **"Non ti sanzionano / per quanto guadagni."** | `brand-assets/video/clean/balcone` |
| 2 · svolta | 2,6 → 4,0 | 1,4 s | **"Per una casella."** (entra in dissolvenza 0,3 s, stessa inquadratura) | stessa scena |
| 3 | 4,0 → 5,4 | 1,4 s | **"Arriva una prenotazione."** | `interno-cucina` |
| 4 | 5,4 → 6,8 | 1,4 s | **"Parte un orologio."** | `interno-cucina` (stacco su seconda finestra ferma) |
| 5 | 6,8 → 8,2 | 1,4 s | **"Tu domani hai / un altro lavoro."** | piano notturno (vedi PROMPT) |
| 6 | 8,2 → 9,6 | 1,4 s | **"L'orologio va avanti / lo stesso."** | piano notturno, seconda inquadratura |
| 7 | 9,6 → 11,0 | 1,4 s | **"E non suona."** | piano notturno, dettaglio |
| 8 · presa in carico | 11,0 → 13,0 | 2,0 s | **"Il CIN resta tuo. / L'orologio lo guardiamo noi."** | `busto-frontale` |
| 9 · chiusura | 13,0 → 15,4 | 2,4 s | **"Gestione completa. / 15% sul fatturato."** + riga oro + CTA | fondo fumè pieno + logo |

Griglia: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso · testo al centro esatto, mai allineato a sinistra
Velo: `radial-gradient(ellipse 92% 30% at 50% 48%, rgba(26,23,19,.62), transparent 64%), linear-gradient(180deg, rgba(46,42,37,.86) 0%, rgba(46,42,37,.20) 34%, rgba(46,42,37,.88) 100%), rgba(63,58,51,.28)`
Nota di scala: il modello reel indica ~72 px; qui **70 px**, il gradino alto della scala tipografica del master template. Fuori scala non si va.

**PROMPT GRAFICO (EN)**
```
Empty entrance hall of a lived-in Roman apartment late at night, travertine floor, a set of
keys left on a walnut console, a linen jacket on a brass hook, the front door closed, a
single floor lamp switched on --
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
--no text, letters, words, numbers, watermark, logo, signage, captions, subtitles,
clock faces with readable dials, calendars, printed documents, phone screens with interface,
distorted furniture, warped perspective, bent walls, tilted horizon,
extra limbs, deformed hands, mannequin faces, plastic skin, people in frame,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows, moonlight blue,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting
```

**PARAMETRI**
`--ar 9:16 --v 6.1 --style raw --s 100 --seed 140926`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Non ti sanzionano per quanto guadagni. Per una casella." | sintesi di posizionamento fondata sui dati 2-3 del brief (CIN obbligatorio e sanzionato). **Nessun importo citato**, come da vincolo |
| 2 | "Il CIN resta tuo" | CONFERMATO (dato 2 + meccanismo del brief) |
| 3 | "L'orologio lo guardiamo noi" — Hadrianus esegue gli atti con le loro scadenze | CONFERMATO dal titolare 14/09/2026 |
| 4 | "Gestione completa. 15% sul fatturato." | CONFERMATO |
| 5 | "Guadagniamo solo se guadagni tu" | lessico di brand — obbligatorio alla lettera, solo in chiusura |
| 6 | elenco di adempimenti · importi di sanzione · aliquote | **assenti per scelta**: pezzo affidato al carosello e al post Facebook |

---

### C1 · Carosello Instagram · 1080×1350 · gancio / slide da salvare

**COPY**
```
Gancio A    | Cosa parte davvero quando ricevi
            | una prenotazione.
Gancio B    | Ricevi una prenotazione. Parte una catena.
Corpo       | Sei anelli. Ognuno con la sua scadenza.
CTA         | Scorri →
Caption     | Una prenotazione non porta solo un ospite: fa partire una catena di
            | atti, e ognuno ha la sua scadenza. Qui c'è tutta, in ordine, dal
            | momento prima che l'annuncio sia online fino al bonifico di fine mese.
            | Nessuno di questi atti è difficile. Il problema è che scadono a ogni
            | prenotazione, spesso di notte, mentre tu hai un altro lavoro.
            | La dichiarazione dei redditi resta col tuo commercialista: noi facciamo
            | gli adempimenti operativi legati alla gestione.
            | La responsabilità resta tua. Il lavoro no.
            | Salvalo, ti serve alla prossima prenotazione. Scrivi CATENA in DM.
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| marca temporale | 200-240 | T ZERO | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| gancio | 600-860 | 3 righe | Archivo 900 | 70 | #FFF |
| sottotitolo | 900-980 | Sei anelli. Ognuno con la sua scadenza. | Manrope 500 | 40 | #d8d2c4 |
| CTA scorri | 1140-1220 | pill outline (x 64-380) | Archivo 700 | 33 | #C8A24B |
| arco avanzamento | 1120-1260 (x 820-960) | arco 1/5 oro su traccia fumè | — | — | #C8A24B su rgba(245,240,230,.14) |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · centro ottico y 675 · passo 20 px
Velo: `radial-gradient(ellipse 90% 34% at 50% 52%, rgba(26,23,19,.60), transparent 64%), linear-gradient(180deg, rgba(46,42,37,.88) 0%, rgba(46,42,37,.22) 36%, rgba(46,42,37,.90) 100%)`

**PROMPT GRAFICO (EN)**
```
Quiet living room of a lived-in Roman apartment at first light, travertine floor, olive linen
sofa, brass floor lamp, a balcony door left ajar onto a silent street, nobody in the room --
composition follows the rule of thirds, camera perfectly level on a tripod, vertical lines
straight, the central horizontal band of the frame is empty negative space with no objects at
eye level, generous headroom, lower third free of furniture --
warm smoky-grey and sand colour palette, muted olive and brass accents, golden hour light,
soft directional sunlight from a side window, warm neutral white balance, low saturation,
gentle film-like contrast --
shot on Canon EOS R5, 16-35mm at 20mm, f/8, ISO 200, architectural interior photography,
natural light only, photorealistic, real estate listing photography, no CGI look
```

**NEGATIVE**
```
--no text, letters, words, numbers, watermark, logo, signage, captions,
printed documents, phone screens with interface, calendars, clock faces with readable dials,
distorted furniture, warped perspective, bent walls, tilted horizon, people in frame,
extra limbs, deformed hands, mannequin faces, plastic skin,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting
```

**PARAMETRI**
`--ar 4:5 --v 6.1 --style raw --s 150 --seed 140926`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Sei anelli. Ognuno con la sua scadenza." | CONFERMATO dal titolare 14/09/2026 (i sei anelli) + dati 1-2-4-6-8-9-10 del brief (le scadenze) |
| 2 | "Cosa parte davvero quando ricevi una prenotazione" | descrizione di processo, nessun dato |

---

### C2 · Carosello Instagram · 1080×1350 · anello 01

**COPY**
```
Gancio A    | Il CIN deve essere nell'annuncio.
            | E deve corrispondere.
Gancio B    | Prima ancora dell'ospite, c'è il codice.
Corpo       | Oggi il codice lo controlla anche
            | la piattaforma, prima di pubblicare.
CTA         | —
Caption     | —
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #F5F0E6 |
| marca temporale | 200-240 | 01 · PRIMA CHE L'ANNUNCIO SIA ONLINE | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| titolo | 400-620 | 3 righe | Archivo 800 | 62 | #F5F0E6 |
| corpo | 680-800 | 2 righe | Manrope 500 | 40 | #d8d2c4 |
| nota | 1080-1140 | Va anche esposto all'esterno dello stabile. | Manrope 500 | 31 | #9a8f7c |
| arco avanzamento | 1120-1260 (x 820-960) | arco 2/5 oro | — | — | #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · passo 20 px
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
| 1 | CIN obbligatorio in ogni annuncio ed esposto all'esterno dello stabile | CONFERMATO (dato 2) |
| 2 | "Oggi il codice lo controlla anche la piattaforma, prima di pubblicare" | CONFERMATO (dato 1) — **data e nome del regolamento restano al solo post Facebook** |
| 3 | importi di sanzione CIN (500-8.000 €) | **mai stampati in grafica** (dato 3, confermato solo con riserva sulla singola fattispecie) |

---

### C3 · Carosello Instagram · 1080×1350 · anello 02

**COPY**
```
Gancio A    | Prima lo riconosci.
            | Poi gli dai l'accesso.
Gancio B    | L'ospite arriva. E l'ordine conta.
Corpo       | L'identificazione è de visu: di persona
            | o in videochiamata in tempo reale.
CTA         | —
Caption     | —
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #F5F0E6 |
| marca temporale | 200-240 | 02 · QUANDO L'OSPITE ARRIVA | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| titolo | 400-620 | 3 righe | Archivo 800 | 62 | #F5F0E6 |
| corpo | 680-800 | 2 righe | Manrope 500 | 40 | #d8d2c4 |
| marca temporale 2 | 900-940 | +24:00 (chip oro, x 64-300) | Archivo 800 maiusc. | 33 | #C8A24B |
| nota | 980-1100 | Da lì partono le 24 ore per comunicare le generalità. Sei, se il soggiorno dura meno di un giorno. | Manrope 500 | 31 | #b7ad9a |
| arco avanzamento | 1120-1260 (x 820-960) | arco 3/5 oro | — | — | #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · passo 20 px
Velo: — (artboard pieno fumè)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1350)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Identificazione de visu (di persona o videochiamata in tempo reale) **prima** dell'accesso digitale | CONFERMATO nella sostanza (dato 8). **Numero e data della sentenza non citati**, restano DA VERIFICARE |
| 2 | Comunicazione delle generalità entro 24 ore, 6 se il soggiorno dura meno di un giorno | CONFERMATO (dato 6) |
| 3 | sanzione ex art. 17 TULPS / rischio penale | **escluso per scelta di registro** (dato 7) |
| 4 | articoli di legge, commi, numeri di circolare | **assenti**: vincolo del brief sul carosello |

---

### C4 · Carosello Instagram · 1080×1350 · anello 03

**COPY**
```
Gancio A    | L'imposta di soggiorno la incassi tu.
            | E la versi tu.
Gancio B    | Il soggiorno finisce. Gli obblighi no.
Corpo       | A Roma sono 6 € a persona a notte,
            | fino a 10 notti consecutive.
CTA         | —
Caption     | —
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #26241F |
| marca temporale | 200-240 | 03 · DURANTE E DOPO IL SOGGIORNO | Manrope 600 maiusc. tracking 8 | 17 | #b3892f |
| titolo | 380-600 | 3 righe | Archivo 800 | 62 | #26241F |
| corpo | 660-780 | 2 righe | Manrope 500 | 40 | #46423a |
| riga chiave | 820-940 | Resti responsabile del versamento anche se l'ospite non paga la sua quota. | Archivo 700 | 40 | #b3892f |
| nota | 1000-1100 | Estintore e rilevatori al loro posto e manutenuti. Poi la casa torna in ordine, in standard alberghiero. | Manrope 500 | 31 | #6f695c |
| arco avanzamento | 1120-1260 (x 820-960) | arco 4/5 oro | — | — | #b3892f su rgba(38,36,31,.14) |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · passo 20 px
Velo: — (artboard pieno chiaro `#F5F0E6` — unica slide chiara del carosello, fa da respiro prima della chiusura)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1350)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Imposta di soggiorno a Roma: 6 € a persona a notte, max 10 notti consecutive | CONFERMATO (dato 9, fonti concordanti). **La delibera non va citata** (riferimento DA VERIFICARE) |
| 2 | Il gestore resta responsabile del versamento anche se l'ospite non paga | CONFERMATO (dato 9) |
| 3 | Estintori e rilevatori obbligatori anche per locazioni non imprenditoriali | CONFERMATO (dato 4). **Importi di sanzione e quantità per m² non citati** (dato 5, fonte singola) |
| 4 | "standard alberghiero" | lessico di brand + servizio confermato |
| 5 | Applicabilità dell'imposta agli immobili del Litorale fuori dal Comune di Roma | **[DATO DA VERIFICARE: tariffa e regolamento dell'imposta di soggiorno per gli immobili in gestione fuori da Roma Capitale, es. Fiumicino.]** Finché non è chiuso, il copy resta ancorato a "A Roma", che è accurato così com'è scritto |

---

### C5 · Carosello Instagram · 1080×1350 · chi la esegue + chiusura

**COPY**
```
Gancio A    | La responsabilità resta tua.
            | Il lavoro no.
Gancio B    | Non smetti di essere il titolare.
            | Smetti di essere l'esecutore.
Corpo       | Il proprietario riceve solo
            | il bonifico netto a fine mese.
CTA         | Scrivi CATENA in DM
Caption     | —
```

Elenco dei sei anelli (voci della slide, Archivo/Manrope 31, spunta oro):
```
Il CIN nell'annuncio
L'identificazione dell'ospite, de visu
La comunicazione delle generalità entro 24 ore
L'imposta di soggiorno a Roma: incasso e versamento
Il controllo delle dotazioni di sicurezza
L'incasso dei canoni e la certificazione a fine anno
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 80-160 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #F5F0E6 |
| marca temporale | 200-240 | 04 · CHI ESEGUE LA CATENA | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| elenco 6 anelli | 300-640 | 6 righe, passo 56 px, spunta oro 28 px | Manrope 600 | 31 | #d8d2c4 |
| frase onesta | 700-850 | 2 righe | Archivo 900 | 62 | #F5F0E6 |
| claim di chiusura | 890-1010 | 2 righe | Archivo 800 | 50 | #C8A24B |
| riga offerta | 1050-1130 | Tutto dentro il 15% sul fatturato. Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #b7ad9a |
| CTA | 1170-1286 | pill oro piena larghezza | Archivo 800 | 40 | #2E2A25 su #C8A24B |
| arco avanzamento | — | arco 5/5 chiuso, integrato nel bordo della pill | — | — | #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · passo 20 px · margine inferiore 64 px rispettato
Velo: — (artboard pieno, `radial-gradient(120% 80% at 50% 10%, #4a443a 0%, #3F3A33 55%, #2E2A25 100%)`)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1350)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Hadrianus esegue tutti e sei gli anelli della catena | **CONFERMATO dal titolare 14/09/2026** (sblocca il dato 14) |
| 2 | "Il proprietario riceve solo il bonifico netto a fine mese." | **CONFERMATO — frase del titolare, utilizzabile alla lettera** |
| 3 | "La responsabilità resta tua. Il lavoro no." | dichiarazione di perimetro, obbligatoria: è ciò che distingue il contenuto da una rassicurazione |
| 4 | "L'incasso dei canoni e la certificazione a fine anno" | CONFERMATO (dato 10 + conferma del titolare). **Vietato citare l'aliquota della ritenuta**: nessuna percentuale fiscale in copy |
| 5 | "Tutto dentro il 15% sul fatturato" | CONFERMATO (offerta + meccanismo del brief) |
| 6 | "Guadagniamo solo se guadagni tu" | lessico di brand — alla lettera, solo in chiusura |
| 7 | "zero multe", "conformità garantita", "non rischi più niente" | **assenti per scelta**: nessuna garanzia di risultato normativo |

---

### F1 · Facebook · 1080×1920 · gancio + problema (la data)

**COPY**
```
Gancio A    | Dal 20 maggio le piattaforme
            | verificano il codice della tua casa.
Gancio B    | Da maggio l'irregolarità non aspetta
            | un controllo.
Corpo       | Non ti sanzionano
            | per quanto guadagni.
CTA         | —
Caption     | (unica per le 3 immagini — vedi blocco F3)
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| marca temporale | 300-340 | 20 MAGGIO 2026 | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| gancio | 700-1020 | 4 righe | Archivo 900 | 70 | #FFF |
| corpo | 1080-1240 | 2 righe | Archivo 800 | 62 | #FFF |
| riga oro | 1280-1400 | Ti sanzionano per / una casella dimenticata. | Archivo 800 | 50 | #C8A24B |
| nota | 1440-1500 | Non è una stretta. È un cambio di meccanismo. | Manrope 500 | 33 | #d8d2c4 |

Griglia: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso (nulla di leggibile sotto y 1600)
Velo: `radial-gradient(ellipse 92% 32% at 50% 54%, rgba(26,23,19,.62), transparent 64%), linear-gradient(180deg, rgba(46,42,37,.86) 0%, rgba(46,42,37,.20) 32%, rgba(46,42,37,.90) 100%)`

**PROMPT GRAFICO (EN)**
```
Interior landing of an old Roman apartment building seen from inside the flat, heavy wooden
front door half open, travertine steps, a small blank brass plate on the wall beside the
door frame, morning light from a stairwell window --
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
--no text, letters, words, numbers, engraved plaques, house numbers, watermark, logo,
signage, captions, subtitles,
printed documents, phone screens with interface, calendars, clock faces with readable dials,
distorted furniture, warped perspective, bent walls, tilted horizon, people in frame,
extra limbs, deformed hands, mannequin faces, plastic skin,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting
```

**PARAMETRI**
`--ar 9:16 --v 6.1 --style raw --s 150 --seed 140926`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Dal 20 maggio 2026 le piattaforme verificano il numero di registrazione dell'alloggio | CONFERMATO (dato 1, fonti secondarie concordanti) |
| 2 | "Non è una stretta. È un cambio di meccanismo." | lettura di contesto, coerente col dato 1. Registro non allarmistico, come da vincolo |
| 3 | "Ti sanzionano per una casella dimenticata" | sintesi fondata sui dati 2-3. **Nessun importo in grafica** |
| 4 | regolamento di Roma Capitale (limiti di notti, IMU) | **escluso**: non approvato (dato 13) |
| 5 | aliquote fiscali (21% / 26% / 30%) | **escluse**: fonti discordanti (dato 12) |

---

### F2 · Facebook · 1080×1080 · soluzione (la catena in 3 momenti)

**COPY**
```
Gancio A    | Cosa parte a ogni prenotazione
Gancio B    | Tre momenti, tre scadenze
Corpo       | PRIMA · il CIN nell'annuncio, e deve corrispondere
            | ALL'ARRIVO · prima identifichi l'ospite, poi gli dai l'accesso.
            | Da lì: 24 ore per comunicare le generalità
            | DURANTE E DOPO · imposta di soggiorno da incassare e versare,
            | dotazioni di sicurezza al loro posto, casa in standard alberghiero
CTA         | —
Caption     | (unica per le 3 immagini — vedi blocco F3)
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 72-140 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #26241F |
| titolo | 200-300 | Cosa parte a ogni prenotazione | Archivo 800 | 50 | #26241F |
| marca temporale 1 | 360-390 | PRIMA | Manrope 600 maiusc. tracking 8 | 17 | #b3892f |
| riga 1 | 400-500 | 2 righe | Manrope 500 | 40 | #26241F |
| marca temporale 2 | 560-590 | ALL'ARRIVO · +24:00 | Manrope 600 maiusc. tracking 8 | 17 | #b3892f |
| riga 2 | 600-700 | 2 righe | Manrope 500 | 40 | #26241F |
| marca temporale 3 | 760-790 | DURANTE E DOPO | Manrope 600 maiusc. tracking 8 | 17 | #b3892f |
| riga 3 | 800-900 | 2 righe | Manrope 500 | 40 | #26241F |
| arco avanzamento | 940-1010 (x 880-1010) | arco 2/3 oro | — | — | #b3892f |

Griglia: margine 64 px · colonna utile 952 px · safe area 0 · centro ottico y 540 · scala massima 62 · margine inferiore 70 px
Velo: — (artboard pieno chiaro `#F5F0E6`, filo oro 3 px a sinistra di ogni marca temporale)

**PROMPT GRAFICO (EN)**
`—` (artboard editabile tipo C)

**NEGATIVE**
`—`

**PARAMETRI**
`—` (artboard 1080×1080)

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | CIN nell'annuncio e coerente | CONFERMATO (dato 2) |
| 2 | identificazione prima dell'accesso · 24 ore per la comunicazione | CONFERMATO (dati 8 e 6) |
| 3 | imposta di soggiorno da incassare e versare · dotazioni di sicurezza | CONFERMATO (dati 9 e 4). Nessun importo di sanzione |
| 4 | "standard alberghiero" | lessico di brand + servizio confermato |
| 5 | ingresso dell'ospite senza identificazione | **mai descritto**: l'ordine "prima identifichi, poi dai l'accesso" è vincolante in ogni riga |

---

### F3 · Facebook · 1080×1080 · offerta / CTA

**COPY**
```
Gancio A    | Sei anelli. Tutti eseguiti.
Gancio B    | La catena la esegue qualcuno il cui
            | mestiere è eseguirla.
Corpo       | Il proprietario riceve solo
            | il bonifico netto a fine mese.
CTA         | Commenta CATENA o scrivici in privato
Caption     | Il 20 maggio 2026 è diventato applicabile il
            | Regolamento UE 2024/1028. Da quella data le piattaforme di
            | prenotazione verificano il numero di registrazione dell'alloggio — in
            | Italia il CIN — e trasmettono ogni mese i dati delle prenotazioni alle
            | autorità nazionali.
            |
            | Non è una stretta e non è un allarme. È un cambio di meccanismo: prima
            | un'irregolarità emergeva con un controllo, adesso emerge dai dati.
            |
            | Per chi affitta da solo cambia una cosa sola, ma pesante: ogni
            | prenotazione fa partire una catena di atti, e ognuno ha la sua scadenza.
            |
            | Prima che l'annuncio sia visibile: il CIN dev'esserci e deve
            | corrispondere.
            | All'arrivo dell'ospite: prima lo identifichi — di persona o in
            | videochiamata in tempo reale — poi gli dai l'accesso. Da lì hai 24 ore
            | per comunicare le generalità. Sei, se il soggiorno dura meno di un
            | giorno.
            | Durante e dopo: a Roma l'imposta di soggiorno è 6 € a persona a notte
            | fino a 10 notti consecutive, e la versa il gestore anche se l'ospite non
            | paga la sua quota. Estintore e rilevatori devono essere al loro posto.
            |
            | Nessuno di questi atti è difficile. Il problema è la frequenza e
            | l'orario: scadono a ogni prenotazione, spesso di notte, mentre tu hai
            | un altro lavoro.
            |
            | Il tuo commercialista lavora una volta l'anno. Questi atti scadono a
            | ogni prenotazione: non sono lo stesso lavoro. La tua dichiarazione dei
            | redditi resta col tuo commercialista — noi non la facciamo e non diamo
            | consulenza fiscale. Noi facciamo gli adempimenti operativi legati alla
            | gestione.
            |
            | E diciamo la cosa che nessuno dice: la responsabilità resta tua. Il CIN
            | è il tuo, la casa è la tua. Non smetti di essere il titolare. Smetti di
            | essere l'esecutore.
            |
            | Noi eseguiamo tutti e sei gli anelli: CIN nell'annuncio, identificazione
            | dell'ospite, comunicazione entro 24 ore, imposta di soggiorno, controllo
            | delle dotazioni di sicurezza, incasso dei canoni con la certificazione a
            | fine anno. Il proprietario riceve solo il bonifico netto a fine mese.
            |
            | Tutto dentro la gestione completa: 15% sul fatturato generato.
            | Guadagniamo solo se guadagni tu.
            |
            | Se hai una casa a Roma o a Ostia e vuoi capire cosa scatta a ogni
            | prenotazione, commenta CATENA o scrivici in privato.
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 72-140 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #F5F0E6 |
| marca temporale | 200-230 | FINE MESE | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| titolo | 250-330 | Sei anelli. Tutti eseguiti. | Archivo 800 | 50 | #F5F0E6 |
| claim di chiusura | 380-580 | 3 righe | Archivo 900 | 62 | #C8A24B |
| riga perimetro | 620-700 | La dichiarazione dei redditi resta col tuo commercialista. Noi facciamo gli adempimenti operativi della gestione. | Manrope 500 | 31 | #b7ad9a |
| riga offerta | 740-820 | 15% sul fatturato. | Archivo 700 | 40 | #F5F0E6 |
| riga oro | 850-900 | Guadagniamo solo se guadagni tu. | Archivo 800 | 33 | #C8A24B |
| CTA | 930-1016 | pill oro piena larghezza | Archivo 800 | 33 | #2E2A25 su #C8A24B |

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
| 1 | Hadrianus esegue tutti e sei gli anelli | **CONFERMATO dal titolare 14/09/2026** |
| 2 | "Il proprietario riceve solo il bonifico netto a fine mese." | **CONFERMATO — frase del titolare** |
| 3 | "15% sul fatturato generato" | CONFERMATO |
| 4 | **"Nessun costo fisso"** | **[DATO DA VERIFICARE: esiste davvero zero costo una tantum in avvio — servizio fotografico, set biancheria iniziale, sistemazioni pre-pubblicazione? Claim ereditato, ancora aperto dalla campagna `facebook-stagionalita-reel-proprietari`.]** Se non viene chiuso prima della pubblicazione, **in grafica resta solo "15% sul fatturato"** e la riga sparisce dalla caption |
| 5 | "Non facciamo la tua dichiarazione dei redditi e non diamo consulenza fiscale" | dichiarazione di perimetro **obbligatoria**: separa Hadrianus dal commercialista e neutralizza i claim vietati sul fisco |
| 6 | "Guadagniamo solo se guadagni tu" | lessico di brand — alla lettera, solo in chiusura |
| 7 | numeri su sanzioni evitate, clienti gestiti, controlli superati | **assenti**: nessun dato esistente (dato 15) |

---

### S1 · Storia Instagram · 1080×1920 · autoconclusiva — l'estremo "prima"

**COPY**
```
Gancio A    | Il CIN nell'annuncio è quello giusto?
Gancio B    | Il tuo annuncio è online. E il codice?
Corpo       | Se manca, o non corrisponde,
            | l'annuncio può non passare la verifica.
            | L'annuncio lo curiamo noi.
            | Il codice ci sta dentro dal primo giorno.
CTA         | Scrivi in DM
Caption     | —
```

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| marca temporale | 260-300 | PRIMA DELLA PUBBLICAZIONE (allineata a destra) | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| gancio | 780-940 | 2 righe | Archivo 900 | 70 | #FFF |
| corpo problema | 1000-1120 | 2 righe | Manrope 500 | 40 | #d8d2c4 |
| riga risposta | 1180-1300 | 2 righe | Archivo 800 | 50 | #C8A24B |
| CTA | 1420-1540 | pill oro piena larghezza | Archivo 800 | 40 | #2E2A25 su #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso (nulla di leggibile sotto y 1600)
Velo: `radial-gradient(ellipse 90% 30% at 50% 56%, rgba(26,23,19,.60), transparent 64%), linear-gradient(180deg, rgba(46,42,37,.84) 0%, rgba(46,42,37,.18) 34%, rgba(46,42,37,.90) 100%)`

**PROMPT GRAFICO (EN)**
```
Front door of a Roman apartment seen from the landing, heavy wooden door with brass handle,
a small blank brass plate mounted on the wall beside the frame, travertine floor, warm
morning light coming from a stairwell window --
composition follows the rule of thirds, camera perfectly level on a tripod, vertical lines
straight, the central horizontal band of the frame is empty negative space with no objects
at eye level, generous headroom --
warm smoky-grey and sand colour palette, muted olive and brass accents, golden hour light,
soft directional sunlight from a side window, warm neutral white balance, low saturation,
gentle film-like contrast --
shot on Sony A7RIV, 35mm, f/4, ISO 200, architectural interior photography, natural light
only, photorealistic, real estate listing photography, no CGI look
```

**NEGATIVE**
```
--no text, letters, words, numbers, engraved plaques, house numbers, door signs, watermark,
logo, signage, captions,
printed documents, phone screens with interface, keys hanging from a keybox,
distorted furniture, warped perspective, bent walls, tilted horizon, people in frame,
extra limbs, deformed hands, mannequin faces, plastic skin,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting
```

**PARAMETRI**
`--ar 9:16 --v 6.1 --style raw --s 150 --seed 140926`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Un CIN mancante o non corrispondente può far fallire la verifica della piattaforma | CONFERMATO (dati 1 e 2) |
| 2 | "L'annuncio lo curiamo noi" (foto e testo) | CONFERMATO (servizi inclusi: ottimizzazione annuncio) |
| 3 | "Il codice ci sta dentro dal primo giorno" | CONFERMATO dal titolare 14/09/2026 (anello 1) |
| 4 | importi di sanzione · blocco dell'annuncio dato per certo | **assenti**: si dice "può non passare la verifica", mai "ti bloccano l'annuncio" |

---

### S2 · Storia Instagram · 1080×1920 · autoconclusiva — l'estremo "dopo"

**COPY**
```
Gancio A    | L'ospite entra alle 23:40.
Gancio B    | Alle 23:40 parte un orologio.
Corpo       | Lo identifichi. Poi entra.
            | Da lì: 24 ore per la comunicazione.
            | E l'imposta di soggiorno la versi tu,
            | anche se l'ospite non la paga.
CTA         | Scrivi in DM
Caption     | —
```
Riga di risposta (chiusura della storia): **"Da noi succede mentre dormi. È già dentro la gestione."**

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| marca temporale | 260-300 | +24:00 (chip oro, allineata a destra) | Manrope 600 maiusc. tracking 8 | 17 | #C8A24B |
| gancio | 700-860 | 2 righe — "23:40" in oro dentro la riga | Archivo 900 | 70 | #FFF / #C8A24B |
| corpo problema | 920-1100 | 4 righe | Manrope 500 | 40 | #d8d2c4 |
| riga risposta | 1160-1280 | 2 righe | Archivo 800 | 50 | #C8A24B |
| CTA | 1420-1540 | pill oro piena larghezza | Archivo 800 | 40 | #2E2A25 su #C8A24B |

Griglia: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso (nulla di leggibile sotto y 1600)
Velo: `radial-gradient(ellipse 90% 30% at 50% 50%, rgba(26,23,19,.64), transparent 62%), linear-gradient(180deg, rgba(46,42,37,.88) 0%, rgba(46,42,37,.24) 36%, rgba(46,42,37,.92) 100%)`

**PROMPT GRAFICO (EN)**
```
Hallway of a lived-in Roman apartment late at night, a single warm floor lamp switched on,
travertine floor, closed front door at the end of the corridor, a folded towel on a walnut
bench, nobody in the room --
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
phone screens with interface, keyboxes, lockboxes,
distorted furniture, warped perspective, bent walls, tilted horizon, people in frame,
extra limbs, deformed hands, mannequin faces, plastic skin,
oversaturated colours, HDR halos, heavy vignette, lens flare,
blue tones, navy, teal and orange grading, cyan shadows, moonlight blue,
cluttered surfaces, messy cables, visible brand appliances, TV screens with content,
fisheye distortion, low resolution, jpeg artifacts, noise, blur,
generic stock photo look, 3D render look, videogame lighting
```

**PARAMETRI**
`--ar 9:16 --v 6.1 --style raw --s 150 --seed 140926`

**CLAIM**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Lo identifichi. Poi entra." | CONFERMATO (dato 8) — **riga non rimovibile**: senza di essa la storia descriverebbe un ingresso non conforme |
| 2 | 24 ore per la comunicazione delle generalità | CONFERMATO (dato 6) |
| 3 | Imposta di soggiorno versata dal gestore anche se l'ospite non paga | CONFERMATO (dato 9) |
| 4 | "Da noi succede mentre dormi. È già dentro la gestione." | CONFERMATO dal titolare 14/09/2026 (anelli 2, 3 e 4) + check-in smart H24 |
| 5 | importi di sanzione · rischio penale · aliquote | **assenti** |

---

## Claim da verificare — riepilogo per `compliance-checker`

| # | Claim | Dove compare | Nota |
|---|---|---|---|
| 1 | **"Nessun costo fisso"** | `F3` (grafica + caption) | **[DATO DA VERIFICARE: esiste davvero zero costo una tantum in avvio — servizio fotografico, set biancheria iniziale, sistemazioni pre-pubblicazione?]** Claim ereditato e ancora aperto da `facebook-stagionalita-reel-proprietari`. **Se non chiuso prima della pubblicazione: si toglie la riga e resta solo "15% sul fatturato".** |
| 2 | **Imposta di soggiorno fuori dal Comune di Roma** | `C4` (indirettamente) | **[DATO DA VERIFICARE: tariffa e regolamento per gli immobili in gestione sul Litorale fuori da Roma Capitale, es. Fiumicino.]** Il copy dice "A Roma sono 6 € a persona a notte": scritto così è accurato. Serve la risposta pronta per i commenti, non una correzione del testo. |
| 3 | Sanzioni CIN 500-8.000 € | nessuna grafica | Confermato solo con riserva sulla singola fattispecie (dato 3): **alluso, mai stampato**. Da tenere così anche in eventuali risposte ai commenti. |
| 4 | Numero e data della sentenza del Consiglio di Stato sul self check-in | nessun contenuto | Non citata di proposito (dato 8): si usa solo la sostanza — identificazione de visu prima dell'accesso. |
| 5 | Delibera capitolina sull'imposta di soggiorno | nessun contenuto | Riferimento DA VERIFICARE (dato 9): si cita la tariffa, mai l'atto. |

### Regole rispettate nel testo (da non rompere in revisione)

- **Nessuna aliquota fiscale** (21% / 26% / 30%) in nessun contenuto, nemmeno nell'anello sull'incasso dei canoni.
- **Nessun riferimento al regolamento di Roma Capitale** (limiti di notti, IMU).
- **Nessun rischio penale**, nessun TULPS, nessun "arresto".
- **Nessun importo di sanzione stampato in grafica.** La sanzione è allusa, mai quantificata.
- **Nessun "pensiamo noi alle tasse"**: al contrario, `F3` e la caption del carosello dicono esplicitamente che la dichiarazione dei redditi resta col commercialista del proprietario e che Hadrianus non dà consulenza fiscale.
- **Nessuna garanzia di risultato normativo**: mai "zero multe", "conformità garantita", "non rischi più niente".
- **Mai un ingresso senza identificazione**: in `C3`, `F2` e `S2` l'ordine "prima lo identifichi, poi gli dai l'accesso" è vincolante.
- **Nessun articolo di legge, comma o numero di circolare** nel carosello e nelle storie. La data e il nome del regolamento stanno **solo** nel post Facebook.
- **Nessuna struttura nominata** come prova. Nessun numero di clienti, sanzioni evitate, controlli superati.
- **"standard alberghiero"**, mai "hotel-style". **"Guadagniamo solo se guadagni tu"**, mai "guadagni solo se guadagni tu", e sempre in chiusura.
- **La frase onesta non si ammorbidisce**: "La responsabilità resta tua. Il lavoro no." resta in `C5`, e la sua variante ("non smetti di essere il titolare, smetti di essere l'esecutore") resta nella caption di `F3`. Se in revisione diventa "stai tranquillo, pensiamo a tutto noi", il contenuto perde esattamente ciò che lo distingue dai competitor.
- **Anti-sovrapposizione rispettata**: il reel non elenca adempimenti, il carosello non porta date né norme, Facebook è l'unico con il 20 maggio 2026, le storie prendono i due estremi e non si citano a vicenda.

---

## Nota per `art-director`

**Pattern visivo nuovo, obbligatorio.** Nessuno dei layout registrati in `design-system.md` §"Pattern già usati" va ripreso: niente blocchi invertiti a piena larghezza, niente scontrino/ledger con spina verticale oro, niente calendario a 12 caselle, niente step numerati giganti, niente box con bordo sinistro oro, niente device mockup.

**Firma grafica di questa campagna: "la marca temporale + l'arco che si chiude".**
1. Ogni artboard porta in alto una **marca temporale in oro, maiuscola, tracking 8** (`T ZERO`, `01 · PRIMA CHE L'ANNUNCIO SIA ONLINE`, `+24:00`, `20 MAGGIO 2026`, `FINE MESE`): è il modo di rendere visibile *il tempo*, che è l'argomento della giornata.
2. In basso a destra un **arco oro sottile** su traccia fumè che si chiude di contenuto in contenuto (1/5 → 5/5 nel carosello, 1/3 → 3/3 su Facebook). Nel reel lo stesso concetto è la **barra di avanzamento oro** già prevista dal modello per i formati sopra i 10 secondi.
3. Nessuna card, nessun riquadro: il testo vive sul fondo, la gerarchia la fanno corpo e colore.

**Altre indicazioni:**
- **Le foto reali vincono sulle generate.** Dove `brand-assets/immobili/` e `brand-assets/ambientazione/` hanno uno scatto pertinente, si usa quello e il prompt resta come alternativa. Per il reel usare le clip pulite di `brand-assets/video/clean/` (`balcone`, `interno-cucina`, `busto-frontale`), mai le versioni con filigrana.
- **Un'immagine generata non è mai un immobile in gestione**: nessuna didascalia, nessun sottinteso di possesso.
- `C4` e `F2` sono le uniche superfici chiare (sabbia `#F5F0E6`): servono da respiro nel mezzo di due sequenze scure. Non aggiungerne altre.
- Base scura **grigio fumè caldo** (`#3F3A33`), **mai blu navy**. Tipografia Archivo/Manrope. Tutti i file consegnati come **artboard editabili** (`.dc.html` su canvas Claude Design), PNG solo come export aggiuntivo.
- **Blocco:** la riga "Nessun costo fisso" di `F3` non va impaginata come definitiva finché il claim 1 del riepilogo non è chiuso. In grafica un claim diventa più assertivo che nel testo.
- I sei controlli di qualità di `master-template.md` vanno fatti sul PNG renderizzato, a dimensione telefono, **prima** di mostrare qualcosa.

---

**Prossimo passo obbligatorio:** `compliance-checker`. Questo materiale non va consegnato al cliente né pubblicato prima di quel passaggio. Dopo la revisione, la giornata va registrata in `campagne/giornaliero/PIANO.md` e l'angolo ("esposizione amministrativa / la casella dimenticata / la catena di ogni prenotazione") aggiunto a `campagne/INDEX.md`.
