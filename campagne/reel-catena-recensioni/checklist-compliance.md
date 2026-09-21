# Checklist compliance — reel-catena-recensioni

**Data controllo:** 2026-09-21 · **File controllato:** `campagne/reel-catena-recensioni/copy.md`
**Riferimenti usati:** `CLAUDE.md`, `.claude/reference/lessico-brand.md`, `riferimenti/riferimento-1.md`, `riferimenti/riferimento-2.md`, `campagne/INDEX.md`

## Esito

**BLOCCATO**

Il lessico di brand è pulito (nessun errore sulle tre regole fisse) e non c'è nessuna cifra a schermo — su questo il copy è in ordine. Ma restano cinque blocchi, di cui tre riguardano claim che la tabella «Claim e verificabilità» dichiara «OK» senza che lo siano.

## Bloccanti (da correggere prima della consegna)

1. **`Superhost` (slot «Just Listed») — dichiarato verificato, ma altrove nel repo risulta NON verificato.**
   `copy.md` riga 59 scrive: «Confermato dal titolare il 18/09/2026: livello attivo. OK.»
   `campagne/INDEX.md` riga 14 tiene però la campagna `facebook-recensioni-superhost/` in stato «🟡 Pronta salvo **verifica Superhost tuttora attivo** e totale recensioni». Le due affermazioni non possono essere entrambe vere: o la verifica è arrivata (e allora va chiusa anche in INDEX.md, con la data e chi l'ha confermata) o non è arrivata (e allora il badge non può andare a schermo).
   → Serve: conferma scritta e datata dello stato Superhost attivo **alla data di pubblicazione** — il badge decade a ogni valutazione trimestrale, una conferma del 18/09 non copre indefinitamente. Fino ad allora lo slot va lasciato vuoto o riassegnato a testo di concetto.

2. **`Superhost` + `★★★★★` insieme = prova di singola struttura riciclata.**
   L'unica fonte del badge nei `riferimenti/` è `riferimento-2.md` riga 8, dove Superhost e la valutazione 5.0 sono attributi **di Rome Smart Sea**, una struttura singola nominata. Nel reel gli stessi due segnali compaiono senza soggetto, quindi lo spettatore li legge come performance di Hadrianus nel suo complesso. È la regola di `lessico-brand.md` riga 12 (niente struttura singola come prova in acquisizione) aggirata togliendo il nome invece che togliendo il claim: l'anonimizzazione peggiora il problema, non lo risolve, perché generalizza un dato che vale per un immobile solo.
   → Serve: o un dato aggregato sul portafoglio in gestione (media valutazioni su N strutture, con N), o la rimozione di entrambi gli slot.

3. **`Ti diciamo quanto puoi guadagnare` (slot «Schedule Your Private Tour Today») — promessa di risultato.**
   «quanto **puoi** guadagnare» afferma che la cifra è ottenibile. I `riferimenti/` usano sistematicamente il condizionale e la parola «simulazione»: `riferimento-1.md` riga 14 → «Vuoi scoprire quanto **potrebbe rendere** davvero il tuo appartamento? Scrivi CALCOLO in DM per una **simulazione gratuita**». `lessico-brand.md` riga 14 vieta il rendimento presentato come garantito (rischio pubblicità ingannevole).
   → Correzione suggerita: **«Ti diciamo quanto potrebbe rendere»** (stessa lunghezza, entra nello stesso slot).

4. **`Più punteggio, più in alto esci` / `Più in alto esci, più ti trovano` — meccanismo di ranking dato come fatto, senza fonte.**
   La tabella lo archivia come OK perché «nessuna percentuale, nessun portale nominato» (riga 58), ma l'assenza di numeri non rende verificabile un'affermazione causale: qui si sta descrivendo il funzionamento dell'algoritmo di ranking di piattaforme terze, che non è documentato pubblicamente in forma citabile e cambia senza preavviso. Non nominare il portale non attenua il claim, lo rende solo non falsificabile.
   → Serve: o una fonte citata nel brief di campagna (documentazione ufficiale della piattaforma), o una riformulazione che resti dalla parte dell'esperienza e non della meccanica — es. «Il punteggio pesa su dove ti vedono.» / «Se non ti vedono, non ti prenotano.»

5. **I 12 video stock di ville di lusso con piscina.**
   È già annotato negli «Aperti» (righe 69-72) come problema di messaggio, ma è prima di tutto un problema di compliance: in un contenuto di acquisizione, immagini di immobili che Hadrianus non gestisce, montate sotto testi come «Standard alberghiero» e «È lavoro», si leggono come portfolio. È rappresentazione ingannevole del servizio, indipendentemente dal fatto che lo stock sia licenziato.
   → Serve: riprese reali degli appartamenti in gestione (sostituzione in Canva da parte del titolare), oppure visual puramente tipografico/astratto senza immobili riconoscibili. Da verificare nello stesso passaggio l'assenza di loghi di terzi negli interni ripresi (elettrodomestici, smart TV con servizi di streaming) — vedi `brand-assets/README.md`.

## Osservazioni (non bloccanti, ma da considerare)

- **CTA senza canale.** La sequenza `Scrivici` → `Scrivi CALCOLO` → `CALCOLO` non dice mai *dove*. `riferimento-1.md` specifica «Scrivi CALCOLO **in DM**». Su un reel, senza il canale la keyword finisce nei commenti e la conversazione si perde.
- **Area geografica incoerente tra due slot.** Riga 39 «Ostia, Roma e litorale», riga 49 «a / Ostia e Roma». Se compaiono entrambe nello stesso reel, allineare la formula.
- **Ordine di apparizione (Aperti punto 2).** La catena PUNTEGGIO→PREZZO è l'intero angolo: se il template la fa uscire fuori sequenza il reel non veicola nulla. Da verificare in anteprima Canva **prima** della pubblicazione, non dopo — va trattato come step di consegna, non come nota aperta.
- **Refuso nella prosa del documento** (non a schermo): riga 12 «entrano e escono» → «entrano ed escono».
- **Completezza di campagna.** La cartella contiene il solo `copy.md`: mancano brief di ricerca e direzione artistica, il contenuto non è nel Master Template (`.claude/reference/master-template.md`, preferenza fissa 7) e la campagna non ha una riga in `campagne/INDEX.md`. Con l'angolo «recensioni» già presente in due campagne (righe 14 e 16 dell'INDEX), l'inserimento serve anche a non ripetersi.

## Lessico di brand

Nessun errore. Verificati puntualmente:

| Regola | Esito |
|---|---|
| «Guadagniamo solo se guadagni tu» (mai «guadagni solo se…») | Corretto, riga 48 |
| Mai «hotel-style» → «standard alberghiero» | Corretto, riga 37 |
| Nessuna struttura singola nominata | Nessun nome presente — ma vedi bloccante 2: il claim sopravvive senza il nome |
| Nessun numero non verificato a schermo | Confermato: tutti gli slot numerici del template originale ($685,000, 2,150 Sq Ft, 4 Beds, +123-456-7890) sono stati riassegnati a testo di concetto. Buon lavoro di bonifica |

## Coerenza col tono Hadrianus

**In linea**, con una deriva localizzata. La costruzione per parole singole martellate (PUNTEGGIO → POSIZIONE → … → PREZZO) e la chiusura «Non è fortuna. / È metodo. / È lavoro.» riprendono fedelmente `riferimento-2.md` riga 13 («Non si tratta di fortuna, ma di un metodo alberghiero») — è l'asse giusto del brand.

La deriva è sul finale commerciale: `riferimento-1.md` chiude con cautela e concretezza («simulazione gratuita», «il 15% che paghi, per il 100% di stress che non paghi più»), mentre qui «Ti diciamo quanto puoi guadagnare / Senza impegno» scivola verso un registro da lead magnet generico. Correggendo il bloccante 3 la frase rientra da sola nel tono.

Segnalo anche un'occasione mancata, non un errore: la commissione 15% — l'elemento più concreto e distintivo dell'offerta, presente in entrambi i riferimenti — non compare in nessuno slot. È un dato verificato e disponibile, e in un reel che argomenta «è lavoro» darebbe sostanza dove ora c'è solo affermazione.
