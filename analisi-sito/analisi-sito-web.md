# Analisi del sito hadrianusmultiservice.it

**Data:** 11 settembre 2026
**Fonte dell'analisi:** 7 screenshot integrali mobile forniti dal titolare (Home, Gestione Case Vacanza, Pulizie/Templum Purum, Appartamenti, Chi Siamo, Contatti, menu di navigazione).
**Metodo:** lettura diretta delle schermate. Il sito **non è raggiungibile** dall'ambiente Claude Code on the web (proxy di rete con allowlist: `EGRESS_BLOCKED` sul dominio), quindi non è stato possibile verificare codice sorgente, meta tag, velocità, indicizzazione e comportamento dei form.

## Attendibilità di questo documento

Tre livelli, sempre distinti nel testo:

| Livello | Significato |
|---|---|
| **Verificato** | Letto direttamente negli screenshot, testo leggibile senza ambiguità. |
| `[da rileggere]` | Presente nello screenshot ma a risoluzione troppo bassa per trascriverlo con certezza. Va riletto sul sito prima di agire. |
| `[DA VERIFICARE]` | Non deducibile dagli screenshot (codice, performance, comportamento dei form, dati aziendali). Richiede accesso al sito o al titolare. |

**Nota importante.** Un'analisi precedente prodotta da un altro strumento è stata scartata: dichiarava esplicitamente di *dedurre* font, palette e stack tecnologico, e le deduzioni si sono rivelate sbagliate su entrambi i punti verificabili — indicava "Blu Navy profondo" (`slate-900`) come colore del brand, quando il sito non contiene blu, e ipotizzava font sans-serif geometrici sui titoli, quando i titoli sono in serif. Il codice React allegato a quell'analisi **non va usato**: introdurrebbe il blu navy, vietato dalla regola fissa n. 2 di `CLAUDE.md`.

---

## 1. Architettura e pubblici

### Struttura reale

```
Home
├── Gestione (Case Vacanza)        → proprietari immobiliari
├── Pulizie (Templum Purum)        → property manager, host, B&B, locali
├── Appartamenti                   → ospiti che prenotano
├── Chi Siamo                      → brand, storytelling, doppia anima
└── Contatti                       → smistamento a due percorsi
```

Nel footer compare anche **"Guide e Risorse"**, che **non esiste nel menu principale** (verificato sul menu mobile: Home, Gestione, Pulizie, Appartamenti, Chi Siamo, Contatti). Pagina orfana o accessibile solo dal footer. `[DA VERIFICARE: la pagina esiste e ha contenuto?]`

### Il nodo strategico: tre pubblici, un solo sito

Il sito serve **tre** pubblici con bisogni opposti, non due:

1. **Proprietari** — vogliono rendita senza lavoro. È il target primario di tutte le campagne social del progetto.
2. **Property manager / host** — vogliono un fornitore operativo. B2B, divisione Templum Purum.
3. **Ospiti** — vogliono prenotare una casa. Non comprano nulla di ciò che il sito vende ai primi due.

**Cosa funziona.** Lo smistamento 1 vs 2 è gestito bene e in tre punti diversi: la Home ha la coppia di box "Sei un proprietario?" / "Sei un property manager?", Chi Siamo ha la sezione "A Chi Ci Rivolgiamo" con le stesse due card, e Contatti si apre con "Quale Servizio Ti Interessa?" separando i due percorsi prima ancora dei recapiti. È una scelta corretta e coerente: il lead commerciale non si mescola mai.

**Cosa non funziona.** Il terzo pubblico non è separato allo stesso modo:

- **"Appartamenti" sta nel menu principale**, allo stesso livello dei due servizi. Un proprietario che arriva dai social trova nel menu una vetrina di case da prenotare — che per lui è rumore.
- Peggio: la pagina **Gestione**, cioè la pagina di vendita ai proprietari, contiene una sezione **"I Nostri Appartamenti"** con le foto degli immobili e il rimando alla pagina di prenotazione. Nel mezzo dell'argomentazione di vendita al proprietario, il sito cambia interlocutore.

**Raccomandazione.** Portare "Appartamenti" fuori dal menu principale (o in fondo), e sostituire la sezione "I Nostri Appartamenti" sulla pagina Gestione con la prova che serve *a un proprietario*: cosa è successo agli immobili in gestione, non quanto sono belli da prenotare.

---

## 2. Il copy, pagina per pagina, contro `framework-vendita`

Il metodo di riferimento è `Hook → Problema → Agitazione → Soluzione → Prova → Offerta → Urgenza → CTA`, con il principio guida: *si vende un risultato, non un prodotto*, e *le prime righe parlano del lettore, non dell'azienda*.

### Home — l'apertura più debole del sito

Hero verificato:

> **Hadrianus Multiservice**
> Gestione Case Vacanze e Pulizie Professionali a Roma

Questa è una **targa aziendale, non un gancio**. Viola il primo principio del framework: apre presentando l'azienda e la categoria merceologica. Non nomina un problema, non si rivolge a "tu", non dice a chi parla, e **non ha alcuna CTA sopra la piega** — il primo bottone compare solo diverse schermate più in basso.

Subito sotto, il secondo blocco ripete il nome — "Hadrianus Multiservice" come titolo di sezione — seguito da una descrizione ancora di servizio ("Gestione completa di case vacanza a Roma per unica tecnologia, procedure strutturate e cura dei dettagli...") `[da rileggere]`. Due schermate spese per dire chi siamo, prima di dire al lettore qualcosa che lo riguardi.

**Il resto della Home invece funziona:** le quattro card (Gestione Completa, Processi Strutturati, Ottimizzazione Tariffe, Reportistica Chiara) sono chiare, e i box "Sei un proprietario?" / "Sei un property manager?" sono il primo momento in cui il sito parla davvero al lettore. Il problema è che arrivano tardi.

**Intervento a più alto ritorno di tutto il sito:** riscrivere l'hero della Home come gancio sul problema del proprietario, con una CTA sopra la piega.

### Gestione Case Vacanza — buona struttura, promessa male tarata

Hero verificato:

> **Gestione Case Vacanza a Roma**
> Metodo, controllo e rendimento per immobili di valore.
> `[SCOPRI DI PIÙ]`

Molto meglio della Home: c'è un beneficio, c'è una CTA. Due riserve:

1. **"immobili di valore"** restringe il pubblico. Il target descritto in `brand-identity.md` è il proprietario del bilocale a Ostia, della casa sfitta ereditata, di chi ha paura della morosità. "Immobili di valore" gli comunica *questo non è per te*. È un posizionamento premium che contraddice il target reale delle campagne.
2. È ancora una promessa sul **prodotto** ("metodo, controllo, rendimento"), non sul **risultato per il lettore**.

**La sezione più forte del sito è qui: "Manutenzioni Interne".** Claim verificato: *"Prevenzione, non emergenza"*, con la checklist dei "Controlli ad Ogni Check-out" — verifica elettrodomestici, controllo rubinetteria, ispezione serrature, verifica connessione Wi-Fi, stato pareti e pavimenti, verifica dotazioni `[da rileggere: l'elenco esatto delle 6 voci]`.

Funziona perché è **l'unico punto del sito in cui una caratteristica è concreta e verificabile invece che aggettivale**. Risponde alla paura numero uno del proprietario ("e se me la rovinano?") mostrando un processo, non una rassicurazione. È anche il miglior materiale per una campagna che il sito contenga (vedi §7).

Seguono il **Modello di Gestione in 8 step** (Prenotazioni, Check-in Smart, Assistenza, Manutenzioni, Controllo, Pricing, Reportistica, Gestione) — chiaro e ben impaginato — e la sezione consulenza su fondo verde salvia, con sopralluogo gratuito, analisi di mercato, **stima del rendimento potenziale** `[da rileggere]` e CTA "RICHIEDI CONSULENZA".

Quella **stima del rendimento è l'asset di conversione più importante del sito, ed è sepolta in fondo a una pagina interna.** Nelle campagne social è l'offerta ricorrente ("Scrivi CALCOLO in DM per una simulazione gratuita" — `riferimenti/riferimento-1.md`). Sul sito non è mai promossa, non ha una pagina propria, non compare nella Home.

### Pulizie / Templum Purum — il copy migliore del sito

Verificato:

> Se gestisci appartamenti turistici, sai che le pulizie e il turnover sono l'origine di metà dei problemi operativi. `[da rileggere: formulazione esatta]`
> **Hadrianus risolve tutto alla radice:**

Questa è l'unica pagina che **apre dal problema del lettore**, e non a caso è la più persuasiva. Segue una checklist di otto punti operativi e concreti (qualità verificabile, controllo multilivello, biancheria inclusa, nessun extra per festivi/urgenze/prodotti, report fotografico, manutenzione rapida inclusa, procedure testate, pulizia profonda a ogni check-out), poi la chiusura:

> Il nostro obiettivo è permetterti di fare una sola cosa: far crescere il tuo business senza preoccuparti della parte operativa. Se vuoi un partner stabile e professionale, scrivici ora.
> `[CONTATTACI ORA]`

Problema/soluzione/offerta/CTA in sequenza pulita. **Paradosso da correggere: la pagina B2B secondaria vende meglio della pagina principale rivolta al target primario.** La pagina Gestione va portata a questo livello.

### Appartamenti — l'unica pagina con prova sociale vera

Pagina rivolta agli ospiti. Scheda "Rome Smart Sea" (Lido di Ostia, Via delle Randi `[da rileggere]`) con descrizione dettagliata, chip di servizi (300 m dal mare, metro Stella Polare, fibra fino a 2 Gbps, Smart TV streaming inclusi, ascensore, coppie & famiglie), mappa Google, bottone "PRENOTA" verso il motore esterno.

Contiene **"5.0 — Amato dagli ospiti"** e **quattro recensioni verbatim** di ospiti con nome puntato e data (A.L., L., K., S. — `[da rileggere: iniziali e date esatte]`). Più il widget Google **5.0 / 12 recensioni** presente nel footer di ogni pagina.

**Questa è l'unica prova sociale reale del sito, e sta sulla pagina che parla a chi non deve comprare la gestione.** Il proprietario non la vede mai nel suo percorso.

### Chi Siamo — la pagina di marca meglio scritta, commercialmente inerte

Hero su fondo oro/sabbia:

> **Costruire Valore, Custodire Bellezza**
> *"Costruire è facile. Mantenere l'eccellenza nel tempo è la vera conquista."*

Poi "La Nostra Doppia Anima" (Anima Strategica per i proprietari / Anima Operativa per property manager e host), la sezione "A Chi Ci Rivolgiamo" con le due card, e "La Nostra Storia":

> L'Imperatore Adriano è il nostro modello. Non era un semplice condottiero, ma un "Architetto del Mondo": colui che non si limitava a conquistare, ma consolidava e curava ogni provincia con rigore, bellezza e visione. `[da rileggere: trascrizione parziale]`

Due frasi verificate che valgono come materiale di campagna: **"Gestire una casa vacanze non è un hobby, è business"** e **"Non siamo concorrenti, siamo alleati"** (rivolta ai property manager). La seconda è una delle migliori righe dell'intero sito.

Difetti:

- Il testo dell'Anima Strategica **ripete la stessa frase due volte** nello stesso blocco ("Gestire una casa vacanze non è un hobby, è business" compare all'inizio e di nuovo poche righe dopo) `[da rileggere — confermare sul sito]`.
- La pagina **non ha CTA proprie oltre ai due "Scopri il Servizio"**: chiude sul racconto storico, senza chiedere niente.
- Claim personali non verificabili dal lettore: "background direzionale in grandi realtà corporate", "esperienza operativa decennale sul campo" `[DA VERIFICARE con il titolare: sono sostenibili se qualcuno chiede dettagli?]`

### Contatti — smistamento corretto, esecuzione da sistemare

> **Quale Servizio Ti Interessa?**
> Scegli il percorso più adatto alle tue esigenze e contattaci per una consulenza personalizzata

Due card (Gestione Case Vacanza / Per proprietari — Pulizie Professionali / Per Property Manager), ciascuna con tre bullet e **due bottoni**: "Scopri il Servizio" + "Richiedi Consulenza" (o "Richiedi Preventivo").

**Due CTA per card violano la regola "una sola azione chiara".** Su una pagina Contatti, "Scopri il Servizio" rimanda indietro nel funnel proprio quando il visitatore era pronto a convertire. Va tenuto un solo bottone: quello che raccoglie il contatto.

Recapiti verificati: **+39 3517305472**, **info@hadrianusmultiservice.it**, zona **Roma e Litorale**. Nota: il numero è scritto **senza spazi** qui e **con spazi** ("+39 351 7305472") nel footer — uniformare.

`[DA VERIFICARE: esiste un vero form con campi, o i bottoni aprono solo mail/WhatsApp? Negli screenshot non si vedono campi compilabili, ma il testo della pagina Pulizie dice "Compila il form".]`

---

## 3. I due problemi commerciali più gravi

### 3.1 Il modello economico non esiste sul sito

**In sette pagine non compaiono mai né il 15% né "Guadagniamo solo se guadagni tu".**

È il problema più grosso emerso dall'analisi, per tre ragioni:

1. È **l'unica leva realmente differenziante** del brand. Tutto il resto (gestione completa, check-in smart, pricing dinamico, reportistica) lo dichiara identico qualunque concorrente romano.
2. È **la chiusura ricorrente di ogni campagna social** del progetto, registrata in `campagne/INDEX.md` come leva sempre valida. Il funnel porta traffico a un sito che non conferma la promessa su cui quel traffico si è mosso.
3. È **la risposta all'obiezione che blocca la conversione**: "quanto mi costa?". Il sito non la nomina mai, quindi il visitatore deve chiedere — e chiedere è attrito.

**Azione:** portare sul sito il modello economico completo così come è già consolidato nelle campagne — 15% sul fatturato generato, nessun costo fisso, nessun deposito cauzionale, pagamento il 10 di ogni mese — con la formula esatta **"Guadagniamo solo se guadagni tu"** (mai "guadagni solo se guadagni tu", cfr. `lessico-brand.md`). Posizione: sezione dedicata sulla pagina Gestione, più un richiamo nella Home.
`[DA VERIFICARE prima di pubblicare: "nessun costo fisso" e "nessun deposito" sono ancora aperti in `_handover` e in due checklist di compliance — vanno chiusi col titolare.]`

### 3.2 Il proprietario viene mandato all'account delle pulizie

Sulla pagina Contatti, sezione "Seguici su Instagram", testo verificato:

> Scopri i nostri lavori e le nostre case vacanza su **@templum.purum**

E nella sezione "Rimani Connesso" i due bottoni social sono **Instagram → @templum.purum** e **Facebook → Hadrianus Multiservice**.

Quindi: l'unico Instagram linkato dal sito è quello della **divisione pulizie B2B**, e gli viene attribuito anche il contenuto "case vacanza". Un proprietario che clicca finisce sull'account sbagliato. Tutte le campagne Instagram prodotte in questo progetto sono di acquisizione proprietari: **non hanno una destinazione coerente**.

**Azione:** decidere l'architettura degli account (un handle Hadrianus per i proprietari + @templum.purum per il B2B, oppure un handle unico) e allineare il sito. È una decisione da prendere prima di pubblicare altre campagne Instagram.

---

## 4. Compliance dei claim

Applicando le regole non negoziabili di `CLAUDE.md` e `lessico-brand.md`.

| # | Claim (verificato negli screenshot) | Dove | Gravità | Problema e azione |
|---|---|---|---|---|
| 1 | *"Trasformiamo la tua casa in una **fonte di guadagno sicuro**"* | Contatti, Chi Siamo | 🔴 **Grave** | È una **promessa di rendimento garantito**, esplicitamente vietata (`lessico-brand.md`: rendimento "garantito" → usare "una simulazione gratuita", "quanto potrebbe rendere"). Rischio di pubblicità ingannevole. **Riscrivere subito**, es. *"Trasformiamo la tua casa in una rendita, con una stima di rendimento prima di firmare"*. |
| 2 | Assenza di 15% e "Guadagniamo solo se guadagni tu" | Tutto il sito | 🔴 **Grave** | Vedi §3.1. Non è un claim scorretto: è l'omissione della sola prova di allineamento che il brand possiede. |
| 3 | *"Standard alberghiero **4 stelle**"* | Contatti | 🟡 Medio | "Standard alberghiero" è il termine corretto (✅ il sito non usa mai "hotel-style"). L'aggiunta di **"4 stelle"** è però una classificazione specifica e opinabile. `[DA VERIFICARE]` o rimuovere la stella. |
| 4 | *"procedure chiare, digitali e già testate su **centinaia di check-out**"* | Pulizie | 🟡 Medio | Claim numerico. `[DA VERIFICARE: il numero regge?]` Se non documentabile, riformulare senza la quantità. |
| 5 | *"Trasparenza Assoluta"*, *"Disponibilità Totale"*, *"Trasparenza Totale"*, *"Zero Pensieri"* | Pulizie, Gestione | 🟡 Medio | Assoluti non dimostrabili. Ironia: la pagina che promette "trasparenza assoluta" è la stessa che non pubblica il prezzo. Sostituire ciascuno con il fatto che lo prova (es. "Report fotografico a ogni intervento" al posto di "Trasparenza Assoluta"). |
| 6 | *"Nessun extra per festivi, urgenze o prodotti"* · *"Biancheria professionale inclusa fino a 2 ospiti"* | Pulizie | 🟡 Medio | Claim commerciali precisi e vincolanti. Ottimi se veri. `[DA VERIFICARE col titolare — sono impegni contrattuali.]` |
| 7 | *"Servizio attivo 7 giorni su 7"*, *"reperibilità garantita"*, assistenza H24 | Pulizie, Gestione | 🟡 Medio | "Garantita" e "H24" sono impegni operativi. `[DA VERIFICARE: sono sostenibili in agosto e a Natale?]` |
| 8 | *"protocolli da Superhost"* | Chi Siamo, Pulizie | 🟡 Medio | Già aperto in `campagne/facebook-recensioni-superhost/`: il badge Superhost va confermato ancora attivo. |
| 9 | *"massimizzare **costantemente** i profitti"* `[da rileggere]` | Gestione, Home | 🟡 Medio | "Costantemente" trasforma un'attività in una promessa di risultato continuo. Togliere l'avverbio. |
| 10 | **"Rome Smart Sea"** nominata con foto, indirizzo e recensioni | Appartamenti | 🟢 OK **con vincolo** | Sulla pagina di **prenotazione** è legittimo e necessario: lì si vende il soggiorno agli ospiti. Il divieto di `lessico-brand.md` riguarda l'uso come **prova nei contenuti di acquisizione proprietari**. ⚠️ Il vincolo va però presidiato: oggi un proprietario può arrivarci in due clic dal menu e dalla pagina Gestione. |
| 11 | *"Smart TV con **Netflix**, **Disney+** e **DAZN** inclusi"* | Appartamenti | 🟡 Medio | Marchi di terzi citati come dotazione. Su una scheda alloggio è prassi comune, ma `[DA VERIFICARE: i termini di servizio di quegli abbonamenti consentono l'uso da parte degli ospiti?]` Rischio contrattuale, non di brand. |
| 12 | Recensioni Google **5.0 / 12** e recensioni ospiti verbatim | Footer, Appartamenti | ✅ **Prova reale** | L'asset più sotto-utilizzato del sito. Vedi §7. |
| 13 | P.IVA / ragione sociale | Footer | 🔴 **Da verificare subito** | Negli screenshot il footer mostra copyright, Privacy Policy e Cookie Policy (✅), ma **nessuna partita IVA visibile**. Per un sito aziendale italiano è un obbligo di legge. `[DA VERIFICARE: presente altrove?]` |

---

## 5. Errori concreti e bug

Ordinati per impatto sulla credibilità.

| # | Problema | Dove | Perché conta |
|---|---|---|---|
| 1 | **Due embed Instagram su tre non caricano** — mostrano il messaggio *"È possibile che il link a questa foto o a questo video sia rotto o che il post sia stato rimosso. Accedi a Instagram"* | Contatti | Due riquadri d'errore a tutta larghezza su una pagina di conversione. È il danno di credibilità più visibile del sito. Sostituire con un link semplice al profilo o rigenerare gli embed. |
| 2 | **Logo quasi invisibile nel menu mobile** — il lockup "HADRIANUS MULTISERVICE" è grigio scuro su fondo nero, praticamente illeggibile | Menu (tutte le pagine) | Il marchio sparisce nel momento in cui l'utente naviga. Serve la variante chiara del logo. Coincide con la variante trasparente/chiara già segnalata come mancante in `brand-assets/README.md`. |
| 3 | **Didascalie di sviluppo lasciate visibili** — sotto le due immagini della Doppia Anima si leggono stringhe tipo *"Mockup all'Anima Element \| Gestione"* e *"Mockup Templum Purum — L'Anima Operativa per il Property M…"* `[da rileggere]` | Chi Siamo | Sembrano segnaposto di lavorazione rimasti in produzione. Da rimuovere o sostituire con didascalie reali. |
| 4 | **Riquadro nero vuoto** con l'etichetta *"Eccellenza Visibile"* | Pulizie | Immagine o video che non carica. Da riparare o togliere. |
| 5 | **Testo ripetuto** nel blocco Anima Strategica `[da rileggere]` | Chi Siamo | Errore di redazione su una pagina di marca. |
| 6 | **"Guide e Risorse" nel footer ma non nel menu** | Globale | Pagina orfana, o voce morta nel footer. |
| 7 | **Numero di telefono in due formati** (`+39 3517305472` / `+39 351 7305472`) | Contatti vs footer | Dettaglio, ma è il dato che il cliente copia. |
| 8 | **Icone social a colori nativi** (gradiente Instagram, blu Facebook, verde WhatsApp) sul footer scuro | Globale | Introducono blu acceso e verde in una palette che non li prevede. Renderle monocromatiche oro `#C8A24B`. |
| 9 | **Bottone WhatsApp flottante** sovrapposto al contenuto in fondo alla pagina | Globale | `[DA VERIFICARE su dispositivo reale: copre link o testo del footer?]` |

---

## 6. Design: cosa mostrano davvero gli screenshot

### Palette reale (osservata, non dedotta)

| Ruolo osservato | Dove |
|---|---|
| **Bruno/fumè caldo molto scuro** | Hero, sezioni scure, footer, menu |
| **Oro bronzeo desaturato** | Bottoni, titoli accento, bordi, logo |
| **Bianco / sabbia chiarissimo** | Sezioni chiare, card |
| **Verde salvia** | Sezione "Richiedi una Consulenza" (pagina Gestione) |
| **Oro/sabbia pieno** | Hero di Chi Siamo, banda "Richiedi Informazioni" (Pulizie) |

**Nessun blu.** La regola fissa n. 2 del progetto è rispettata dal sito.

### I due disallineamenti col design system delle campagne

1. **Tipografia.** I titoli del sito sono in **serif** (classico, alto contrasto, coerente con l'immaginario imperiale). Il design system delle grafiche social prescrive **Archivo** (sans, 600-900) per i titoli e **Manrope** per il corpo. Oggi sito e social hanno **due identità tipografiche diverse**. Va presa una decisione: o il serif entra nel design system per i titoli, o il sito adotta Archivo. Il serif è più distintivo e più coerente con "Hadrianus" — **la mia raccomandazione è portare il serif nel design system**, non il contrario.
2. **Tonalità dell'oro.** L'oro del sito appare più **bronzeo e desaturato** dell'oro brand `#C8A24B` codificato in `design-system.md`. Da campionare con precisione dal sito e allineare in una sola direzione. `[DA VERIFICARE: valore hex esatto — non ricavabile da uno screenshot compresso.]`
3. **Il verde salvia** non esiste nel design system. O viene aggiunto come colore secondario documentato, o va sostituito.

### Cosa il design fa bene

- Il **busto/tempio di Adriano** è usato con costanza e in modo riconoscibile: è un marchio forte e il sito lo sfrutta.
- L'**alternanza scuro/chiaro** tra le sezioni dà ritmo e rende leggibile una pagina lunga.
- Le **foto reali** (interni, corridoio, balcone, prodotti) sono coerenti di tono e non sembrano stock generico.
- Il **widget recensioni Google in ogni footer** è una scelta giusta.

---

## 7. Cosa il sito regala alle prossime campagne

Materiale reale trovato sul sito e **non ancora usato** in nessuna campagna dell'indice:

1. **La checklist di manutenzione a ogni check-out** (elettrodomestici, rubinetteria, serrature, Wi-Fi, pareti e pavimenti, dotazioni) con il claim *"Prevenzione, non emergenza"*. `campagne/INDEX.md` registra l'angolo "la paura dei danni" risolto sulla *frequenza* del controllo, ma **non la checklist operativa**. È più concreta, più dimostrativa e più difficile da copiare per un concorrente. **È il miglior angolo disponibile per la prossima campagna proprietari.**
2. **"Non siamo concorrenti, siamo alleati"** — l'angolo B2B verso property manager e host. `campagne/INDEX.md` elenca esplicitamente la divisione pulizie B2B tra gli angoli **non ancora esplorati**. La frase è già scritta, è già del cliente, ed è ottima.
3. **"Costruire Valore, Custodire Bellezza"** e **l'Imperatore come "Architetto del Mondo"** — storytelling di marca già formulato, mai comparso nei social. Utile per un contenuto di brand, non di conversione diretta.
4. **Le recensioni Google (5.0 su 12) e le recensioni ospiti verbatim.** `campagne/facebook-recensioni-superhost/` ha già lavorato sulle recensioni Airbnb; queste sono Google, sono pubbliche, sono verificabili da chiunque e **oggi le vede solo chi visita la pagina di prenotazione**.
5. **"Gestire una casa vacanze non è un hobby, è business"** — una riga secca, già del cliente, adatta a un reel.

---

## 8. Piano d'intervento, in ordine

### P0 — Legale e compliance (prima di qualunque altra cosa)

1. Riscrivere **"fonte di guadagno sicuro"** su Contatti e Chi Siamo. È l'unico claim del sito con un rischio reale.
2. Verificare la presenza della **P.IVA** nel footer; se manca, aggiungerla.
3. Chiudere col titolare i claim `[DA VERIFICARE]` della tabella §4: "centinaia di check-out", "4 stelle", "nessun extra", "biancheria inclusa fino a 2 ospiti", "reperibilità garantita", Superhost attivo.

### P1 — Conversione (il ritorno più alto)

4. **Pubblicare il modello economico** — 15%, "Guadagniamo solo se guadagni tu", nessun costo fisso — su Gestione e in Home. *(Subordinato alla chiusura dei punti aperti su costi e deposito.)*
5. **Riscrivere l'hero della Home**: gancio sul problema del proprietario + una CTA sopra la piega, al posto della targa aziendale.
6. **Promuovere la stima di rendimento gratuita** a offerta principale: CTA a bassa frizione, coerente con il "Scrivi CALCOLO" già usato nei social, invece della sola "Richiedi una Consulenza" (che è ad alto attrito per traffico freddo).
7. **Portare la prova sociale sul percorso proprietario**: recensioni Google e risultati di gestione sulla pagina Gestione, non solo sulla pagina di prenotazione.
8. **Una sola CTA per card** sulla pagina Contatti.
9. **Aggiungere una sezione obiezioni/FAQ** sulla pagina Gestione: il materiale è già pronto in `campagne/instagram-fiducia-proprietari/`.

### P2 — Bug (veloci, alto impatto sulla credibilità)

10. Riparare o rimuovere i **due embed Instagram rotti**.
11. **Logo chiaro nel menu mobile**.
12. Rimuovere le **didascalie segnaposto** su Chi Siamo e il **riquadro vuoto** su Pulizie.
13. Correggere la **ripetizione di testo** su Chi Siamo e uniformare il **numero di telefono**.

### P3 — Coerenza di sistema

14. **Decidere l'architettura degli account social** e correggere i link (oggi il proprietario finisce su @templum.purum).
15. **Riconciliare tipografia e oro** tra sito e `design-system.md` — con la raccomandazione di portare il serif nel design system.
16. Icone social **monocromatiche oro** nel footer.
17. Spostare **"Appartamenti"** fuori dal menu principale e togliere la sezione appartamenti dalla pagina Gestione.
18. Decidere il destino di **"Guide e Risorse"**.

---

## 9. Verifiche che richiedono accesso al sito

Non deducibili dagli screenshot. Da fare appena il dominio è raggiungibile (allowlist dell'ambiente) o da postazione locale:

- **Indicizzazione**: cercare `site:hadrianusmultiservice.it` su Google. Se il sito è una SPA con rendering lato client, il contenuto potrebbe non essere indicizzato. Segnale debole ma convergente: nessuna pagina del sito è emersa nelle ricerche web fatte durante questa analisi.
- **Meta tag**: `title` e `meta description` univoci per pagina, un solo `H1` per pagina.
- **Performance mobile** e Core Web Vitals (le pagine sono molto lunghe e ricche di immagini).
- **Funzionamento reale dei form** e dove arrivano le richieste.
- **Google Business Profile**: per un'attività locale Roma/Ostia è probabilmente il canale di acquisizione più sottovalutato. Verificare che esista, sia completo e colleghi il sito.
- **Valore hex esatto** dell'oro e del verde salvia, per allineare `design-system.md`.
