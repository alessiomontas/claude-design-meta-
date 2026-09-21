# Modelli e ganci — catalogo per property manager

Catalogo di riferimento, da consultare **prima** di scegliere il formato di un contenuto nuovo.
Non sostituisce `reel-virali.md` (che resta il manuale di *montaggio*, secondo per secondo):
qui c'è la mappa dei **modelli disponibili** e dei **ganci** che ciascuno regge.

**Come è stato costruito (21/09/2026).** Ricerca web sulle strutture virali del formato corto
2026 + i formati già codificati in `reel-virali.md` + i 25 angoli già usati in `campagne/INDEX.md`.

**Due limiti della ricerca, dichiarati.**
1. **La libreria pubblica dei template Canva non è interrogabile da qui.** `search-brand-templates`
   sull'account torna vuoto, e `search-designs` vede solo i design già tuoi. Un template Canva
   entra nel flusso **solo** se il titolare lo applica a un progetto e ne manda il link `/edit`.
   Quindi «modelli» in questo documento significa **modelli di contenuto**, non file Canva.
2. **L'egress di rete blocca la maggior parte dei siti** consultati (opus.pro, socialync,
   virvid, jamilacademy, multihousingnews e altri). Ho i riassunti dei motori di ricerca, non
   le pagine intere. Dove un numero viene dal web è marcato `[web]`; dove è prassi di settore
   senza misura, `[opinione di settore]`. **Nessun numero qui va copiato dentro un contenuto**
   senza passare dalle regole di `CLAUDE.md`.

---

## 0. Le tre regole che valgono per ogni modello

1. **Il gancio sta nei primi 3 secondi, 10-14 parole.** Un reel che tiene oltre il 60% degli
   spettatori dopo il terzo secondo ha molta più probabilità di essere spinto dai feed `[web]`.
2. **Hook → corpo → payoff.** Il payoff non è la CTA: è la cosa che lo spettatore è rimasto a
   vedere. La CTA viene dopo, e se manca il payoff non converte comunque.
3. **Durata utile 15-30 s**, con l'algoritmo che favorisce la fascia 20-25 s `[web]`.
   Sotto i 15 s il gancio non ha profondità, sopra i 45 s la ritenzione crolla. La nostra serie
   da 8 s è un'eccezione voluta (vedi `modello-reel-8-secondi.md`), non la norma.

---

## 1. I dodici modelli

Otto sono già codificati in `reel-virali.md` (§1.1-1.8) e qui sono solo richiamati con i ganci
che reggono. Quattro sono nuovi e non ancora usati da Hadrianus.

### Già codificati

| # | Modello | Obiettivo | Ganci che regge | Stato |
|---|---|---|---|---|
| M1 | **Lista negata** — «non è quello che pensi» | salvataggi, condivisioni | Negazione, Contrarian | usato (reel 8 s, 15 s) |
| M2 | **Prima/dopo a tendina** ×3 | condivisioni | Trasformazione, Errore | usato (giornaliero 14/09, foto annuncio) |
| M3 | **Checklist che si compila da sola** | **salvataggi** | Lista numerata, Promessa | usato (7 controlli) |
| M4 | **Finta interfaccia** (calendario, notifiche, chat) | **contatti in DM** | Prova, Curiosità | usato (calendario prezzi 15/09) |
| M5 | **Split screen permanente** | condivisioni | Confronto, Contrarian | usato (agosto/novembre 17/09) |
| M6 | **Contatore che sale** | attenzione su formati cortissimi | Numero, Costo nascosto | usato (costo del vuoto 16/09) |
| M7 | **Micro-tour a parallasse** | desiderabilità (non conversione) | nessuno da solo | usato come inserto |
| M8 | **Kinetic type puro** | nessuno da solo — solo ponte 1-2 s | — | vietato da solo |

### Nuovi — non ancora usati

| # | Modello | Obiettivo | Perché funziona qui | Meccanica |
|---|---|---|---|---|
| **M9** | **La catena** — parole singole che si concatenano | condivisioni + completion | Ogni parola è una promessa che la successiva mantiene. Nessun numero necessario: il senso sta nella sequenza. | 5-6 parole grandi, una per stacco, 0,8-1,0 s l'una, colore oro crescente. È il modello del reel `reel-catena-recensioni`. |
| **M10** | **Il conto alla rovescia dell'errore** — «3 cose che stai sbagliando», dalla meno alla più grave | salvataggi | Il crescendo obbliga ad arrivare in fondo: la #1 è la ragione per restare. Inverte la listicle normale. | Numero grande in alto che **scende** 3→2→1, la riga sotto cambia. Ultimo blocco senza numero: è la soluzione. |
| **M11** | **La domanda che resta aperta** — si pone un problema e si risponde solo a metà | **commenti in DM** | Il commento è il modo per chiudere il loop. È il modello che genera conversazioni, non like. | Gancio interrogativo a schermo pieno → 2-3 elementi di risposta → l'ultimo è esplicitamente rinviato alla DM. Rischio: se abusato si legge come clickbait. Massimo uno ogni due settimane. |
| **M12** | **Il documento che si annota** — un finto annuncio/contratto/estratto su cui compaiono cerchiature e frecce | salvataggi + autorevolezza | Legge come «analisi», non come pubblicità. È il formato che dimostra competenza senza affermarla. | Mock disegnato in HTML (mai un annuncio reale di terzi, mai un nome), su cui entrano 4-5 annotazioni in oro con tratto disegnato (`stroke-dashoffset`). Parente di M4 ma statico e più denso. |

---

## 2. Le nove famiglie di gancio

Per ognuna: il meccanismo, e **ganci scritti per Hadrianus** — pronti, in italiano, che rispettano
il lessico di brand. Quelli marcati ⛔ sono già usati e non vanno ripetuti.

### G1 — Negazione dell'aspettativa
Apre dicendo che la cosa ovvia è falsa. Il cervello deve restare per sapere cosa è vero.
- ⛔ «I proprietari non cercano un property manager.»
- «Non è la casa che non rende. È il calendario.»
- «Non stai perdendo prenotazioni. Non ti stanno proprio vedendo.»
- «Il problema non è agosto. È che ti sei abituato ad agosto.»
- «Non ti serve abbassare il prezzo. Ti serve smettere di essere l'ultimo della lista.»

### G2 — Affermazione contraria (contrarian)
Dichiara il contrario del senso comune del settore. `[web]` è una delle tre formule più virali del 2026.
- «Le recensioni a cinque stelle non fanno prenotare. Fanno pagare di più.» (variante di ⛔ 18/09)
- «Una casa vuota costa più di una casa che rende poco.»
- «Il mese peggiore dell'anno è quello in cui sei pieno.»
- «Più foto metti nell'annuncio, meno prenoti.»
- «Il minimo di due notti ti sta costando più di quanto ti fa guadagnare.»

### G3 — Avviso di errore (mistake warning)
«Stai sbagliando X.» Autorilevanza immediata. `[web]` seconda formula più virale.
- ⛔ «Sei errori che fanno perdere prenotazioni.» (Facebook)
- «Se rispondi in due ore, hai già perso quella prenotazione.»
- «Tre righe del tuo annuncio stanno filtrando via gli ospiti che pagano di più.»
- «Hai messo il check-in alle 16. Ecco chi hai appena escluso.»
- «Stai fotografando la casa vuota. Si prenota quella apparecchiata.»

### G4 — Lista numerata (list tease)
Promette un elenco finito. `[web]` terza formula; è **il** gancio da salvataggi.
- ⛔ «I sette controlli prima di ogni check-in.»
- «Le quattro cose che un ospite guarda prima del prezzo.»
- «Cinque voci che paghi anche a casa chiusa.»
- «Tre righe da togliere dall'annuncio, stasera.»
- «Le due date di ottobre che decidono il tuo novembre.»

### G5 — Numero secco
Un numero è l'unica cosa che non si guarda a metà: si aspetta che si fermi.
**Regola dura**: ogni numero è un claim. Solo verificati, o `[DATO DA VERIFICARE]` e non si pubblica.
- «15%.» (l'unico numero sempre verificato dell'offerta)
- «Zero costi fissi.» — ⚠️ **da verificare col titolare se è letteralmente vero**, è ancora aperta
- «Dodici mesi. Non tre.»
- «Una notte vuota fra due prenotazioni. Ogni settimana.»

### G6 — Confronto
Leggibile da fermo, in qualsiasi fotogramma: alza il completion perché chi apre a metà capisce.
- ⛔ «Agosto contro novembre.»
- ⛔ «Affitto lungo contro breve.»
- «La tua settimana. La nostra settimana.»
- «Quello che vedi tu nell'annuncio. Quello che vede il portale.»
- «Chi prende una percentuale sul lordo. Chi la prende sull'incassato.» *(mai nomi di concorrenti)*

### G7 — Costo nascosto
Rende visibile una perdita che il proprietario non contabilizza. È la leva più forte su chi già gestisce da solo.
- ⛔ «Il costo del vuoto: cinque voci che paghi comunque.»
- ⛔ «Il conto che non hai mai fatto» (ore del fai-da-te)
- «Quanto ti costa rispondere tu ai messaggi. In ore, non in euro.»
- «Il mese di giugno che devi rifare da capo ogni anno.»
- «Ogni notte singola che resta vuota fra due prenotazioni è un prezzo che hai già pagato.»

### G8 — Prova / dietro le quinte
Mostra il lavoro invece di affermarlo. Nessuna promessa, quindi nessun claim da verificare.
- ⛔ «Superhost in due mesi su una casa non nostra.»
- ⛔ «Questa casa non esiste. Lo standard, sì.»
- «Ore 11. Check-out. Ore 15. Check-in. Cosa succede in mezzo.»
- «Il messaggio che mandiamo il giorno prima dell'arrivo.»
- «Cosa guardiamo quando entriamo in una casa per la prima volta.»

### G9 — Domanda diretta
Bassa resa in reach, alta in commenti/DM. Usarla con parsimonia.
- «Quanto rende la tua casa a novembre? Scrivilo, te lo dico io se è poco.»
- «Hai un minimo di notti? Quanto?»
- «Da quanto tempo non cambi la prima foto dell'annuncio?»

---

## 3. Matrice modello × obiettivo

Quale modello scegliere in base a cosa serve **quella settimana**.

| Obiettivo | Modelli migliori | Ganci che li alimentano |
|---|---|---|
| **Reach su chi non ci segue** (inoltri in DM) | M2, M5, M9 | G2, G6 |
| **Salvataggi** (contenuto utile fuori dal momento) | M3, M10, M12 | G3, G4, G7 |
| **Contatti in DM** | M4, M11 | G5, G9 |
| **Autorevolezza / differenziazione** | M12, M8-dentro-M4 | G8 |
| **Riempire la serie senza consumare angoli** | M6, M7 | G5 |

**Rotazione consigliata su quattro settimane**, per non consumare tutto: una da salvataggi (M3/M10),
una da condivisioni (M2/M5/M9), una da contatti (M4/M11), una da prova (M12/M8-in-M4).
`[opinione di settore]`: i creator che tengono ruotano 5-10 formule, non una sola.

---

## 4. Venti angoli ancora liberi

Costruiti incrociando le famiglie di gancio con i pain point in `brand-identity.md`, ed
**esclusi** tutti i 25 già registrati in `INDEX.md`. Ordinati per forza stimata.

| # | Angolo | Gancio | Modello | Note |
|---|---|---|---|---|
| 1 | La velocità di risposta come fattore di prenotazione | G3 | M4 | Meccanismo di piattaforma, verificabile come prassi; niente percentuali |
| 2 | Le tre righe dell'annuncio che filtrano via gli ospiti alto-spendenti | G3 | M12 | Mock di annuncio disegnato, mai reale |
| 3 | La notte singola orfana fra due prenotazioni | G7 | M4 | Calendario mock, senza importi |
| 4 | Il minimo di notti come costo, non come tutela | G2 | M5 | Già toccato in una storia 14/09: qui diventa contenuto pieno |
| 5 | L'ora del check-in e chi esclude | G3 | M10 | Conto alla rovescia 3→1 |
| 6 | Cosa guardiamo alla prima visita in una casa | G8 | M3 | Puro valore, alto salvataggio |
| 7 | Il calendario eventi di Roma come leva | G4 | M4 | **Già segnalato come libero in INDEX.md** |
| 8 | Retention/referral per proprietari già clienti | G9 | M11 | **Già segnalato come libero in INDEX.md** |
| 9 | Le quattro cose che l'ospite guarda prima del prezzo | G4 | M3 | |
| 10 | La casa apparecchiata contro la casa vuota in foto | G2 | M2 | Prima/dopo, mai casa di cliente riconoscibile |
| 11 | Il messaggio pre-arrivo come pezzo di lavoro | G8 | M12 | Mock di chat |
| 12 | Cosa succede fra un check-out e il check-in successivo | G8 | M3 | Il formato «ore 11 → ore 15» |
| 13 | Perché il prezzo è l'ultima leva, non la prima | G2 | M9 | Catena, parente del reel 21/09 — verificare distanza |
| 14 | La manutenzione che scopri solo se qualcuno entra ogni settimana | G7 | M6 | |
| 15 | Il proprietario che gestisce due case e non ne gestisce bene nessuna | G1 | M5 | |
| 16 | Chi risponde alle 23 di sabato | G6 | M5 | La tua settimana / la nostra |
| 17 | Le foto fatte col sole sbagliato | G3 | M2 | Complementare al 14/09, non uguale |
| 18 | Cosa cambia nel calendario il giorno dopo la firma | G8 | M4 | |
| 19 | L'annuncio che non si aggiorna da un anno | G3 | M12 | |
| 20 | «Quanto rende a novembre?» — stima chiesta in DM | G9 | M11 | Variante reel della meccanica Facebook già usata |

---

## 5. Cosa non è un modello

- **Kinetic type da solo** (M8): senza volto e senza voce degrada subito. Solo come ponte.
- **Parallasse oltre 3 s per stanza** (M7): definizione di reel povero.
- **Una sola tendina prima/dopo**: il formato regge a tre coppie incalzanti, non a una.
- **Lista che si sostituisce invece di accumularsi** (M3): sembra una presentazione.
- **Qualunque modello con un numero non verificato a schermo**: non è un modello, è un blocco
  di compliance che arriva dopo.
