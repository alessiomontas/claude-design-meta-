# Direzione artistica — Giornaliero 18/09/2026 · «Le recensioni non sono un complimento»

Impianto approvato dal titolare e realizzato: **la catena ad anelli**. Nessuna alternativa proposta:
l'impianto regge su tutti e quattro i ritmi richiesti e supera i sei controlli di qualità senza
compromessi sulla leggibilità. Le uniche deviazioni sono elencate in fondo, nella sezione *Deviazioni*.

## Mood

**Dimostrativo, progressivo, asciutto.**

- *Dimostrativo* perché l'angolo è un **modello economico**, non un vanto: la grafica deve far vedere un
  meccanismo che avanza, non esibire un badge. Da qui la catena, che è un diagramma travestito da indice.
- *Progressivo* perché la promessa del copy è una catena di conseguenze: ogni schermata deve dire **dove
  siamo** dentro quella catena, anche a chi entra a metà reel.
- *Asciutto* perché il target è competente e stanco dei complimenti. Nessuna decorazione, nessuna icona,
  nessun ornamento: solo cerchi, un filo e una superficie di carta.

## Palette

| Ruolo | Hex | Perché qui |
|---|---|---|
| Fondo (fumè caldo) | `#3F3A33` → `#2E2A25` | Base scura di brand. Il gradiente ha il vertice chiaro **in alto al centro**, sotto il lockup: è la luce che tiene su la catena, e sostituisce la luce in alto a sinistra dei giorni scorsi |
| Oro | `#C8A24B` | È **sempre il colore dell'azione**: anelli accesi, filo percorso, numero `+11%`, CTA, evidenziatore. Un anello oro = un passaggio incassato |
| Anello spento | `rgba(255,255,255,0.30)` su `#2E2A25` | Il non-ancora. Deve leggersi come vuoto, non come grigio sporco |
| Sabbia | `#F5F0E6` | **Solo le prove**: la card recensione e la fascia offerta. Mai altro |
| Oro su sabbia | `#86692A` | `#C8A24B` su chiaro dà 2,25:1 e non è leggibile. Nome dell'ospite e «15%» usano l'oro scuro |
| Inchiostro su sabbia | `#26241F` / `#6f695c` | Testo della recensione e riga «traduzione di Airbnb» |

**Niente blu navy, niente teal, niente virata fredda.** Nessuna fotografia in tutto il pacchetto: la card
della recensione deve essere l'unico punto chiaro del fotogramma, e una foto le ruberebbe l'occhio.

## Formati per canale

| Canale | Dimensioni | Ritmo della catena |
|---|---|---|
| Carosello (C1-C5) | 5 × 1080×1350 (4:5) | **Tutti e quattro gli anelli sempre presenti, cambia quello pieno.** C1 → 1° acceso, C2 → 2°, C3 → 3°, C4 → 4°. C5 catena completa, senza etichette |
| Facebook F1 | 1080×1920 (9:16) — obbligatorio, un 4:5 verrebbe tagliato nel collage | Catena grande Ø 64, **solo il primo anello acceso**: la recensione c'è già, la catena si ferma lì. È esattamente il dolore del gancio |
| Facebook F2 | 1080×1080 (1:1) | **Catena ruotata in verticale**: filo oro a sinistra, quattro anelli, numeri `01→04` in oro |
| Facebook F3 | 1080×1080 (1:1) | Catena piccola Ø 22 completa, senza etichette: è la firma di chiusura |
| Storie S1-S2 | 2 × 1080×1920 | **Filo oro centrato sotto il lockup + etichetta** (`PREZZO`, `LE SEI VOCI`). Il medaglione numerato è stato tolto dopo compliance: il pacchetto contava la stessa catena in tre modi diversi, e il numero nelle storie era quello che non significava niente |
| Reel | cover + 12 scene 1080×1920 | Gli anelli **si accendono uno per scena** (scene 3-8). Fuori dalla catena (1-2, 9-12) la catena non c'è: entra e esce |

Griglia unica: margine 64 px · colonna utile 952 px · safe area 180 alto / 320 basso sui 9:16 ·
passo 20 px · scala 70·62·50·45·40·33·31·17. Nessun corpo fuori scala.

## Elementi chiave — gerarchia di lettura

1. **La card recensione in sabbia con bordo sinistro oro da 6 px** (C4 Attila, F2 Fanny, S1 Stefania). È l'unica superficie
   luminosa su un fondo interamente fumè e ha un'ombra portata `0 18px 48px rgba(20,17,13,.34)`: su un
   feed scuro deve leggersi come **un foglio di carta appoggiato**. È lì che l'occhio cade per primo.
   Dove c'è la card **non c'è nessun'altra superficie chiara**: card e fascia offerta non convivono mai.
2. **La catena** — secondo elemento letto, e l'unico costante. Dà l'orientamento prima del testo.
3. **La colonna di testo**, allineata a sinistra sotto il lockup centrato (centrata nel reel e su F1).
4. **La CTA** — pillola oro piena a tutta colonna, sempre l'ultimo elemento: C5 y 1080, F3 y 808,
   S1/S2 y 1460, reel scena 11 y 1400.
5. **Un solo accento di rottura per pacchetto**: l'evidenziatore oro sotto `non lo devi abbassare`
   (scena 7 del reel). Unico, altrimenti non pesa più.

### Le regole sulle recensioni, applicate

A schermo compaiono **solo**: `★★★★★` in oro, il testo verbatim, il nome di battesimo, il mese e — **solo
dove il testo è davvero tradotto** — la riga `traduzione di Airbnb` in `#6f695c` corpo 17. La porta Attila
(C4); **non** la portano Stefania (italiana) e Fanny (non marcata come tradotta nell'archivio): metterla
dove non serve sarebbe un'attribuzione falsa. **Assenti per costruzione**: nome della
casa, indirizzo, foto dell'immobile, avatar, logo o interfaccia Airbnb, finti screenshot, **e qualsiasi
punteggio aggregato** (né media, né numero di recensioni, né voci per categoria). Le stelle stanno
**fuori** dalla card, sopra, in oro su fumè: dentro sarebbero una riproduzione di schermata.
La card è chiaramente grafica Hadrianus.

## Da evitare (e perché non c'è)

| Vietato | Motivo |
|---|---|
| Barra di avanzamento a 4 tacche (17/09, reel inverno/inquilino) | Bruciata. **L'avanzamento è il filo della catena**: tolta anche dal reel, dove il copy la prevedeva |
| Lo «scalino» agosto/novembre (17/09) | Bruciato. Nessun pannello rientrato, nessuna stecca oro verticale accanto a una riga |
| Cinque voci in colonna (16/09) | Le sei voci di S2 non sono un elenco con leader tratteggiati: **ogni voce è un micro-anello** (Ø 22), cinque pieni e «Posizione» vuoto — unico anello spento del pacchetto |
| Prima/dopo affiancato (14/09) | Nessun confronto a due colonne in tutto il pacchetto |
| «Marchio in alto a sinistra + blocco di testo a metà altezza» | **Il lockup è centrato.** Marchio centrato a y 80/112, catena centrata subito sotto. Il primo elemento letto non è più il marchio a sinistra |
| Fotografie sotto il testo | Ruberebbero l'occhio alla card recensione. Zero foto, zero veli |
| Loghi Airbnb/Booking come elemento grafico | Citati a parole nel testo del post, mai disegnati |
| Punteggio aggregato, badge come protagonista | Scelta chiusa del titolare, non un dato mancante |
| `#C8A24B` come testo su sabbia | 2,25:1. Sul chiaro l'oro è solo superficie; le parole in oro usano `#86692A` |

## Reel — tabella scena per scena, pronta per Canva

Pagine **1080×1920**, una per scena, fondo `#3F3A33` (gradiente `radial-gradient(120% 80% at 50% 12%, #4a443a, #3F3A33 52%, #2E2A25)`).
Marchio `HADRIANUS` (Archivo 800, 33, tracking 9, `#FFF`) a y 112 e `MULTISERVICE` (Manrope 600, 17,
tracking 7, `rgba(255,255,255,.72)`) a y 156, **centrati, fissi su tutte le pagine**.

Catena (scene 3-8): anelli **Ø 64** a y 430, centri x **96 · 405 · 675 · 984**, filo spesso 4 px a y 460.
Anello acceso `#C8A24B` pieno; spento `#2E2A25` con bordo 3 px `rgba(255,255,255,.30)`.
Filo percorso `#C8A24B`, filo residuo `rgba(255,255,255,.18)`.
Etichette Manrope 600 corpo 17 tracking .16em maiuscolo a y 512. **Il reel ha etichette proprie**
— `RECENSIONE · VISIBILITÀ · FIDUCIA · PREZZO` — perché racconta in ordine 1→3→2 mentre il carosello
segue l'ordine della catena economica: con le etichette del carosello l'anello acceso non corrispondeva
alla frase a schermo. `RECENSIONE` è ancorata a x 64, `VISIBILITÀ` e `FIDUCIA` centrate sul loro anello,
`PREZZO` ancorata a destra, x 1016.
Accese `#C8A24B`, spente `rgba(255,255,255,.55)`.

| # | t (s) | Testo esatto a schermo | Posizione e stile | Anelli accesi | Animazione da mettere in Canva |
|---|---|---|---|---|---|
| 1 | 0,0-2,0 | `Le recensioni` / `non sono un complimento.` | y 820 Archivo 900 70 `#FFF` centrato · y 930 Archivo 800 62 `rgba(255,255,255,.88)` centrato | — | riga 1 maschera dal basso 200 ms; riga 2 a +280 ms |
| 2 | 2,0-3,4 | `Sono un prezzo.` | y 880 Archivo 900 70 `#FFF` centrato · filo oro 180×3 px a y 1010, x 450 | — | scatto di scala 1,10→1 in 180 ms; il filo si disegna da sinistra in 260 ms |
| 3 | 3,4-5,2 | `FUNZIONA COSÌ` | y 300 Manrope 600 31 tracking .18em `#C8A24B` centrato | **1** — `RECENSIONE` (la premessa) | kicker in dissolvenza 200 ms; la catena entra e si accende il primo anello |
| 4 | 5,2-7,2 | `Il punteggio conta` / `in come esci nelle ricerche.` | y 820 / y 930, come scena 1 | **2** — `VISIBILITÀ` | anello 1 con scatto 220 ms; testo a accumulo 110 ms per parola |
| 5 | 7,2-9,2 | `E la tua casa` / `la trova chi scorre un portale.` | idem | **2** — `VISIBILITÀ` (resta) | filo oro si allunga da sinistra 260 ms, poi si accende l'anello 2 |
| 6 | 9,2-11,4 | `Chi ti trova` / `ha già un motivo per fidarsi.` | idem | **3** — + `FIDUCIA` | due tempi: riga 2 a +400 ms dalla riga 1 |
| 7 | 11,4-13,6 | `Quindi il prezzo` / `non lo devi abbassare.` | y 820 Archivo 900 70 `#FFF` centrato · y 930 Archivo 900 62 **su banda `#C8A24B`, testo `#2E2A25`**, centrato | **4** — + `PREZZO` | anello 4 scatto 1,08→1; **evidenziatore oro che corre da sinistra 260 ms**. Unico del reel |
| 8 | 13,6-14,2 | — | solo catena + kicker | **4** | immobilità totale 0,6 s. È il fotogramma da fermo-immagine |
| 9 | 14,2-16,2 | `Un punteggio alto` / `non è fortuna.` | y 820 / y 930 | catena assente | i quattro anelli escono verso l'alto in maschera 300 ms; il testo entra dal basso |
| 10 | 16,2-18,4 | `È pulizia, risposte,` / `check-in. Tutti i giorni.` | y 820 / y 930 | — | il testo sostituisce se stesso a rullo, 200 ms |
| 11 | 18,4-21,0 | `Guadagniamo solo` / `se guadagni tu.` poi `SCRIVI «PUNTEGGIO» IN DM` | testo y 820/930 · CTA pillola y 1400, h 90, `#C8A24B`, Archivo 800 40 `#2E2A25`, da x 64 a x 1016, raggio 999 | — | la frase resta 1,2 s, poi la CTA sale dal basso 260 ms e resta ferma |
| 12 | 21,0-21,6 | `Le recensioni` / `non sono un complimento.` | come scena 1 | — | la CTA si ritira in basso 200 ms, torna il fondo della scena 1. **Loop di stato, nessun fade to black** |

Durata **21,6 s** (21,0 s di racconto + 0,6 s di chiusura del loop).
**Nessun numero a schermo in tutto il reel.** **Nessun anello 5.** **Nessun Superhost.**

**Vincoli Canva rispettati:** il connettore non imposta la famiglia di font e non fa animazioni, quindi
niente nel reel dipende da un carattere specifico o da un movimento per essere capito. Se Archivo e
Manrope non arrivano, il senso resta: gli anelli, il filo e la banda oro sono forme, non tipografia.
Le animazioni della colonna di destra sono **indicazioni per il titolare**, non requisiti di lettura.

## Deviazioni dal copy — dichiarate

| Dove | Cosa | Perché |
|---|---|---|
| Reel | **Tolta la barra di avanzamento a 4 segmenti** prevista dal layout del copy | Veto esplicito del titolare sulla barra a tacche. La catena fa già quel lavoro, meglio e senza ripetere il 17/09 |
| C4, card Attila | Citazione tagliata alla forma **già approvata nel testo Facebook**: `« … L'appartamento era in ordine sotto ogni aspetto, splendidamente pulito, ordinato e confortevole… »` | La versione da 158 battute andava su 4 righe e la card sforava di ~50 px addosso alla riga di lettura. **Accorciata la citazione, non ridotto il corpo** (resta Manrope 500 a 38). Nessuna parola riscritta |
| S1, card Paweł | Citazione tagliata: `«… L'appartamento era pulito, confortevole e preparato per il nostro arrivo… Consiglio vivamente questo posto!»` | È il punto critico dichiarato: 198 battute sul 9:16 portavano la card a 5 righe, 414 px, sotto la CTA. Il taglio tiene **l'apertura tematica (pulizia, arrivo preparato) e la raccomandazione finale**, cioè esattamente ciò che il copy chiede di far vedere. Corpo invariato a 38 |
| S1 | Il blocco «soluzione» resta su 3 righe ma il gancio va su 2 righe a corpo 62 invece di 1 riga a 70 | `Non abbassare il prezzo. Ancora.` a 70 px non entra nei 952 px di colonna. Si accorcia lo spazio, non il testo |
| C1, C2 | Aggiunta la pillola outline **«Scorri →»** | Senza, restava un vuoto di 380 px in coda (controllo 3) e una freccia orfana in basso a destra |
| F1 | Catena grande con **il primo anello acceso** invece che tutti spenti | Con quattro anelli spenti la catena spariva nel fondo e il terzo superiore era morto. Un anello acceso dice meglio il gancio: la recensione c'è, il resto non è ancora successo |
| F3 | Gancio spezzato su 2 righe | `Quel punteggio lo fa qualcuno.` a corpo 62 su una riga sola sfora la colonna e si sovrapponeva al corpo |

## Correzioni applicate dopo `checklist-compliance.md` (18/09)

| # | Bloccante | Cosa è cambiato |
|---|---|---|
| 1 | Riuso delle recensioni | **CHIUSO 18/09** — scelta rimessa a noi dal titolare. **S1: Paweł → Stefania** (mai pubblicata, italiana, senza riga di traduzione, minuscolo iniziale verbatim) · **F2: Katarzyna → Fanny** (mai pubblicata, integrale, senza taglio e senza traduzione) · **C4: Attila invariato**, è la citazione più forte dell'archivio · testo Facebook: Aline e Martin → **Anne Loes**. Pubblicazioni annotate in `facebook-recensioni-superhost/recensioni-reali.md` |
| 2 | Katarzyna tagliata senza `…` | **Superato dal punto 1**: Katarzyna esce dal pacchetto. Al suo posto Fanny, citata **integrale** — nessun taglio, quindi nessun puntino da segnalare |
| 3 | Caveat Cornell illeggibili | C3: corpo **17 → 26**, opacità **.62 → .80**, blocco risalito a y 866. Slide non ricomposta |
| 4 | Due conteggi delle sei voci | Post Facebook allineato al **cinque** (quello a schermo e quello disegnato in S2) |
| 5 | Parafrasi Booking | Il dettaglio sulla recency è fuori; resta la formulazione congiunta Booking+Airbnb. Il resto del paragrafo intatto |
| 6 | Off-by-one del reel | Etichette proprie del reel: `RECENSIONE · VISIBILITÀ · FIDUCIA · PREZZO`. R04 accende `VISIBILITÀ`, R06 `FIDUCIA`, R07 `PREZZO` — e l'evidenziatore oro cade sull'ultimo anello. Aggiornati anche `reel/scene.json` e `reel/canva.html` |
| 7 | Tre numerazioni in contraddizione | Numero tolto dai kicker: C2 `VISIBILITÀ`, C3 `PREZZO`, C4 `CHI PRENOTA`. Storie senza medaglione: S1 `PREZZO`, S2 `LE SEI VOCI`. **F2 invariato** |

**Conseguenza obbligata del cambio di recensioni.** La riga «Guarda di cosa parlano: pulizia, arrivo
preparato, risposte. **Non parlano del mare.**» non è più vera su questo gruppo — Stefania scrive
«vicinissima al mare», Attila la spiaggia e il parcheggio, Anne Loes il treno e i ristoranti. Riscritta
in C4 e nel paragrafo corrispondente del post nella forma difendibile: **la posizione è già lì e non la
puoi migliorare; quello che raccontano è la pulizia e le risposte.** E **nessun conteggio per tema**:
sul gruppo citato nessun singolo tema copre tutte e quattro le recensioni (Fanny non nomina la pulizia,
Anne Loes non nomina l'host), quindi «quattro su quattro parlano di X» sarebbe falso e non si scrive.
Il conteggio sopravvive solo dove è vero: «quattro recensioni, quattro modi di dire la stessa cosa».

Non bloccanti chiusi nello stesso giro: `copy.md` riallineato ai PNG (citazioni di Paweł e Attila,
gancio di S2, tabella slot, tabelle di layout) · `Attila · 3 settimane fa` → **`agosto 2026`**, data
assoluta come le altre card *(mese da confermare sullo screenshot)* · vuoto di ~160 px a metà C2 chiuso
alzando la fascia sabbia a y 700 e la pillola «Scorri» a y 970.

## Controllo qualità — eseguito sui PNG, a dimensione telefono

| # | Controllo | Esito |
|---|---|---|
| 1 | Centratura | OK — lockup e blocchi centrati in asse; colonna a sinistra sempre a x 64 |
| 2 | Troncature | OK — nessun elemento fuori frame, nessuna card tagliata. Verificato a macchina su tutte e 23 le artboard |
| 3 | Vuoti | OK su carosello, Facebook e storie. **Sui fotogrammi del reel i vuoti sono voluti**: sono pagine di un video in cui il testo entra ed esce, non post statici |
| 4 | Contrasto | OK — testo bianco su fumè; sabbia su fumè per le prove; oro solo come superficie sul chiaro |
| 5 | Safe area | OK — niente di leggibile sopra y 180 (oltre al lockup di marca, che sta a 112-205 per contratto su tutti i 9:16 del progetto) né sotto y 1600 |
| 6 | Marchi di terzi | OK — nessuna fotografia, nessun logo, nessuna interfaccia. Airbnb è citato solo come **parola** nella riga «traduzione di Airbnb» |

Strumento di controllo misurato: `grafiche/verifica.py` (fuori frame, sovrapposizioni, safe area, vuoti).
Esito corrente: **10 artboard statiche su 10 pulite** (rieseguito dopo le correzioni di compliance).

**Verifica specifica sul caveat Cornell (bloccante 3):** il PNG di C3 è stato ridotto a **390 px di
larghezza reale** — la larghezza di un telefono — e guardato lì. A 26 px le due righe
«Cornell Center for Hospitality Research — Anderson, 2012. / Studio sul settore alberghiero, non su
case vacanza.» **si leggono**, con lo stesso sforzo della riga di spiegazione sopra. Il `+11%` non
resta più solo sullo schermo. Verificato guardando, non solo impostando.

## Grafiche editabili

- **Sorgenti modificabili**: `campagne/giornaliero/2026-09-18/grafiche/*.dc.html` — 23 artboard su un'unica
  canvas Claude Design (`grafiche/canvas.json`), tutte editabili elemento per elemento.
  `grafiche/base.py` è la libreria della giornata, `grafiche/build.py` la ricostruisce da zero.
- **Export**: `campagne/giornaliero/2026-09-18/png/*.png` (23 PNG alle dimensioni esatte di canale).
- **Reel**: `reel/scene.json` è la fonte unica dei tempi; `reel/canva.html` è il file da importare in
  Canva (11 pagine 1080×1920, una per scena, testi e forme separati e modificabili);
  `reel/reel.html` è il montaggio di riferimento per rivedere tempi e animazioni prima di portarle in Canva.
- **Da rigenerare tutto**: `python3 grafiche/build.py && python3 grafiche/verifica.py && python3 .claude/skills/giornata/render.py campagne/giornaliero/2026-09-18`
