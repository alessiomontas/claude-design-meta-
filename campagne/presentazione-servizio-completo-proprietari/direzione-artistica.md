# Direzione artistica — Deck "servizio completo" (bilocale Ostia Lido Centro)

Presentazione commerciale 1-a-1, non contenuto social. Si guarda su schermo (laptop/tablet in salotto) e si invia dopo la riunione. Sedici artboard 16:9.

## Decisioni di partenza

| Decisione | Valore | Perché |
|---|---|---|
| Formato artboard | **1280 × 720 px** | È esattamente la misura PowerPoint 16:9 (13,333 × 7,5 pollici a 96 px/pollice): l'export PDF esce a pagina piena senza riscalature, e i PNG si rendono a 2× (2560 × 1440) per lo schermo |
| Fondo | **crema caldo `#FAF6EC`** su 13 slide, **fumè `#3F3A33`** su 3 | Richiesta esplicita del titolare (fondo bianco/crema). Il fumè resta come punteggiatura: solo dove serve stacco |
| Motore | canvas Claude Design (`.dc.html`) | Regola fissa: ogni grafica editabile, mai immagini piatte |
| Logo | **busto di Adriano ritagliato su fondo trasparente** | Prima volta: la variante trasparente non esisteva (vedi `brand-assets/logo/trasparenti/`) |

## Palette (derivata dal design system, versione chiara)

| Ruolo | Hex | Uso nel deck |
|---|---|---|
| Fondo crema | `#FAF6EC` | 13 slide su 16 |
| Carta (card) | `#FFFDF8` | box di chiusura della slide-snodo |
| Filigrana numerica | `#F0E7D3` | i numeri di sezione giganti in basso a sinistra |
| Fumè | `#3F3A33` → `#2E2A25` | slide 04 (calendario), 14 (condizioni), 16 (chiusura) |
| Oro | `#C8A24B` | trattini di elenco, numeri di sezione, banda CTA, etichette di frequenza |
| Oro su chiaro | `#b3892f` | testo oro su fondo crema (leggibilità) |
| Inchiostro | `#26241F` · `#46423a` · `#6f695c` | titolo · corpo · secondaria |
| Pietra | `#9A8A63` | occhielli maiuscoli |
| Su fondo scuro | `#E8E1D2` · `#b7ad9a` | corpo · secondaria |

Nessun blu navy, nessun gradiente decorativo, nessuna emoji, nessun angolo arrotondato: il deck è squadrato.

## Griglia

| Parametro | Valore |
|---|---|
| Margine laterale | 88 px (colonna utile 1104 px) |
| Occhiello di sezione | y 58, in alto a sinistra — trattino oro 30 × 2 px + etichetta maiuscola 12,5 px |
| Marchio `HADRIANUS` | y 56, in alto a destra, 12,5 px, opacità ridotta |
| Piede | y 44 dal basso — trattino oro a sinistra, numerazione `05 / 16` a destra |
| Colonna sinistra (slide di sezione) | x 88, larghezza 400 px |
| Filo verticale di separazione | x 552, da y 148 a y 588 |
| Colonna destra (elenchi) | x 600, larghezza 592 px, blocco centrato verticalmente |
| Slide 04 (calendario) | fascia a tutta larghezza: etichetta di frequenza 196 px + due colonne di voci da 17 px |

## Scala tipografica (Archivo + Manrope, come da design system)

`60` copertina · `52` slide-snodo · `44` prossimo passo · `40` titolo di sezione · `34` titolo su fondo scuro · `19` voce forte · `17,5` promessa / voce di elenco · `15,5` riga secondaria · `12,5` occhielli e piede.

## Firma visiva del deck — "colonna e filo"

Pattern **nuovo**, non presente in `design-system.md` (nessuna campagna precedente è un deck):

1. **Colonna sinistra fissa** con titolo e promessa, **filo verticale sottile** di separazione, **elenco a destra**: la stessa impaginazione su tutte le slide di servizio, così il contenuto cambia e l'occhio no.
2. **Numero di sezione gigante in filigrana** (`01`…`07`) in basso a sinistra, colore crema più scuro: dà profondità senza aggiungere inchiostro.
3. **Trattino oro da 14 × 2 px** al posto del punto elenco: è il dettaglio che si ripete su tutte e sedici le slide.
4. **Tre slide scure come punteggiatura** (il calendario, le condizioni, la chiusura): il deck respira e le due slide che devono restare in testa staccano dal resto.
5. **Niente card, niente ombre, niente icone**: solo fili, filetti e tipografia. Le uniche immagini sono il logo in marmo, due foto reali di un immobile in gestione e il tramonto del Litorale in chiusura.
6. **Banda oro** (fondo `rgba(200,162,75,0.17)` + filo oro a sinistra) per le due righe che devono essere lette e non scorse: "perché conta" sugli accessi, "prenotazioni dirette" sui canali, lo stacco della slide 02 e la CTA finale a tutta larghezza. Dove la riga è una precisazione e non un argomento di vendita resta il filetto grigio con l'etichetta NOTA.

## Uso delle immagini

| Slide | Immagine | Nota |
|---|---|---|
| 01 Copertina | logo marmo trasparente **senza plinto** (`hadrianus-tempio-900.webp`), 516 px, dentro la cornice oro | il plinto inciso "HADRIANUS" duplicava il marchio tipografico in basso a sinistra e sconfinava sulla cornice |
| 02 L'immobile | **nessuna foto** | mostrare un altro immobile proprio sulla slide dedicata al suo creerebbe confusione |
| 07 La casa pronta · 09 Identità | foto reale **400 × 300 px** nella colonna sinistra, didascalia in sovrimpressione su velo scuro | è l'unica prova visiva dello standard: a 400 × 208 pesava troppo poco. La didascalia deve dire che **non è l'immobile della proprietaria** |
| 16 Chiusura | tramonto del Litorale a pieno formato con velo fumè | chiude sul territorio, non su un interno |

Regola di compliance applicata: le foto illustrano lo **standard**, mai la struttura (nessun indirizzo, nessun nome, nessun case study). Esclusa `smart-tv-streaming-mockup.jpg` (marchi di terzi).

## Ritaglio del logo (novità di questa campagna)

Le quattro varianti in `brand-assets/logo/` avevano tutte lo sfondo. La versione trasparente è stata prodotta **in locale** (Chromium headless: riempimento dai bordi con tolleranza locale + tenuta della sola componente connessa più grande + rifinitura del bordo), non con il connettore Adobe. Risultato in `brand-assets/logo/trasparenti/logo-marmo-frontale-trasparente.png` (641 × 708). Nel deck si usa la variante **senza plinto** e sfumata in basso (`slide/hadrianus-tempio-900.webp`).

## Come si rigenera

```bash
node emit.mjs      # scrive le 16 slide .dc.html da build-slides.mjs (componenti) + testi
node render.mjs    # PNG 2560×1440 in png/ (font Archivo/Manrope iniettati in locale)
```

`build-slides.mjs` contiene la griglia e i componenti, `emit.mjs` i testi. Una modifica di testo si fa in `emit.mjs` e si rigenera — così il canvas editabile e i PNG non divergono mai.

> **Attenzione:** se la presentazione viene modificata a mano dentro il canvas pubblicato, rigenerare da qui **sovrascrive** quelle modifiche. Prima di rilanciare `emit.mjs` su un canvas già ritoccato dall'utente, rileggere l'Artifact.
