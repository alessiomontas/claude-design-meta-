# Checklist compliance — Giornaliero 14/09/2026 · pacchetto v2 "Ti hanno scattato le foto col telefono"

**Materiale controllato:** `copy-v2-foto.md` (R2, K1-K5, FB1-FB3, S3, S4), i 10 artboard v2 in `png/` (`Main`, `K2`-`K5`, `FB1`-`FB3`, `S3`, `S4`) guardati uno per uno a dimensione telefono, `grafiche/build_v2.py`, `reel/build_reel.py` + `reel/reel.html`, le foto sorgente in `grafiche/`, `PUBBLICAZIONE.md`, `brand-assets/README.md`, `.claude/reference/lessico-brand.md`, `riferimenti/riferimento-1.md` e `riferimento-2.md`.
**Non riaperti (come da mandato):** `copy.md` (pacchetto bocciato, storico), `S1` e `S2` già approvate.
**Limite dichiarato:** `reel/reel-foto-col-telefono.mp4` non è ispezionabile fotogramma per fotogramma in questo ambiente. Il controllo sul reel è stato fatto sul sorgente che lo genera (`reel/build_reel.py`, `reel/reel.html`), che è deterministico.

## Esito

**DA CORREGGERE** — 6 rilievi bloccanti. Nessuno riguarda il registro assertivo (che è corretto e rispettato) né i claim di servizio confermati dal titolare: riguardano un claim non verificato pubblicato come fatto, una riga di caption che descrive qualcosa che il lettore non vede, la fonte della foto "prima" documentata in modo errato, i marcatori `[DATO DA VERIFICARE]` ancora aperti, una parola tagliata su `FB2` e la dichiarazione di simulazione assente dalla caption del carosello.

---

## Bloccanti (da correggere prima della consegna)

### B1 · `S3` — un claim non verificato è stampato come fatto sulla storia

**Dove:** `png/S3.png` (riga di garanzia oro, l'ultima cosa che si legge prima della CTA) · `grafiche/build_v2.py` riga 331 · `copy-v2-foto.md` riga 646 · marcatore aperto alla riga 791 · `PUBBLICAZIONE.md` righe 102 e 105.

Testo pubblicato: **"Prezzo e minimo notti si muovono insieme, data per data."**
Il copy stesso dichiara che il minimo notti **non è confermato** (`[DATO DA VERIFICARE: Hadrianus gestisce anche il minimo di notti, o solo la tariffa?]`), e `PUBBLICAZIONE.md` riga 105 conclude che "nessuno dei tre blocca la pubblicazione". Blocca: è un claim di servizio non verificato, affermato in grafica, nel punto di massima visibilità della storia.

**Correzione (formulazione di ripiego già prevista dal copy, riga 791):**
- `build_v2.py` riga 331: `['Prezzo e minimo notti', 'si muovono insieme, data per data.']` → `['Le tariffe si muovono', 'data per data. Ci pensiamo noi.']`
- `copy-v2-foto.md` riga 646 → *"Con noi le tariffe si muovono data per data. Ci pensiamo noi."*
- riesportare `png/S3.png`; correggere `PUBBLICAZIONE.md` riga 105.
- **In alternativa**: conferma scritta del titolare prima della pubblicazione, con il marcatore chiuso nel riepilogo (data + esito). Senza conferma scritta, vale la riscrittura.

### B2 · Caption Facebook — dichiara un confronto che nelle tre immagini non c'è

**Dove:** `PUBBLICAZIONE.md` riga 53 · `copy-v2-foto.md` righe 555-559.

Testo: **"Nelle immagini qui sopra c'è la stessa stanza, due volte."**
Falso sul post pubblicato: `FB1` è l'unica immagine con una foto (quella degradata), `FB2` e `FB3` sono artboard tipografici senza foto. Il "dopo" non compare in nessuna delle tre. Una nota di trasparenza che descrive qualcosa di inesistente produce l'effetto opposto a quello voluto — e la prima domanda nei commenti sarà "dov'è la seconda foto?".

**Correzione, due strade (la (a) è a costo zero):**
- **(a)** riscrivere il paragrafo: *"La foto della prima immagine è una simulazione: abbiamo comprato una foto d'archivio e l'abbiamo rovinata apposta — storta, scura, tagliata male, con le lampade accese e le tende aperte insieme. Non è la casa di nessun cliente, e volevamo dirlo prima che lo chiedesse qualcuno. La stessa stanza fotografata bene la vedi nel reel."*
- **(b)** mettere davvero il "dopo" (`grafiche/salone-pro.jpg`) dentro `FB2`, che oggi è solo testo, e lasciare la caption com'è.

### B3 · La fonte della foto "prima" è documentata in modo errato nel copy

**Dove:** `copy-v2-foto.md` righe 26, 113, 203, 470, 792 (e, per gli inserti, 254, 302, 349).

Il copy dichiara come sorgente unica **`brand-assets/immobili/salotto-divano-azzurro.jpg` — foto reale di un immobile in gestione**, e per conseguenza tiene aperto il claim 3 del riepilogo (*"il proprietario dell'immobile reale autorizza la pubblicazione di una versione volutamente peggiorata del suo appartamento?"*, marcato **Bloccante**), più la nota all'`art-director` #8 (*"niente va impaginato come definitivo finché il claim 3 non è chiuso"*) — nota già violata dagli artboard esportati.

La produzione ha invece usato **una foto Adobe Stock regolarmente licenziata** (`grafiche/stock-salone.jpg` → `salone-telefono.jpg` degradata / `salone-pro.jpg` corretta; confermato in `PUBBLICAZIONE.md` riga 89). Prima e dopo sono effettivamente lo stesso file sorgente: **la riga "Stessa stanza" è vera** (verificato confrontando i due file) e nessun immobile di cliente è stato degradato.

Il rilievo non è sul contenuto pubblicato, è sul documento da cui si rigenera: chiunque ripassi dal copy degraderebbe davvero la foto di una casa in gestione, che è esattamente ciò che il titolare ha voluto evitare.

**Correzione:**
- righe 26, 113, 203, 470: sostituire il riferimento a `brand-assets/immobili/salotto-divano-azzurro.jpg` con *"foto Adobe Stock, licenza commerciale — file `grafiche/stock-salone.jpg`. Scelta deliberata: nessun immobile in gestione, nessun consenso di terzi necessario."*
- riga 792 (claim 3 del riepilogo): chiudere il marcatore → *"RISOLTO 14/09/2026: il 'prima' è una foto d'archivio licenziata, non un immobile in gestione. Vincolo che resta: mai degradare la foto di una casa di un cliente."*
- righe 254, 302, 349: gli inserti del carosello sono `k-banda-pro.jpg` / `k-banda-caldo.jpg` (stock), non `cucina-soggiorno-open-space.png` / `balcone-terrazzo.jpeg` / `salotto-divano-azzurro.jpg`. Allineare.

### B4 · Marcatori `[DATO DA VERIFICARE]` ancora aperti nel pacchetto

**Dove:** `copy-v2-foto.md` righe 434, 790, 791, 792, 794.

Regola non negoziabile di `CLAUDE.md`: nessun contenuto esce con marcatori aperti. Tre dei cinque si chiudono a costo zero perché il copy pubblicato non li usa; vanno però chiusi **per iscritto**, non lasciati aperti nel file consegnato:
- **#1 chi scatta le foto** (righe 434, 790) — il copy dice solo "il servizio fotografico" / "la fotografiamo noi", mai "fotografo professionista": marcare *"non usato nel copy — la formulazione alzata resta vietata finché il titolare non conferma"*. (Nota: `riferimenti/riferimento-2.md` parla di "servizio fotografico editoriale", ma è dentro il case study `Rome Smart Sea`, materiale vietato: non vale come conferma.)
- **#2 minimo notti** (riga 791) → vedi **B1**, è l'unico che tocca un contenuto pubblicato.
- **#3 consenso foto reale** (riga 792) → vedi **B3**, si chiude come risolto.
- **#5 peso dei soggiorni 1-2 notti** (riga 794) — nessun numero è scritto da nessuna parte: marcare *"non usato, nessuna quantificazione nel pacchetto"*.

### B5 · `FB2` — le etichette sono tagliate: si legge "UCE", "RDINE", "NQUADRATURA"

**Dove:** `png/FB2.png` · causa in `grafiche/build_v2.py` righe 296-299 (il filo oro è disegnato a `left: 64px` e la funzione `kicker()` scrive anch'essa da `left: 64px`, quindi il filo copre la prima lettera di ogni etichetta).

`FB2` è la seconda immagine del post Facebook, quella pensata per essere salvata e rimandata: esce con quattro parole mozzate su cinque righe. È il tipo di difetto che il controllo sui PNG a dimensione telefono deve intercettare prima della consegna (preferenza fissa 9 di `CLAUDE.md`).

**Correzione:** portare il kicker a `left: 86px` (allineato al corpo, che già usa `left=86`) oppure spostare il filo verticale a `left: 56px`; riesportare `png/FB2.png`.

### B6 · Carosello — la foto degradata esce senza nessuna spiegazione in testo

**Dove:** `png/Main.png` (chip `SIMULAZIONE` in alto a destra) · caption del carosello in `PUBBLICAZIONE.md` righe 33-43 e `copy-v2-foto.md` righe 376-387.

La slide 1 del carosello è interamente la foto degradata. La dichiarazione c'è solo come chip di due parole, e la stessa caption chiude con *"Scrivi CALCOLO in DM per **una simulazione gratuita**"*: la parola "simulazione" compare due volte nello stesso pezzo con due significati diversi, e il chip finisce per leggersi come "simulazione di rendita". Sul reel e su Facebook la dichiarazione è in chiaro nel testo; qui no — ed è il pezzo costruito per girare e per essere salvato.

**Correzione:** aggiungere in caption, come secondo paragrafo (subito dopo "Succede, e si corregge."):
> *"La foto della prima slide è una simulazione: una foto d'archivio che abbiamo rovinato apposta — storta, scura, tagliata male. Non è la casa di nessun cliente."*

---

## Osservazioni (non bloccanti, ma da considerare)

**O1 · `K1`/`Main` non mostra il confronto che il copy descrive.** Il copy (righe 52, 198-199, 204) prevede metà sinistra corretta e metà destra degradata; l'artboard (`build_v2.py` riga 180) usa `k-tel-45.jpg` a pieno formato e la tendina a x 216 è praticamente invisibile sul fondo scuro. Non è un problema di onestà (semmai è la versione più prudente), ma nel pacchetto pubblicato il confronto prima/dopo esiste **solo nel reel**: il carosello e Facebook lo evocano senza mostrarlo. O si monta davvero la doppia metà, o si allinea il copy.

**O2 · Consiglio sulla luce: "finestra aperta" è impreciso.** `K2`, `FB2` e la caption Facebook (PUBBLICAZIONE riga 57) dicono *"Lampade accese e finestra aperta insieme"*: si aprono **le tende**, non la finestra — aprire la finestra non cambia la luce. Proposta: *"Lampade accese e tende aperte insieme danno una foto di due colori."* Sul resto il consiglio è tecnicamente corretto (dominanti diverse per temperatura colore). Piccola precisione in più su *"Scatta a metà mattina"*, che dipende dall'esposizione delle finestre: *"Scatta a metà mattina, quando il sole non batte diretto sui vetri."*

**O3 · `K4` — "Se la stanza pende, sembra più piccola" non è l'effetto reale.** Le verticali cadenti producono **deformazione**, non rimpicciolimento. Proposta: *"Se le verticali pendono, la stanza sembra storta."* È un contenuto che punta a essere salvato: un consiglio tecnico va detto giusto.

**O4 · `K4` — i due fili oro "sugli stipiti" cadono su un divano e su un plaid.** `build_v2.py` riga 229 + funzione `inserto()`: i fili sono fissi a x 238 e 714, e la foto usata non ha né stipiti né finestre. La slide che spiega le verticali dimostra il contrario di quello che afferma. Usare un inserto con uno stipite o un infisso, oppure togliere i fili.

**O5 · `K3` — l'inserto ha la dominante arancione contro cui mette in guardia `K2`.** `k-banda-caldo.jpg` (stessa scena di `S3`) è esattamente la "foto metà gialla" del consiglio 01, messa una slide dopo. Sostituire con una foto a bilanciamento neutro.

**O6 · Divergenze copy ↔ artboard da allineare** (la specifica è la fonte da cui si rigenera, il difetto era già stato segnalato sul pacchetto v1):
- `K3` riga oro: render *"Chi guarda vede una casa pronta."* vs copy riga 285 *"…, non una da sistemare."*
- `S3` consiglio: il render lascia fuori *"e alza un po' la tariffa per coprire il riassetto"* (copy riga 645).
- `K1` gancio su 3 righe nel render, 2 nel copy (riga 177-178); y dei blocchi di `K2`-`K4` diverse dalle tabelle LAYOUT (render 470/710/890, copy 380-560/620-800/860-920).

**O7 · `S4` — l'identificazione c'è, ma non nella riga più grande.** Il consiglio dice *"l'ospite va identificato prima di entrare"* ✅ (il vincolo è rispettato). La riga oro di garanzia, però — l'ultima e la più visibile — è *"Ti assicuriamo il check-in smart H24, a qualsiasi ora."*, mentre il copy (riga 724) prevedeva *"l'ospite ricevuto a qualsiasi ora, identificato prima di entrare"*. Consigliato riportare la condizione nella riga oro: la promessa più forte non deve restare sola.

**O8 · "Abbiamo preso una foto reale" → dire che è d'archivio.** Caption Facebook (PUBBLICAZIONE riga 53) e caption reel (riga 77). La risposta pronta ai commenti (riga 89) già dice *"è una foto comprata da Adobe Stock"*: conviene che sia nel testo pubblicato, non solo nella risposta. Toglie di mezzo il sospetto che sia la casa di qualcuno.

**O9 · Reel, da guardare sul montato prima delle 18:00.** Dal sorgente: chip `SIMULAZIONE` visibile 0 → 6,6 s (scene 1-4) ✅, scompare con la metà degradata ✅, chiusura con *"GUADAGNIAMO SOLO SE GUADAGNI TU"* e CTA *"Scrivi CALCOLO in DM"* ✅, nessun logo di piattaforma nella scena 3 ✅. Da verificare a occhio sul fotogramma finale: `build_reel.py` righe 148-150 e 255 mettono il logo mascherato a 640-1040 e il blocco testo a y 1000 — è lo stesso accoppiamento che nella v1 aveva prodotto il testo sopra la scritta del logo.

**O10 · Il pacchetto v2 non ha né brief né direzione artistica.** `brief-mercato.md` e `direzione-artistica.md` restano quelli dell'angolo bocciato (*"la casella dimenticata"*, firma "marca temporale + arco"): chi apre la cartella oggi trova una direzione artistica che descrive un pacchetto che non esiste più. Serve almeno una nota d'angolo v2 e una DA v2 ("la tendina che attraversa"), per il controllo di completezza e per la regola di output tracciabile. `PIANO.md` (riga 40) e `INDEX.md` (righe 46-47) risultano invece già aggiornati.

**O11 · Coerenza del piano orario.** `PUBBLICAZIONE.md` righe 11 e 17 tengono `S1` ("l'annuncio e il CIN") alle 09:00 e `S2` alle 21:30 dentro una giornata il cui pacchetto ha bandito la burocrazia come gancio. Non riapro `S1` e `S2` — segnalo solo che nella stessa giornata le storie 1-2 e le storie 3-4 parlano due lingue diverse.

---

## Claim: esito del controllo puntuale

| Claim vietato | Esito |
|---|---|
| Garanzie su risultati di mercato ("guadagno garantito", "prenotazioni garantite", "sempre pieno") | ✅ **assenti** in ogni pezzo. Le garanzie riguardano solo lavoro e standard: *"Ti garantiamo il servizio fotografico"*, *"Ti garantiamo la gestione completa"*, *"Ti assicuriamo il check-in smart H24"*, *"Con noi la tua casa la fotografiamo noi"* — corrette e volute |
| Percentuali/statistiche inventate, dati sugli algoritmi | ✅ **assenti**. L'unico numero è il 15% di commissione. *"La prima foto è l'unica cosa che vede chi sta scorrendo"* è posizionamento, non un dato |
| "Nessun costo fisso" / "zero costi iniziali" | ✅ **non rientrato** in nessuna grafica e in nessuna caption (resta solo nella sezione interna "Da confermare", `PUBBLICAZIONE.md` riga 103) |
| "hotel-style" | ✅ assente, ovunque **"standard alberghiero"** (`K5`, `FB3`, caption) |
| Case study su struttura nominata / "Templum Purum" / "Rome Smart Sea" | ✅ assenti da tutti i file v2 |
| Ingresso ospite senza identificazione (`S4`) | ✅ rispettato: *"a qualunque ora, l'ospite va identificato prima di entrare"* in grafica (vedi però **O7**) |
| Marchi di terzi nelle foto | ✅ nessun logo, nessuna TV accesa, nessun elettrodomestico di marca nelle 6 foto usate; `smart-tv-streaming-mockup.jpg` non è stato usato, ed è vietato negli inserti |
| Nota di demerito in chiusura | ✅ *"La responsabilità resta tua. Il lavoro no."* non compare in nessun testo pubblicato: ogni pezzo chiude su cosa fa Hadrianus |
| Lessico "Guadagniamo solo se guadagni tu" | ✅ formula esatta e sempre in chiusura: `K5`, `FB3`, reel (scena finale), caption carosello/Facebook/reel. Nessuna occorrenza della forma sbagliata |
| CTA | ✅ **"Scrivi CALCOLO in DM"** su `K5`, `FB3`, `S3`, `S4` e reel; *"per una simulazione gratuita"* in tutte e tre le caption. `K1` porta *"Scorri →"*, coerente |

**Consigli di fotografia — verifica di merito:** luce (temperatura colore), ordine, macchina livellata a mezza altezza, scatto da un angolo, telefono in orizzontale, sequenza copertina → giorno → camere → bagno/esterno sono **corretti e utili anche a chi non diventerà cliente**. Due imprecisioni da sistemare: **O2** ("finestra aperta") e **O3** ("sembra più piccola").

---

## Coerenza col tono Hadrianus

**In linea.** Il registro assertivo richiesto dal titolare è applicato bene e senza sbandare: *"ti garantiamo"*, *"ti assicuriamo"*, *"con noi la tua casa"*, *"ci pensiamo noi"* stanno sempre su ciò che Hadrianus esegue, mai sul risultato di mercato — che è la linea giusta e che il pacchetto tiene in tutti e dieci i pezzi. La chiusura di `riferimento-1.md` (*15% sul fatturato generato · guadagniamo solo se guadagni tu · Scrivi CALCOLO in DM per una simulazione gratuita*) è riprodotta alla lettera in tutte le caption: è il punto in cui il pacchetto suona più "di casa".

Due note di voce, non di regola:
- Il carosello dà valore prima di chiedere (*"Valgono anche se fai da solo — salvale e usale al prossimo scatto"*) e la risposta pronta *"Ma tanto le foto le so fare anch'io" → "Benissimo, e il carosello serve proprio a quello"* è esattamente il tono adulto dei `riferimenti/`: nessun paternalismo, nessuna pressione.
- L'unico punto che scivola verso il generico è `FB2` (*"Non serve un'altra casa. Serve un'altra foto."* + elenco di quattro voci): funziona, ma è la superficie più "agenzia" del pacchetto. In `riferimento-1.md` lo stesso passaggio si fa con una frase che conta i costi al proprietario (*"È il 15% che paghi, per il 100% di stress che non paghi più"*): se `FB2` deve reggere da sola nel collage, una riga di quel tipo la riporta dentro la voce del brand.

---

**Prossimo passo:** correzioni B1-B6 (B1, B2, B5, B6 toccano materiale pubblicabile; B3 e B4 toccano i documenti), riesportazione di `png/S3.png` e `png/FB2.png`, poi `revisione-marketing-design` prima della consegna. Fino ad allora **il pacchetto non è pubblicabile**: in particolare `S3` (B1), il post Facebook (B2, B5) e il carosello (B6).
