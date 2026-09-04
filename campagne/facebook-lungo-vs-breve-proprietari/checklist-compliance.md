# Checklist compliance — Facebook: affitto lungo vs gestione totale in affitto breve

**Controllo sulla VERSIONE 2** (copy e grafiche rifatti il 4 settembre 2026 su direttive del titolare, dopo la bocciatura della v1).
File esaminati: `copy.md` (v2), `grafiche/Main.dc.html` (1080×1920), `grafiche/Numeri.dc.html` (1080×1080), `grafiche/Offerta.dc.html` (1080×1080), `grafiche/canvas.json`, `grafiche/post-facebook-lungo-vs-breve.html` (canvas pubblicato), `grafiche/immobile-standard.jpg`, `direzione-artistica.md`, `brief-mercato.md`, `campagne/INDEX.md`.
Data controllo: 4 settembre 2026. Sostituisce l'esito sulla v1 (in fondo, § Stato dei bloccanti v1).

## Esito

**DA CORREGGERE**

La v2 è più pulita della v1 su quasi tutto: il gancio fiscale è sparito davvero, le formule assolute sui costi non ci sono in nessun materiale pubblicabile, le due frasi obbligate ("Le utenze restano tue." / "Media, non una promessa: ogni casa fa storia a sé.") sono al loro posto anche in grafica, la colonna sinistra dice "tasse e spese", la promessa sui cinque anni è formulata come impegno dell'azienda in tutti e tre i ganci e nell'artboard. Le quattro verifiche di forma chieste dal titolare **passano tutte** (dettaglio in § Verifiche richieste dal titolare).

Restano **cinque punti che bloccano la pubblicazione** — nessuno riguarda le decisioni già prese dal titolare, tutti sono formulazioni o perimetri — e **due che bloccano la consegna/tracciabilità** ma non le immagini. Quattro dei cinque si chiudono riscrivendo una riga; uno (l'assicurazione) richiede una risposta scritta del titolare.

---

## Bloccanti — bloccano la pubblicazione

### 1. Assicurazione danni ospiti: marcatore ancora aperto e già impaginato come definitivo

**Dove:** `copy.md` riga 77 e claim #2 (riga 106, `[DATO DA VERIFICARE]` aperto); `Numeri.dc.html` riga 80 ("Un'assicurazione copre i danni causati dagli ospiti."); `Offerta.dc.html` riga 68 (stessa frase).
**Problema:** doppio.
- Il marcatore `[DATO DA VERIFICARE]` è ancora aperto nel copy: regola non negoziabile di `CLAUDE.md`, niente esce con un marcatore aperto. L'esistenza della copertura è confermata dal titolare, **il perimetro no** — e il perimetro è tutto ciò che conta in un gruppo di proprietari.
- Il copy stesso (riga 168) prescrive che i claim 1, 2 e 4 **non vengano impaginati come definitivi** finché non chiusi. Sono impaginati in due artboard su tre. In più, la grafica ha perso la parola "eventuali" che nel copy attenua la frase: `Numeri` e `Offerta` dicono "copre i danni causati dagli ospiti", senza condizionale, senza soggetto emittente, senza limite. Detta così è una promessa di indennizzo.

**Cosa serve prima di pubblicare** (bastano tre righe scritte dal titolare, da archiviare in `conferme-titolare.md` nella cartella campagna):
1. **Chi emette** la copertura: polizza propria di Hadrianus, oppure la protezione della piattaforma di prenotazione (AirCover o equivalente). Se è la seconda, la parola "assicurazione" va sostituita in copy e in entrambe le grafiche con "la copertura della piattaforma": questo pubblico conosce la differenza e la solleva nei commenti entro poche ore.
2. **Cosa copre**: danni all'immobile e all'arredo; furti sì o no; danni a terzi/vicini sì o no.
3. Esistenza di **franchigia** e ordine di grandezza del massimale (non vanno in grafica, servono per rispondere).
Poi: riallineare le due grafiche al copy reinserendo "eventuali" → *"Un'assicurazione copre gli eventuali danni causati dagli ospiti."* e chiudere il marcatore nel copy.

### 2. "E per partire non ti chiediamo un euro." — assoluto più largo di ciò che il titolare ha confermato

**Dove:** `copy.md` riga 81 (la grafica, correttamente, non la riporta).
**Problema:** il titolare ha confermato **nessun deposito cauzionale, nessun costo fisso, 15% solo sulle prenotazioni generate**. "Non ti chiediamo un euro" copre anche le **una tantum di avvio** — servizio fotografico, set biancheria iniziale, piccole sistemazioni pre-pubblicazione, eventuali marche da bollo — che non sono state confermate. È esattamente il tipo di affermazione che, smentita da un commento di un cliente attuale, costa più di quanto renda; ed è l'unica riga del post in cui il copy è **più assoluto della grafica** (`Offerta.dc.html` riga 60 elenca correttamente le quattro voci, senza generalizzare).
**Cosa serve:** o un sì/no scritto del titolare sull'assenza di qualunque costo una tantum in avvio, oppure allineare il copy alla grafica — *"E per partire non ti chiediamo né deposito, né anticipo, né quota d'ingresso, né canone fisso."* La frase resta forte, l'assoluto non verificato sparisce.

### 3. `Numeri.dc.html` — le due colonne non confrontano le stesse cose, e il condominio compare solo a sinistra

**Dove:** `Numeri.dc.html` righe 62-67 (blocco "Guadagni reali"); stessa costruzione in `copy.md` righe 67-69.
**Problema:** a sinistra si legge *"800-900 € al mese — tolte tasse e spese (condominio, TARI, manutenzione) il netto che ti resta è molto più basso"*; a destra *"1.000-1.100 € netti — di media al mese, con le procedure di gestione già pagate"*. Nessuna delle due frasi, presa da sola, afferma il falso. Messe **una accanto all'altra nella stessa immagine** producono due letture non volute:
- che i 1.000-1.100 € siano netti **anche delle tasse** (a sinistra "netto" è definito come post-tasse, a destra "netti" resta indefinito);
- che condominio, TARI e manutenzione **non esistano** con Hadrianus, visto che compaiono solo nella colonna dell'affitto lungo. È la negazione implicita che la regola vincolante vieta: si possono omettere, non si può far intendere che spariscano.
Nella v1 lo stesso rischio era gestito da un caveat esplicito in grafica; nella v2 quel caveat non c'è più, e l'elenco "condominio, TARI, manutenzione" è rimasto solo da un lato. Sotto il profilo pubblicitario è un confronto tra grandezze non omogenee.
**Cosa serve — una sola modifica chiude entrambi i problemi, senza elencare nulla sul lato Hadrianus** (quindi senza toccare la scelta del titolare):
- colonna destra, seconda riga → *"Di media al mese, al netto delle procedure di gestione: commissione, pulizie, biancheria, consumabili."* (perimetro chiuso e vero, nessun riferimento fiscale, nessun numero nuovo);
- colonna sinistra → togliere l'elenco tra trattini e lasciare *"Tolte tasse e spese, il netto che ti resta è molto più basso."* Il confronto torna simmetrico e la frase perde il fianco.
La stessa correzione va riportata in `copy.md` righe 67 e 69.

### 4. "Bilocale a Ostia. Stesso immobile, due strade." — il dato di destra non è su quel perimetro

**Dove:** `Numeri.dc.html` riga 29 (titolo dell'artboard); `copy.md` riga 57.
**Problema:** il titolare ha confermato i 1.000-1.100 € come **media reale sugli immobili in gestione**; il brief (riga 27) li registra come media su "un bilocale in periferia/litorale", cioè un paniere più ampio di Ostia. Il titolo afferma invece un confronto **a parità di immobile**: stesso bilocale, stessa zona. È lo stesso difetto già bloccato nella v1 (bloccante 7) e allora corretto in "Stesso tipo di immobile": nella riscrittura è rientrato. Su questo pubblico la domanda "questi 1.000-1.100 li fate su bilocali a Ostia o è la vostra media generale?" arriva al primo commento, e se la risposta è "media generale" il titolo diventa indifendibile.
**Cosa serve**, in alternativa:
- titolo → *"Stesso tipo di immobile, due strade."* (una parola, il gancio regge identico); oppure
- conferma scritta del titolare che i 1.000-1.100 € valgono **specificamente su bilocali a Ostia/litorale**, e allora il titolo resta com'è.

### 5. "La soluzione migliore per il tuo immobile è affidarlo a noi." — superlativo assoluto senza prova

**Dove:** `copy.md` riga 91 (non presente in grafica).
**Problema:** è un superlativo assoluto affermato come fatto, non come posizione dell'azienda. È una categoria di claim che va sempre segnalata a prescindere dal brief, e qui stona anche col resto del post: due righe prima il testo invita il lettore a valutare da sé ("Valuta tu"), qui gli dice qual è il risultato della valutazione. La **sfida** voluta dal titolare ("Oppure trova una gestione più efficiente della nostra") non è in discussione e non è questo il punto: quella è una sfida verificabile, questa è una sentenza.
**Cosa serve:** la stessa mitigazione che il titolare ha già scelto per la promessa sui cinque anni — trasformarla da dato in posizione dichiarata. Es.: *"Per noi la strada migliore per il tuo immobile è questa. Poi valuta tu."* oppure *"Se vuoi che il tuo immobile lavori tutto l'anno senza pensarci, la strada è la gestione completa."*

---

## Bloccanti — bloccano la consegna, non le immagini

### 6. `direzione-artistica.md` è ancora la versione 1: descrive grafiche che non esistono più

**Dove:** tutto il file.
**Problema:** il documento descrive il mood "scheda tecnica / perizia su carta millimetrata", la linea di quota sulla cauzione, l'`art. 11 L. 392/1978`, le barre proporzionali 74%/87%, le etichette `LORDI`/`NETTI`, il caveat fiscale, la banda "UTENZE ESCLUSE", la banda fotografica 1080×392 e una tabella di "correzioni compliance applicate" alla v1. **Nessuno di questi elementi è presente negli artboard v2**, che hanno un impianto completamente diverso (tabella a due colonne su tre righe, foto a tutto campo con gradiente, nessuna quota, nessun riferimento normativo). Peggio: alla riga 99 istruisce chi dovrà ruotare i ganci a usare "il gancio A = *La cauzione non basta*", che nella v2 non esiste — chi prende in mano il file dopo di noi sbaglia il lavoro seguendo le istruzioni.
**Cosa serve:** riscrivere `direzione-artistica.md` sulla v2 (mood "contrasto marketing secco", palette effettivamente usata, i tre artboard reali, la regola di rotazione dei ganci A/B/C sulla headline di `Main`, il divieto di formule assolute, le due frasi obbligate in `Numeri`). Le note operative in `canvas.json` sono invece **già corrette e allineate alla v2**: sono la base da cui riscriverlo.

### 7. La campagna non è in `campagne/INDEX.md`

**Problema:** regola di `CLAUDE.md` ("ogni campagna va aggiunta a `campagne/INDEX.md`"). L'indice non ha la riga di questa campagna né l'angolo v2 nella lista "angoli/ganci già usati" — quindi la prossima campagna rischia di ripescare "la sfida diretta" credendola inedita.
**Cosa serve:** una riga in tabella (obiettivo: acquisizione proprietari; angolo: **la sfida diretta — promessa sulle condizioni a 5 anni + "trovane una più efficiente"**; target: proprietari in gruppi di categoria Roma/Ostia; formati: post Facebook 3 immagini) e una voce in "angoli già usati".

---

## Da avere pronto per i commenti — non blocca la pubblicazione

Nessuno di questi punti impedisce di pubblicare: sono le domande che questo pubblico farà, e a cui bisogna poter rispondere **senza andarle a cercare**. Vanno in un file di risposte pronte (`risposte-commenti.md`) prima di postare, non dentro le immagini.

- **"1.000-1.100 su quanti immobili e in quanto tempo?"** — numerosità del campione e arco temporale della media. Il dato è confermato dal titolare come media reale; se gli immobili sono pochi o il periodo è una sola stagione, in risposta conviene la formula prudente ("sugli immobili che gestiamo abbiamo visto in media…"), non una difesa del numero.
- **"Netti anche delle tasse?"** — arriverà comunque, anche dopo la correzione del bloccante 3. Risposta corretta e breve: la ritenuta la versa Hadrianus, la posizione fiscale il proprietario la chiude con il proprio commercialista. **Da non scrivere nel post**: appena entra nel testo diventa consulenza fiscale a nome del brand, che è esattamente ciò per cui il gancio fiscale è stato archiviato.
- **"E il condominio? La TARI?"** — restano al proprietario. La risposta va data dritta, senza giri: è la scelta di non elencarli nel post, non di negarli. Una risposta esitante nei commenti vale meno di una riga in più nel post.
- **"Più efficiente di chi? In base a cosa?"** — la sfida ("oppure trova una gestione più efficiente della nostra") è una decisione del titolare e resta; ma invita esplicitamente al confronto, quindi la risposta va preparata sui tre elementi verificabili che il post già dichiara: 15% solo sulle prenotazioni generate, nessun costo fisso né d'ingresso, pagamento il 10 di ogni mese.
- **"L'impegno sui cinque anni è scritto nel contratto?"** — il claim #1 del copy porta un `[DATO DA VERIFICARE]` su questo. La promessa è pubblicabile così com'è (è un impegno unilaterale che l'azienda sceglie di dichiarare, non un dato), ma serve un sì/no del titolare: se **non** è nel contratto, va deciso se metterlo per iscritto o come rispondere a chi lo chiede. Una promessa pubblica non ripetibile per iscritto è la più fragile delle promesse.
- **"Il pagamento il 10 è garantito?"** — confermato come prassi effettiva; nel post non è presentato come esclusiva, ed è corretto così (almeno un competitor romano dichiara lo stesso).

---

## Osservazioni (non bloccanti, ma da considerare)

**Coerenza tra i materiali**
- **Cinque anni vs 3-4 anni nella stessa lettura.** I tre ganci parlano di *cinque anni*, il corpo e `Numeri.dc.html` riga 50 di *"3-4 anni alla stessa persona"*. Con i ganci A e B è una sfumatura; con il **gancio C** è una contraddizione diretta nella stessa schermata ("Affitto lungo: dopo cinque anni riprendi la casa" + tabella che dice 3-4 anni). Se si ruota su C, allineare la tabella o il gancio.
- `copy.md` riga 71 scrive *"È una media, non una promessa"*, la grafica *"Media, non una promessa"*. La formula obbligata è quella della grafica: allineare il copy evita che in una riscrittura futura si perda la versione giusta.
- Il **brief** consiglia ancora l'angolo n. 2 (usura/cauzione) e i ganci v1: va aggiunta in testa una nota di due righe che dice che la v2 nasce da un mandato diverso del titolare, altrimenti sembra che il copy sia andato fuori brief.

**Grafica**
- *"Media, non una promessa: ogni casa fa storia a sé."* (`Numeri.dc.html` riga 70) è il testo **più piccolo e meno contrastato** dell'artboard: 23px in `#b7ad9a` su `#3F3A33`, contro i 25-26px delle altre didascalie, e qualifica un numero scritto a 34px in grassetto. Formalmente c'è, ma il rapporto di forza tra claim e caveat è sbilanciato. Portarlo a 25px e `#cfc7b8` costa nulla e regge molto meglio a un eventuale screenshot.
- `Offerta.dc.html` non porta "Le utenze restano tue.". Nel collage a tre immagini non è un problema; ma la scheda 3 è quella che più spesso viene rispedita da sola in DM o in risposta a un commento — una hairline con quella frase, anche a 22px, la rende autoportante.
- `Offerta.dc.html`: la foto (`immobile-standard.jpg`, 1080×560) è usata a tutto campo su 1080×1080 con `object-fit: cover` → viene ingrandita circa 1,9× e mostra solo la fascia centrale (il frigorifero), con sopra un gradiente da 0.80 a 0.97 di opacità. Risultato: è una texture scura, non una foto — e l'immagine perde la funzione di "prova visiva dello standard alberghiero" che la direzione artistica le attribuiva. O si alleggerisce il gradiente nella metà alta, o si ritaglia un sorgente più alto, o si prende atto che lì la foto è solo materia.
- `Main.dc.html`: la banda chiara *"Non è una speranza. È l'impegno che ci prendiamo noi."* è **ciò che tiene la promessa dentro il perimetro dell'impegno**. In qualunque riuso (storia IG, ritaglio, anteprima) non va tagliata: senza quella banda resta una promessa di risultato futuro su un bene altrui.
- `grafiche/support.js` continua a non esserci (i tre `.dc.html` lo richiamano). Il canvas pubblicato `post-facebook-lungo-vs-breve.html` è autoconsistente e contiene la v2 — verificato — quindi è quello il file da aprire per l'editing; ma vale la pena controllare che i singoli artboard aprano prima della consegna.

**Editoriali**
- Gancio B, seconda riga della sfida: *"Oppure trovane una più efficiente."* — "una" non ha antecedente, perché nel gancio B la parola "gestione" non compare mai (si dice "Noi lo gestiamo per te"). Scrivere *"Oppure trova una gestione più efficiente."*
- Gancio B, prima riga: *"Vuoi davvero stare tranquillo e non pensare più a nulla con il tuo immobile?"* — "non pensare più a nulla **con** il tuo immobile" è sintatticamente storto. Es.: *"Vuoi smettere di pensare al tuo immobile e incassare e basta?"*
- *"Quando lo riprendi, te lo ritrovi da rifare."* è affermato come esito certo di qualunque affitto lungo. È il contrasto voluto dal titolare e non lo tocco, ma un "rischi di ritrovartelo da rifare" costerebbe una parola e toglierebbe l'unico punto in cui il post afferma un fatto su contratti che non sono nostri.
- *"Rigoroso."* (riga 77) come frase isolata dopo il pagamento è l'unico punto in cui il registro scivola nello slogan. Funziona a voce, letto stona; valutabile in revisione, non è un problema di compliance.

**Foto e marchi di terzi — verificato, nessun rilievo**
- `immobile-standard.jpg`: sul piano cucina a destra ci sono un tostapane e una macchina da caffè. Nessun logo leggibile alla risoluzione del file, e nell'uso finale l'area è coperta dal gradiente al 90%+ di opacità. Nessun marchio di terzi protagonista dell'inquadratura. **Conforme.**
- `smart-tv-streaming-mockup.jpg` resta correttamente fuori dalla campagna.
- Nessuna struttura nominata come prova, in nessun materiale. **Conforme.**

---

## Verifiche richieste dal titolare — esito

| # | Verifica | Esito |
|---|---|---|
| 1 | La promessa sui cinque anni resta **impegno dichiarato**, mai dato o previsione impersonale | **PASSA.** Gancio A: "Non è una speranza. È l'impegno che ci prendiamo noi." Gancio B e C: "è l'impegno che ci prendiamo". `Main.dc.html` riga 40: la frase è in banda chiara, Archivo 800 a 56px, sulla stessa immagine della promessa. Mai al futuro impersonale, mai presentata come esito misurato. Unica cautela in § Osservazioni: quella banda non va tagliata nei riusi. |
| 2 | Il **gancio fiscale** non compare in nessun materiale pubblicabile | **PASSA.** Nessuna occorrenza di TUIR, detassazione, intimazione di sfratto, ingiunzione o commercialista in `Main`, `Numeri`, `Offerta`, `canvas.json` o nel canvas pubblicato. Nel copy resta confinato in "Archivio — non pubblicabile", correttamente marcato. |
| 3 | I claim confermati dal titolare sono scritti nelle formulazioni confermate | **PASSA nella sostanza**, con i due scostamenti già elencati nei bloccanti 1 e 2 (l'assicurazione perde "eventuali" in grafica; "non ti chiediamo un euro" allarga il perimetro del "nessun costo fisso"). Tutti gli altri — 800-900 € lordi, 15% solo sulle prenotazioni generate, pagamento il 10, ripristino a ogni check-out — sono riportati alla lettera in copy e grafica. |
| 4 | Nessuna formula assoluta sui costi; presenti "Le utenze restano tue." e "Media, non una promessa: ogni casa fa storia a sé." | **PASSA.** Nessuna occorrenza di "tutto incluso", "l'unica spesa", "l'unico", "una voce sola", "nessun altro costo" in alcun materiale pubblicabile (compare solo negli elenchi dei divieti). Le due frasi obbligate sono in `Numeri.dc.html` righe 89 e 70 e in `copy.md` righe 69 e 71. **Attenzione:** il bloccante 3 riguarda una negazione *implicita* prodotta dall'accostamento delle colonne, non una formula assoluta: la lettera della regola è rispettata, la sostanza no. |
| 5 | Colonna sinistra: "tasse e spese", mai "tasse e utenze" | **PASSA.** `Numeri.dc.html` riga 63 e `copy.md` riga 67 dicono "tasse e spese". Nessuna occorrenza di "tasse e utenze" in tutta la campagna. |

---

## Stato dei bloccanti della v1

| v1 | Stato nella v2 |
|---|---|
| 1. Gancio B fiscale con marcatore aperto | **Chiuso** — archiviato, fuori da ogni materiale pubblicabile |
| 2. "Netti delle tasse" | **Chiuso alla lettera, riaperto in forma implicita** → bloccante 3 |
| 3. "Resta a carico tuo una voce sola: le utenze" | **Chiuso** — sostituito da "Le utenze restano tue.", nessun assoluto |
| 4. Claim non confermati (#3, #4, #5, #6, #10) | **Chiuso** — confermati dal titolare; report mensile e sostituto d'imposta sono usciti dai materiali |
| 5. Promessa di risultato sullo stato dell'immobile | **Riaperto per decisione del titolare**, con mitigazione formale verificata e accettata (verifica 1) |
| 6. "Con noi non ti arriva niente di tutto questo" sugli adempimenti | **Chiuso** — la riga non esiste più nella v2 |
| 7. "Lo stesso bilocale" — confronto non a parità | **Riaperto nella riscrittura** → bloccante 4 |
| 8. "A pieno regime a gennaio" / up-sell centro Roma | **Chiuso** — l'up-sell non c'è più in nessun materiale |

---

## Coerenza col tono Hadrianus

**In linea con il nuovo mandato, con uno scostamento da correggere.**

La v2 è deliberatamente più commerciale della v1, ed è una scelta del titolare, non una deriva. Rispetto a `riferimenti/riferimento-1.md` gli elementi identitari ci sono tutti e nella forma giusta: il "tu" diretto, le frasi corte, il 15% sul fatturato come chiusura e non come apertura, la formula esatta **"Guadagniamo solo se guadagni tu"** (`copy.md` riga 87, `Offerta.dc.html` riga 65), la **simulazione gratuita** come CTA — che è la formula del lessico di brand, non "proiezione dei guadagni". "Standard alberghiero" è usato correttamente in copy e in `Numeri.dc.html`; **mai "hotel-style"**, nonostante `riferimenti/riferimento-3.md` (divisione Templum Purum) lo usi ancora.

La distanza da `riferimento-2.md` è quella giusta e va difesa: là la prova era il case study "Rome Smart Sea" con ADR e Superhost, qui la prova è processo, media dichiarata e condizioni contrattuali. Nessuna struttura nominata, in nessun materiale.

Un punto in cui il testo esce dal registro: **"La soluzione migliore per il tuo immobile è affidarlo a noi."** (riga 91). Anche mettendo da parte il problema di compliance (bloccante 5), è una riga che non somiglia né ai riferimenti né al resto della v2. In `riferimento-1.md` lo stesso concetto è reso lasciando la conclusione al lettore — *"Vuoi scoprire quanto potrebbe rendere davvero il tuo appartamento?"* — e la v2 fa lo stesso, meglio, due righe prima con "Valuta tu.". La sentenza finale toglie forza proprio alla sfida che il titolare voleva come elemento centrale: chi sfida non emette anche il verdetto.

La direzione visiva della v2 (contrasto ✕/✓, colonne scuro/sabbia, oro solo su numeri e azione, angoli vivi) è coerente con il mandato "corto, marketing, contrasto fortissimo", rispetta la palette fumè senza blu navy, è diversa dai pattern delle campagne precedenti e dalla v1 stessa, ed è consegnata in formato editabile (tre `.dc.html` + canvas pubblicato). Formato Facebook rispettato alla lettera: 1ª 1080×1920, 2ª e 3ª 1080×1080.
