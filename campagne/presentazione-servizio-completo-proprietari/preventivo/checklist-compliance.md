# Checklist compliance — Preventivo "messa in regola documentale" (bilocale Ostia Lido Centro)

Oggetto del controllo: il testo montato in `preventivo/Main.dc.html` (pagina 1) e `preventivo/Pagina2.dc.html` (pagina 2), letto anche sui PNG renderizzati `preventivo-1.png` / `preventivo-2.png`.
Metro: dati confermati dal titolare (oggetto, 500 € non soggetti a IVA, costi vivi a carico della proprietaria, pagamento alla consegna) · `brief-mercato.md` (ricerca normativa con stati CONFERMATO / DA VERIFICARE) · `copy.md` e `slide/` della presentazione già consegnata · `CLAUDE.md` · `.claude/reference/lessico-brand.md`.

**Differenza di genere rispetto al deck, e perché conta:** il deck è materiale di vendita, questo è un **documento commerciale che la cliente firma** ("Per accettazione del preventivo", pagina 2). Ogni riga di pagina 1 diventa oggetto dell'obbligazione. Il metro di severità qui è più alto, non più basso.

## Esito

**DA CORREGGERE — non inviabile nello stato attuale.**
9 rilievi bloccanti, 9 osservazioni. Nessun problema di lessico, tono, registro o palette: i rilievi sono tutti di sostanza contrattuale, fiscale e di coerenza con la proposta già consegnata.

---

## Tabella dei rilievi

Le correzioni vanno fatte **nel generatore** `build-preventivo.mjs` (colonna "riga · gen."), non solo negli `.dc.html`: altrimenti al primo `node preventivo/build-preventivo.mjs` tornano indietro.

| Pag. | Riga (`.dc.html` · gen.) | Testo oggi montato | Esito | Correzione |
|---|---|---|---|---|
| 1 | 31-33 · 84-86 | `Preventivo n. [numero]` · `Data [gg/mm/aaaa]` | **DA CORREGGERE — bloccante** | Compilare prima dell'invio → **B-3** |
| 1 | 33 · 86 | `Valido 30 giorni dall'emissione` | **DA VERIFICARE** | Default proposto da noi, mai confermato dal titolare → **R-4** |
| 1 | 39 · 92 | `[Nome e cognome della proprietaria]` | **DA CORREGGERE — bloccante** | Compilare prima dell'invio → **B-3** |
| 1 | 47 · 100 | `al termine, l'appartamento è in regola per essere affittato e pubblicato` | **DA CORREGGERE — bloccante** | Stringa pronta → **B-2** |
| 1 | 47 · 100 | *(assente)* rapporto con la proposta di gestione già consegnata | **DA CORREGGERE — bloccante** | Riga da aggiungere → **B-9** |
| 1 | 56 · 59 | `per accertare che l'immobile possa essere destinato a locazione turistica` | DA CORREGGERE | `…per verificare sulla documentazione che l'immobile possa essere destinato a locazione turistica.` → **R-5** |
| 1 | 63 · 60 | `Richiesta e ottenimento del codice della Regione Lazio` | **DA CORREGGERE — bloccante** | `Richiesta del codice alla Regione Lazio, intestato alla proprietà, e pratica seguita fino all'esito.` → **B-1** |
| 1 | 70 · 61 | `Richiesta e ottenimento del codice della Banca Dati Strutture Ricettive` | **DA CORREGGERE — bloccante** | `Richiesta del codice al Ministero del Turismo, con la pratica seguita fino all'esito: senza il codice, l'immobile non può essere pubblicato su nessun portale.` → **B-1** |
| 1 | 77 · 62 | `Predisposizione e presentazione al SUAR di Roma Capitale, nella forma prevista per la tipologia scelta (SCIA o CIA)` | OK | Formulazione conforme al brief (mai "le facciamo la SCIA"). Tipologia da chiudere col titolare → **R-2** |
| 1 | 84 · 63 | `Alloggiati Web — Polizia di Stato · Apertura della posizione e attivazione delle credenziali` | OK | — |
| 1 | 91 · 64 | `ROSS 1000 — Regione Lazio · Apertura della posizione` | **DA VERIFICARE** | Possibile sovrapposizione con la voce 02 (stessa piattaforma regionale) → **R-3** |
| 1 | 98 · 65 | `Contributo di soggiorno — Roma Capitale · Registrazione della struttura presso il Comune` | OK | Ma va disambiguato con l'esclusione di pagina 2 → **R-1** |
| 1 | 105 · 66 | `Consegna del fascicolo` | OK | — |
| 1 | 114 · 112 | `Importo non soggetto a IVA · costi vivi delle pratiche esclusi` | **DA CORREGGERE — bloccante** | Manca il regime → **B-5** |
| 1 | 116 · 114 | `500,00 €` | OK | Coerente con pagina 2, riga 64 |
| 2 | 24 · 148 | `Pagina 2 di 2` in testata + `2 / 2` nel piede | DA CORREGGERE | Ridondanza → **R-7** |
| 2 | 34 · 120 | `Servizio fotografico, testi dell'annuncio, pubblicazione sui portali e landing page.` | OK | Coerente col perimetro dichiarato dal titolare |
| 2 | 38 · 121 | `…flussi statistici, contributo di soggiorno.` | DA CORREGGERE | `…flussi statistici, dichiarazioni e versamenti del contributo di soggiorno.` → **R-1** |
| 2 | 42 · 122 | `Dotazioni di sicurezza… la fornitura resta alla proprietà.` | **DA CORREGGERE — bloccante** | Manca la dipendenza dai codici → **B-8** |
| 2 | 46 · 123 | `Interventi tecnici o di conformità sull'immobile…` | OK | — |
| 2 | 50 · 124 | `Adempimenti fiscali e dichiarativi, che restano al suo commercialista.` | OK | — |
| 2 | 60 · 140 | `Diritti di segreteria, imposte di bollo ed eventuali oneri comunali…` | **DA CORREGGERE — bloccante** | Manca il tecnico abilitato → **B-7** |
| 2 | 64 · 141 | `Alla conferma del preventivo si sostengono i soli costi delle pratiche. I 500,00 € si pagano a lavoro concluso…` | OK | Corrisponde al dato confermato. Manca modalità/termine → **R-8** |
| 2 | 68 · 142 | `I tempi di rilascio dipendono dagli enti competenti e non sono nella nostra disponibilità…` | OK | La clausola meglio scritta del documento |
| 2 | 72 · 143 | `L'esito dipende dai requisiti dell'immobile. Se dalla verifica preliminare emerge un impedimento…` | **DA CORREGGERE — bloccante** | Non bilancia "ottenimento" → **B-4** |
| 2 | 82-94 · 128-131 | `Cosa ci serve da lei` (4 voci) | **DA VERIFICARE** | Servono SPID/CIE oltre alla delega? Manca la conferma sulle dotazioni → **B-8**, **R-6** |
| 2 | 99-110 · 175-187 | Blocco `Per accettazione del preventivo` | DA CORREGGERE | Nessuna firma del prestatore; recesso da verificare → **R-9**, **R-10** |
| 2 | *(assente)* | Clausola su privacy / trattamento dei dati | **DA CORREGGERE — bloccante** | Riga da aggiungere → **B-6** |
| 2 | 113 · 188 | `Hadrianus Multiservice · hadrianusmultiservice.it` | **DA CORREGGERE — bloccante** | Nessun dato fiscale né contatto → **B-10** |

---

## Bloccanti — dettaglio e stringhe pronte

### B-1 · Pagina 1, righe 63 e 70 — "richiesta e **ottenimento**" è un'obbligazione di risultato

**Perché blocca.** Su un documento che la cliente firma, "ottenimento" non è una sfumatura: promette l'**esito**, non l'attività. I codici non li rilascia Hadrianus, li rilasciano la Regione e il Ministero, e il brief (§1, §3) è esplicito sul fatto che l'assegnazione dipende da requisiti dell'immobile e da autocertificazioni. Se il codice non arriva, il documento firmato dice che era dovuto. È anche il claim che `brief-mercato.md` §"Vietato nel deck" vieta in blocco ("garanzie di qualsiasi tipo"), e che il deck ha rispettato per 16 slide: qui rientra dalla finestra.

Seconda imprecisione nella stessa riga 70: il CIN non è "il codice della Banca Dati Strutture Ricettive". La BDSR è la banca dati; **il codice lo assegna il Ministero del Turismo** (brief §1, CONFERMATO). Nominare il portale al posto dell'ente è sbagliato e in più è l'unico punto del documento che scivola verso l'istruzione operativa.

**Stringhe pronte:**

Riga 63 (voce 02 · CIR):
```
Richiesta del codice alla Regione Lazio, intestato alla proprietà, e pratica seguita fino all'esito.
```

Riga 70 (voce 03 · CIN):
```
Richiesta del codice al Ministero del Turismo, con la pratica seguita fino all'esito: senza il codice, l'immobile non può essere pubblicato su nessun portale.
```

Va corretto **anche** il titolo della sezione se si vuole essere coerenti fino in fondo: oggi "Cosa comprende" elenca attività, e con queste due stringhe lo restano tutte.

---

### B-2 · Pagina 1, riga 47 — "al termine, l'appartamento è in regola per essere affittato e pubblicato"

**Perché blocca.** È una garanzia di risultato **assoluta**, e per di più smentita da pagina 2 dello stesso documento: le dotazioni di sicurezza (condizione per i codici) sono escluse dalla fornitura, gli interventi tecnici sono esclusi, e gli adempimenti che servono per stare in regola mentre si affitta (comunicazione a ogni arrivo, flussi, contributo di soggiorno) sono esclusi. Il documento promette uno stato che, per sua stessa ammissione, non dipende solo da lui. Firmato, è la riga su cui si litiga.

**Stringa pronta (sostituisce l'intero paragrafo):**
```
Oggetto del preventivo è la sola messa in regola documentale dell'immobile: codici identificativi, pratica comunale di avvio e apertura delle posizioni presso gli enti. Con il fascicolo consegnato l'appartamento ha i titoli per essere pubblicato e affittato; gli adempimenti che tornano a ogni ospite e a ogni scadenza restano fuori da questo preventivo.
```
(`la sola messa in regola documentale` resta in `<b>`.)

---

### B-3 · Pagina 1 righe 31, 32, 39 e pagina 2 riga 23 — campi non compilati

`[numero]` (due volte: pagina 1 riga 31 e testata di pagina 2 riga 23, e **devono coincidere**), `[gg/mm/aaaa]` (riga 32), `[Nome e cognome della proprietaria]` (riga 39).

**Perché blocca.** Sono marcatori, esattamente come `[DATO DA VERIFICARE]`: regola non negoziabile di `CLAUDE.md`, nessun contenuto esce con marcatori dentro. Su un preventivo intestato a una cliente reale l'effetto è peggiore che su un post: un documento senza numero, senza data e senza intestatario non è un preventivo, è una bozza — e con "Valido 30 giorni dall'emissione" scritto sopra, senza data la validità non decorre da niente. Già segnalato in `README.md` riga 29 della campagna: qui diventa condizione di invio.

---

### B-4 · Pagina 2, riga 72 — la clausola "Esito delle pratiche" non bilancia l'obbligazione di risultato

**Testo attuale:**
```
L'esito dipende dai requisiti dell'immobile. Se dalla verifica preliminare emerge un impedimento, glielo diciamo prima di procedere e il preventivo si ferma, senza alcun costo di onorario.
```

**Perché non basta.** Copre **un solo scenario**: l'impedimento che emerge *dalla verifica preliminare*, cioè prima di iniziare. Non dice niente su (a) chi rilascia i codici, (b) che cosa succede se l'impedimento emerge **a pratiche avviate** — che è lo scenario realistico, visto che una parte dei requisiti si autocertifica e viene verificata a valle. Letta insieme a "richiesta e **ottenimento**" di pagina 1, la coppia produce il risultato peggiore: pagina 1 promette l'esito, pagina 2 si limita a scusarsi in anticipo per un caso solo. Con la correzione **B-1** montata, questa clausola diventa il punto in cui l'obbligazione è definita di mezzi: va scritta bene.

**Stringa pronta:**
```
I codici e i titoli sono rilasciati dagli enti competenti: l'esito dipende dai requisiti dell'immobile e dalla loro valutazione, non dalla nostra attività. Se un impedimento emerge dalla verifica preliminare, glielo diciamo prima di procedere e il preventivo si ferma senza alcun onorario; se emerge a pratiche avviate, la informiamo subito e concordiamo con lei come proseguire.
```

**Decisione che manca e va presa dal titolare (non inventarla):** se la pratica si blocca **dopo** l'avvio, i 500 € sono dovuti in tutto, in parte, o non sono dovuti? La stringa sopra è onesta e neutra, ma la domanda arriverà. Se il titolare ha una risposta, va scritta qui; se non ce l'ha, va almeno saputa prima di firmare.

---

### B-5 · Pagina 1, riga 114 — "Importo non soggetto a IVA" senza indicazione del regime

**Perché blocca.** "Non soggetta a IVA" è una categoria tecnica precisa, diversa da "esente", "esclusa" e "fuori campo", e in ogni caso va **motivata** indicando il regime fiscale del prestatore. Scritta nuda su un documento commerciale è una dicitura incompleta: se la cliente la gira al suo commercialista — e lo farà, visto che pagina 2 nomina il commercialista — la prima domanda è "in base a cosa?". Nel repository non esiste **nessun** dato sul regime fiscale di Hadrianus: non è un dato che possiamo dedurre, va chiesto.

**Stringa pronta (con il marcatore da chiudere prima dell'invio):**
```
Operazione non soggetta a IVA ai sensi di [regime fiscale del prestatore — da confermare al commercialista] · costi vivi delle pratiche esclusi
```

Da chiedere al commercialista nella stessa occasione, perché oggi il documento non lo dice: **sull'emissione del documento di pagamento è dovuta imposta di bollo, e a carico di chi?** Su un importo di 500 € non è una domanda teorica, ed è esattamente il tipo di piccola somma che, se spunta dopo, incrina un rapporto che è appena cominciato — nello stesso documento in cui scriviamo "nessuna spesa viene sostenuta senza il suo consenso".

---

### B-6 · Pagina 2 — nessuna clausola su privacy e trattamento dei dati personali

**Perché blocca.** Il documento chiede **documento d'identità, codice fiscale, visura catastale, planimetria e una delega a operare a suo nome**, e prevede che Hadrianus apra a suo nome posizioni presso Polizia di Stato, Regione, Comune e Ministero. È una raccolta di dati personali a tutti gli effetti, contestuale alla firma, e il documento non ne fa parola: né a che cosa servono, né a chi vengono comunicati, né per quanto restano a noi. È l'assenza che si nota di più in un documento per il resto scrupoloso.

**Stringa pronta (nuova riga in "Condizioni", etichetta `Trattamento dei dati`) — versione da usare se l'informativa esiste:**
```
I documenti che ci fornisce sono utilizzati esclusivamente per le pratiche indicate in questo preventivo e comunicati ai soli enti competenti. L'informativa completa sul trattamento dei dati personali le viene consegnata insieme alla delega.
```

**Versione da usare se l'informativa non esiste ancora** (non promettere un documento che non c'è — sarebbe un claim non verificato):
```
I documenti che ci fornisce sono utilizzati esclusivamente per le pratiche indicate in questo preventivo, comunicati ai soli enti competenti e conservati per il tempo necessario a concluderle.
```

La prima versione è preferibile, ma **solo** se l'informativa viene preparata prima dell'invio.

---

### B-7 · Pagina 2, riga 60 — manca il compenso dell'eventuale tecnico abilitato

**Perché blocca.** Il dato confermato dal titolare è: *diritti di segreteria, bolli, **eventuale tecnico**, a carico della proprietaria*. Il documento elenca "diritti di segreteria, imposte di bollo ed eventuali oneri comunali" e **salta il tecnico**, che è la voce potenzialmente più pesante delle tre. La riga successiva dice "nessuna spesa viene sostenuta senza il suo consenso": una spesa non prevista nell'elenco, per una cliente che legge quell'elenco come esaustivo, è il modo più veloce per trasformare una clausola di trasparenza nel suo contrario. L'esclusione di pagina 2 riga 46 ("interventi tecnici o di conformità") riguarda le **opere**, non l'onorario del tecnico che asseveri o presenti la pratica: non copre il caso.

**Stringa pronta:**
```
Diritti di segreteria, imposte di bollo, eventuali oneri comunali e il compenso di un tecnico abilitato, se la pratica lo richiede, sono a carico della proprietà. Vengono quantificati e comunicati prima di procedere: nessuna spesa viene sostenuta senza il suo consenso.
```
(`prima` resta in `<b>`.)

---

### B-8 · Pagina 2, riga 42 — dotazioni di sicurezza escluse senza dichiarare che sono condizione per i codici

**Perché blocca.** Il brief §2 è chiaro: in fase di richiesta del CIN si autocertifica il rispetto dei requisiti di sicurezza; **senza requisiti, niente codice** (CONFERMATO). Il documento esclude la fornitura ("le indichiamo, la fornitura resta alla proprietà") ma non dice che, finché non sono installate, la pratica **non parte**. Il risultato è un buco esattamente nel punto che tiene insieme il preventivo: pagina 1 promette i codici (B-1), pagina 2 lascia alla proprietaria — senza dirglielo — la condizione da cui i codici dipendono. È anche l'unico modo per rendere vera la clausola "Tempi" di riga 68: oggi dice "l'avvio è immediato alla ricezione dei documenti", il che non è vero se mancano i rilevatori.

**Stringa pronta (riga 42):**
```
Dotazioni di sicurezza richieste per i codici (rilevatori ed estintore): le indichiamo, la fornitura resta alla proprietà. Devono essere presenti prima che le richieste possano essere presentate.
```

**Quinta voce da aggiungere in "Cosa ci serve da lei"** (dopo riga 94), così la condizione ha un posto anche nell'elenco operativo:
```
Conferma che le dotazioni di sicurezza indicate sono installate.
```

---

### B-9 · Pagina 1 — il preventivo non dice che rapporto ha con la proposta di gestione già consegnata

**Perché blocca.** È il rilievo di coerenza più pesante del lotto. Alla stessa persona abbiamo già consegnato un deck di 16 slide in cui:

- la **messa in regola è la sezione 01 di 07 del servizio** (`slide/Regola.dc.html` riga 25: *"Prima di pubblicare, l'immobile deve esistere per legge. **Questa parte la seguiamo noi.**"*);
- il perimetro economico è *"15%. Sulle prenotazioni che generiamo"* con **`Nessun costo fisso.`** (`slide/Condizioni.dc.html` righe 25-33);
- *"**Fuori dal 15% restano i dispositivi di accesso** — spioncino digitale e apertura del portone — fatturati a parte. Gli eventuali costi vivi delle pratiche glieli indichiamo prima di sostenerli."* (riga 50).

Quel deck le ha detto, nero su crema, che **fuori dal 15% ci sono i dispositivi di accesso e i costi vivi**. Oggi le arriva un documento che chiede **500 € di onorario per la sezione 01**, senza una riga che spieghi perché. Due letture possibili, entrambe pessime se non le preveniamo noi: "mi avevano detto nessun costo fisso" oppure "il 15% era solo l'inizio". È esattamente il punto su cui la figlia — che il brief identifica come il veto, e che quel deck era costruito per non perdere — ha ragione senza sforzo.

Il preventivo è legittimo **se** è la sola messa in regola richiesta separatamente dalla gestione (è il perimetro confermato dal titolare: niente foto, niente annunci, niente gestione). Ma questo va **scritto**, non lasciato all'interpretazione.

**Stringa pronta — da aggiungere come secondo paragrafo di pagina 1, subito sotto l'oggetto (riga 47):**
```
Riguarda la sola messa in regola: non sostituisce e non modifica la proposta di gestione già consegnata, che resta valida se e quando vorrà affidarci anche la gestione dell'immobile.
```

**Decisione che manca e va presa dal titolare:** se in caso di successivo mandato di gestione i 500 € vengono **scomputati** (o non dovuti), va detto qui — è un argomento di vendita forte e gratuito. Se invece restano dovuti in ogni caso, meglio saperlo prima che glielo chieda lei. Non inventare la risposta: oggi non è confermata da nessuna fonte.

---

### B-10 · Pagina 2, riga 113 — nessun dato identificativo e fiscale del prestatore

**Perché blocca.** In calce c'è solo `Hadrianus Multiservice · hadrianusmultiservice.it`. Su un documento che la cliente **firma per accettazione** mancano: denominazione completa, partita IVA e/o codice fiscale, sede, e — cosa che salta agli occhi ancora prima — **un recapito per rispondere**. Non c'è un'email, non c'è un telefono: le stiamo chiedendo di firmare e di mandarci il documento d'identità, e non le stiamo dicendo a chi. Nel repository non esiste nessuno di questi dati: vanno chiesti al titolare, non dedotti.

**Stringa pronta per il piede di pagina 2 (due righe, corpo 10px, colore `#6f695c`):**
```
Hadrianus Multiservice di [denominazione completa] · P. IVA [•] · C.F. [•] · [indirizzo della sede]
[email] · [telefono] · hadrianusmultiservice.it
```

Consigliato anche **sulla pagina 1**, sotto la dicitura `Multiservice · Property management · Roma · Ostia` (riga 20): email e telefono in corpo 10px. Pagina 1 è quella che verrà fotografata e mandata alla figlia: deve reggere da sola.

**Nota di impaginazione:** il piede attuale è su una riga sola e i dati non ci stanno. Va portato a due righe alzando il blocco da `bottom: 40px` a circa `bottom: 34px`, oppure riducendo il `padding-top` da 12 a 8.

---

## Osservazioni (non bloccanti)

**R-1 · Pagina 2 riga 38 — "contributo di soggiorno" sembra incluso e escluso insieme.** Pagina 1 voce 07 include la *registrazione* presso il Comune; pagina 2 elenca "contributo di soggiorno" tra le cose che **non** comprende. Vero entrambi (registrazione dentro, dichiarazioni e versamenti fuori), ma a colpo d'occhio è una contraddizione, e su un documento firmato le contraddizioni apparenti si pagano lo stesso. Stringa pronta:
```
Gestione dell'immobile e adempimenti ricorrenti: comunicazioni a ogni arrivo, flussi statistici, dichiarazioni e versamenti del contributo di soggiorno.
```

**R-2 · Pagina 1 riga 77 — SUAR e SCIA/CIA.** La formulazione è quella giusta e prescritta dal brief (§4): neutra sull'esito, mai "le facciamo la SCIA". Resta però che nel brief **sia la competenza del SUAR sia la distinzione SCIA/CIA sono DA VERIFICARE su fonte istituzionale** (la pagina di Roma Capitale non è mai stata apribile). La riga è dicibile così com'è; la **tipologia** (casa vacanze / alloggio per uso turistico) va chiusa col titolare prima dell'invio, perché da lì dipendono la pratica, i diritti di segreteria e il preventivo dei costi vivi che le promettiamo di quantificare "prima".

**R-3 · Pagina 1 righe 63 e 91 — CIR e ROSS 1000 potrebbero essere la stessa posizione.** Il brief §3 dice che il CIR del Lazio si gestisce su **"Ross1000 Anagrafica Lazio"**, e §7 che ROSS 1000 è il sistema regionale per i flussi. Sono due funzioni dello stesso sistema regionale. Presentarle come due voci su otto è difendibile (sono due adempimenti distinti), ma è il punto in cui un tecnico — o la figlia, che il brief descrive come la persona che "sa usare i portali" — può dire "queste due sono la stessa cosa". Da far confermare al titolare che si tratta di due posizioni distinte. Se non lo sono, fondere in una voce e portare l'elenco a sette:
```
CIR e ROSS 1000 — Regione Lazio
Richiesta del codice regionale e apertura della posizione per la rilevazione dei flussi turistici.
```

**R-4 · Pagina 1 riga 33 — "Valido 30 giorni dall'emissione".** È un default proposto da noi, **mai confermato dal titolare**. Non è un claim rischioso, ma è una condizione contrattuale che vincola noi: 30 giorni su un prezzo che include costi vivi ancora da quantificare va deciso, non ereditato da un template. Da confermare o cambiare prima dell'invio.

**R-5 · Pagina 1 riga 56 — "per accertare".** "Accertare" promette una determinazione definitiva che un controllo di visura e planimetria non può dare (conformità urbanistica, agibilità, abusi non si accertano su una visura) — e stride con l'esclusione di riga 46 di pagina 2, che prevede che dalla verifica possano emergere interventi di conformità. Stringa pronta:
```
Controllo di visura catastale, planimetria e dati dell'unità, per verificare sulla documentazione che l'immobile possa essere destinato a locazione turistica.
```

**R-6 · Pagina 2 righe 82-94 — "Cosa ci serve da lei" potrebbe essere incompleto.** Oggi chiede visura, planimetria, documento e codice fiscale, dati dell'unità, delega. Da far confermare al titolare se per operare a suo nome servano anche **SPID/CIE della proprietaria** (per più di una delle posizioni in elenco l'accesso è personale). Se servono e non sono scritte, il lavoro si ferma il giorno dopo la firma — e la clausola "Tempi" di riga 68 ("l'avvio è immediato alla ricezione dei documenti") diventa falsa senza che nessuno l'abbia voluto.

**R-7 · Pagina 2 riga 24 — numerazione doppia.** La testata dice `Pagina 2 di 2` e il piede dice `2 / 2`. Pagina 1 non ha numerazione in testata. Meglio togliere la ridondanza e usare lo spazio per identificare il foglio sciolto:
```
Bilocale, Ostia Lido Centro
```
(lasciando `Preventivo n. [numero]` sopra e `2 / 2` nel piede).

**R-8 · Pagina 2 riga 64 — modalità e termine di pagamento assenti.** Si dice *quando* (alla consegna del fascicolo) ma non *come* né *entro quanto*. Da decidere col titolare, per esempio: `…si pagano alla consegna del fascicolo, a mezzo bonifico, entro [•] giorni.`

**R-9 · Pagina 2 righe 99-110 — nel blocco di accettazione firma solo lei.** Ci sono "Luogo e data" e "Firma della proprietaria", non c'è uno spazio per la firma di Hadrianus. Su un documento che vale come proposta accettata, la firma del proponente è la norma. Aggiungere una terza colonna o una riga `Per Hadrianus Multiservice` sopra le due esistenti.

**R-10 · Da far verificare al consulente, non da scrivere a intuito.** Il preventivo viene firmato da una persona fisica, verosimilmente a casa sua o a distanza, e prevede che le pratiche partano subito. Se in questo contesto è dovuta un'informativa sul diritto di recesso — e se l'avvio immediato richiede una sua richiesta espressa di iniziare prima del termine — oggi il documento non ne contiene traccia. Non lo affermo come regola applicabile: lo segnalo come la domanda da girare a chi segue Hadrianus sul legale, prima dell'invio.

---

## Nota di impaginazione — le correzioni non stanno nello spazio attuale

Le stringhe di **B-4**, **B-6** e **B-7** allungano il blocco "Condizioni" di circa 3-4 righe. Oggi quel blocco parte da `top: 358px` e arriva a circa 690px, mentre "Cosa ci serve da lei" è ancorato a `top: 712px`: il margine è di una ventina di pixel. Applicando le correzioni senza toccare il layout, pagina 2 si sovrappone.

Interventi possibili, in ordine di preferenza:
1. spostare la clausola **Trattamento dei dati** (B-6) in una riga compatta sopra il blocco di accettazione, invece che dentro "Condizioni";
2. riportare "Cosa ci serve da lei" a `top: 760px` circa e comprimere il blocco di accettazione (`bottom: 96px` → `bottom: 76px`, padding 22 → 18);
3. se non basta, spostare "Cosa ci serve da lei" in fondo a pagina 1 — l'elenco delle voci "Cosa comprende" è già serrato, ma il blocco Totale può salire.

Va verificato sul PNG rigenerato, non a occhio sul codice.

---

## Coerenza col tono Hadrianus

**In linea, con una sola eccezione — ed è uno dei bloccanti.**

Il documento tiene il registro del deck e dei `riferimenti/`: frasi corte, verbi al presente, nessun aggettivo di vendita, il valore mostrato nominando le cose invece che promettendole. Due righe sono proprio il tono del brand nel suo momento migliore:

- *"I tempi di rilascio dipendono dagli enti competenti e non sono nella nostra disponibilità: la teniamo aggiornata a ogni passaggio."* (pagina 2, riga 68) — è lo stesso patto di onestà della slide 15 del deck (*"Non a occhio, e non prima di aver visto le carte"*): si rinuncia a una promessa e ci si guadagna in credibilità.
- *"nessuna spesa viene sostenuta senza il suo consenso"* (pagina 2, riga 60) — stessa famiglia di *"Guadagniamo solo se guadagni tu"*: allineamento, non rassicurazione.

L'eccezione è **"Richiesta e ottenimento"** (B-1). È l'unica formula del documento che suona come l'agenzia qualunque descritta nel brief §Concorrenza — *"zero pensieri / ci occupiamo di tutto"*, la promessa che "dice tutto e non prova niente". Ed è tanto più stonata in un documento che tre righe dopo, a pagina 2, ammette con precisione che l'esito non dipende da noi. Corretta in "pratica seguita fino all'esito", la riga dice **di più** sul livello del servizio, non di meno.

Verifiche di lessico e di forma, una per una:

| Controllo | Esito |
|---|---|
| "hotel-style" | **Mai.** Il termine non compare (né compare "standard alberghiero": qui non serve) |
| "guadagni solo se guadagni tu" | La formula non compare affatto — corretto, non è il documento giusto |
| Strutture nominate, indirizzi, case study | **Nessuno** |
| Emoji | **Nessuna** |
| Blu navy | **Assente.** Crema `#FAF6EC`, oro `#C8A24B`, inchiostro `#26241F` |
| Registro al lei | **Coerente su entrambe le pagine** (`intestato a lei`, `la teniamo aggiornata`, `il suo commercialista`, `glielo diciamo`, `a suo nome`, `Cosa ci serve da lei`). Nessun "tu" |
| Allarmismo | **Nessuno.** L'unica riga di conseguenza (`senza il codice, l'immobile non può essere pubblicato`) è un fatto CONFERMATO dal brief, detto senza enfasi |
| Articoli di legge, decreti, sentenze | **Nessuno** |
| Importi di sanzione, pena, "fuorilegge" | **Nessuno** |
| Istruzioni operative (come si fa una pratica, link, credenziali, ordine) | **Nessuna.** Unico residuo: `Banca Dati Strutture Ricettive` a riga 70, che la correzione B-1 elimina |
| Numeri presenti nel documento | `500,00 €` (×2, coerenti) · `30 giorni` (DA VERIFICARE, R-4) · numerazione 01-08 e 1/2-2/2. **Nessun'altra cifra**: nessun importo di contributo di soggiorno, nessun diritto di segreteria, nessuna aliquota, nessuna tempistica di rilascio promessa. Corretto: sono tutti dati che il brief marca DA VERIFICARE |
| Refusi | **Nessuno.** Apostrofi tipografici `’` coerenti ovunque, nessun doppio spazio |
| Sciatterie di lingua | Una sola: `senza alcun costo di onorario` (pagina 2, riga 72) → `senza alcun onorario`, già dentro la stringa B-4 |
| Marchi di terzi | **Nessuna foto nel documento.** Unico elemento grafico: il logo Hadrianus (`hadrianus-tempio-220.webp`, presente in cartella, riferimento corretto) |
| Coerenza pagina 1 ↔ pagina 2 | Importo coerente · perimetro coerente · numerazione coerente (1/2, 2/2) · `[numero]` da far coincidere alla compilazione |

---

## Verdetto

**Non inviabile alla cliente nello stato attuale.**

Il documento è ben costruito e, sul perimetro, dice la verità: il problema non è quello che promette in più, è che **promette l'esito di pratiche che non rilascia lui** (B-1, B-2, B-4) e che **arriva dopo un deck che diceva "nessun costo fisso"** senza spiegare che rapporto abbia con quello (B-9). Il resto sono lacune di documento commerciale: chi lo emette (B-10), con che regime (B-5), con quale trattamento dei dati (B-6), con quali costi davvero a carico di chi (B-7, B-8).

### Condizioni per l'invio

1. **Montare le stringhe di B-1, B-2, B-4, B-7, B-8, B-9** — sono pronte sopra e non richiedono nessuna decisione esterna. Correggere **in `build-preventivo.mjs`**, non solo negli `.dc.html`.
2. **Ottenere dal titolare / dal commercialista**, prima di montare: regime fiscale per la dicitura IVA e trattamento del bollo (B-5) · dati identificativi, fiscali e recapiti (B-10) · esistenza dell'informativa privacy per scegliere la variante di B-6 (se non esiste, prepararla o usare la variante breve) · sorte dei 500 € se la pratica si blocca dopo l'avvio (B-4) e in caso di successivo mandato di gestione (B-9) · conferma o modifica della validità a 30 giorni (R-4) · tipologia casa vacanze / alloggio per uso turistico (R-2) · se CIR e ROSS 1000 sono due posizioni distinte (R-3) · se serve SPID/CIE oltre alla delega (R-6).
3. **Sistemare l'impaginazione di pagina 2** secondo la nota sopra, e verificare sul PNG rigenerato che nulla si sovrapponga.
4. **Compilare i quattro campi** — numero (×2, coincidenti), data, nome e cognome della proprietaria (B-3). Ultimo passaggio, dopo tutto il resto.
5. **Rigenerare gli export**: `node preventivo/build-preventivo.mjs` poi `node preventivo/render-preventivo.mjs` — altrimenti PNG, PDF (`Hadrianus-Preventivo-Messa-in-Regola.pdf`) e canvas pubblicato (`preventivo-messa-in-regola.html`) restano quelli sbagliati, e il PDF è il file che la cliente si tiene.

Fatti 1, 2, 3 e 4, il preventivo è inviabile. I rilievi R-1, R-5, R-7, R-8, R-9 sono consigliati nello stesso giro di correzioni: costano cinque minuti e tolgono cinque appigli. R-10 è una domanda da girare al consulente legale, indipendente dalle altre.
