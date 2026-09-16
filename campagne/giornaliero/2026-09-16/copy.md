# Copy — Giornaliero 2026-09-16 (mercoledì · pilastro IL NUMERO)

**Angolo**: il costo del vuoto. Una casa chiusa non è a zero: i costi fissi corrono uguale, e l'unica variabile è chi li paga.
**Gancio guida**: *La tua casa chiusa non costa zero euro al mese.*
**CTA unica**: Scrivi CALCOLO in DM
**Seed di campagna**: 260916
**Registro grafico del giorno**: **variante CHIARA** (fondo bianco caldo `#FAF7F1`) — nessun velo, foto accanto al testo in blocchi pieni, oro testuale sempre `#86692A`, oro pieno `#C8A24B` solo come superficie.

> Nota di perimetro (verificata riga per riga):
> nessun totale del costo del vuoto · nessuna media · **nessuna aliquota IMU** (l'IMU compare solo come **scadenza**: 16 giugno e 16 dicembre) · nessuna tariffa, occupazione, incremento o rendimento · nessun importo di condominio, assicurazione o utenze (si nominano come **voci**, mai come cifre).
> L'unico numero stampato in tutto il pacchetto è il dato ISTAT, **sempre con fonte a video**.
> Zero demerito al proprietario: la formula usata è sempre *"nessuno te l'ha mai messo su una riga sola"*.
> Non nominati: morosità, sfratti, inquilini, affitto 4+4, ore/tempo perso, "gente in casa dei miei".
> Nessun gergo da consulente: solo bollettini, quote, contatori, scadenze.

---

## Varianti hook/apertura (per la revisione)

1. **A — la negazione secca** (usata nel reel e su tutto il pacchetto)
   `Una casa vuota non costa niente.` → stop → `Falso.`
2. **B — il conto in cinque pezzi** (usata su Facebook e nel carosello S1)
   `La tua casa chiusa non costa zero euro al mese. L'hai solo sempre visto diviso in cinque pezzi.`
3. **C — il ribaltamento** (usata nelle storie e in chiusura)
   `Non esiste la casa a costo zero. Esiste la casa che i suoi costi se li paga, e quella che te li manda.`

---

## Le cinque voci — testo canonico (identico in tutti i formati)

| # | Voce, come si scrive a schermo | Riga di dettaglio |
|---|---|---|
| 1 | **IMU** | Acconto 16 giugno, saldo 16 dicembre. |
| 2 | **Tassa rifiuti** | Si paga anche se non risiede nessuno. |
| 3 | **Quote condominiali** | Le ordinarie arrivano sui millesimi, non sulle presenze. |
| 4 | **Assicurazione della casa** | Copre l'anno intero, chiusa o aperta. |
| 5 | **Quota fissa dei contatori** | C'è anche a consumo zero. |

Nessuna cifra accanto a nessuna voce, in nessun formato. **Il totale lo fa il lettore.**

---

# 1 · REEL — 17,0 s · formato 1.3 "documento che si compila da sola" + negazione iniziale

### R1 · Instagram Reel · 1080×1920 · 30 fps · gancio freddo → salvataggi e contatto

**COPY**
Gancio      | Una casa vuota non costa niente.
Corpo       | Cinque voci corrono uguale.
            | Cambia solo chi le paga.
CTA         | Scrivi CALCOLO in DM
Caption     | vedi §1.3

### 1.1 Tabella scene — tempi al decimo di secondo

Fondo bianco caldo `#FAF7F1` per tutto il reel. Marchio fisso in alto. Nessuna dissolvenza, nessun nero finale.

| t (s) | Testo esatto a schermo (max 6 parole) | Cosa si muove | Meccanica |
|---|---|---|---|
| 0,0-0,9 | `Una casa vuota non costa niente.` | **Frame 0 già in movimento**: la frase è a metà della sua entrata in maschera dal basso e una fascia sabbia `#F5F0E6` sta scorrendo verso destra dietro il testo | `clip-path: inset(100% 0 0 0)→inset(0)`, 220 ms con `animation-delay:-0.16s`; fascia `translateX(-40px→0)` 400 ms, delay `-0.4s` |
| 0,4-0,9 | *(stessa frase)* | **Secondo evento**: una **riga oro piena `#C8A24B` da 6 px** attraversa la frase da sinistra a destra (cancellatura animata) | `width:0→100%`, 200 ms, `cubic-bezier(.16,1,.3,1)` |
| 0,9-1,5 | `Falso.` | La frase cancellata **esce verso l'alto in maschera**, `Falso.` entra dal basso nella stessa posizione, Archivo 900 gigante, inchiostro `#2E2A25` | rullo `overflow:hidden`, 200 ms |
| 1,5-1,9 | `Falso.` | Immobilità totale. Micro-pausa dopo il picco | 400 ms |
| **1,9** | — | **Stacco netto.** Fondo bianco pulito. Parte la barra oro di avanzamento in alto (0/5) | 0 ms |
| 1,9-2,5 | `Cinque voci che corrono`<br>`a serranda chiusa` | Titolo in due righe, entra parola per parola in accumulo, 110 ms a parola | RSVP in accumulo |
| 2,5-3,6 | `01 IMU`<br>`Acconto 16 giugno, saldo 16 dicembre.` | Riga 1 entra da sinistra con overshoot 8 px; la spunta oro si disegna; barra a 1/5 | `stroke-dashoffset` 220 ms |
| 3,6-4,6 | `02 Tassa rifiuti`<br>`Anche se non risiede nessuno.` | Riga 2 entra; **la riga 1 resta a schermo**, scala 0,86 e opacità 0,45. Barra a 2/5 | la lista **si accumula**, non si sostituisce |
| 4,6-5,5 | `03 Quote condominiali`<br>`Sui millesimi, non sulle presenze.` | Idem. Battuta accorciata di 100 ms. Barra a 3/5 | curva di accelerazione |
| 5,5-6,3 | `04 Assicurazione`<br>`Copre l'anno, chiusa o aperta.` | Idem. Barra a 4/5 | |
| 6,3-7,0 | `05 Quota fissa dei contatori`<br>`C'è anche a consumo zero.` | Idem. Barra a 5/5 con **scatto di scala 1,08→1** | 180 ms |
| 7,0-7,4 | *(lista completa, ferma)* | **Immobilità totale** sulle cinque righe | pausa dopo il picco |
| 7,4-8,6 | `Nessuno te l'ha mai messo`<br>`su una riga sola.` | Le cinque righe si comprimono a sinistra (scala 0,55) e vanno a opacità 0,35; a destra atterra la frase in maschera | compressione di scala, 400 ms |
| **8,6** | — | **Stacco netto.** Fondo bianco pulito | 0 ms |
| 8,6-9,6 | `Il contatore gira anche`<br>`a serranda chiusa.` | Entra da sotto una **serranda disegnata in CSS** che scende (100% in 420 ms) e si ferma; sotto la serranda un quadrante che continua a ruotare lentissimo, senza mai fermarsi | terza grammatica: rotazione continua |
| 9,6-10,0 | *(quadrante che gira)* | Immobilità del testo, il quadrante **non si ferma** | continuità di movimento |
| 10,0-11,4 | `Quelle voci non spariscono.`<br>`Cambia da dove escono i soldi.` | Stacco. Due righe in accumulo, 1ª poi 2ª sfasate di 300 ms | |
| 11,4-12,6 | `Dal tuo stipendio`<br>→<br>`Dalla casa` | **Split orizzontale**: la fascia sabbia superiore (`Dal tuo stipendio`) collassa in altezza fino a 0, quella inferiore (`Dalla casa`) sale a occupare tutto | collasso 500 ms, `cubic-bezier(.16,1,.3,1)` |
| 12,6-13,0 | *(fascia sabbia piena)* | Immobilità | pausa |
| 13,0-14,4 | `L'unica voce che compare solo`<br>`se la casa ha incassato.` | La riga entra in maschera; **evidenziatore oro `#C8A24B` che corre** sotto `se la casa ha incassato`, il testo sopra resta `#2E2A25` | `background-size:0% 100%→100% 100%`, 260 ms, `transform-origin:left` |
| 14,4-14,8 | `15%` | Il badge `15%` scatta in scala 1,12→1 accanto alla riga | 180 ms |
| 14,8-15,2 | *(immobilità)* | Nessun movimento | pausa dopo il dato |
| 15,2-16,4 | `Scrivi CALCOLO in DM`<br>sopra la banda: `Guadagniamo solo se guadagni tu.` | CTA: banda oro piena `#C8A24B` con testo `#2E2A25`, entra dal basso e si ferma di colpo | 260 ms |
| 16,4-16,7 | — | La CTA **si ritira** verso il basso, la fascia sabbia sfuma via, resta il fondo bianco pulito | preparazione del loop |
| 16,7-17,0 | `Una casa vuota non costa niente.` | La frase d'apertura **ricomincia a entrare** in maschera dal basso, stessa velocità del frame 0 | loop di stato + loop di domanda |

**Conteggio parole per schermata**: massimo 6 (`Il contatore gira anche a serranda chiusa.` = 6 su due righe; `Cambia da dove escono i soldi.` = 6).
**Grammatiche di movimento (≥3)**: maschera di rivelazione · cancellatura oro che corre · rullo verticale in maschera · accumulo di lista con scala · compressione · serranda che scende · rotazione continua del quadrante · collasso di fascia · evidenziatore · scatto di scala. → **10**.
**Eventi nei primi 2 s (≥3)**: frase già in entrata al frame 0 · fascia sabbia che scorre · cancellatura oro a 0,4 s · rullo su `Falso.` a 0,9 s. → **4**.
**Elementi persistenti**: marchio in alto per tutti i 17 s · barra oro di avanzamento da 1,9 a 7,0 s · oro presente in ogni scena · margini identici (64 px).
**Differenza dal reel del 15/09**: quello era Struttura C (finta interfaccia + 4 fasi + calendario, fondo fumè). Questo è 1.3 (checklist che si accumula, fondo **chiaro**, negazione iniziale). Struttura e registro cromatico diversi.

**LAYOUT (reel — variante chiara)**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| barra avanzamento | 250-256 | barra 5 segmenti | — | — | #C8A24B su #E7E0D3 |
| gancio negato | 820-1000 | 1-2 righe | Archivo 900 | 70 | #2E2A25, cancellatura #C8A24B 6 px |
| `Falso.` | 830-960 | 1 riga | Archivo 900 | 70 | #86692A |
| lista voci | 480-1300 | 5 righe, altezza 150, gap 16, raggio 20, fondo #F5F0E6 | — | — | — |
| — numero + voce | +30 da cima riga | `01 IMU` | Archivo 800 | 50 | #86692A / #2E2A25 |
| — dettaglio | +92 da cima riga | riga unica | Manrope 500 | 33 | #5A5349 |
| — spunta | destra, 64×64 | segno di spunta | — | — | #C8A24B pieno |
| frase di riscatto | 1180-1320 | 2 righe | Archivo 800 | 62 | #2E2A25 |
| serranda | 420-1100 | pannello CSS a doghe + quadrante rotante Ø 220 | — | — | #E7E0D3 / #C8A24B |
| fasce del ribaltamento | 620-1240 | 2 fasce piene, altezza 310 | Archivo 800 | 62 | #5A5349 su #F5F0E6 → #2E2A25 su #C8A24B |
| riga chiave | 1300-1430 | 2 righe | Archivo 800 | 62 | #2E2A25, evidenziatore #C8A24B |
| badge 15% | 1300-1380 | pastiglia, destra | Archivo 900 | 50 | #2E2A25 su #C8A24B |
| firma | 1450-1490 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #5A5349 |
| CTA | 1510-1600 | banda oro piena a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |
Griglia: margine 64 px · colonna utile 952 px · safe area 180 px alto, 320 px basso · passo 20 px
Velo: **nessuno** — variante chiara, testo mai su foto.
Fondo: `#FAF7F1` pieno; fasce e card in `#F5F0E6`; stacco di superficie, non di luce.

**PROMPT GRAFICO (EN)**
*Nessuna immagine generata: il reel è interamente HTML/CSS (tipografia cinetica + serranda e quadrante disegnati), come da vincolo di produzione di `reel-virali.md`.* — Non serve alcun fondo fotografico: sul chiaro la gerarchia si fa con superficie e peso.

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, captions, numbers, invoices, bills, tax forms, distorted architecture, warped perspective, tilted horizon, oversaturated colours, HDR halos, **blue tones, navy**, teal and orange grading, dark moody interiors, heavy vignette, people, faces, visible brand appliances, TV screens with content, 3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
--ar 9:16 --v 6.1 --style raw --s 150 --seed 260916

**CLAIM (reel)**
| # | Affermazione | Stato |
|---|---|---|
| 1 | "Una casa vuota non costa niente" → "Falso" | costruzione retorica, smentita dalle 5 voci elencate |
| 2 | IMU: acconto 16 giugno, saldo 16 dicembre | CONFERMATO (scadenze di legge, brief punto 1). **Nessuna aliquota a schermo** |
| 3 | Tassa rifiuti dovuta anche senza residenti | CONFERMATO (regolamento TARI Roma Capitale, brief punto 3) |
| 4 | Quote condominiali ordinarie sui millesimi | CONFERMATO — fatto di regola condominiale, nessun importo |
| 5 | Assicurazione: copertura annua | CONFERMATO — natura del contratto, nessun importo |
| 6 | Quota fissa dei contatori a consumo zero | CONFERMATO come voce (brief punto 9). **Nessun importo** |
| 7 | Nessun totale del costo del vuoto | assente per costruzione (brief punto 10) |
| 8 | "Nessuno te l'ha mai messo su una riga sola" | formula imposta dal brief — zero demerito al proprietario |
| 9 | "L'unica voce che compare solo se la casa ha incassato" / 15% sul fatturato | CONFERMATO (offerta) |
| 10 | "Guadagniamo solo se guadagni tu" | lessico di brand (formula esatta) |

### 1.3 Caption del reel

```
Una casa vuota non costa niente.
Falso.

Ci sono cinque voci che una casa paga uguale, aperta o chiusa:
1. IMU — acconto il 16 giugno, saldo il 16 dicembre.
2. Tassa rifiuti — si paga anche se in casa non risiede nessuno.
3. Quote condominiali ordinarie — arrivano sui millesimi, non sulle presenze.
4. Assicurazione — copre l'anno intero.
5. Quota fissa dei contatori — c'è anche a consumo zero.

Non ti diciamo quanto fa: il totale ce l'hai tu, sono cinque bollettini che stanno già in un cassetto. Nessuno te l'ha mai messo su una riga sola, tutto qui.

Mettere la casa a reddito non cancella quelle voci. Le sposta: continuano a uscire, ma escono da soldi che la casa ha prodotto, invece che dal tuo stipendio.

E la nostra è l'unica voce dell'elenco che compare solo se la casa ha incassato: 15% sul fatturato generato. Dentro ci sono pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero e annuncio.

Guadagniamo solo se guadagni tu.
Scrivi CALCOLO in DM.

#affittibrevi #roma #ostia #secondacasa #propertymanagement
```

---

# 2 · CAROSELLO — 5 slide · 1080×1350

*Il pezzo da salvare è **S3**: le cinque voci come modulo da compilare. Deve reggere da sola come screenshot.*
Griglia comune: margine 64 px · colonna utile 952 px · centro ottico y 675 · passo 20 px · scala massima 62.
Fondo `#FAF7F1` su tutte le slide. Nessun velo. Le foto, dove ci sono, stanno in **blocchi pieni accanto al testo**.

### C1 · Instagram carosello · 1080×1350 · gancio

**COPY**
Gancio      | La tua casa chiusa
            | non costa zero euro al mese.
Corpo       | L'hai solo sempre visto
            | diviso in cinque pezzi.
CTA         | → scorri
Caption     | vedi §2.6

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| blocco foto | 240-620 | pannello pieno a tutta colonna, raggio 24 — **foto accanto al testo, mai sotto** | — | — | — |
| gancio | 680-860 | 2 righe | Archivo 900 | 70 | #2E2A25, `non costa zero` in #86692A |
| filo oro | 890-896 | linea 3 px, larghezza 220 | — | — | #C8A24B |
| corpo | 930-1050 | 2 righe | Manrope 500 | 45 | #5A5349 |
| indicatore | 1230-1270 | → SCORRI | Manrope 600 maiusc. | 31 | #86692A |

---

### C2 · Instagram carosello · 1080×1350 · il dato di contesto

**COPY**
Gancio      | Più di 1 casa su 4
            | in Italia non è occupata.
Corpo       | 9.581.772 abitazioni su 35.271.829.
            | Il 27,2%.
CTA         | → scorri
Caption     | —

Riga di fonte, obbligatoria e visibile: `ISTAT, Censimento permanente 2021`
Riga di chiusura slide: `Non è un problema di pochi. È come è fatto il Paese.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| kicker | 260-300 | IL DATO | Manrope 700 maiusc., ls 0,18em | 31 | #86692A |
| numero | 340-520 | 27,2% | Archivo 900 | 70 (display 180 in artboard) | #2E2A25 |
| gancio | 560-700 | 2 righe | Archivo 800 | 62 | #2E2A25 |
| barra proporzione | 740-800 | 4 blocchi affiancati, 1 pieno oro e 3 sabbia | — | — | #C8A24B / #F5F0E6 |
| corpo | 850-960 | 2 righe | Manrope 500 | 40 | #5A5349 |
| chiusura | 1010-1130 | 2 righe | Archivo 800 | 45 | #2E2A25 |
| fonte | 1240-1280 | ISTAT, Censimento permanente 2021 | Manrope 500 | 17 | #5A5349 |

---

### C3 · Instagram carosello · 1080×1350 · **la slide da screenshottare — il modulo**

**COPY**
Gancio      | Le cinque voci che paghi
            | anche a casa chiusa
Corpo       | Scrivi i tuoi importi.
            | Il totale fallo tu.
CTA         | Salva questa slide
Caption     | —

Contenuto della card — **cinque righe con campo vuoto a destra**, più la riga del totale:

| # | Voce | Dettaglio | Campo |
|---|---|---|---|
| 01 | IMU | Acconto 16 giugno, saldo 16 dicembre | `€ ______` |
| 02 | Tassa rifiuti | Anche se non risiede nessuno | `€ ______` |
| 03 | Quote condominiali | Ordinarie, sui millesimi | `€ ______` |
| 04 | Assicurazione | Copre l'anno, chiusa o aperta | `€ ______` |
| 05 | Quota fissa dei contatori | C'è anche a consumo zero | `€ ______` |
| — | **TOTALE IN UN ANNO** | — | `€ ______` |

Riga sotto il modulo: `Non ci sono cifre nostre: questo conto è solo tuo.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| kicker | 220-260 | IL CONTO DEL VUOTO | Manrope 700 maiusc., ls 0,18em | 31 | #86692A |
| titolo | 290-410 | 2 righe | Archivo 900 | 62 | #2E2A25 |
| modulo | 460-1080 | fascia sabbia unica, raggio 24, fondo #F5F0E6, 5 righe altezza 104, separatori 1 px #E2DACB | — | — | — |
| — numero | x 64 | 01…05 | Archivo 900 | 40 | #86692A |
| — voce | x 140 | IMU | Archivo 800 | 45 | #2E2A25 |
| — dettaglio | sotto voce | riga unica | Manrope 500 | 31 | #5A5349 |
| — campo | destra, larghezza 250 | `€ ______` | Manrope 600 | 40 | #5A5349, filo 2 px #C8A24B sotto |
| riga totale | 1100-1180 | banda oro piena, `TOTALE IN UN ANNO  € ______` | Archivo 800 maiusc. | 50 | #2E2A25 su #C8A24B |
| nota | 1200-1240 | Non ci sono cifre nostre: questo conto è solo tuo. | Manrope 500 | 31 | #5A5349 |
| firma | 1270-1310 | SALVA QUESTA SLIDE | Manrope 600 maiusc. | 31 | #86692A |
Nessuna foto su questa slide: la leggibilità del modulo viene prima.

---

### C4 · Instagram carosello · 1080×1350 · il ribaltamento

**COPY**
Gancio      | Quelle voci non spariscono.
Corpo       | Cambia da dove escono i soldi.
CTA         | → scorri
Caption     | —

Confronto a due fasce (impilate, non colonne — sul 4:5 le colonne strozzano il testo):

| Fascia | Etichetta | Riga |
|---|---|---|
| Sopra (sabbia) | CASA CHIUSA | `Le cinque voci escono dal tuo stipendio.` |
| Sotto (oro pieno) | CASA A REDDITO | `Le stesse voci escono da quello che la casa ha incassato.` |

Riga di chiusura: `Non esiste la casa a costo zero. Esiste la casa che i suoi costi se li paga.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| gancio | 250-330 | 1 riga | Archivo 900 | 62 | #2E2A25 |
| corpo | 360-420 | 1 riga | Manrope 500 | 40 | #5A5349 |
| fascia 1 | 470-720 | blocco sabbia, raggio 24 | Archivo 800 | 45 | #5A5349 su #F5F0E6 |
| — etichetta 1 | +28 | CASA CHIUSA | Manrope 700 maiusc., ls 0,18em | 31 | #86692A |
| freccia | 740-800 | ↓ freccia oro piena, 56 px | — | — | #C8A24B |
| fascia 2 | 820-1090 | blocco oro pieno, raggio 24 | Archivo 800 | 45 | #2E2A25 su #C8A24B |
| — etichetta 2 | +28 | CASA A REDDITO | Manrope 700 maiusc., ls 0,18em | 31 | #2E2A25 |
| chiusura | 1130-1250 | 2 righe | Archivo 800 | 45 | #2E2A25 |
| indicatore | 1280-1310 | → SCORRI | Manrope 600 maiusc. | 31 | #86692A |

---

### C5 · Instagram carosello · 1080×1350 · offerta + CTA

**COPY**
Gancio      | La nostra voce compare
            | solo se la casa ha incassato.
Corpo       | 15% sul fatturato generato.
CTA         | Scrivi CALCOLO in DM
Caption     | vedi §2.6

Elenco incluso nel 15% (5 righe, spunte oro piene):
`Pricing dinamico` · `Check-in smart H24` · `Gestione ospiti` · `Pulizie in standard alberghiero` · `Annuncio e foto`
Riga sotto l'elenco: `Si parte da com'è la casa: il primo passo è una valutazione, non un cantiere.`
Firma: `Guadagniamo solo se guadagni tu.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 100-180 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| gancio | 250-390 | 2 righe | Archivo 900 | 62 | #2E2A25, `solo se ha incassato` in #86692A |
| badge 15% | 430-520 | pastiglia oro piena `15% SUL FATTURATO GENERATO` | Manrope 700 maiusc. | 40 | #2E2A25 su #C8A24B |
| corpo | 550-610 | La nostra voce compare solo a incasso avvenuto. | Manrope 500 | 40 | #5A5349 |
| elenco | 660-1000 | fascia sabbia, 5 righe altezza 64, spunta oro 40 px | Manrope 600 | 40 | #2E2A25 su #F5F0E6 |
| riga valutazione | 1030-1110 | 2 righe | Manrope 500 | 33 | #5A5349 |
| firma | 1140-1180 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #5A5349 |
| CTA | 1200-1290 | banda oro piena a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |

**PROMPT GRAFICO (EN) — blocco foto di C1**
Closed roller shutter of a ground-floor apartment on a quiet sunlit street in Rome, pale plaster wall, warm sand and cream tones, a sliver of dusty window frame at the edge, nobody around --
composition follows the rule of thirds, camera perfectly level, vertical lines straight, flat frontal framing, the left third of the frame is empty pale wall as negative space --
warm off-white and sand colour palette, muted brass accents, bright diffuse midday light, warm neutral white balance, low saturation, airy high-key exposure, gentle film-like contrast --
shot on Canon EOS R5, 35mm, f/5.6, ISO 100, editorial architectural photography, natural light only, photorealistic, no CGI look
*(C2, C3, C4 e C5 sono grafiche piene su bianco caldo: nessuna foto.)*

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, graffiti, street numbers, captions, numbers, bills, invoices, people, faces, cars, recognizable landmarks, distorted architecture, warped perspective, tilted horizon, oversaturated colours, HDR halos, **blue tones, navy**, teal and orange grading, dark moody shadows, heavy vignette, 3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
--ar 4:5 --v 6.1 --style raw --s 150 --seed 260916

**CLAIM (carosello)**
| # | Affermazione | Stato |
|---|---|---|
| 1 | 9.581.772 abitazioni non occupate su 35.271.829 = 27,2% | CONFERMATO — ISTAT, Censimento permanente 2021 (brief punto 5). **Fonte stampata in slide** |
| 2 | "1 casa su 4 in Italia non è occupata" | CONFERMATO — arrotondamento fedele del 27,2%, affiancato al dato esatto nella stessa slide |
| 3 | Dato Lazio (618.760 / ~19,5%) e Città metropolitana di Roma (2.240.719) | **ESCLUSI** — brief punti 6 e 7, da ricontrollare sulla tavola ISTAT |
| 4 | IMU: acconto 16 giugno, saldo 16 dicembre | CONFERMATO. Nessuna aliquota |
| 5 | Aliquota IMU Roma 2026 | **ESCLUSA** — fonti discordanti (brief punto 2) |
| 6 | Tassa rifiuti dovuta anche senza residenti | CONFERMATO (brief punto 3) |
| 7 | Numero di rate TARI 2026 e riduzione ~1% | **ESCLUSI** — fonte secondaria (brief punto 4), non necessari |
| 8 | Quote condominiali, assicurazione, quota fissa contatori | CONFERMATE come **voci**; nessun importo (brief punti 8 e 9) |
| 9 | Totale del costo del vuoto | **ASSENTE** — il campo è vuoto, lo compila il lettore (brief punto 10) |
| 10 | 15% sul fatturato generato, servizi inclusi | CONFERMATO (offerta) |
| 10b | "nessun costo fisso" | **RIMOSSO DAL PACCHETTO** — domanda aperta al titolare dal 14/09, mai confermata: non è noto se esistano costi una tantum d'avvio. Non rientra finché non arriva conferma |
| 11 | "il primo passo è una valutazione, non un cantiere" | CONFERMATO — processo, nessuna promessa di spesa zero |
| 12 | "standard alberghiero" · "Guadagniamo solo se guadagni tu" | lessico di brand (formule esatte) |

### 2.6 Caption del carosello

```
La tua casa chiusa non costa zero euro al mese. L'hai solo sempre visto diviso in cinque pezzi.

In Italia 9.581.772 abitazioni risultano non occupate su 35.271.829: il 27,2%, più di una su quattro (ISTAT, Censimento permanente 2021). Non è la situazione di pochi.

Il punto è che il conto di una casa ferma arriva spezzettato e in momenti diversi dell'anno: l'IMU a giugno e a dicembre, la tassa rifiuti a rate, il condominio a quote, i contatori ogni due mesi. Nessuno te l'ha mai messo su una riga sola.

Salva la terza slide e compilala con i tuoi bollettini. Non ci trovi nessuna cifra nostra: il totale è solo tuo, e ha il segno meno davanti.

Mettere la casa a reddito non cancella quelle voci. Le sposta: continuano a uscire, ma escono da quello che la casa ha incassato, non dal tuo stipendio.

E la nostra è l'unica voce dell'elenco che compare solo se la casa ha incassato: 15% sul fatturato generato. Dentro: pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero, annuncio e foto. Si parte da com'è la casa — il primo passo è una valutazione, non un cantiere.

Guadagniamo solo se guadagni tu.
Scrivi CALCOLO in DM.
```

---

# 3 · POST FACEBOOK — 3 immagini

*Registro annuncio di valore. 1ª **9:16**, 2ª e 3ª **1:1**.*

### F1 · Facebook · 1080×1920 · gancio + il problema

**COPY**
Gancio      | La tua casa chiusa
            | non costa zero euro al mese.
Corpo       | Cinque voci corrono uguale,
            | serranda alzata o abbassata.
CTA         | Salva questo post
Caption     | vedi §3.4

Riga di contesto in alto (con fonte): `In Italia il 27,2% delle abitazioni non è occupato — ISTAT, Censimento permanente 2021`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| blocco foto | 260-780 | pannello pieno a tutta colonna, raggio 24 (serranda chiusa) — foto **accanto**, nessun testo sopra | — | — | — |
| pastiglia dato | 700-770 | sovrapposta al bordo basso del blocco, fondo #FAF7F1 pieno: `27,2%` + `abitazioni non occupate in Italia` | Archivo 900 / Manrope 500 | 50 / 31 | #2E2A25 / #5A5349 |
| gancio | 840-1020 | 2 righe | Archivo 900 | 70 | #2E2A25, `zero euro` in #86692A |
| filo oro | 1050-1056 | linea 3 px, larghezza 240 | — | — | #C8A24B |
| corpo | 1090-1210 | 2 righe | Manrope 500 | 45 | #5A5349 |
| fonte | 1250-1290 | ISTAT, Censimento permanente 2021 | Manrope 500 | 17 | #5A5349 |
| CTA | 1400-1490 | banda oro piena a tutta colonna: SCRIVI CALCOLO IN DM | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |
| firma | 1510-1550 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #5A5349 |
Griglia: margine 64 px · colonna utile 952 px · safe area 180/320
Velo: **nessuno** (variante chiara)
*(la 1ª resta 9:16: nel collage Facebook un 4:5 viene tagliato ai lati)*

---

### F2 · Facebook · 1080×1080 · l'elenco

**COPY**
Gancio      | Cinque voci a casa chiusa
Corpo       | Il totale fallo tu, coi tuoi bollettini.
CTA         | —
Caption     | —

Righe: `01 IMU — acconto 16 giugno, saldo 16 dicembre` · `02 Tassa rifiuti — anche se non risiede nessuno` · `03 Quote condominiali — sui millesimi, non sulle presenze` · `04 Assicurazione — copre l'anno intero` · `05 Quota fissa dei contatori — anche a consumo zero`
Riga di chiusura: `Nessuno te l'ha mai messo su una riga sola.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 64-140 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| titolo | 190-260 | 1 riga | Archivo 900 | 62 | #2E2A25 |
| sottotitolo | 280-320 | Il totale fallo tu, coi tuoi bollettini. | Manrope 500 | 33 | #5A5349 |
| modulo | 370-830 | fascia sabbia #F5F0E6, raggio 24, 5 righe altezza 84, separatori 1 px #E2DACB | — | — | — |
| — numero | x 64 | 01…05 | Archivo 900 | 40 | #86692A |
| — voce + dettaglio | x 130 | riga unica | Archivo 800 / Manrope 500 | 40 / 31 | #2E2A25 / #5A5349 |
| — campo | destra, 190 | `€ ____` | Manrope 600 | 33 | #5A5349, filo 2 px #C8A24B |
| chiusura | 880-940 | 1 riga | Archivo 800 | 45 | #2E2A25 |
| filo oro | 980-986 | linea 3 px a tutta colonna | — | — | #C8A24B |
Griglia 1:1: margine 64 · centro ottico y 540 · scala massima 62

---

### F3 · Facebook · 1080×1080 · ribaltamento + offerta + CTA

**COPY**
Gancio      | Quelle voci non spariscono.
Corpo       | Cambia da dove escono i soldi.
CTA         | Scrivi CALCOLO in DM
Caption     | —

Due fasce: `CASA CHIUSA — escono dal tuo stipendio` (sabbia) → `CASA A REDDITO — escono da quello che la casa ha incassato` (oro pieno)
Riga: `La nostra voce compare solo se la casa ha incassato: 15% sul fatturato generato.`
Firma: `Guadagniamo solo se guadagni tu.`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 64-140 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| gancio | 190-250 | 1 riga | Archivo 900 | 62 | #2E2A25 |
| corpo | 270-320 | 1 riga | Manrope 500 | 40 | #5A5349 |
| fascia 1 | 360-520 | blocco sabbia, raggio 24 | Archivo 800 | 45 | #5A5349 su #F5F0E6 |
| freccia | 535-580 | ↓ oro pieno, 44 px | — | — | #C8A24B |
| fascia 2 | 590-760 | blocco oro pieno, raggio 24 | Archivo 800 | 45 | #2E2A25 su #C8A24B |
| riga 15% | 790-860 | 2 righe | Manrope 500 | 33 | #5A5349, `15%` in #86692A |
| firma | 880-915 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #5A5349 |
| CTA | 930-1010 | banda oro piena a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |

**PROMPT GRAFICO (EN) — blocco foto F1**
Closed roller shutter of a ground-floor apartment on a quiet sunlit Roman street, pale cream plaster, sand-coloured stone kerb, a dusty doormat, nobody around, late-morning stillness --
composition follows the rule of thirds, camera perfectly level, vertical lines straight, flat frontal framing, the upper third of the frame is empty pale wall as negative space --
warm off-white and sand colour palette, muted brass accents, bright diffuse daylight, warm neutral white balance, low saturation, airy high-key exposure, gentle film-like contrast --
shot on Canon EOS R5, 35mm, f/5.6, ISO 100, editorial architectural photography, natural light only, photorealistic, no CGI look
*(F2 e F3 su bianco caldo pieno, nessuna foto.)*

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, graffiti, street numbers, mailboxes with names, captions, numbers, bills, invoices, tax forms, people, faces, cars, recognizable landmarks, distorted architecture, warped perspective, tilted horizon, oversaturated colours, HDR halos, **blue tones, navy**, teal and orange grading, dark moody shadows, heavy vignette, 3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
F1: --ar 9:16 · F2/F3: --ar 1:1 · --v 6.1 --style raw --s 150 --seed 260916

**CLAIM (Facebook)**: identici alla tabella §2 (voci 1-12).

### 3.4 Caption Facebook

```
Le cinque voci che una casa a Roma paga anche se è chiusa tutto l'anno. Fai il totale con i tuoi numeri.

In Italia risultano non occupate 9.581.772 abitazioni su 35.271.829: il 27,2%, più di una su quattro (ISTAT, Censimento permanente 2021).

Una casa ha due tipi di spese: quelle che dipendono da quanto la usi, e quelle che non dipendono da niente. Le seconde non guardano il calendario.

1️⃣ IMU — acconto il 16 giugno, saldo il 16 dicembre.
2️⃣ Tassa rifiuti — si paga anche se in casa non risiede nessuno.
3️⃣ Quote condominiali ordinarie — arrivano sui millesimi, non sulle presenze.
4️⃣ Assicurazione — copre l'anno intero, chiusa o aperta.
5️⃣ Quota fissa dei contatori — c'è anche a consumo zero.

Non trovi nessun totale in questo post, ed è voluto: dipende dalla rendita, dai millesimi, dal fornitore. Il totale ce l'hai tu, in cinque bollettini che stanno già in un cassetto. Arrivano separati, in mesi diversi: per questo nessuno te l'ha mai messo su una riga sola.

Sì, mettendo la casa a reddito qualche spesa sale: pulizie, utenze, un po' di usura. Ma quelle salgono perché c'è qualcuno dentro che paga la notte. Le cinque qui sopra le paghi comunque.

Mettere la casa a reddito non cancella quelle voci: le sposta. Continuano a uscire, ma escono da quello che la casa ha incassato, invece che dal tuo stipendio.

E la nostra è l'unica voce dell'elenco che compare solo se la casa ha incassato: 15% sul fatturato generato. Dentro ci sono pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero, annuncio e foto. Se pensi che la casa non sia pronta: il primo passo è una valutazione, non un cantiere. Si parte da com'è.

Guadagniamo solo se guadagni tu.

👉 Dicci nei commenti quante di queste cinque voci paghi: 3 o 5?
👉 Oppure scrivi CALCOLO in DM.
```

---

# 4 · STORIE — 2, autoconclusive · 1080×1920

*Ognuna dà da sola problema + soluzione + CTA. Mai in sequenza, mai un rimando all'altra.*

### S1 · Instagram Storia · 1080×1920 · "la casa dei tuoi"

**COPY**
Gancio      | «Tanto chiusa non costa niente.»
Corpo       | Cinque voci corrono
            | anche a serranda abbassata.
CTA         | Scrivi CALCOLO in DM
Caption     | —

**Testo integrale a schermo**
1. `«Tanto chiusa non costa niente.»`
2. `La casa dei tuoi è ferma da anni. Non è una svista: il conto arriva a pezzi, in mesi diversi. IMU a giugno e a dicembre. Tassa rifiuti anche se non risiede nessuno. Quote condominiali sui millesimi. Assicurazione. Quota fissa dei contatori. Nessuno te l'ha mai messo su una riga sola.`
3. `Quelle voci non spariscono se la casa lavora. Cambia solo da dove escono i soldi: da quello che la casa ha incassato, non dal tuo stipendio.`
4. `La casa la mettiamo a reddito noi: pricing dinamico, check-in smart H24, gestione ospiti, pulizie in standard alberghiero, annuncio e foto. Si parte da com'è — il primo passo è una valutazione, non un cantiere. 15% sul fatturato generato.`
5. `Guadagniamo solo se guadagni tu.`
6. CTA: `Scrivi CALCOLO in DM`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| gancio | 420-580 | 2 righe, tra virgolette | Archivo 900 | 70 | #2E2A25 |
| filo oro | 610-616 | linea 3 px, larghezza 220 | — | — | #C8A24B |
| elenco voci | 660-1080 | fascia sabbia #F5F0E6, 5 righe altezza 76, spunta oro | Manrope 600 / Manrope 500 | 40 / 31 | #2E2A25 / #5A5349 |
| riga di riscatto | 1110-1190 | Nessuno te l'ha mai messo su una riga sola. | Archivo 800 | 45 | #2E2A25 |
| ribaltamento | 1220-1340 | 2 righe | Manrope 500 | 40 | #5A5349, `dalla casa` in #86692A |
| offerta | 1360-1440 | 15% sul fatturato generato. | Manrope 600 | 33 | #2E2A25 |
| firma | 1460-1500 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #5A5349 |
| CTA | 1510-1600 | banda oro piena a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |
Griglia: margine 64 · safe area 180/320 · **nessun velo**

---

### S2 · Instagram Storia · 1080×1920 · "i mesi vuoti"

**COPY**
Gancio      | I mesi vuoti pagano
            | le stesse spese dei pieni.
Corpo       | Il condominio non guarda
            | quante notti hai fatto.
CTA         | Scrivi CALCOLO in DM
Caption     | —

**Testo integrale a schermo**
1. `I mesi vuoti pagano le stesse spese dei mesi pieni.`
2. `Il tuo calendario ha dei buchi. La tassa rifiuti, le quote condominiali, l'assicurazione e la quota fissa dei contatori non li guardano: arrivano uguali a febbraio e ad agosto.`
3. `Tenere un calendario aperto tutto l'anno è un mestiere a parte.`
4. `Il calendario lo teniamo noi, aperto e aggiornato, dentro la gestione completa: check-in smart H24, gestione ospiti, pulizie in standard alberghiero. 15% sul fatturato generato: la nostra è l'unica voce che compare solo se la casa ha incassato.`
5. `Guadagniamo solo se guadagni tu.`
6. CTA: `Scrivi CALCOLO in DM`

**LAYOUT**
| Zona | y (px) | Elemento | Font | Corpo | Colore |
|---|---|---|---|---|---|
| marchio | 112-205 | HADRIANUS / MULTISERVICE | Archivo 800 / Manrope 600 | 33 / 17 | #2E2A25 / #5A5349 |
| barra dei 12 mesi | 300-420 | 12 celle 68×92, gap 10, iniziali dei mesi sotto; alcune piene oro `#C8A24B`, altre vuote `#F5F0E6` con bordo 2 px #E2DACB. **Nessun numero, nessuna percentuale** | Manrope 700 maiusc. | 17 | #2E2A25 / #5A5349 |
| gancio | 480-640 | 2 righe | Archivo 900 | 70 | #2E2A25, `stesse spese` in #86692A |
| filo oro | 670-676 | linea 3 px, larghezza 220 | — | — | #C8A24B |
| corpo | 710-900 | 4 righe | Manrope 500 | 40 | #5A5349 |
| card mestiere | 940-1140 | fascia sabbia, raggio 24, 3 righe | Manrope 600 | 40 | #2E2A25 su #F5F0E6 |
| cosa facciamo | 1180-1380 | 4 righe | Manrope 500 | 40 | #5A5349, `lo teniamo noi` in #86692A |
| offerta | 1400-1450 | 15% sul fatturato generato. | Manrope 600 | 33 | #2E2A25 |
| firma | 1460-1500 | Guadagniamo solo se guadagni tu. | Manrope 600 | 31 | #5A5349 |
| CTA | 1510-1600 | banda oro piena a tutta colonna | Manrope 700 maiusc. | 45 | #2E2A25 su #C8A24B |

**PROMPT GRAFICO (EN) — fondo/blocco foto S1 e S2**
Bright empty room in a Roman apartment seen from the doorway, white-washed walls, pale terrazzo floor, a single sheet-covered armchair, closed light-coloured shutters letting in thin daylight stripes, dust in the air --
composition follows the rule of thirds, camera perfectly level, vertical lines straight, the upper half of the frame is empty pale wall as negative space, generous headroom --
warm off-white, cream and sand colour palette, muted brass accents, soft diffuse daylight, warm neutral white balance, low saturation, airy high-key exposure, gentle film-like contrast --
shot on Canon EOS R5, 24mm, f/5.6, ISO 200, architectural interior photography, natural light only, photorealistic, no CGI look
*(La foto occupa un blocco pieno accanto/sopra il testo, mai sotto il testo: variante chiara, niente veli.)*

**NEGATIVE**
--no text, letters, words, watermark, logo, signage, captions, numbers, calendars, bills, invoices, people, faces, visible brand appliances, TV screens with content, clutter, distorted furniture, warped perspective, bent walls, tilted horizon, oversaturated colours, HDR halos, **blue tones, navy**, teal and orange grading, dark moody shadows, heavy vignette, derelict or damaged interior, peeling paint, 3D render look, generic stock photo look, low resolution, jpeg artifacts

**PARAMETRI**
--ar 9:16 --v 6.1 --style raw --s 150 --seed 260916

**CLAIM (storie)**
| # | Affermazione | Stato |
|---|---|---|
| 1 | Le cinque voci elencate in S1 | CONFERMATE come voci; nessun importo, nessuna aliquota |
| 2 | IMU a giugno e a dicembre | CONFERMATO (scadenze di legge) |
| 3 | "I mesi vuoti pagano le stesse spese dei mesi pieni" | CONFERMATO — deriva dalla natura fissa delle voci, nessuna quantificazione |
| 4 | Celle di calendario piene/vuote in S2 | simbolo di **stato**, non promessa di occupazione: nessuna % affiancata |
| 5 | "Gestire da soli non dà gli strumenti" | mancanza di strumenti, **mai colpa**: nessuna nota di demerito |
| 6 | Calendario tenuto aperto e aggiornato, gestione completa | CONFERMATO — registro assertivo ammesso (dipende da noi) |
| 7 | 15% sul fatturato generato | CONFERMATO (offerta). "Nessun costo fisso" rimosso: domanda aperta al titolare, mai confermata |
| 8 | Nessun riferimento a "gente in casa dei miei", morosità, inquilini, ore perse | verificato: assenti in entrambe le storie |
| 9 | "standard alberghiero" · "Guadagniamo solo se guadagni tu" | lessico di brand (formule esatte) |
| 10 | Storie autoconclusive, nessun rimando reciproco | verificato |

---

## Claim da verificare — riepilogo

**Nessun marcatore aperto: il pacchetto esce senza `[DATO DA VERIFICARE]`.**

Dove serviva una quantificazione, si è scelta la riformulazione senza numero:

| Punto a rischio | Come è stato chiuso |
|---|---|
| Totale del costo del vuoto | **Non pubblicato.** Sostituito dal modulo a campi vuoti (C3, F2): il totale lo scrive il lettore |
| Aliquota IMU Roma 2026 | **Non citata.** L'IMU compare solo come scadenza (16 giugno / 16 dicembre) |
| Spesa condominiale media | **Non citata.** Nominata come voce: "arrivano sui millesimi, non sulle presenze" |
| Quota fissa dei contatori | **Non quantificata.** "C'è anche a consumo zero" |
| Rate e riduzione TARI 2026 | **Escluse** (fonte secondaria, non necessarie) |
| Dati Lazio e Città metropolitana di Roma | **Esclusi** (da ricontrollare sulla tavola ISTAT) |
| Qualsiasi tariffa, occupazione, incremento, rendimento | **Assenti per costruzione** in tutti e cinque i contenuti |

**Unico numero stampato in tutto il pacchetto**: `9.581.772 su 35.271.829 = 27,2%` — ISTAT, Censimento permanente 2021. Compare in C2 (con fonte in slide), in F1 (con fonte in grafica) e nelle caption di carosello e Facebook, **sempre** con la fonte accanto. Nel reel **non compare**: nessuna cifra a schermo, per non dover stampare una fonte in un formato che scorre.

---

## Ritocchi applicati dopo la revisione (16/09)

| # | Dove | Cosa è cambiato |
|---|---|---|
| 1 | C3 | **collisione reale**: "Quote condominiali ordinarie" a 45 px andava a capo e spingeva il dettaglio sotto il separatore della riga 04, dove veniva tagliato. Voce accorciata, dettaglio a riga unica, righe più alte |
| 2 | C3 | la riga "Non ci sono cifre nostre: questo conto è solo tuo." è passata **sopra** la banda del totale, in inchiostro pieno: è quella che impedisce di leggere il modulo come una grafica non finita, e stava sotto in grigio chiaro |
| 3 | S1, S2 | le bande CTA finivano sotto la UI di Instagram (1808 e 1768 contro una safe area di 1600). Ora chiudono entro |
| 4 | C1, S1 | le foto contraddicevano il copy: un salotto arredato con fiori sotto "La tua casa chiusa", e un letto da catalogo. Ora tre inquadrature diverse della **stessa casa vuota** |
| 5 | F1 | due CTA in conflitto a 60 px di distanza: resta solo "Scrivi CALCOLO in DM" |
| 6 | C5 | badge 15% da contorno a **oro pieno**: beige su beige non si leggeva |
| 7 | C2 | aggiunto l'indicatore "→ scorri", che C1 e C4 avevano e lui no |
| 8 | S1 | il modulo compariva identico su C3, F2 e S1. Nella storia diventa un elenco di tre voci senza campo, e libera lo spazio per la CTA |
| 9 | C5 | aggiunta la riga che dice **cosa succede dopo il DM**: nessun artboard lo diceva |
| 10 | reel | tre pause ravvicinate fra 7,0 e 9,6 s, proprio dove il ritmo deve accelerare: sosta sulla lista accorciata, serranda e ribaltamento anticipati |

---

## Prossimo passo obbligatorio

`compliance-checker` → poi `art-director` per le grafiche editabili (variante chiara) → `revisore-marketing-design`.
Nessuna consegna diretta al cliente da questo file.
