# Copy — Giornaliero 2026-09-15 (martedì · pilastro IL METODO)

**Angolo**: il prezzo di una notte a Roma lo decide il calendario della città, non un software.
**Gancio guida**: *Ci sono notti a Roma che valgono il doppio di altre — e noi sappiamo quali.*
**CTA unica**: Scrivi CALCOLO in DM
**Seed di campagna**: 260915

> Nota di perimetro: nessuna tariffa, nessuna percentuale di occupazione, nessun incremento di ricavo.
> "Valgono il doppio" resta figura di linguaggio sulla **domanda della città**; dove poteva leggersi come
> promessa di ricavo è stato riformulato in "non vale come" / "non sono lo stesso prezzo".
> Le date dei concerti a Piazza di Siena segnalate dal brief come da ricontrollare **non sono usate**.

---

## Varianti hook/apertura (per la revisione)

1. **A — la notte che non vale come l'altra** (usata come principale)
   `Ci sono notti a Roma che valgono il doppio.`
2. **B — il calendario contro l'istinto**
   `Il prezzo di stanotte lo decide Roma, non tu.`
3. **C — due date a confronto** (usata nel carosello S1)
   `23 ottobre e 3 novembre non sono lo stesso prezzo.`

---

# 1 · REEL — 18,0 s · Struttura C adattata

### R1 · Instagram Reel · 1080×1920 · 30 fps · gancio freddo → contatto

**COPY**
Gancio      | Ci sono notti che valgono il doppio.
Corpo       | Il calendario di Roma decide
            | il prezzo. Noi lo leggiamo.
CTA         | Scrivi CALCOLO in DM
Caption     | Vedi §1.3

### 1.1 Tabella scene — tempi al decimo di secondo

| t (s) | Testo esatto a schermo | Cosa si muove | Meccanica |
|---|---|---|---|
| 0,0-0,5 | `Richiesta · 24 ottobre` | Notifica 1 entra dall'alto, **già a metà corsa al frame 0** | `translateY(-40px→0)` + scala 0,94→1, 220 ms, `animation-delay:-0.22s`, `cubic-bezier(.16,1,.3,1)` |
| 0,5-1,1 | `Richiesta · 3 novembre` | Notifica 2 entra; la 1 scende di 96 px e va a opacità 0,45 | cadenza 600 ms |
| 1,1-1,6 | `Richiesta · 8 dicembre`<br>+ gancio: `Ci sono notti che valgono il doppio.` | Notifica 3 entra; **sopra tutto atterra il gancio** in maschera dal basso; filo oro 3 px sotto il gancio si disegna | `clip-path: inset(100% 0 0 0)→inset(0)`, 180 ms; `width:0→100%` 220 ms sul filo |
| 1,6-2,1 | `Richiesta · 25 ottobre` | Notifica 4, cadenza 500 ms | |
| 2,1-2,5 | `Richiesta · 1 novembre` | Notifica 5, cadenza 400 ms | |
| 2,5-2,8 | `Richiesta · 7 dicembre` | Notifica 6, cadenza 320 ms. La pila è ora di 6 righe sfalsate | il ritmo che accelera è il cuore del blocco |
| 2,8-3,2 | *(gancio ancora a schermo)* | Le notifiche si stringono di 6 px verso l'alto, immobilità del gancio | micro-tensione prima dello stacco |
| **3,2** | — | **Stacco netto.** Tutto sparisce. Fondo fumè pulito | 0 ms, nessuna dissolvenza |
| 3,2-4,4 | `A Roma il prezzo lo decide il calendario.` | Frase che ribalta, **parola per parola** al centro, 170 ms a parola, in accumulo. La parola `calendario` arriva in oro | RSVP in accumulo, `translateY(12px)`+opacità |
| 4,4-4,8 | *(nessun nuovo elemento)* | **Immobilità totale 400 ms** | pausa dopo il picco |
| 4,8-5,0 | `IL PREZZO, IN ORDINE` | Stacco. Il kicker entra in alto con `letter-spacing` che si chiude da 0,4em a 0,02em. Parte la barra oro di avanzamento (0/4) | 400 ms sul kerning |
| 5,0-6,6 | `01` gigante oro<br>`Il calendario di Roma`<br>`Fiere, festival, ponti, feste.` | Numero `01` (Archivo 900, 240 px) entra da sinistra; titolo e riga di dettaglio sfasati di 250 ms. Barra a 1/4 | maschera `overflow:hidden` |
| 6,6-8,2 | `02` gigante oro<br>`La base e il minimo`<br>`Sotto una soglia non si scende.` | `01` **esce verso l'alto in maschera** mentre `02` entra dal basso, stessa posizione. Barra a 2/4 | scorrimento numero 200 ms |
| 8,2-9,8 | `03` gigante oro<br>`Le date calde`<br>`Le notti di un evento non valgono come le altre.` → a schermo: `Una notte di evento fa storia a sé.` | Idem, con lo sfondo che fa un micro-zoom 1,00→1,03. Barra a 3/4 | terza grammatica di movimento |
| 9,8-11,4 | `04` gigante oro<br>`Ogni giorno, di nuovo`<br>`Si guarda la città e si corregge.` | Idem. Barra a 4/4 con **scatto di scala 1,08→1** | 180 ms |
| 11,4-11,8 | `01 02 03 04` | Le quattro fasi si affiancano compresse in alto (scala 1→0,25) e vanno a opacità 0,4 | compressione, 400 ms |
| 11,8-12,2 | *(griglia vuota)* | Sotto entra il **calendario mensile** vuoto, celle fumè chiaro | maschera dal basso 220 ms |
| 12,2-13,2 | *(nessun testo)* | **Le celle si riempiono d'oro a ondata diagonale** — momento clou. Nessuna cifra dentro le celle | `animation-delay` per riga+colonna, 900 ms totali |
| 13,2-13,6 | *(immobilità)* | Calendario pieno, fermo | respiro 400 ms |
| 13,6-15,0 | `Il calendario di Roma lo teniamo noi.` | La riga entra in maschera sopra il calendario; **evidenziatore oro che corre** sulle ultime tre parole (`lo teniamo noi`), che virano a `#2E2A25` a metà corsa | `background-size:0% 100%→100% 100%`, 260 ms, `transform-origin:left` |
| 15,0-15,4 | *(immobilità)* | Nessun movimento | pausa dopo il picco |
| 15,4-15,7 | — | Il calendario va in `blur(10px)` | 300 ms |
| 15,7-17,2 | `Scrivi CALCOLO in DM`<br>kicker sotto: `Guadagniamo solo se guadagni tu.` | CTA oro a pillola entra dal basso e si ferma di colpo | 260 ms |
| 17,2-17,6 | — | La CTA **si ritira** verso il basso, il blur si scioglie, il calendario sfuma via | preparazione del loop |
| 17,6-18,0 | `Richiesta · 24 ottobre` | Fondo fumè pulito col marchio. **La prima notifica ricomincia a entrare** dall'alto, stessa velocità del frame 0 | loop di stato + movimento |

**Conteggio parole per schermata**: massimo 6 (`Il calendario di Roma lo teniamo noi.` = 6).
**Grammatiche di movimento presenti (≥3)**: entrata-notifica con overshoot · RSVP parola per parola · maschera-rullo verticale sui numeri · compressione di scala · ondata diagonale sul calendario · evidenziatore che corre · blur. → **7**.
**Eventi nei primi 2 s (≥3)**: notifica già in corso al frame 0 · seconda e terza notifica · atterraggio del gancio · filo oro. → **5**.
**Elementi persistenti**: marchio in alto per tutti i 18 s · barra oro di avanzamento da 4,8 a 11,4 s · oro in ogni scena.

**LAYOUT (reel)**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| barra avanzamento | 250-256 | barra oro 4 segmenti | — | — | #C8A24B su #57504733 |
| notifiche | 420-1080 | 6 card pila, altezza 152, raggio 20 | Manrope 600 | 40 | #FFF su #4A443C |
| gancio | 1180-1330 | 2 righe | Archivo 900 | 70 | #FFF |
| numero fase | 700-940 | `01`…`04` | Archivo 900 | 240 | #C8A24B |
| titolo fase | 760-820 | riga 1 | Archivo 800 | 62 | #FFF |
| dettaglio fase | 840-900 | riga 2 | Manrope 600 | 40 | #E6DFD4 |
| calendario | 760-1240 | griglia 7×5, cella 128 px, gap 12 | — | — | celle #4A443C → #C8A24B |
| riga chiave | 1330-1450 | 1 riga | Archivo 800 | 62 | #FFF, evidenziatore #C8A24B |
| CTA | 1470-1560 | pillola oro | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |
| firma | 1580-1620 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #E6DFD4 |
Griglia: margine 64 px · colonna utile 952 px · safe area 180 px alto, 320 px basso · passo 20 px
Velo: `linear-gradient(180deg, rgba(38,34,29,.92) 0%, rgba(38,34,29,.55) 40%, rgba(38,34,29,.94) 100%)`
Fondo: `radial-gradient(ellipse 120% 70% at 50% 28%, #4A443C 0%, #3F3A33 55%, #2E2A25 100%)`

**PROMPT GRAFICO (EN)**
*Nessuna immagine generata: il reel è interamente HTML/CSS (finta interfaccia + tipografia cinetica), come da vincolo di produzione di `reel-virali.md`.* — Se serve un fondo fotografico per la sola scena 0,0-3,2 s:
Aerial view of a Roman residential rooftop skyline at dusk, terracotta roofs, domes far in the background, no landmarks in focus --
composition follows the rule of thirds, camera level, vertical lines straight, the upper half of the frame is empty sky as negative space, generous headroom --
warm smoky-grey and sand colour palette, muted brass accents, blue hour warmth, low saturation, gentle film-like contrast --
shot on Canon EOS R5, 24-70mm at 35mm, f/5.6, ISO 400, architectural photography, natural light only, photorealistic, no CGI look

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, captions, calendars, numbers, distorted architecture, warped perspective, tilted horizon, oversaturated colours, HDR halos, **blue tones, navy**, teal and orange grading, crowds, recognizable landmarks in sharp focus, event logos, festival branding, 3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
--ar 9:16 --v 6.1 --style raw --s 150 --seed 260915

**CLAIM (reel)**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Ci sono notti che valgono il doppio" | figura di linguaggio sulla **domanda**, non sul ricavo — nessuna cifra a schermo |
| 2 | Date nelle notifiche (24 e 25 ottobre, 1 e 3 novembre, 7 e 8 dicembre) | CONFERMATO (Maker Faire 23-25/10; Roma Jazz 1-24/11; 1/11 domenica; 8/12 martedì) |
| 3 | Metodo in 4 fasi | CONFERMATO — processo interno, nessun risultato promesso |
| 4 | Celle di calendario che si riempiono | simbolo di **processo**, non promessa di occupazione — nessuna % affiancata |
| 5 | "Guadagniamo solo se guadagni tu" | lessico di brand (formula esatta) |
| 6 | "Il calendario di Roma lo teniamo noi" | CONFERMATO — dipende da noi, registro assertivo ammesso |

### 1.3 Caption del reel

```
Ci sono notti a Roma che valgono il doppio di altre.
Non è istinto: è il calendario della città.

Il 23-25 ottobre c'è Maker Faire Rome al Gazometro.
L'1 novembre cade di domenica, e il weekend si allunga.
Dall'1 al 24 novembre c'è la 50ª edizione del Roma Jazz Festival.
L'8 dicembre cade di martedì: ponte pieno con il lunedì 7.

Chi gestisce da solo mette un prezzo e lo lascia lì.
Noi lo costruiamo in quattro passaggi e lo rivediamo ogni giorno.

Pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero, foto e annuncio: dentro il 15% sul fatturato generato. A fine mese ricevi il bonifico netto.

Guadagniamo solo se guadagni tu.
Scrivi CALCOLO in DM: ti facciamo la simulazione gratuita del rendimento.

#affittibrevi #roma #ostia #propertymanagement #casavacanze
```

---

# 2 · CAROSELLO — 5 slide · 1080×1350

*Il pezzo da salvare. S2 deve funzionare come screenshot autonomo.*
Griglia comune: margine 64 px · colonna utile 952 px · centro ottico y 675 · passo 20 px · scala massima 62.

### C1 · Instagram carosello · 1080×1350 · gancio

**COPY**
Gancio      | Non tutte le notti di Roma
            | valgono uguale.
Corpo       | 23 ottobre e 3 novembre
            | non sono lo stesso prezzo.
CTA         | → scorri
Caption     | vedi §2.6

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| gancio | 520-700 | 2 righe | Archivo 900 | 70 | #FFF, `uguale` in #C8A24B |
| filo oro | 730-736 | linea 3 px, larghezza 220 | — | — | #C8A24B |
| corpo | 780-900 | 2 righe | Manrope 600 | 45 | #E6DFD4 |
| indicatore | 1230-1270 | → scorri | Manrope 600 maiusc. | 31 | #C8A24B |
Velo: `linear-gradient(180deg, rgba(38,34,29,.86) 0%, rgba(38,34,29,.40) 45%, rgba(38,34,29,.90) 100%)`

---

### C2 · Instagram carosello · 1080×1350 · **la slide da screenshottare**

**COPY**
Gancio      | Le date da segnare
Corpo       | Autunno 2026 a Roma
CTA         | Salva questa slide
Caption     | —

Contenuto della card (4 righe, formato `data · evento`):

| Data | Riga a schermo |
|---|---|
| 23-25 ottobre | `Maker Faire Rome — Gazometro` |
| 1-24 novembre | `Roma Jazz Festival, 50ª edizione` |
| 1 novembre | `Cade di domenica: weekend lungo` |
| 7-8 dicembre | `L'8 cade di martedì: ponte pieno` |

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| kicker | 260-300 | LE DATE DA SEGNARE | Manrope 700 maiusc., ls 0,18em | 31 | #C8A24B |
| titolo | 330-400 | Autunno 2026 a Roma | Archivo 900 | 62 | #FFF |
| card | 460-1160 | 4 righe, altezza 160, gap 16, raggio 20, fondo `#4A443C` | — | — | — |
| — data | +32 da cima riga | 23-25 ottobre | Archivo 800 | 50 | #C8A24B |
| — evento | +96 da cima riga | Maker Faire Rome — Gazometro | Manrope 600 | 40 | #FFF |
| firma | 1200-1250 | Salva questa slide | Manrope 600 | 31 | #E6DFD4 |
Nessun logo di terzi, nessun riferimento a biglietti: sono informazioni di pubblico dominio.

---

### C3 · Instagram carosello · 1080×1350 · il metodo

**COPY**
Gancio      | Come si costruisce
            | il prezzo di una notte
Corpo       | Quattro passaggi, in ordine.
CTA         | → scorri
Caption     | —

| # | Titolo | Riga di dettaglio |
|---|---|---|
| 01 | Il calendario di Roma | Fiere, festival, ponti, feste. Prima della casa, si guarda la città. |
| 02 | La base e il minimo | Un prezzo feriale, uno weekend, una soglia sotto cui non si scende. |
| 03 | Le date calde | Una notte di evento fa storia a sé. Non vale come quella dopo. |
| 04 | Ogni giorno, di nuovo | Si guarda cosa resta libero in zona e si corregge. |

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| titolo | 280-410 | 2 righe | Archivo 900 | 62 | #FFF |
| blocchi | 470-1180 | 4 blocchi, altezza 160, gap 18 | — | — | — |
| — numero | sinistra, larghezza 120 | 01…04 | Archivo 900 | 62 | #C8A24B |
| — titolo | colonna destra | La base e il minimo | Archivo 800 | 45 | #FFF |
| — dettaglio | sotto titolo | riga unica | Manrope 600 | 33 | #E6DFD4 |
| indicatore | 1230-1270 | → scorri | Manrope 600 maiusc. | 31 | #C8A24B |

---

### C4 · Instagram carosello · 1080×1350 · la notte-buco

**COPY**
Gancio      | La notte singola
            | fra due prenotazioni
Corpo       | A listino resta vuota.
            | Si abbassa e si vende.
CTA         | → scorri
Caption     | —

Riga di chiusura slide: `È il pezzo che chi gestisce da solo non ha tempo di guardare.`
*(nessuna nota di demerito: constata il vincolo di tempo, non attribuisce una colpa — la riga successiva è sempre nostra)*
Riga finale: `Noi lo guardiamo ogni giorno.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| mini-calendario | 280-660 | riga di 7 celle 120×120, 2 piene oro, 1 vuota al centro, 4 piene oro | Manrope 700 | 40 | #C8A24B / #4A443C |
| gancio | 720-860 | 2 righe | Archivo 900 | 62 | #FFF |
| corpo | 900-1010 | 2 righe | Manrope 600 | 45 | #E6DFD4 |
| chiusura | 1060-1180 | 2 righe | Archivo 800 | 45 | #FFF, `ogni giorno` in #C8A24B |

---

### C5 · Instagram carosello · 1080×1350 · offerta + CTA

**COPY**
Gancio      | Il calendario di Roma
            | lo teniamo noi.
Corpo       | Aggiornato tutti i giorni,
            | incluso nella gestione.
CTA         | Scrivi CALCOLO in DM
Caption     | vedi §2.6

Elenco incluso nel 15% (5 voci, icone a spunta oro):
`Pricing dinamico` · `Check-in smart H24` · `Gestione ospiti` · `Pulizie in standard alberghiero` · `Foto e annuncio`
Riga sotto l'elenco: `A fine mese ricevi il bonifico netto.`
Firma: `Guadagniamo solo se guadagni tu.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| gancio | 260-390 | 2 righe | Archivo 900 | 62 | #FFF, `noi` in #C8A24B |
| corpo | 430-540 | 2 righe | Manrope 600 | 45 | #E6DFD4 |
| badge 15% | 580-680 | pastiglia `15% sul fatturato generato` | Manrope 700 | 40 | #C8A24B su #4A443C |
| elenco | 720-1030 | 5 righe con spunta oro, altezza 60 | Manrope 600 | 40 | #FFF |
| bonifico | 1060-1100 | riga unica | Manrope 600 | 33 | #E6DFD4 |
| CTA | 1140-1230 | banda oro a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |
| firma | 1250-1290 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #E6DFD4 |

**PROMPT GRAFICO (EN) — fondo comune C1 e C5**
Quiet Roman street in the Prati district at golden hour, warm stone façades, shuttered windows, empty pavement, a single scooter out of focus in the distance --
composition follows the rule of thirds, camera perfectly level, vertical lines straight, the central horizontal band of the frame is empty negative space, generous headroom --
warm smoky-grey and sand colour palette, muted brass accents, golden hour side light, warm neutral white balance, low saturation, gentle film-like contrast --
shot on Canon EOS R5, 35mm, f/4, ISO 200, editorial travel photography, natural light only, photorealistic, no CGI look
*(C2, C3 e C4 sono grafiche piene fumè: nessuna foto, la leggibilità dei dati viene prima.)*

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, captions, calendars, numbers, recognizable faces, crowds, festival branding, event logos, distorted architecture, warped perspective, tilted horizon, oversaturated colours, HDR halos, **blue tones, navy**, teal and orange grading, 3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
--ar 4:5 --v 6.1 --style raw --s 150 --seed 260915

**CLAIM (carosello)**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Maker Faire Rome, 23-25 ottobre 2026, Gazometro | CONFERMATO (brief) |
| 2 | Roma Jazz Festival, 50ª edizione, 1-24 novembre 2026 | CONFERMATO (brief) |
| 3 | 1 novembre 2026 cade di domenica | CONFERMATO (calendario civile) |
| 4 | 8 dicembre 2026 cade di martedì, ponte con lunedì 7 | CONFERMATO (calendario civile) |
| 5 | Concerti Piazza di Siena | **ESCLUSI** — segnalati dal brief come da ricontrollare |
| 6 | 15% sul fatturato generato, bonifico netto a fine mese | CONFERMATO (offerta) |
| 7 | Servizi inclusi (pricing, check-in H24, ospiti, pulizie, foto e annuncio) | CONFERMATO (offerta) |
| 8 | "standard alberghiero" | lessico di brand |
| 9 | "Guadagniamo solo se guadagni tu" | lessico di brand (formula esatta) |
| 10 | Nessuna tariffa, % di occupazione o incremento di ricavo | assente per costruzione |

### 2.6 Caption del carosello

```
Ci sono notti a Roma che valgono il doppio di altre. Queste sono quelle dell'autunno.

23-25 ottobre — Maker Faire Rome, al Gazometro.
1-24 novembre — Roma Jazz Festival, 50ª edizione.
1 novembre — cade di domenica: il weekend si allunga.
7-8 dicembre — l'8 cade di martedì: ponte pieno.

Salva la seconda slide: ti serve anche se non ci scrivi mai.

Il prezzo di una notte non è un numero che si mette una volta. Si costruisce in ordine: calendario della città, base e minimo, date calde, correzione quotidiana.

Il calendario di Roma lo teniamo noi, aggiornato tutti i giorni, incluso nella gestione. Con pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero, foto e annuncio. 15% sul fatturato generato, e a fine mese ricevi il bonifico netto.

Guadagniamo solo se guadagni tu.
Scrivi CALCOLO in DM per la simulazione gratuita.
```

---

# 3 · POST FACEBOOK — 3 immagini

### F1 · Facebook · 1080×1920 · gancio + le date

**COPY**
Gancio      | Le notti di Roma
            | non valgono tutte uguale.
Corpo       | Le date dell'autunno 2026,
            | in chiaro. Segnatele.
CTA         | Salva questo post
Caption     | vedi §3.4

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| gancio | 420-580 | 2 righe | Archivo 900 | 70 | #FFF, `uguale` in #C8A24B |
| filo oro | 610-616 | linea 3 px, larghezza 240 | — | — | #C8A24B |
| card date | 680-1340 | 4 righe, altezza 150, gap 16, raggio 20, fondo #4A443C | Archivo 800 / Manrope 600 | 50 / 40 | #C8A24B / #FFF |
| firma | 1400-1450 | Salva questo post | Manrope 600 maiusc. | 31 | #E6DFD4 |
Griglia: margine 64 px · colonna utile 952 px · safe area 180/320
Velo: `linear-gradient(180deg, rgba(38,34,29,.90) 0%, rgba(38,34,29,.50) 40%, rgba(38,34,29,.92) 100%)`
*(la 1ª deve restare 9:16: nel collage Facebook un 4:5 viene tagliato ai lati)*

---

### F2 · Facebook · 1080×1080 · il metodo

**COPY**
Gancio      | Come si costruisce il prezzo
Corpo       | Quattro passaggi, in ordine.
CTA         | —
Caption     | —

Righe: `01 Il calendario di Roma` · `02 La base e il minimo` · `03 Le date calde` · `04 Ogni giorno, di nuovo`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 64-140 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| titolo | 200-270 | 1 riga | Archivo 900 | 62 | #FFF |
| sottotitolo | 290-330 | Quattro passaggi, in ordine. | Manrope 600 | 33 | #E6DFD4 |
| blocchi | 390-900 | 4 righe, altezza 110, gap 16 | Archivo 900 / Archivo 800 | 50 / 40 | #C8A24B / #FFF |
| filo oro | 960-966 | linea 3 px a tutta colonna | — | — | #C8A24B |
Griglia 1:1: margine 64 · centro ottico y 540 · scala massima 62

---

### F3 · Facebook · 1080×1080 · offerta + CTA

**COPY**
Gancio      | Il calendario lo teniamo noi.
Corpo       | Aggiornato tutti i giorni,
            | incluso nel 15%.
CTA         | Scrivi CALCOLO in DM
Caption     | —

Elenco (3 righe per stare nel quadrato): `Pricing dinamico` · `Check-in smart H24 e gestione ospiti` · `Pulizie in standard alberghiero`
Riga: `Foto e annuncio inclusi. A fine mese ricevi il bonifico netto.`
Firma: `Guadagniamo solo se guadagni tu.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 64-140 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| gancio | 210-280 | 1 riga | Archivo 900 | 62 | #FFF, `noi` in #C8A24B |
| corpo | 310-410 | 2 righe | Manrope 600 | 40 | #E6DFD4 |
| elenco | 460-700 | 3 righe con spunta oro, altezza 70 | Manrope 600 | 40 | #FFF |
| riga bonifico | 730-790 | 1 riga | Manrope 600 | 33 | #E6DFD4 |
| CTA | 830-910 | banda oro a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |
| firma | 940-980 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #E6DFD4 |

**PROMPT GRAFICO (EN) — fondo F1**
Rooftop view over warm terracotta Roman roofs in late October light, chimney pots, distant hills, an overcast-to-clear sky --
composition follows the rule of thirds, camera perfectly level, vertical lines straight, the upper two thirds of the frame are empty sky as negative space, generous headroom --
warm smoky-grey and sand colour palette, muted brass accents, low autumn sun, warm neutral white balance, low saturation, gentle film-like contrast --
shot on Canon EOS R5, 50mm, f/5.6, ISO 200, editorial architectural photography, natural light only, photorealistic, no CGI look
*(F2 e F3 su fondo fumè pieno, nessuna foto.)*

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, captions, numbers, calendars, recognizable landmarks in sharp focus, event logos, crowds, faces, distorted architecture, warped perspective, tilted horizon, oversaturated colours, HDR halos, **blue tones, navy**, teal and orange grading, 3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
F1: --ar 9:16 · F2/F3: --ar 1:1 · --v 6.1 --style raw --s 150 --seed 260915

**CLAIM (Facebook)**: identici alla tabella §2 (voci 1-10).

### 3.4 Caption Facebook

```
Un post di servizio per chi ha una casa a Roma. Non serve chiamarci per usarlo.

Il prezzo di una notte non lo decide l'istinto: lo decide il calendario della città. Queste sono le date dell'autunno 2026 che portano gente a Roma.

📌 23-25 ottobre — Maker Faire Rome, al Gazometro.
📌 1-24 novembre — Roma Jazz Festival, 50ª edizione.
📌 1 novembre — cade di domenica: weekend lungo.
📌 7-8 dicembre — l'8 cade di martedì: ponte pieno.

Segnatele e guardate il vostro calendario con queste date davanti.

Poi c'è il mestiere: si parte dal calendario della città, si fissa una base e un minimo sotto cui non si scende, si trattano le date calde per quello che sono, e si corregge ogni giorno guardando cosa resta libero in zona. È un lavoro quotidiano, non un file da compilare una volta.

Questo calendario lo teniamo noi, aggiornato tutti i giorni e incluso nella gestione: pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero, foto e annuncio. 15% sul fatturato generato, bonifico netto a fine mese.

Guadagniamo solo se guadagni tu.

👉 Scrivi la tua zona nei commenti: ti diciamo quali di queste date ti riguardano.
👉 Oppure scrivi CALCOLO in DM per la simulazione gratuita del rendimento.
```

---

# 4 · STORIE — 2, autoconclusive · 1080×1920

*Ognuna dà da sola problema + consiglio vero + cosa facciamo noi + CTA. Mai in sequenza.*

### S1 · Instagram Storia · 1080×1920 · "il prezzo che non si muove"

**COPY**
Gancio      | Da quanto non tocchi
            | il prezzo della tua casa?
Corpo       | Il consiglio: apri il calendario
            | di Roma prima di quello tuo.
CTA         | Scrivi CALCOLO in DM
Caption     | —

**Testo integrale a schermo**
1. `Da quanto non tocchi il prezzo della tua casa?`
2. `Il criterio è semplice: prima del tuo calendario, apri quello di Roma. Ogni data che porta gente in città è una riga a parte — e non vale come la settimana dopo.`
3. `Il 1 novembre cade di domenica. Il 7 e l'8 dicembre sono ponte pieno. Due prezzi diversi, non uno.`
4. `Noi quel calendario lo teniamo aggiornato tutti i giorni e correggiamo il prezzo di conseguenza. È dentro il 15%, insieme a check-in smart H24, ospiti e pulizie in standard alberghiero.`
5. `Guadagniamo solo se guadagni tu.`
6. CTA: `Scrivi CALCOLO in DM`

*(Angolo "prezzo fermo" tenuto sul piano del **metodo per muoverlo**, non nell'elenco di errori già usato da `facebook-campagna-virale`. La storia consegna un criterio operativo — "prima il calendario della città, poi il tuo" — e chiude su cosa facciamo noi.)*

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| gancio | 560-720 | 2 righe | Archivo 900 | 70 | #FFF |
| filo oro | 750-756 | linea 3 px, larghezza 220 | — | — | #C8A24B |
| criterio | 800-980 | 3 righe | Manrope 600 | 45 | #E6DFD4 |
| card date | 1020-1220 | 2 righe, altezza 90, gap 16, fondo #4A443C | Archivo 800 / Manrope 600 | 45 / 33 | #C8A24B / #FFF |
| cosa facciamo | 1260-1400 | 3 righe | Manrope 600 | 40 | #FFF |
| CTA | 1440-1530 | banda oro a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |
| firma | 1550-1590 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #E6DFD4 |
Griglia: margine 64 · safe area 180/320
Velo: `linear-gradient(180deg, rgba(38,34,29,.88) 0%, rgba(38,34,29,.45) 38%, rgba(38,34,29,.94) 100%)`

---

### S2 · Instagram Storia · 1080×1920 · "una data in arrivo"

**COPY**
Gancio      | 23-25 ottobre:
            | Maker Faire Rome.
Corpo       | Tre notti che non valgono
            | come quelle dopo.
CTA         | Scrivi CALCOLO in DM
Caption     | —

**Testo integrale a schermo**
1. `23-25 ottobre: Maker Faire Rome, al Gazometro.`
2. `Tre notti che non valgono come quelle della settimana dopo.`
3. `Il consiglio: segna la data adesso, non a ottobre. Chi prenota per un evento cerca con settimane di anticipo — se il prezzo arriva tardi, la ricerca è già passata.`
4. `Noi apriamo il calendario della città a dodici mesi e marchiamo ogni data calda prima che arrivi. Ogni giorno lo rivediamo. È dentro il 15%: pricing dinamico, check-in smart H24, ospiti, pulizie in standard alberghiero, foto e annuncio.`
5. `Guadagniamo solo se guadagni tu.`
6. CTA: `Scrivi CALCOLO in DM`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #FFF |
| data | 520-600 | 23-25 OTTOBRE | Manrope 700 maiusc., ls 0,18em | 33 | #C8A24B |
| gancio | 620-760 | Maker Faire Rome, al Gazometro. | Archivo 900 | 70 | #FFF |
| corpo | 800-920 | 2 righe | Manrope 600 | 45 | #E6DFD4 |
| consiglio | 960-1160 | 4 righe, card fondo #4A443C, raggio 20 | Manrope 600 | 40 | #FFF |
| cosa facciamo | 1200-1400 | 4 righe | Manrope 600 | 40 | #FFF, `dodici mesi` in #C8A24B |
| CTA | 1440-1530 | banda oro a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |
| firma | 1550-1590 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #E6DFD4 |

**PROMPT GRAFICO (EN) — fondo S1/S2**
Warm Roman interior at dusk, a linen armchair beside a tall window, travertine floor, brass lamp, city rooftops softly out of focus beyond the glass --
composition follows the rule of thirds, camera perfectly level, vertical lines straight, the upper half of the frame is empty wall as negative space, generous headroom --
warm smoky-grey and sand colour palette, muted olive and brass accents, warm lamp light mixed with blue-hour daylight rendered warm, low saturation, gentle film-like contrast --
shot on Canon EOS R5, 24mm, f/4, ISO 400, architectural interior photography, natural light, photorealistic, no CGI look

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, captions, numbers, calendars, people, faces, visible brand appliances, TV screens with content, distorted furniture, warped perspective, bent walls, tilted horizon, oversaturated colours, HDR halos, **blue tones, navy**, teal and orange grading, cluttered surfaces, 3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
--ar 9:16 --v 6.1 --style raw --s 150 --seed 260915

**CLAIM (storie)**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Maker Faire Rome 23-25 ottobre 2026, Gazometro | CONFERMATO |
| 2 | 1 novembre 2026 domenica · 7-8 dicembre ponte (8 martedì) | CONFERMATO |
| 3 | "chi prenota per un evento cerca con settimane di anticipo" | **[DATO DA VERIFICARE: finestra media di prenotazione (booking window) per soggiorni legati a eventi a Roma — serve fonte o va riformulato in "si cerca in anticipo", senza quantificazione]** |
| 4 | Calendario aperto a dodici mesi, rivisto ogni giorno | CONFERMATO — processo interno (brief, passaggi 1 e 5) |
| 5 | 15% e servizi inclusi | CONFERMATO |
| 6 | Nessuna chiusura sul peso che resta al proprietario | verificato: entrambe le storie chiudono su cosa facciamo noi |
| 7 | "Guadagniamo solo se guadagni tu" | lessico di brand (formula esatta) |

---

## Claim da verificare — riepilogo

| # | Dove | Cosa serve |
|---|---|---|
| 1 | S2, riga 3 | **[DATO DA VERIFICARE: anticipo medio di prenotazione per soggiorni legati a eventi]** — in assenza di fonte, sostituire la riga con `Chi prenota per un evento cerca in anticipo: il prezzo va messo prima, non il giorno prima.` (nessuna quantificazione) |

Tutto il resto del pacchetto è su date confermate dal brief, su processo interno o su lessico di brand.
**Escluse volutamente**: date dei concerti a Piazza di Siena (segnalate come da ricontrollare); qualsiasi tariffa, % di occupazione o incremento di ricavo.

---

## Prossimo passo obbligatorio

`compliance-checker` → poi `art-director` per le grafiche editabili → `revisore-marketing-design`.
Nessuna consegna diretta al cliente da questo file.
