# Checklist compliance — Giornaliero 14 settembre 2026 · "La casella dimenticata"

**Materiale verificato:** `brief-mercato.md`, `copy.md`, `direzione-artistica.md`, i 19 artboard `.dc.html`, i 19 PNG renderizzati, `grafiche/build.py`, `reel/battute.json`, il canvas pubblicato `giornata-14-settembre-casella-dimenticata.html`.
**Riferimenti usati per il giudizio:** tabella dati del brief, `.claude/reference/lessico-brand.md`, `riferimenti/riferimento-1.md` e `riferimento-2.md` (tono), `CLAUDE.md` (regole fisse).

## Esito

**DA CORREGGERE** — 5 rilievi bloccanti, 4 sul blocco `F3` e 1 su `F2`. Tutto il resto del pacchetto è conforme: l'angolo più rischioso finora è stato gestito bene, i vincoli normativi del brief sono rispettati uno per uno.

---

## Bloccanti (da correggere prima della consegna)

### `F3` — caption: marcatore `[DATO DA VERIFICARE]` ancora nel testo pubblicabile

`copy.md` righe 562-565, caption unica del post Facebook:

> Tutto dentro la gestione completa: 15% sul fatturato generato, nessun costo fisso [DATO DA VERIFICARE: eventuali costi una tantum in avvio — servizio fotografico, set biancheria iniziale, sistemazioni pre-pubblicazione]. Guadagniamo solo se guadagni tu.

La caption è testo che si incolla su Facebook: il marcatore uscirebbe a video, e "nessun costo fisso" resta un claim economico non confermato. Regola non negoziabile: nessun contenuto esce con un marcatore ancora dentro.

**Due sole uscite, nessuna terza:**
- se il titolare conferma che non esiste alcun costo una tantum in avvio → si toglie il marcatore e la riga resta com'è;
- se non lo conferma prima della pubblicazione → riscrittura: **"Tutto dentro la gestione completa: 15% sul fatturato generato. Guadagniamo solo se guadagni tu."**

**Confermato come richiesto:** la grafica è già pulita. `grafiche/F3.dc.html` riga 25 e `png/F3.png` stampano solo **"15% sul fatturato."**, senza "Nessun costo fisso". Su questo il passaggio art-director ha tenuto.

### `F3` — `copy.md`, tabella LAYOUT: la specifica stampa il claim non verificato

`copy.md` riga 579:

> | riga offerta | 740-820 | 15% sul fatturato. Nessun costo fisso. | Archivo 700 | 40 | #F5F0E6 |

Contraddice l'artboard reale, la riga 601 dello stesso file e il blocco dichiarato alla riga 789 ("la riga 'Nessun costo fisso' di `F3` non va impaginata come definitiva"). Chi rigenerasse le grafiche dalla specifica stamperebbe il claim aperto — in grafica un claim pesa più che in caption.

**Riscrittura riga 579:** `| riga offerta | 740-820 | 15% sul fatturato. | Archivo 700 | 40 | #F5F0E6 |`

### `F3` — caption: "quattro mesi fa" è una data sbagliata

`copy.md` riga 521:

> Il 20 maggio 2026, quattro mesi fa, è diventato applicabile il Regolamento UE 2024/1028.

Dal 20 maggio al 14 settembre passano **3 mesi e 25 giorni**. È l'unico contenuto del brand ancorato a una data, pubblicato su un pubblico competente che quella data la conosce: un conteggio gonfiato costa esattamente l'autorità che il post sta cercando di costruire.

**Riscrittura:** *"Il 20 maggio 2026 è diventato applicabile il Regolamento UE 2024/1028."* (il conteggio non serve, la data fa già il lavoro).
Stesso errore alla riga 38 di `brief-mercato.md`: da non riportare nei contenuti futuri su questo angolo.

### `F3` — caption: manca "consecutive" sul limite delle 10 notti

`copy.md` riga 539:

> Durante e dopo: a Roma l'imposta di soggiorno è 6 € a persona a notte fino a 10 notti, e la versa il gestore anche se l'ospite non paga la sua quota.

Il dato 9 del brief dice "massimo 10 notti **consecutive**", e `C4` lo stampa correttamente ("fino a 10 notti consecutive"). Senza l'aggettivo il limite si legge come tetto per soggiorno o per anno: è un dettaglio normativo detto male, nello stesso pacchetto in cui altrove è detto bene.

**Riscrittura:** *"…è 6 € a persona a notte fino a 10 notti consecutive, e la versa il gestore anche se l'ospite non paga la sua quota."*

### `F2` — refuso tipografico visibile nella grafica pubblicata

`grafiche/build.py` riga 417 (e quindi `F2.dc.html` riga 24, `png/F2.png`):

> poi gli dai l’accesso. Da lì: 24 ore

Apostrofo curvo `’` in mezzo a un blocco che usa ovunque l'apostrofo dritto `'` ("l'ospite" nella riga sopra, "nell'annuncio" nella sezione precedente). Si vede a dimensione telefono, nella stessa colonna di testo. Un carattere da cambiare in `build.py` + riesportare `F2`.

**Riscrittura riga 417:** `'poi gli dai l\'accesso. Da lì: 24 ore',`

---

## Rilievi per blocco

### `R1` · Reel — nessun bloccante
- **Battuta 2, "Per una casella."** — ellissi senza verbo: regge solo se lo spettatore ha letto la battuta 1. Su un reel che parte in mute e in scroll, il rischio è che la svolta non arrivi. Proposta: **"Per una casella dimenticata."** (sta su due righe a 70 px, come le battute 5, 6 e 8).
- **Battuta 8** — `copy.md` riga 71 dichiara 2 righe ("Il CIN resta tuo. / L'orologio lo guardiamo noi."), `R1b8.dc.html` ne stampa 3 ("Il CIN resta tuo." / "L'orologio" / "lo guardiamo noi."). Allineare la specifica all'artboard.
- Verificato: nessun elenco di adempimenti, nessun importo, nessuna data. Anti-sovrapposizione col carosello rispettata. Chiusura `R1b9` con "GUADAGNIAMO SOLO SE GUADAGNI TU" alla lettera. Tempi coerenti: `battute.json` somma 15,4 s.

### `C1` · Carosello, gancio — nessun bloccante
- **"Sei anelli. Ognuno con la sua scadenza."** — per due dei sei anelli una scadenza ricorrente verificata non c'è: il CIN nell'annuncio è un prerequisito, non una scadenza, e la manutenzione semestrale delle dotazioni sta nel dato 5 (fonte singola, `DA VERIFICARE`, giustamente non stampato). La grafica non quantifica niente, quindi non è bloccante, ma la formula promette più precisione di quella che il brief regge. Proposta più difendibile: **"Sei anelli. Ognuno con il suo momento."**
- **Numerazione**: `C1` annuncia sei anelli, poi le marche temporali contano `01 · 02 · 03 · 04`. Chi conta vede quattro numeri per sei anelli. Proposta: togliere il numero dalle marche (`PRIMA CHE L'ANNUNCIO SIA ONLINE`, `QUANDO L'OSPITE ARRIVA`, …) oppure sottotitolo `C1` "Sei anelli, in tre momenti."
- `copy.md` riga 146 dichiara il gancio su 3 righe: corrisponde all'artboard (Gancio A spezzato in tre). Nessun disallineamento.

### `C2` · anello 01 — nessun rilievo
CIN obbligatorio in annuncio + esposizione all'esterno (dato 2), verifica della piattaforma senza citare data né nome del regolamento (dato 1, correttamente riservato a Facebook). Nessun importo di sanzione: verificato sull'artboard e sul PNG.

### `C3` · anello 02 — nessun bloccante
- **Titolo "Prima lo riconosci."** — il corpo della stessa slide, `F2` e `S2` usano "identifichi", che è il termine del dato 8 ("identificazione de visu"). "Riconoscere" è più debole e non è il verbo della norma. Proposta: **"Prima lo identifichi. / Poi gli dai l'accesso."**
- Verificato: ordine identificazione → accesso presente e stampato; niente numero di sentenza, niente circolari, niente TULPS.

### `C4` · anello 03 — nessun rilievo
6 €/persona/notte, fino a 10 notti **consecutive**, responsabilità del versamento anche se l'ospite non paga: tutto dentro il dato 9, delibera capitolina mai citata. Dotazioni di sicurezza senza importi né quantità per m². "standard alberghiero" corretto. È il blocco meglio scritto del pacchetto.

### `C5` · chiusura — nessun rilievo
Sei anelli, frase onesta ("La responsabilità resta tua. Il lavoro no."), claim autorizzato dal titolare alla lettera, "Tutto dentro il 15% sul fatturato. Guadagniamo solo se guadagni tu." in chiusura. Nessuna aliquota sull'anello dei canoni. Nessuna garanzia di risultato.

### `F1` · Facebook 1ª immagine — nessun bloccante
- **Gancio B, "Da maggio l'irregolarità non aspetta un controllo"** non compare nella tabella claim di `F1`. È un'inferenza dal dato 1 (trasmissione mensile dei dati) e il brief la sostiene alla riga 38, ma se si sceglie la variante B va mappata in tabella come le altre.
- **Arco di avanzamento assente** (vedi rilievo trasversale sotto).
- Verificato: 9:16 come da preferenza fissa 6, nulla di leggibile sotto y 1600, nessun accenno a Roma Capitale, IMU o aliquote.

### `F2` · Facebook 2ª immagine — 1 bloccante (refuso, sopra)
Per il resto conforme: ordine "prima identifichi, poi gli dai l'accesso" stampato in grafica, imposta di soggiorno senza importi di sanzione, "standard alberghiero". Unica superficie chiara insieme a `C4`, come previsto.

### `F3` · Facebook 3ª immagine — 4 bloccanti (sopra)
- **Osservazione aggiuntiva:** `F3` è la superficie più assertiva del pacchetto ("Sei anelli. Tutti eseguiti." + "Il proprietario riceve solo il bonifico netto a fine mese.") e nel collage Facebook può essere aperta da sola. La frase onesta sta solo nella caption e su `C5`. La riga di perimetro fiscale in grafica c'è ed è ottima; valutare di affiancarle, o di sostituire "Sei anelli. Tutti eseguiti.", con **"La responsabilità resta tua. Il lavoro no."**
- **Caption lunga oltre 2.200 caratteri**: regge nel formato "annuncio di valore per la community" chiesto dal brief, ma il blocco centrale PRIMA / ALL'ARRIVO / DURANTE E DOPO ripete parola per parola `F2`, che è l'immagine accanto. Non bloccante: si può ridurre a due righe e lasciare il lavoro all'immagine.

### `S1` · Storia "prima" — nessun bloccante
- **"Il codice ci sta dentro dal primo giorno."** — nello stesso pacchetto "dentro" è il verbo dell'offerta ("Tutto dentro il 15%", "È già dentro la gestione"). Qui può leggersi "il CIN è compreso nel servizio", cioè che lo otteniamo noi: l'anello confermato è *CIN presente e coerente nell'annuncio*, non il rilascio dalla BDSR. Proposta: **"L'annuncio lo curiamo noi. / Il codice è nell'annuncio, / coerente, dal primo giorno."**
- `copy.md` riga 629 dichiara la riga di risposta su 2 righe, l'artboard ne stampa 3: allineare la specifica.
- Verificato: "può non passare la verifica" (mai "ti bloccano l'annuncio"), nessun importo.

### `S2` · Storia "dopo" — nessun bloccante
- **Ordine invertito tra gancio e corpo**: il gancio dice "L'ospite entra alle 23:40", il corpo subito sotto rimette l'ordine giusto ("Lo identifichi. Poi entra."). Non descrive un flusso non conforme — il corpo corregge — ma si legge meglio con **"Alle 23:40 l'ospite è alla porta."**
- Verificato e stampato in grafica: identificazione prima dell'accesso, 24 ore per la comunicazione, imposta di soggiorno versata dal gestore. Nessun TULPS, nessun importo, nessuna aliquota. La riga "Lo identifichi. Poi entra." è presente sull'artboard e **non va rimossa in nessuna revisione successiva**.

---

## Rilievi trasversali (non bloccanti)

- **L'arco che si chiude esiste solo su `F2` (2/3).** `direzione-artistica.md` e la nota all'art-director in `copy.md` dichiarano entrambe "1/3 → 3/3 su Facebook", ma `F1` e `F3` non lo hanno (verificato in `build.py`: `arco()` è chiamato solo per `F2`). O si aggiunge 1/3 su `F1` e 3/3 su `F3` — anche integrato nella pill come su `C5` — o si corregge la dichiarazione nei due documenti. Nel carosello invece la sequenza 1/5 → 5/5 è completa e corretta.
- **Marchi di terzi nelle foto:** nei fotogrammi `r-cucina-a.jpg` / `r-cucina-b.jpg` (battute 3 e 4 del reel) compare uno split di climatizzazione con un piccolo marchio sul frontalino. Nel PNG a dimensione telefono non è leggibile, non è protagonista dell'inquadratura e non suggerisce nessuna partnership → **non bloccante**. Da riguardare sul `reel.mp4` a risoluzione piena: se il marchio si legge, scurire quella porzione o ritagliare. `C1`-`C5`, `F1`-`F3`, `S1`, `S2`: nessun logo di terzi, nessuno schermo con contenuto.
- **Imposta di soggiorno fuori Roma Capitale (es. Fiumicino):** confermato come chiesto — `C4` e la caption di `F3` restano ancorate a "A Roma", quindi il testo è accurato e **non va toccato**. Serve solo la risposta pronta per i commenti: *"La tariffa che citiamo è quella di Roma Capitale. Fuori dal Comune la regola la fa il regolamento locale: se la casa è a Fiumicino o altrove sul Litorale, scrivici e verifichiamo la tua."* — da tenere nel materiale di community management, non nel copy.
- **`PUBBLICAZIONE.md` non esiste** nella cartella della giornata. `CLAUDE.md` lo richiede per ogni pacchetto quotidiano (orari, file, caption pronte). Va prodotto prima della pubblicazione, **con la caption `F3` nella versione corretta**, non con quella attuale.
- **Registrazione:** la giornata non è ancora in `campagne/giornaliero/PIANO.md` né l'angolo in `campagne/INDEX.md`. È il passaggio successivo previsto, lo segnalo solo perché non si perda.

---

## Controlli superati (verificati uno per uno, non a campione)

| Vincolo del brief | Esito |
|---|---|
| Nessun claim fiscale ("pensiamo noi alle tasse", "ti mettiamo in regola") | ✅ Superato, e **rovesciato**: `F3` stampa in grafica "La dichiarazione dei redditi resta col tuo commercialista" e la caption dice esplicitamente "non diamo consulenza fiscale" |
| Nessuna garanzia di risultato normativo | ✅ "zero multe", "conformità garantita", "non rischi più niente" assenti da tutti i file |
| Nessuna aliquota fiscale (21/26/30) | ✅ Assenti ovunque, anche sull'anello dell'incasso dei canoni |
| Nessun regolamento di Roma Capitale, IMU, limiti di notti | ✅ Assenti |
| Nessun rischio penale / art. 17 TULPS | ✅ Assente, nessun "arresto", registro mai allarmistico |
| Nessun importo di sanzione stampato in grafica | ✅ Verificato su tutti i `.dc.html` e sui 19 PNG: la sanzione è allusa ("una casella dimenticata"), mai quantificata |
| Mai un ingresso ospite senza identificazione | ✅ `C3`, `F2`, `S2` portano l'ordine corretto, e `S2` lo stampa in grafica |
| Nessun numero su sanzioni evitate, clienti, controlli | ✅ Assenti |
| "Guadagniamo solo se guadagni tu", alla lettera e in chiusura | ✅ `R1b9`, `C5`, `F3` — mai "guadagni solo se guadagni tu" |
| "standard alberghiero", mai "hotel-style" | ✅ `C4` e `F2` |
| Nessuna struttura nominata come prova | ✅ Nessun case study, nessun "Rome Smart Sea" |
| "Templum Purum" fuori dal brand dal 14/09/2026 | ✅ Assente da tutti i file della giornata (grep su copy, brief, direzione artistica, grafiche, canvas) |
| Claim autorizzati dal titolare usati alla lettera | ✅ "Il proprietario riceve solo il bonifico netto a fine mese" su `C5` e `F3`; sei anelli su `C5`, `F3` e nella caption |
| Grafiche editabili, mai immagini piatte | ✅ 19 artboard `.dc.html` + canvas pubblicato + `canvas.json`; i PNG sono export aggiuntivi |
| Post Facebook: 1ª immagine 9:16 | ✅ `F1` è 1080×1920 |
| Storie autoconclusive | ✅ `S1` e `S2` chiudono da sole problema, risposta e CTA, non si citano a vicenda |

## Coerenza col tono Hadrianus

**In linea, e su un punto migliore del riferimento.** `riferimenti/riferimento-1.md` risolve lo stesso tema con uno slogan generico ("burocrazia infinita"); qui la stessa idea è resa per atti e orari — *"Da lì: 24 ore per la comunicazione"*, *"L'ospite entra alle 23:40"* — che è più specifico, meno pubblicitario e coerente con il registro calmo da vicino di casa competente chiesto dal brief. La struttura di `riferimento-1` (problema concreto → presa in carico → 15% → filosofia in chiusura) è rispettata in tutti i blocchi che chiudono (`R1b9`, `C5`, `F3`).

Nessuna deriva verso `riferimenti/riferimento-2.md`, che è il riferimento pericoloso: lì la prova è un case study su struttura nominata con ADR e Superhost, cioè esattamente ciò che il lessico di brand vieta nei contenuti di acquisizione. Qui la prova è il processo. Corretto anche l'esclusione di `riferimento-3.md` (fuori perimetro).

**Unico punto in cui il tono si allontana:** la caption di `F3`, per lunghezza e per la ripetizione letterale di `F2`, scivola verso il registro da guida normativa che il brief mette tra le cose da evitare ("Cosa evitare (a): il tono da guida normativa"). Non è bloccante — su Facebook il formato lungo è dichiarato — ma accorciare il blocco centrale riporterebbe la caption dentro la voce del brand invece che dentro quella dei software di settore (Chekin, Lodgify) da cui il brief vuole distinguersi.

---

**Prossimo passo:** `copywriter` corregge i 4 rilievi su `F3` e `art-director` il carattere di `F2` (+ riesporta `F2`, e `F3` solo se si tocca la grafica). Poi `revisore-marketing-design`, poi `PUBBLICAZIONE.md`, poi registrazione in `PIANO.md` e `INDEX.md`. Nessuna riscrittura oltre le righe elencate: il resto del pacchetto è approvato così com'è.
