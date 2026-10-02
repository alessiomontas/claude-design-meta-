# Checklist compliance — Listino Via Cola di Rienzo

Documento controllato: `listino-hadrianus-cola-di-rienzo.html` (3 pagine) + `anteprime/pagina-01..03.png`
+ `copy-e-claim.md` + `README.md`. Natura: documento commerciale per cliente in trattativa, non
contenuto di acquisizione social.

## Esito

**DA CORREGGERE** — 6 bloccanti. Nessuno riguarda i prezzi (l'aritmetica è corretta): riguardano
contraddizioni interne fra claim "tutto compreso" e voci a consumo, il perimetro di ciò che la
tariffa **non** copre, e due errori di lingua/registro.

## Verifiche superate

- **Aritmetica**: 70+10+15 = 95 ✓ · 60+10+15 = 85 ✓ · 40+10+15 = 65 ✓ · 95+85+65 = 245 ✓.
  Metrature e tipologie coerenti fra pag. 01, pag. 03, `README.md` e `copy-e-claim.md`.
- **Dati dal titolare**: tutti gli importi del documento risalgono alla fonte confermata. Nessun
  marcatore `[DATO DA VERIFICARE]` residuo nell'HTML.
- **Lessico di brand**: nessun "hotel-style", nessuna struttura o azienda nominata come prova,
  nessun "guadagni solo se guadagni tu". Verificato per stringa sull'HTML.
- **Claim vietati per natura**: nessun superlativo assoluto, nessun "garantito", nessun paragone
  con concorrenti, nessuna percentuale di rendimento, nessun claim fiscale.
- **Marchi di terzi**: le uniche immagini sono il logo Hadrianus e il filigranato del capitello.
  Nessun marchio di terzi inquadrato.
- **Resa a schermo**: nessun testo tagliato, nessuna sovrapposizione, contrasto adeguato su tutte e
  tre le pagine (incluse le card scure di pag. 02 e 03).

## Bloccanti (da correggere prima della consegna)

1. **Pag. 01, banda — "quello che paga" è un assoluto smentito dal documento stesso.**
   La banda promette un solo numero; due righe sopra la nota kit, e pag. 03, dicono che i kit in più
   si aggiungono. In un listino questa è la frase su cui si contesta una fattura.
   → Attuale: `Un solo numero per unità: <b>quello che legge nel listino è quello che paga.</b>`
   → Nuovo: `Un solo numero per unità a ogni check-out: <b>quello che legge nel listino è quello che paga</b>, più i soli kit in più effettivamente preparati.`

2. **Pag. 02, banda — il claim è più largo del servizio elencato.**
   "Tutto quello che si consuma" include, per un cliente, caffè, cortesie, sacchi, sale: la voce 02
   elenca cinque consumabili precisi. Appiglio diretto per una richiesta non prevista nel prezzo.
   → Attuale: `Tutto quello che si consuma <b>lo portiamo noi, a ogni intervento.</b>`
   → Nuovo: `I consumabili del refill <b>li portiamo noi, a ogni intervento.</b>`

3. **Pag. 02, occhiello — "uguale ogni volta" non è vero quando si aggiunge un kit.**
   → Attuale: `È la ragione per cui resta un numero solo, uguale ogni volta.`
   → Nuovo: `È la ragione per cui resta un numero solo per ogni check-out.`

4. **Pag. 03, nota legale — dichiarazione di compliance interna esposta al cliente.**
   La seconda metà della nota elenca ciò che il documento *non* fa (rendite, percentuali fiscali,
   altre aziende): temi che nel listino non esistono e che il cliente non ha sollevato. Suona
   difensiva e li introduce lei. In più manca ciò che la nota di un listino deve dire: perimetro,
   esclusioni, validità.
   → Attuale: `Il documento riporta le tariffe del servizio: non promette rendite, guadagni o risultati, non cita percentuali fiscali o statistiche e non nomina altre aziende.`
   → Nuovo: `Le tariffe coprono la pulizia di cambio ospite in condizioni d'uso ordinarie: gli interventi straordinari (ripristini dopo danni o sporco eccessivo) sono concordati di volta in volta. Listino valido fino al [DA CONFERMARE COL TITOLARE].`
   La prima frase della nota (riferimento alle tre unità, euro, IVA inclusa) resta invariata.

5. **Pag. 03, prossimo passo — errore di forma di cortesia.**
   Con il "Lei" l'esortazione vuole il congiuntivo: così com'è è un indicativo che descrive un fatto
   invece di chiederlo, e la CTA perde forza.
   → Attuale: `Ci conferma le tre unità e partiamo dal primo check-out assegnato.`
   → Nuovo: `Ci confermi le tre unità e partiamo dal primo check-out assegnato.`

6. **Perimetro non definito su cinque punti che in un listino generano contestazione.**
   Il documento dice "tutto compreso" quattro volte e non dice mai cosa resta fuori. Servono
   decisioni del titolare, non riscritture:
   - **Composizione del kit biancheria**: "15 € a kit" è addebitabile più volte al mese ma il kit non
     è mai definito (quante lenzuola, quanti asciugamani, per quante persone). Da esplicitare nella
     nota kit di pag. 01.
   - **Proprietà della biancheria e capi persi/danneggiati dall'ospite**: pag. 02 voce 04 fa pensare
     che scorte e rotazione siano di Hadrianus, ma non si dice chi paga la sostituzione.
   - **Pulizia straordinaria**: coperta dalla riformulazione al punto 4, da confermare come policy.
   - **IVA**: "IVA inclusa" senza aliquota né regime. Se il cliente ha partita IVA chiederà imponibile
     + IVA; se Hadrianus fosse in regime forfettario la dicitura sarebbe da riscrivere.
   - **Termini di pagamento** della fattura mensile (mezzo e giorni): assenti.
   - **Validità del listino**: assente (già dichiarata zona grigia in `copy-e-claim.md`); il
     placeholder al punto 4 va riempito dal titolare, non inventato.

## Osservazioni (non bloccanti, ma da considerare)

- **Pag. 01, lead — "prezzo pieno" si legge come "non scontato".** In un listino "pieno" evoca il
  prezzo di partenza prima di uno sconto; qui vuol dire "comprensivo".
  → `Ogni unità ha un prezzo pieno per intervento:` → `Ogni unità ha una tariffa unica per intervento:`
- **Pag. 02, voce 02 — "rimettere a posto" è riordinare, non rifornire.**
  → `e li rimettiamo a posto a ogni passaggio.` → `e li reintegriamo a ogni passaggio.`
- **Pag. 02, voce 04 — due aggettivi in fila senza virgola, si legge come refuso.**
  → `lenzuola e asciugamani puliti pronti a ogni cambio ospite` → `lenzuola e asciugamani puliti, pronti a ogni cambio ospite`
- **Pag. 02, card fatturazione — "un'unità non lavora" è colloquiale** (a non lavorare è la persona).
  → `se un'unità non lavora, non produce costo.` → `se un'unità resta ferma, non produce costo.`
- **Pag. 03, esempio — "Totale della settimana" in corpo grande può essere letto come costo
  settimanale fisso**, anche se l'occhiello dice "Un esempio".
  → `<b>Totale della settimana</b>` → `<b>Totale dell'esempio</b>`
- **Pag. 03 — "Prodotti professionali, portati da noi":** "professionali" qualifica il prodotto, ma
  tra i claim confermati il titolare ha detto "pulizie complete e professionali" (il servizio). Se la
  linea prodotti non è professionale, scrivere `Prodotti di pulizia, portati da noi`.
- **Pag. 03 — "I sopralluoghi per verificare il lavoro"** dice al cliente che non dovrà più
  controllare l'operato: è una promessa di qualità senza rimedio definito. Più prudente legarla alle
  scorte: `I sopralluoghi per rifornire e ricontrollare le scorte`.
- **Ripetizione di schema**: tre voci su cinque di pag. 02 chiudono con "li … noi" (`li compriamo
  noi`, `li portiamo noi`, `li seguiamo noi`). Variarne almeno una.
- **Ordine delle unità incoerente**: l'hero di pag. 01 le elenca dalla più piccola
  (`Small Double Room · Superior Double Room · Double Deluxe`), la tabella e l'esempio di pag. 03
  dalla più grande. Allineare.
- **Pag. 03, resa**: le due colonne del confronto partono sfasate di ~2 px (la card chiara ha un
  bordo da 1 px, quella scura no), quindi le righe `✕` e `◆` non si allineano. Risolvibile con
  `box-sizing: border-box` o un bordo trasparente sulla card scura.
- **Pag. 01, resa**: nella riga di testata il bordo destro di "Pulizia completa" non cade sul bordo
  destro dei valori come nelle altre colonne. Da verificare sul PDF a stampa.
- **Recapiti assenti in calce** (solo "Hadrianus Multiservice · Roma"): è la pagina in cui si chiede
  una conferma ed è il punto in cui il cliente cerca un contatto. Scelta già dichiarata, ma vale la
  pena riproporla al titolare.
- **Tracciabilità**: `README.md` ("Stato: 🟢 Pronto — compliance passata") e la riga del listino in
  `campagne/INDEX.md` ("🟢 Pronto — compliance passata") davano la compliance per superata prima che
  questo controllo esistesse. Da aggiornare all'esito reale.
- **`copy-e-claim.md` non è allineato al PDF** pur dichiarando di riportarne il testo esatto: il
  blocco esempio di pag. 03 è parafrasato (manca la riga "Totale della settimana"), mancano i meta
  "Hadrianus Multiservice · 02 / 03" e i piedi di pagina. Da sistemare contestualmente alle
  correzioni, visto che è il file di riferimento per chi tocca l'HTML.
- **Fuori perimetro ma incoerente**: `CLAUDE.md` afferma che le varianti trasparenti del logo non
  sono disponibili, mentre questa campagna ne ha prodotta una
  (`brand-assets/logo/trasparenti/logo-crema-trasparente.png`, esistente).

## Coerenza col tono Hadrianus

**In linea**, con un'avvertenza di metodo.

Il registro — frasi corte, prezzo dichiarato subito, beneficio detto come lavoro che il cliente
smette di fare ("non entra più in conto"), nessun aggettivo di vendita — è lo stesso dei
`riferimenti/`, trasposto dal "tu" social al "Lei" commerciale. La scelta di giustificare il prezzo
con il processo invece che con superlativi è esattamente il modo in cui il brand parla.

Due note:

1. I file in `riferimenti/` sono tutti social e in "tu": non sono il metro di questo documento. Il
   metro di continuità sono le 3 slide già inviate (`Preventivo-pulizie-Cola-di-Rienzo.pdf`), che
   **non sono nel repository**: la verifica di continuità del registro (in particolare "lei"
   minuscolo vs "Lei" di cortesia) non è stata possibile e va fatta sul file in mano al titolare.
2. Il documento è internamente coerente: usa la forma di cortesia in tutte le occorrenze (`Che cosa
   cambia per lei`, `senza che lei debba occuparsene`, `Ci conferma…`), nessun "tu". Se le slide
   usano la maiuscola di cortesia, qui bastano due sostituzioni (titolo di pag. 03 e voce 04 di
   pag. 02) più il verbo del punto bloccante 5.


---

## Chiusura del giro (dopo la revisione del controllo)

**8 dei 9 rilievi testuali sono stati applicati** all'HTML e il PDF è stato rigenerato; la tabella
completa prima/dopo è in `copy-e-claim.md` §"Correzioni applicate dopo il `compliance-checker`".

**Tre rilievi sono stati respinti**, con motivo scritto nello stesso file:

- le due frasi "Tutto quello che si consuma lo portiamo noi" e "Prodotti professionali, portati da
  noi" sono **citazioni testuali della slide 02 già consegnata al cliente**: riscriverle qui
  produrrebbe due versioni della stessa promessa in due documenti letti insieme. Le slide non sono
  nel repository (sono il PDF che il titolare ha in mano), quindi questo controllo non poteva
  verificarlo;
- la riscrittura della nota legale introduceva **condizioni commerciali nuove** (interventi
  straordinari concordati di volta in volta, data di scadenza del listino) mai dette dal titolare,
  più un placeholder `[DA CONFERMARE]` visibile al cliente: non si scrivono senza sua conferma.

Il merito del rilievo resta: le cinque questioni di perimetro sono state girate al titolare come
**decisioni aperte** (composizione del kit, biancheria danneggiata, interventi straordinari,
aliquota/regime IVA, termini di pagamento e validità) ed elencate in `copy-e-claim.md`.
