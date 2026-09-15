# Checklist compliance — Presentazione servizio completo (bilocale Ostia Lido Centro)

Oggetto del controllo: **il testo montato nelle 16 artboard** `slide/*.dc.html` (fa fede quello, non `copy.md`).
Metro: `brief-mercato.md` (§"Vietato nel deck", §"Come si nomina un adempimento senza insegnarlo", §"Toni da evitare", ricerca normativa con stati CONFERMATO / DA VERIFICARE) · `copy.md` tabella CLAIM · `CLAUDE.md` · `.claude/reference/lessico-brand.md`.

## Esito

**DA CORREGGERE** — 3 rilievi bloccanti su 16 slide. Il resto del deck è pulito.

---

## Tabella per slide

| # | File | Esito | Rilievi |
|---|---|---|---|
| 01 | `Main.dc.html` | DA CORREGGERE (formale) | R-08 numerazione assente · R-10 "in Lido Centro" |
| 02 | `Immobile.dc.html` | OK | — (R-13 divergenza minima con `copy.md`) |
| 03 | `Percorso.dc.html` | OK | R-11 paragrafo aggiunto non presente in `copy.md` |
| 04 | `Calendario.dc.html` | DA VERIFICARE | R-04 "entro il 16 del mese successivo" · R-06 "entro 24 ore" (formulazione parziale) |
| 05 | `Regola.dc.html` | DA VERIFICARE | R-05 "prima la Regione, poi il Ministero" · R-07 SUAR / SCIA o CIA · R-06 "entro 24 ore" |
| 06 | `Responsabilita.dc.html` | OK | — |
| 07 | `Casa.dc.html` | OK | R-09 numero di sezione grande assente (coerenza visiva) |
| 08 | `Accessi.dc.html` | OK sul merito | R-03 "Apertura del portone gestita dal citofono" — ambigua, da irrobustire |
| 09 | `Identita.dc.html` | **DA CORREGGERE — BLOCCANTE** | **B-1** didascalia non dice che non è il suo immobile · R-09 |
| 10 | `Canali.dc.html` | OK | R-12 "Scheda Google" (marchio di terzi nominato a testo) |
| 11 | `Gestione.dc.html` | OK | — |
| 12 | `Strategia.dc.html` | OK | — |
| 13 | `Proprieta.dc.html` | **DA CORREGGERE — BLOCCANTE** | **B-2** claim 22 DA VERIFICARE montato come fatto · R-11 promessa aggiunta non presente in `copy.md` |
| 14 | `Condizioni.dc.html` | **DA CORREGGERE — BLOCCANTE** | **B-3** "restano **solo** i dispositivi di accesso" · R-14 titolo divergente da `copy.md` |
| 15 | `Passo.dc.html` | OK | R-13 CTA senza punto finale (divergenza minima) |
| 16 | `Chiusura.dc.html` | DA CORREGGERE (formale) | R-08 numerazione assente · R-10 "a Lido Centro" · R-15 "farlo rendere" |

---

## Bloccanti (da correggere prima della consegna)

### B-1 · Slide 09 `Identita.dc.html` — la didascalia non dichiara che l'immobile fotografato non è quello della proprietaria

**Dove:** `slide/Identita.dc.html`, riga 29.
**Riga esatta oggi montata:**

```
Foto di un immobile in gestione. Stessa luce, stessa preparazione.
```

**Perché blocca:** la slide 07 dice esplicitamente *"Non è il suo"*; la 09 no. Mostrata a una proprietaria che sta valutando la firma, la formula "un immobile in gestione" accanto alla promessa "la sua casa entra come una struttura con un nome" può essere letta come resa fotografica **del suo** appartamento. È anche la regola fissa di `copy.md` §Note per l'art director ("la didascalia che dice 'non è il suo' è parte del copy, non opzionale").

**Riscrittura proposta (stringa pronta):**

```
Un altro immobile che gestiamo, non il suo. Stessa luce, stessa preparazione.
```

---

### B-2 · Slide 13 `Proprieta.dc.html` — claim marcato DA VERIFICARE montato come fatto

**Dove:** `slide/Proprieta.dc.html`, riga 46.
**Riga esatta oggi montata:**

```
Soggiorni e incassi, visibili quando li chiede.
```

**Perché blocca:** è il **claim 22** della tabella di `copy.md`, stato **DA VERIFICARE** — *"impegno di servizio non documentato in nessun materiale Hadrianus. Se non c'è un canale di consultazione, la voce va sostituita prima della riunione"*. È anche la domanda bloccante n. 3 di `copy.md`. Regola non negoziabile `CLAUDE.md`: un claim non verificato non esce mai. Aggravante: è un **impegno contrattuale di servizio** detto a chi sta per firmare, ed è la riga che la figlia verificherà per prima dopo la firma.

**Riscrittura proposta — opzione A** (se il titolare conferma che esiste un riepilogo allegato al pagamento mensile):

```
Il riepilogo dei soggiorni e degli incassi, insieme al pagamento del 10.
```

**Riscrittura proposta — opzione B** (se non esiste nulla di formalizzato — sostituzione con voce coperta da materiale Hadrianus esistente):

```
La casa resta sua: nessun inquilino fisso, nessun contratto lungo.
```

Non montare la riga attuale in nessuna delle due ipotesi.

---

### B-3 · Slide 14 `Condizioni.dc.html` — l'esclusiva "solo" sui costi fuori dal 15% non è verificata

**Dove:** `slide/Condizioni.dc.html`, riga 50.
**Riga esatta oggi montata:**

```
Fuori dal 15% restano solo i dispositivi di accesso — spioncino digitale e apertura del portone — fatturati a parte.
```

**Perché blocca:** il claim 20 di `copy.md` è marcato CONFERMATO **condizionatamente**: *"regge solo se costi vivi delle pratiche e dotazioni di sicurezza sono dentro il 15% → vedi domanda 2"*. La domanda 2 del brief (diritti di segreteria SUAR, bolli, eventuale tecnico abilitato, estintore e rilevatori) è **tuttora aperta**, ed è ripetuta come bloccante in fondo a `copy.md`. La parola **"solo"** trasforma un elenco in una garanzia economica esclusiva: se in fase di avvio spunta un costo vivo, il deck firmato dice il contrario. In una slide che finisce con «Guadagniamo solo se guadagni tu» è il punto più costoso possibile in cui essere smentiti.

**Riscrittura proposta — minima e sempre vera (stringa pronta):**

```
Fuori dal 15% restano i dispositivi di accesso — spioncino digitale e apertura del portone — fatturati a parte. Gli eventuali costi vivi delle pratiche glieli indichiamo prima di sostenerli.
```

**Alternativa:** la riga attuale (con "solo") può restare **solo se** il titolare conferma per iscritto che diritti di segreteria, bolli, eventuale tecnico abilitato e dotazioni di sicurezza sono dentro il 15%. In quel caso la conferma va registrata nella tabella CLAIM di `copy.md`.

---

## Osservazioni (non bloccanti, ma da considerare)

### R-03 · Slide 08 `Accessi.dc.html`, riga 46 — ambiguità sull'apertura del portone

Riga montata: `Apertura del portone gestita dal citofono.`
Il vincolo del brief §6 è rispettato dal resto della slide — la promessa dice *"Entra solo dopo essere stato identificato"* e la Nota dice *"Questi strumenti intervengono dopo il riconoscimento, non lo sostituiscono. Il check-in resta presidiato."* La slide **non** presenta l'ingresso senza identificazione: requisito soddisfatto. Resta che "gestita dal citofono" non dice **da chi**, e letta isolata (o ritagliata in PDF) suona come apertura automatica. Riscrittura proposta:

```
Apertura del portone comandata da remoto, dopo il riconoscimento.
```

### R-04 · Slide 04 `Calendario.dc.html`, riga 64 — "entro il 16 del mese successivo"

Il brief §8 marca la periodicità **CONFERMATO**, ma la conferma poggia sul **titolo** di una pagina di Roma Capitale non apribile in sessione, e una fonte indicava il 15. Inoltre la stessa data compare nel brief §"Come si nomina un adempimento senza insegnarlo" dentro l'esempio ✘ (*"Su GECOS si genera il PagoPA e si versa entro il 16"*), mentre la formula ✔ prescritta è senza data. Dicibile così com'è, ma da far confermare al titolare prima della riunione. In alternativa, stringa a rischio zero:

```
Versamento entro la scadenza trimestrale.
```

### R-05 · Slide 05 `Regola.dc.html`, riga 40 — sequenza delle operazioni

Riga montata: `È il presupposto del CIN: prima la Regione, poi il Ministero.`
La relazione CIR → CIN è CONFERMATA (claim 7), ma *"prima la Regione, poi il Ministero"* è l'unico punto del deck che indica **l'ordine delle operazioni**, esplicitamente nella lista dei divieti del brief. Riscrittura proposta, stesso effetto di competenza senza istruzione:

```
È il presupposto del CIN: senza CIR, il codice nazionale non arriva.
```

### R-06 · Slide 04 riga 34 e slide 05 riga 54 — "entro 24 ore"

`Comunicazione alla Polizia di Stato entro 24 ore.` / `ogni ospite va comunicato entro 24 ore.`
Il dato è **CONFERMATO** nel brief §5 (art. 109 TULPS, più fonti fra cui legali) e il termine è correttamente citato senza pena, senza articolo e senza procedura: ammissibile. Nota di accuratezza, non di compliance: il brief riporta anche la riduzione a **6 ore** per i soggiorni sotto le 24 ore. La formulazione attuale è una semplificazione, non un errore; se la figlia la conosce, la si concede a voce senza toccare la slide.

### R-07 · Slide 05 `Regola.dc.html`, riga 47 — SUAR e SCIA/CIA

Riga montata: `Al SUAR di Roma Capitale, SCIA o CIA secondo la tipologia scelta.`
Formulazione **conforme** alla prescrizione del brief (non si scrive "le facciamo la SCIA"). Va però segnalato che nel brief §4 sia la competenza del SUAR sia la distinzione SCIA/CIA risultano **DA VERIFICARE su fonte istituzionale**: la pagina di Roma Capitale non è stata apribile. La riga resta dicibile perché è volutamente neutra sull'esito, ma la tipologia va chiusa col titolare **prima** della riunione: è la domanda tecnica più probabile in sala (nota finale del brief §Domande aperte).

### R-08 · Slide 01 e 16 — numerazione del deck incompleta

La numerazione corre da `02 / 16` (`Immobile`) a `15 / 16` (`Passo`). **Mancano `01 / 16` su `Main.dc.html` e `16 / 16` su `Chiusura.dc.html`.** Se la scelta è volontaria (copertina e chiusura senza numero) va scritta nel `README.md` della campagna; altrimenti, stringhe pronte da inserire prima del `</div>` che chiude `.frame`:

`Main.dc.html`:
```html
  <span style="position: absolute; right: 92px; bottom: 44px; font-family: 'Archivo', 'Arial Black', Arial, sans-serif; font-weight: 600; font-size: 11.5px; letter-spacing: 2.4px; color: rgba(38,36,31,0.34);">01 / 16</span>
```

`Chiusura.dc.html`:
```html
  <span style="position: absolute; right: 88px; bottom: 44px; font-family: 'Archivo', 'Arial Black', Arial, sans-serif; font-weight: 600; font-size: 11.5px; letter-spacing: 2.4px; color: rgba(255,255,255,0.45);">16 / 16</span>
```

La numerazione di sezione `01 di 07` … `07 di 07` è invece **coerente e completa**: 01 Regola · 02 Casa · 03 Accessi · 04 Identita · 05 Canali · 06 Gestione · 07 Strategia.

### R-09 · Slide 07 e 09 — numero di sezione grande assente

Le slide di sezione montano un numero "fantasma" in `#F0E7D3` (Regola `01`, Accessi `03`, Canali `05`, Gestione `06`, Strategia `07`). Su `Casa` (`02`) e `Identita` (`04`) non c'è, perché lo spazio è occupato dalla foto. Scelta comprensibile, ma il ritmo visivo del blocco "Il servizio" si interrompe due volte su sette. Se recuperabile, spostare il numero nell'angolo alto destro su quelle due slide; altrimenti lasciare così e non toccare le altre cinque.

### R-10 · Slide 01 riga 26 vs slide 16 riga 23 — preposizione incoerente

Copertina: `Il suo bilocale in Lido Centro oggi è fermo.` · Chiusura: `Il suo bilocale a Lido Centro, e il lavoro…`
Uniformare su **"a Lido Centro"** (più corretto e più naturale). Stringa pronta per la copertina:

```
Il suo bilocale a Lido Centro oggi è fermo. Qui c’è il lavoro che serve per farlo esistere per legge, come prodotto e sul mercato.
```

### R-11 · Divergenze copy.md → artboard: due testi montati che in `copy.md` non esistono

Non sono violazioni, ma **non sono passati dalla tabella CLAIM** e vanno riportati in `copy.md` per tracciabilità:

- `Percorso.dc.html` riga 24: `Un bilocale che si presta non è ancora una struttura che produce. In mezzo ci sono tre passaggi, e vanno fatti in quest’ordine.` — assente in `copy.md` (che per questa slide non prevede paragrafo di apertura). Contenuto innocuo; "vanno fatti in quest'ordine" riguarda le tre fasi di servizio, non un adempimento, quindi non ricade nel divieto di istruzioni operative.
- `Proprieta.dc.html` riga 25: `Affidare la gestione non vuol dire perdere il controllo della casa: le decisioni che contano restano dove devono stare.` — assente in `copy.md`. È un'opinione di posizionamento, non un claim: ammissibile, ma va aggiunta alla tabella CLAIM come tale.

### R-12 · Slide 10 `Canali.dc.html`, riga 39 — marchio di terzi nominato a testo

`Scheda Google della struttura, con mappa e recensioni.`
Nessun logo di terzi compare in nessuna slide (verificato su tutti e 16 i file): il divieto di brand riguarda i **loghi** e la suggestione di partnership, non la descrizione di un servizio. "Canali Google" è inoltre elencato fra i servizi nel brief §C. **Ammissibile così com'è.** Regola da tenere in fase di export: non aggiungere mai il logo Google, né icone di portali, a questa slide.

### R-13 · Divergenze minime di punteggiatura fra `copy.md` e artboard

Sistematiche e deliberate, nessun impatto: i titoli di slide acquistano il punto finale (`Messa in regola.`, `La casa pronta.`, `L’immobile che abbiamo visto.`, ecc.); la CTA di slide 15 è montata senza punto (`Firmiamo il contratto di gestione`) perché è un bottone. Allineare `copy.md` alle stringhe montate, così la prossima revisione non le rilegge come errori.

### R-14 · Slide 14 — titolo divergente

`copy.md` prevede titolo `Il perimetro economico`; l'artboard monta `Un numero solo.` e sposta "Il perimetro economico" nell'occhiello. Miglioramento, non errore: allineare `copy.md`.

### R-15 · Slide 16 `Chiusura.dc.html`, riga 23 — "farlo rendere"

`Il suo bilocale a Lido Centro, e il lavoro che serve per farlo rendere.`
È l'unico punto del deck in cui si afferma un esito economico, anche se senza cifre (claim 25 lo classifica come opinione di posizionamento: ammissibile). Se si vuole azzerare anche questo margine, versione che chiude il cerchio con la slide 04 (*"Gira finché la casa lavora"*):

```
Il suo bilocale a Lido Centro, e il lavoro che serve per farlo lavorare.
```

---

## Controlli superati — verificati uno per uno

| Controllo | Esito |
|---|---|
| Marcatori `[DATO DA VERIFICARE]`, TODO, placeholder | **Nessuno** in nessuno dei 16 file |
| Numeri di rendimento, occupazione %, ADR, proiezioni | **Nessuno** |
| Aliquote fiscali, cedolare, P.IVA, sostituto d'imposta | **Nessuno** |
| Importi di sanzione, riferimenti a pena detentiva/penale | **Nessuno** |
| Articoli di legge, decreti, numeri di sentenza | **Nessuno** |
| Garanzie ("rischio zero", "tutto in regola al 100%", "nessuna sanzione") | **Nessuna** |
| Promesse di crescita, curve, frecce, "+X%" | **Nessuna** — slide 12 monta l'anti-promessa esplicita |
| Cifre presenti nel deck | **15%** (CONFERMATO, claim 19) · **10 del mese** (CONFERMATO) · **24 ore** (CONFERMATO, vedi R-06) · **16 del mese** (CONFERMATO con riserva, vedi R-04) · **50-60 mq** (CONFERMATO, dichiarato dopo sopralluogo) · **Municipio X** (dato amministrativo) · **H24** (materiali Hadrianus). Nessun'altra cifra |
| Istruzioni operative (procedure, link, credenziali, ordine) | **Nessuna** — nessun URL nel testo visibile (l'unico `https://` è il foglio di stile dei font, non a schermo). Unico residuo borderline: R-05 |
| Slide 08 — ingresso senza identificazione | **Non presente.** La promessa dice *"Entra solo dopo essere stato identificato"*, la Nota ribadisce *"Il check-in resta presidiato"*. Conforme al brief §6 |
| «Guadagniamo solo se guadagni tu.» alla lettera | **Sì**, `Condizioni.dc.html` riga 53, tra caporali. Mai "guadagni solo se…" |
| "hotel-style" | **Mai.** Solo `standard alberghiero` (slide 04 e 07) |
| "Templum Purum" o divisione pulizie nominata | **Assente** |
| Emoji | **Nessuna** |
| Blu navy | **Assente** — base scura `#2E2A25`/`#3F3A33` (fumè caldo) su slide 04, 14 e velo della 16 |
| Strutture nominate, indirizzi, quartieri degli immobili in gestione | **Nessuno** |
| Riferimenti a familiari della proprietaria | **Nessuno** |
| Confronto "noi vs fai-da-te" / chi fa da sé | **Nessuno** |
| Urgenza inventata ("offerta valida fino a") | **Nessuna** |
| Registro: lei ovunque | **Sì.** Unica occorrenza di "tu" in tutto il deck: la formula di brand tra caporali (slide 14). Verificato con ricerca su `tu / tuo / tua / tuoi / tue / ti / te` |
| Apostrofi tipografici | **Coerenti**: `’` (U+2019) in tutte e 16 le slide, nessun apostrofo dritto nel testo |
| Doppi spazi nel testo a schermo | **Nessuno** |
| Refusi | **Nessuno rilevato** |
| CTA | **Una sola** in tutto il deck (slide 15, banda oro). Nessun "ci pensi", nessun "le mandiamo un preventivo" |
| Foto usate | `salotto.webp` (slide 07), `cucina.webp` (slide 09), `tramonto.webp` (slide 16), `hadrianus-logo-900.webp` (slide 01) |
| `smart-tv-streaming-mockup.jpg` (loghi Netflix/Prime/Disney+) | **Non presente** nella cartella `slide/` e non referenziata in nessun file. Corretto |
| Marchi di terzi nelle foto | **Nessun logo leggibile.** `salotto.webp`: divano, boiserie, tende — pulita. `cucina.webp`: sul piano ci sono un tostapane e una macchina a capsule, **nessun marchio leggibile** e nessuno dei due è protagonista dell'inquadratura (ritaglio 400×208 `object-fit: cover`). Ammissibile |
| Completezza campagna | `brief-mercato.md` · `copy.md` · `direzione-artistica.md` · 16 artboard editabili + `canvas.json` · export PDF. Angolo e target coerenti fra brief, copy e artboard |

---

## Coerenza col tono Hadrianus

**In linea.** Il deck tiene il registro asciutto e non consolatorio dei `riferimenti/`: frasi corte, verbi al presente, nessun aggettivo di vendita, la prova data nominando le cose invece che promettendole. Le tre mosse che lo rendono riconoscibile come Hadrianus e non come un deck di categoria:

- l'anti-promessa di slide 12 (*"Non le promettiamo una crescita. Le promettiamo che i numeri li guardiamo, e che quando serve cambiamo"*) — è lo stesso patto di onestà di `facebook-campagna-virale`;
- il rifiuto della stima a slide 15 (*"Non a occhio, e non prima di aver visto le carte"*) — la rinuncia al numero usata come argomento, non come reticenza;
- il tono descrittivo di slide 06, che è il punto in cui il deck poteva scivolare nella minaccia e non lo fa: nessun rosso, nessun punto esclamativo, nessuna sanzione, nessuna colpa attribuita.

Nessuna slide scivola verso il "zero pensieri / ci occupiamo di tutto" identificato nel brief come rumore di fondo del settore. Slide 04 e 11 reggono l'ampiezza senza diventare brochure di spunte.

---

## Verdetto

**Non consegnabile al cliente nello stato attuale.** Tre stringhe vanno corrette prima della stampa e prima della riunione: **B-1** (didascalia slide 09), **B-2** (slide 13, claim DA VERIFICARE), **B-3** (slide 14, "solo").

### Condizioni per il via libera

1. Montare le riscritture di **B-1** e **B-3**; per **B-2** ottenere dal titolare la risposta alla domanda 3 di `copy.md` e montare l'opzione A o l'opzione B.
2. **Rigenerare gli export.** Le stesse stringhe sono già dentro `proposta-gestione-lido-centro.html` e `Hadrianus-Presentazione-Bilocale-Lido-Centro.pdf`: dopo la correzione vanno ri-emessi (`build-slides.mjs` / `emit.mjs` / `make-pdf.mjs`), altrimenti il PDF che la proprietaria si porta a casa resta quello sbagliato.
3. Aggiornare la tabella CLAIM di `copy.md` con le stringhe definitive e con i due testi di R-11 oggi non tracciati.
4. **Prima della riunione, non nel deck:** il titolare deve avere pronte a voce (a) la tipologia scelta casa vacanze / alloggio per uso turistico (R-07), (b) durata, esclusiva, recesso e uso personale dell'immobile — domanda bloccante 1 di `copy.md`, oggi senza nessuna slide che risponda: è l'obiezione che arriva **subito dopo** la slide 14.
5. Facoltativi ma consigliati prima della stampa: R-03, R-05, R-08, R-10.

Fatte 1 e 2, il deck è approvabile.
