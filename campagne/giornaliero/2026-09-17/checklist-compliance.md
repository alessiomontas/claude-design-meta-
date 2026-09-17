# Checklist compliance — Giornaliero 17/09/2026 · «Ad agosto sei pieno come tutti»

Controllato: `copy.md` (reel, carosello 5 slide, post Facebook + 3 immagini, 2 storie) contro `brief-mercato.md`,
`.claude/reference/lessico-brand.md`, `.claude/reference/master-template.md`, `riferimenti/riferimento-1.md` e `-2.md`,
`campagne/giornaliero/PIANO.md`, `brand-assets/README.md`.

## Esito

**DA CORREGGERE** — 6 bloccanti, tutti con riscrittura pronta qui sotto. Nessuno è strutturale: l'impianto,
l'angolo e la disciplina sui dati reggono. Dopo le correzioni il pacchetto è approvabile senza rileggerlo da capo.

### Cosa è già a posto (verificato, non serve ritoccarlo)

| Controllo | Esito |
|---|---|
| Marcatori `[DATO DA VERIFICARE]` impaginati | **nessuno**. Le 3 occorrenze (righe 198, 299, 569) stanno solo nelle tabelle CLAIM e nella sezione di chiusura, come documentazione di ciò che è stato **escluso**. Non sono testo destinato a schermo → non bloccanti. **Non devono migrare nelle artboard né nelle caption.** |
| Dati di performance Hadrianus | **zero**, in tutti e cinque i contenuti. Dichiarato esplicitamente nelle tabelle CLAIM di R e S1 |
| 61,5% Roma gen-mar 2026 | sempre con fonte a schermo (reel sc. 14 micro-riga, C4 banda dato, S2 riga dato) e sempre qualificato "alberghiera" |
| Fiumicino +20% nov-dic 2025 | solo nel testo del post FB, con fonte (Aeroporti di Roma/ENAC) — come da perimetro |
| «nessun costo fisso» / deposito / assicurazione | **assenti** da ogni formato |
| RevPAR/ADR ott-dic 2025 · Giubileo · medie 1.000-1.100 €/mese | **assenti** |
| Lessico | «Guadagniamo solo se guadagni tu» corretto in tutte le 9 occorrenze. Mai «hotel-style»: sempre «standard alberghiero». Nessuna struttura nominata, nessun case study |
| Vincoli ereditati dal brief | nessuna lista delle 5 tipologie di ospite, nessun costo del vuoto (16/09), nessun calendario eventi come tema (15/09), nessuna griglia calendario, nessuna tabella a due colonne, nessun grafico stagionale, nessun consiglio fiscale |
| Storie | S1 e S2 sono **autoconclusive**: ognuna ha problema + soluzione + CTA e non rimanda all'altra |
| Marchi di terzi | `smart-tv-streaming-mockup.jpg` escluso esplicitamente nei NEGATIVE di C5 e F3. Tutti i prompt generativi escludono logo/signage/brand appliances |
| Palette | fumè `#3F3A33` + oro `#C8A24B`, nessun blu navy; tutti i prompt hanno "no blue tones, navy" |

---

## Bloccanti (da correggere prima della consegna)

### B1 · S2 usa un gancio vietato dal brief, nega l'inverno e esce dall'angolo del giorno

Tre problemi nello stesso contenuto:

1. **Gancio vietato.** Il brief, §Vincoli: *«❌ "D'inverno non viene nessuno" come gancio: già usato, e comunque oggi l'apertura è un'altra.»* S2 lo usa esattamente come Gancio (riga 512 e riga 520).
2. **Claim falso.** «**Non viene meno gente.** Viene gente diversa» (riga 527) è smentito dai dati dello stesso brief (Q4 2025 70,3% → Q1 2026 61,5%) e contraddice l'istruzione del brief sull'obiezione 2: *«Ostia sì, si svuota come località balneare… Non negare l'inverno: cambiargli il soggetto.»* Negare l'inverno a un proprietario che lo vede coi suoi occhi brucia credibilità.
3. **Fuori angolo + ambiguità.** S2 replica la tesi della campagna precedente (*l'inverno non è vuoto*) invece di quella di oggi (*l'estate non è una prova*): agosto compare solo nell'ultima riga. E «la casa va **venduta** a lei» in un contenuto rivolto a proprietari di immobili si legge, per un istante, come *vendere l'appartamento*.

**Riscrittura completa di S2** (sostituisce righe 511-538):

```
**COPY**
Gancio      | Agosto non fa testo. Gennaio sì.
Corpo       | 61,5% di occupazione alberghiera
            | a Roma, gennaio-marzo 2026.
CTA         | Scrivi NOVEMBRE in DM
Caption     | —
```

Testo integrale a schermo:

```
Agosto non fa testo.
Gennaio sì.

61,5%
occupazione alberghiera a Roma,
gennaio-marzo 2026 — uno dei trimestri
più bassi dell'anno.
Federalberghi Roma su dati STR.

Non è che non viene nessuno: viene gente
diversa. Congressi, fiere, scalo di
Fiumicino, ospedali, università.
E l'annuncio va scritto per loro, non per
il turista di agosto.

Gestione completa in standard alberghiero,
15% sul fatturato generato.
Ad agosto ci guadagnano tutti.
Da ottobre guadagniamo solo se guadagni tu.

Scrivi NOVEMBRE in DM.
```

Gancio alternativo se «non fa testo» suona troppo colloquiale: **«Il mese che dice la verità non è agosto.»**
La riscrittura risolve anche: la ripetizione del 61,5% (ora sta solo nel numero hero + riga dato), la chiusura
obbligata mancante («Ad agosto ci guadagnano tutti» non c'era in S2), e l'ambiguità di «venduta».

### B2 · «Il trimestre più basso dell'anno» — superlativo non sostenuto dalle fonti citate

Il brief riporta **due** trimestri con fonte: Q1 2026 61,5% e Q4 2025 70,3%. Nessun dato Q2/Q3. La frase
«il trimestre più basso dell'anno» è quindi un superlativo assoluto **non provato dal materiale che citiamo**,
e compare a schermo o in caption in 4 punti. Costo della correzione: una parola. Costo del non correggerla:
una contestazione su un dato Federalberghi che non abbiamo verificato.

| Dove | Ora | Sostituire con |
|---|---|---|
| C4, riga territorio (riga 218) | `Il trimestre più basso dell'anno. Federalberghi Roma su dati STR.` | `Uno dei trimestri più bassi dell'anno. Federalberghi Roma su dati STR.` |
| Caption carosello (riga 277) | `Roma nel trimestre più basso dell'anno, gennaio-marzo 2026, ha registrato…` | `Roma in uno dei suoi trimestri più bassi, gennaio-marzo 2026, ha registrato…` |
| Post FB (riga 321) | `Roma nel suo trimestre più basso, gennaio-marzo 2026, ha registrato…` | `Roma in uno dei suoi trimestri più bassi, gennaio-marzo 2026, ha registrato…` |
| S2 | già risolto nella riscrittura B1 (`uno dei trimestri più bassi dell'anno`) | — |

In alternativa si tiene «il più basso» **solo se** il `ricercatore-mercato` recupera i valori Q2/Q3 dallo stesso
comunicato Federalberghi/STR e li mette nel brief. Finché non ci sono, si usa la forma attenuata.

### B3 · «un buco pesa dieci volte di più» — numero senza fonte nel testo pubblicato

Post FB, riga 315. Nel brief «dieci volte di più» è una figura retorica del ricercatore, non un dato: nel testo
pubblicato diventa una quantificazione. Regola del pacchetto: ogni numero ha fonte, o non si scrive.

- **Ora:** `I soggiorni diventano più lunghi e più rari. Meno turnover, ma un buco pesa dieci volte di più.`
- **Sostituire con:** `I soggiorni diventano più lunghi e più rari. Meno turnover, ma un buco pesa molto di più.`

### B4 · Impegni operativi non coperti dal brief («risposte in un'ora», «ospiti seguiti H24»)

Distinzione che va tenuta, perché non è la stessa frase a essere vietata ovunque:

- ✅ **Resta** dove è descrizione del mestiere, senza soggetto e dentro il confronto agosto/novembre: reel sc. 9
  (`NOVEMBRE — rispondere in un'ora è fatturato`), C4 voce Risposte, post FB bullet 5
  (`Rispondere in un'ora smette di essere cortesia e diventa fatturato`). È la frase del brief, parla del mercato.
- ❌ **Va tolto** dove diventa un elenco di servizio sotto il marchio Hadrianus: lì il lettore legge un impegno
  contrattuale ("un'ora") che nessun documento conferma. Stesso problema per «ospiti seguiti **H24**»: il brief
  documenta «**check-in** smart H24», non l'assistenza ospiti 24 ore.

| Dove | Ora | Sostituire con |
|---|---|---|
| F2, tre righe (riga 382) | `Prezzo mosso ogni settimana` · `Annuncio riscritto per chi viaggia fuori stagione` · `Risposte in un'ora, manutenzione nei mesi bassi` | `Il prezzo si muove ogni settimana` · `L'annuncio si riscrive per chi viaggia fuori stagione` · `Richieste seguite subito, manutenzione nei mesi bassi` |
| F2, kicker (nuovo, y 150-190, Manrope 600 maiusc. 17, `#C8A24B`) | — | `COSA CAMBIA DA OTTOBRE` — chiarisce che le tre righe descrivono il lavoro, non un listino di garanzie |
| C5, blocco offerta (riga 252) | `…prezzo mosso ogni settimana, annuncio riscritto per chi viaggia fuori stagione, ospiti seguiti H24, pulizie e controlli.` | `…prezzo mosso ogni settimana, annuncio riscritto per chi viaggia fuori stagione, check-in H24, ospiti seguiti, pulizie e controlli.` |
| S1, corpo 2 (righe 465-467) | `Il gestore si vede da ottobre a marzo: prezzo mosso ogni settimana, annuncio riscritto per chi viaggia fuori stagione, risposte in un'ora.` | `Il gestore si vede da ottobre a marzo:` / `come muove il prezzo, per chi riscrive` / `l'annuncio, quanto ci mette a rispondere.` |

La riscrittura di S1 non toglie forza: restituisce al proprietario **il metro di giudizio**, che il brief indica
come gamba portante dell'angolo. Nota per l'art-director: il blocco S1 passa da 4 a 3 righe (zona `corpo 2`, y 960-1180).

### B5 · Il post Facebook mostra l'accusa e nasconde il sollievo

È il rischio di tono che il titolare ha segnalato, e nel formato Facebook si materializza: il collage si vede
sempre, il testo del post si apre solo dopo «Vedi altro». Il sollievo («non è un tuo errore») sta **solo** nel
secondo paragrafo del testo; nelle tre immagini il proprietario legge «Ad agosto sei pieno come tutti» +
«non è lì che si vede chi ti gestisce la casa» + offerta. Senza la scena del perdono, F1 è un rimprovero.
Il reel questo problema non ce l'ha: risolve alla scena 3 con `Meglio così.`; il carosello lo risolve con C2.

**F1 — sostituire il Corpo** (righe 337-338):

- **Ora:** `E non è lì che si vede` / `chi ti gestisce la casa.`
- **Sostituire con:** `E non è un tuo errore:` / `ad agosto si riempie anche da soli.`

Il concetto «non è lì che si vede chi ti gestisce la casa» non si perde: lo porta F2 con
`Ad agosto il lavoro lo fa il calendario. Da ottobre lo deve fare qualcuno.` Se la seconda riga non entra in
due righe a corpo 50, scendere a **45** (in scala), mai accorciare togliendo «anche da soli».

### B6 · C4, indice di slide illeggibile (spec da una riga)

Riga 227: `| indice | 1280-1310 | 4/5 | Manrope 600 | 17 | #2E2A25 |`. La banda dato oro finisce a y 1250:
l'indice sta **sotto**, su fondo fumè `#3F3A33`, in scuro `#2E2A25` → invisibile. Tutte le altre slide usano
`#C8A24B`.

- **Sostituire con:** `| indice | 1280-1310 | 4/5 | Manrope 600 | 17 | #C8A24B |`

---

## Osservazioni (non bloccanti, ma da considerare)

### Tono — gli altri punti in cui il copy accusa

- **Variante hook C (riga 14):** «Hai un mese che ti rassicura e **dieci che non sai leggere**.» Non è impaginata,
  ma è in tabella e qualcuno in revisione può sceglierla: è l'unica delle tre varianti che dà dell'incapace al
  proprietario. Riscrittura: **«Un mese ti rassicura. Gli altri dieci non te li ha spiegati nessuno.»**
- **«Chi non la usa se la ritrova a luglio»** (C4 voce Manutenzione, riga 214; post FB bullet 6, riga 319). È
  l'unico punto dove il copy dice «se non lo fai, peggio per te». Renderlo impersonale costa nulla:
  - C4: `Novembre: è la finestra. Se non si fa adesso, tocca farla a luglio, con la casa piena.`
  - FB: `E i mesi bassi sono la finestra per la manutenzione: se non si fa adesso, tocca farla a luglio, con la casa piena.`
- **Il fai-da-te (target primario, profilo 3) non ha una via d'uscita.** «La domanda da fare a chi ti gestisce la
  casa» funziona per chi ha un gestore; per chi si gestisce da solo diventa un esame su se stesso. Mezza riga in
  caption e nel post, dopo «Non è una critica…», chiude il buco:
  `E se la casa la gestisci da solo, la domanda vale lo stesso: non è un esame, è un punto di partenza.`
- **F3, kicker** (riga 421): `LA DOMANDA DA FARE AL TUO GESTORE` presuppone che un gestore ci sia già, e stona
  con C5 e col post che dicono «a chi ti gestisce la casa». Allineare: `LA DOMANDA DA FARE A CHI TI GESTISCE LA CASA`.

### Claim e dati — attenzioni residue

- **Il 61,5% non deve mai restare da solo sopra l'offerta.** Reel sc. 14 → sc. 15 e S2 (numero hero oro, poi il
  15%) sono i due punti in cui un occhio distratto può leggere quel numero come occupazione di Hadrianus. La
  parola «alberghiera» e la fonte devono stare **nello stesso blocco visivo del numero**, mai relegate in una
  riga che può essere tagliata in fase di impaginazione. È già scritto così: va solo tenuto al rendering.
- **«nessun costo fisso» è assente per scelta**: l'art-director non deve "completare" l'offerta con badge tipo
  *0 costi fissi* / *nessun deposito*. Restano `[DATO DA VERIFICARE]` col titolare.
- **«pulizie e controlli»** (C5): «controlli» non è nel brief. Come descrizione della gestione va bene; non va
  trasformato in impegno numerico in grafica (es. «controlli settimanali»).
- **`[DATO DA VERIFICARE]` nelle tabelle CLAIM** (righe 198, 299): è documentazione corretta di ciò che è stato
  escluso, non copy. Va però verificato che non finisca copiato nelle artboard o in `PUBBLICAZIONE.md`.

### Formale, punteggiatura, coerenza fra i cinque contenuti

- **Virgolette della CTA.** A schermo `Scrivi "NOVEMBRE" in DM` usa virgolette dritte dentro un blocco già
  maiuscolo: su pillola oro fanno sporco e sono ridondanti. Uniformare a `SCRIVI NOVEMBRE IN DM` in tutte le
  grafiche (reel sc. 16, C5, F3, S1, S2). Nel testo del post FB, dove la virgoletta serve davvero, usare i
  caporali: `Scrivi «NOVEMBRE» in DM o in un commento.`
- **«Cosa fai a novembre» ha tre punteggiature diverse.** C5 riga 247 e F3 riga 408: `«Cosa fai a novembre.»`
  (maiuscola, punto **dentro**); post FB riga 323: `«cosa fai a novembre»` (minuscola, punto **fuori**).
  Scegliere una forma sola: consigliata `«Cosa fai a novembre?»` ovunque — è letteralmente la domanda da fare,
  e il punto interrogativo la rende più forte, non più debole.
- **CTA Facebook incoerente:** il testo del post dice «in DM o in un commento», la grafica F3 dice solo «in DM».
  Su Facebook il commento è il canale che funziona meglio: allineare F3 a `SCRIVI NOVEMBRE NEI COMMENTI`
  oppure `SCRIVI NOVEMBRE IN DM O NEI COMMENTI`.
- **Campo CTA ≠ testo a schermo** in S1 e S2: il blocco COPY dice `Scrivi "NOVEMBRE"`, il testo integrale dice
  `Scrivi "NOVEMBRE" in DM.` Allineare i due (vince la versione con «in DM»).
- **Master Template incompleto per il blocco F** (testo del post, righe 305-329): ha solo il corpo del testo,
  mancano COPY / LAYOUT / PROMPT GRAFICO / NEGATIVE / PARAMETRI / CLAIM. Il template dice che un blocco non
  applicabile si scrive `—`, non si elimina. Conseguenza concreta: il claim **Fiumicino +20%** è tabellato sotto
  **F3**, che non lo contiene — va spostato nella tabella CLAIM di F.
- **C3, riga 192:** NEGATIVE e PARAMETRI sono collassati sulla stessa riga (`**NEGATIVE** — · **PARAMETRI** …`).
  Separarli, come in tutti gli altri contenuti.
- **S2, fuori scala tipografica:** `70 (display 160 in scala titolo)` (riga 545). La scala fissa del master
  template è 70·62·50·45·40·33·31·17 e «fuori scala non si va». O si resta a 70, o il passo "display" va
  aggiunto formalmente a `design-system.md` prima di usarlo.

### Rischi di impaginazione da verificare sul PNG (controlli 2 e 3 del master template)

- **C3 e C4, righe «Novembre» troppo lunghe per il corpo 40.** A 40 px in colonna 952 entrano ~43 caratteri:
  `Novembre: si muove ogni settimana, a volte ogni giorno.` (55), `Novembre: congressi, fiere, aeroporto, ospedali, università.` (60),
  `Novembre: è la finestra. Chi non la usa se la ritrova a luglio, con la casa piena.` (81) vanno tutte a capo,
  mentre `Novembre: soggiorni più lunghi e più rari.` (42) no → i blocchi **non avranno l'altezza identica** che
  il copy stesso impone («identica altezza», righe 188 e 228). Due soluzioni: righe dei blocchi a corpo **33**,
  oppure accorciare i testi in modo che tutte le voci «Novembre» stiano su due righe. Da decidere prima di
  impaginare, non dopo.
- **S2, layout e testo non combaciano** (anche dopo la riscrittura B1): `riga dato` è descritta come «2 righe +
  fonte» ma il testo ne ha 3 + fonte; `corpo` è «4 righe» ma il testo ne ha 5; `offerta` mette 3 righe a corpo
  45/33 in 100 px (1280-1380), che non bastano. Ricalcolare le zone sul testo definitivo.

### Immagini e asset

- **C5 e F3 non dicono quale foto usare** («foto reale da `brand-assets/immobili/`, interno»). Gli interni
  disponibili sono tre e due sono problematici: `smart-tv-streaming-mockup.jpg` (loghi Netflix/Prime/Disney+,
  già escluso nei NEGATIVE — l'esclusione va mantenuta anche nel file dell'art-director) e
  `salotto-divano-azzurro.jpg` (divano blu-fumo: confligge con la palette calda fumè+oro e con il «no blue
  tones» scritto in tutti i prompt di questo pacchetto). **Indicare esplicitamente
  `brand-assets/immobili/cucina-soggiorno-open-space.png`.**
- Nessun altro contenuto usa foto reali: le grafiche generative hanno tutte `no logo, signage, brand names,
  recognisable business fronts` nei NEGATIVE. Nessun marchio di terzi in vista.

### Completezza del pacchetto

- La cartella contiene solo `brief-mercato.md` e `copy.md`: mancano `scene.json`, le artboard `.dc.html` e
  `PUBBLICAZIONE.md`. È atteso a questo stadio del flusso (compliance precede l'art-director) e non è bloccante
  per il copy, ma il pacchetto non è consegnabile finché non ci sono.
- Brief e copy sono **coerenti fra loro** su angolo, target e offerta. L'unico scostamento era S2 (vedi B1).
- Pilastro del giorno rispettato: il territorio spiega **da dove arriva la domanda**, non fa la guida turistica,
  nessun monumento citato.
- Nota di rotazione: «calendario» è il leitmotiv del pacchetto (5 occorrenze) e il 15/09 è uscito
  *«Il calendario di Roma»*. Il significato è diverso (qui è il calendario delle stagioni, lì quello degli
  eventi) e il brief vieta correttamente gli eventi come tema, ma chi segue la pagina tutti i giorni sente la
  parola ripetuta. Valutabile in revisione, non un problema di compliance.

---

## Coerenza col tono Hadrianus

**In linea, con un'evoluzione consapevole.** `riferimenti/riferimento-1.md` ha la struttura di casa —
problema concreto del proprietario → meccanismo → 15% → CTA secca — e la chiusura sull'allineamento:
il pacchetto la rispetta in tutti e cinque i contenuti. Qui il registro si sposta dal *sollievo dallo stress*
(«non dovrebbe essere un secondo lavoro a tempo pieno») al *criterio di giudizio* («la domanda da fare a chi
ti gestisce la casa»): è più asciutto e più adulto, e resta riconoscibile perché non promette mai un risultato
e chiude sempre sul 15%.

`riferimenti/riferimento-2.md` è il tono da **non** imitare (case study su struttura nominata, «risultati
record», ADR a schermo): il pacchetto lo evita completamente — nessuna struttura, nessun numero di performance,
solo dati di mercato con fonte. È esattamente la correzione che il titolare aveva chiesto.

Due punti in cui il tono si allontana, entrambi coperti sopra: **S2**, che scivola sull'angolo della vecchia
campagna stagionalità invece di tenere quello di oggi (B1), e il **collage Facebook**, che nella sequenza di
immagini perde la battuta di sollievo e resta sul rimprovero (B5). Corretti questi due, la frase
«il tuo agosto non dimostra niente» si legge come è stata pensata: *non è colpa tua, stavi solo guardando il
mese sbagliato*.
