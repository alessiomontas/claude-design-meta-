# Revisione marketing & design — Giornaliero 2026-09-16 "Il costo del vuoto"

## Giudizio complessivo
**PRONTA CON RITOCCHI** — l'angolo è il più forte della settimana e la variante chiara funziona, ma C3 (la slide che dovrebbe essere salvata) ha una collisione tipografica visibile e le due storie hanno la CTA sotto la barra di risposta di Instagram: due difetti che si vedono a occhio nudo e vanno chiusi prima della consegna.

## Punteggio per dimensione
| Dimensione | Giudizio | Nota chiave |
|---|---|---|
| Impaginazione/layout | ⚠️ | Collisione reale in C3 (riga 03 su riga 04); CTA storie oltre la safe area; vuoti morti in fondo a C2 e F2 |
| Contenuti/struttura | 👍 | Progressione problema → dato → modulo → ribaltamento → offerta completa e pulita; il modulo ripetuto 3 volte su 10 artboard è l'unico eccesso |
| Grafiche/foto | ⚠️ | Sistema cromatico chiaro impeccabile e regola oro rispettata ovunque; le foto sono il punto debole (C1 e S1 contraddicono il messaggio "casa chiusa") |
| Testi | 👍 | Hook, negazione e "nessuno te l'ha mai messo su una riga sola" sono tono Hadrianus puro; due CTA in conflitto su F1 |
| Efficacia commerciale | 👍 | Il modulo vuoto è un vero meccanismo di salvataggio, non una grafica incompleta — a patto dei ritocchi 1 e 3 |

## Le due novità del giorno — verdetto esplicito

**1. Fondo bianco caldo.** Regola rispettata: nessun testo in `#C8A24B` in tutti e 10 gli artboard, oro acceso solo come superficie (bande CTA, celle piene, fili, freccia, spunte), parole in oro sempre `#86692A`. Verificato nei `.dc.html`, non solo nei PNG. Il pacchetto **resta riconoscibile come Hadrianus** accanto al 14 e 15 settembre: lockup, Archivo/Manrope, raggio 24, margine 64, banda CTA a pillola e la coppia sabbia/oro sono identici — cambia la luce, non l'identità. Unica deriva: il badge 15% di C5 è a contorno con riempimento al 18% mentre il layout lo dichiara **oro pieno**; è l'unico elemento che si legge "beige su beige" e indebolisce il punto commerciale più importante della slide.

**2. Il modulo a caselle vuote.** **Funziona**, e per un motivo preciso: c'è la riga `Non ci sono cifre nostre: questo conto è solo tuo.` e la CTA `SALVA QUESTA SLIDE`. Sono quelle due righe a trasformare il campo vuoto da errore in gesto richiesto. Senza di esse sarebbe letto come artboard non finito. Il rischio non è annullato però: il **TOTALE IN UN ANNO in banda oro con la riga vuota** è l'elemento più grande e più vuoto della slide, ed è l'unico punto dove un lettore veloce può pensare "manca il numero". Va difeso meglio (ritocco 3). Sull'originalità: è diverso dallo **scontrino/ledger** (nessuna perforazione tratteggiata, nessun leader punteggiato, nessun "Voce 0X/05", e soprattutto nessun totale calcolato da noi — lì il totale era il climax, qui è il buco). Regola "varia il design" rispettata verso l'esterno; **non** rispettata verso l'interno: lo stesso modulo compare identico in C3, F2 e S1.

**Coerenza col pilastro IL NUMERO**: rispettata, ma al limite. L'unico numero stampato con fonte è il 27,2% ISTAT, e sta solo in C2 e F1. Il resto è un elenco di voci. Il pilastro regge perché il numero del giorno è *quello che manca* — ma è una lettura raffinata, e funziona solo se il modulo viene percepito come conto da fare (vedi ritocco 3).

## Interventi prioritari (in ordine di impatto)

1. **C3 — collisione tipografica sulla slide da salvare.** `grafiche/C3.dc.html` / `grafiche/build.py` (righe del modulo, altezza 104 px): la voce `Quote condominiali ordinarie` a 45 px va a capo su due righe, spinge il dettaglio `Sui millesimi, non sulle presenze` **sopra il separatore della riga 04**, dove viene tagliato dalla linea. È il difetto più grave del pacchetto perché sta esattamente sull'artboard che chiedete di screenshottare. Fix minimo: usare in C3 la stessa dicitura già usata in F2/S1 — **`Quote condominiali`** come voce e **`Ordinarie, sui millesimi, non sulle presenze`** come dettaglio — così la riga torna su una linea sola.

2. **S1 e S2 — CTA sotto l'interfaccia di Instagram.** `S1.dc.html:24` (banda a `top: 1700px`, fine 1808) e `S2.dc.html:24` (`top: 1660px`, fine 1768). La safe area dichiarata dal vostro stesso layout è **1600 px**: la barra "Invia messaggio" copre entrambe. La CTA del giorno, che è l'unica azione, oggi non si vede sul telefono. Portare la banda CTA a chiudere entro y 1600 (es. `top: 1470px`) e risalire di conseguenza firma e riga 15%.

3. **C3 — difendere il totale vuoto.** La riga `Non ci sono cifre nostre: questo conto è solo tuo.` sta **sotto** la banda oro, in Manrope 500 grigio: è la riga che disinnesca l'ambiguità e oggi è la più debole della slide. Spostarla **sopra la banda del totale** e portarla a Manrope 600 `#2E2A25`. In alternativa, aggiungere dentro la banda oro, a sinistra del campo, il micro-testo `scrivilo tu` — un solo gesto e il vuoto diventa istruzione.

4. **C1 e S1 — le foto contraddicono il copy.** `png/Main.png`: salotto arredato, cuscini, fiori freschi, piante curate, riviste sul tavolino = una casa **abitata e vissuta**, sotto il titolo "La tua casa chiusa". `png/S1.png`: letto rifatto in controluce dorato, registro da catalogo tessile, e il blocco è così basso (banda ~300 px) che non si capisce cosa sia. F1 è l'unica foto giusta — stanza vuota, pavimento nudo, luce ferma — ed è la prova che l'angolo aveva bisogno di *vuoto*, non di comfort. Sostituire le foto di C1 e S1 con scatti della stessa famiglia di F1 (stanza vuota, tapparella abbassata, luce che entra a strisce), già coperti dal prompt EN in `copy.md`. Nota: la finestra di F1 mostra tetti e montagne chiaramente non romani — accettabile, ma se esiste un'alternativa va preferita.

5. **F1 — due CTA in conflitto.** `F1.dc.html:23-24`: banda `SCRIVI CALCOLO IN DM` e sotto `SALVA QUESTO POST` in oro spaziato. Sono due azioni diverse a 60 px di distanza e si annullano. Tenere solo `SCRIVI CALCOLO IN DM` (il "salva" vive già in C3 sul carosello, che è il posto giusto per chiederlo).

6. **C5 — il badge del 15% non si vede.** `C5.dc.html:17`: contorno `#C8A24B` 2 px + fondo `rgba(200,162,75,0.18)` + testo `#86692A`. Sulla slide dell'offerta, il prezzo è l'elemento che deve staccare per primo dopo il titolo, e oggi è il più tenue. Portarlo a **oro pieno `#C8A24B` con testo `#2E2A25`**, come dichiarato nel layout di `copy.md:312` e come già fatto nelle bande CTA.

7. **C2 e F2 — vuoti morti in fondo.** `png/C2.png`: fra la chiusura "È come è fatto il Paese." e la riga fonte c'è circa un quinto di slide vuota, e **manca l'indicatore `→ SCORRI`** presente su C1 e C4: sulla slide 2, che è il punto di caduta del carosello, è proprio lì che serve. `png/F2.png`: sotto il filo oro resta circa il 15% dell'immagine vuoto senza motivo. In entrambi i casi: ridistribuire il blocco verso il centro ottico, e su C2 aggiungere l'indicatore di scorrimento.

8. **Il modulo compare tre volte identico** (C3, F2, S1). Chi vede il carosello, il post Facebook e la storia nello stesso giorno vede tre volte la stessa tabella. Differenziare almeno **S1**: sulla storia bastano **3 voci** (IMU, tassa rifiuti, contatori) senza campo `€`, guadagnando lo spazio verticale che serve al ritocco 2. La storia è il formato dei 2 secondi: cinque righe con campi da compilare non si leggono e non si compilano.

9. **Reel — consegna incompleta rispetto allo standard.** In `reel/` ci sono `build_reel.py`, `reel.html` (animazione unica) e l'MP4; **mancano gli artboard `.dc.html` una per scena** e la **copertina**, che il design-system richiede per ogni reel. Sul merito: i primi due secondi reggono davvero — frame 0 già in movimento, cancellatura oro e rullo su `Falso.` sono quattro eventi reali, non finti. La lista che si accumula scalando a 0,86/opacità 0,45 non affolla e il loop chiude (frame 0 ≡ 16,98). Un solo appunto di ritmo: fra 7,0 e 9,6 s ci sono **tre pause ravvicinate** (immobilità a 7,0, serranda a 8,6, quadrante a 9,6) proprio dove il reel deve accelerare verso l'offerta; accorciare la pausa 7,0-7,4 a 200 ms e la 9,6-10,0 a 250 ms.

10. **Allineare `copy.md` al prodotto finale** (evita che la prossima modifica reintroduca errori corretti): `TOTALE ALL'ANNO` → `TOTALE IN UN ANNO`; F1 ha la CTA in DM oltre al "salva"; C5 non ha la riga di corpo `La nostra voce compare solo a incasso avvenuto.`; S1 non ha i servizi né `Si parte da com'è`; S2 usa il kicker `PERCHÉ SUCCEDE`, assente dal layout.

## Cosa funziona già bene (da non toccare)
- **L'angolo.** "Non costa zero, l'hai solo sempre visto diviso in cinque pezzi" è la riga migliore prodotta in tre giorni: nomina una cosa che il proprietario sa e non ha mai contato, senza dargli del distratto.
- **La rinuncia al totale.** Non pubblicare una media inventata è la scelta che protegge il brand dai commenti scettici e che, per una volta, *aumenta* la persuasione invece di ridurla. Non tornarci sopra nemmeno se il titolare chiede "un numero indicativo".
- **C4 / F3, il ribaltamento.** Fascia sabbia → freccia oro → fascia oro piena: è l'artboard più chiaro del pacchetto e spiega il modello di business in cinque secondi senza dire una cifra.
- **La CTA `Scrivi CALCOLO in DM`.** È credibile proprio perché il pacchetto non ha promesso numeri: chiede il calcolo, non promette un rendimento. Coerente con "Guadagniamo solo se guadagni tu".
- **Il rischio percepito è basso**: 15% solo a incasso avvenuto, "il primo passo è una valutazione, non un cantiere", nessun costo d'avvio promesso. Resta un solo blocco vero per il proprietario — *cosa succede dopo che scrivo CALCOLO* — che oggi nessun artboard dice.

## Suggerimenti opzionali (nice-to-have)
- Su C5, sotto la CTA, una riga da 28 px: `Ti rispondiamo con le domande giuste, non con un preventivo.` Toglie l'ultima frizione (paura del pitch) senza promettere nulla di quantificabile.
- S2, barra dei 12 mesi: 4 celle piene su 12 si leggono come un tasso di occupazione del 33%. Portarle a 5 non consecutive azzera la lettura numerica, coerente con l'osservazione già sollevata da compliance.
- Il commento Facebook `quante di queste cinque voci paghi: 3 o 5?` è un ottimo innesco: vale la pena fissarlo come primo commento anche sul carosello Instagram.
