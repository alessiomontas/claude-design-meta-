# Direzione artistica — Facebook: affitto lungo vs gestione totale in affitto breve

## Mood

**Documentale, tecnico, non-difensivo.**

Il pubblico sono proprietari dentro gruppi Facebook: competenti, già scottati, allergici alla pubblicità. Riconoscono un'inserzione dalla prima immagine e la puniscono. L'angolo di vendita non è l'urgenza, è **l'autorevolezza verificabile** ("i conti li può rifare chiunque, le norme che cito sono pubbliche"): quindi la grafica non deve *convincere*, deve *documentare*.

Da qui la metafora visiva scelta: **la scheda tecnica / perizia su carta millimetrata**. Griglia di fondo sottile, linee di quota da disegno tecnico, righe orizzontali come separatori, riferimenti normativi in piccolo, numerazione "Scheda 01/03". Nessun angolo arrotondato, nessuna pillola, nessuna emoji: il linguaggio è quello di un documento, non di un annuncio.

La conseguenza pratica è che i numeri non vengono "urlati" ma **quotati**: la cauzione è misurata da una linea di quota con i due estremi a T, il confronto dei canoni è una coppia di barre in scala proporzionale. Su questo pubblico misurare vale più che enfatizzare.

## Palette

Palette fumè caldo di brand (`.claude/reference/design-system.md`), senza deroghe. **Nessun blu navy.**

| Colore | Hex | Dove e perché |
|---|---|---|
| Fumè base | `#3F3A33` | Fondo delle schede 1 e 3. È il colore del problema e della gravità: la scheda del rischio e quella dell'impegno stanno sullo scuro. |
| Fumè profondo | `#2E2A25` | Banda "utenze escluse" nella scheda 2 e vignettatura in basso nelle schede scure. Serve a far pesare la riga più scomoda invece di nasconderla. |
| Oro | `#C8A24B` | Solo tre lavori: le quote/misure, i numeri che il copy autorizza, l'azione. Mai decorativo. Nella griglia millimetrata compare al 6% di opacità, come inchiostro di stampa tecnica. |
| Oro scuro | `#b3892f` | Accenti sul fondo chiaro (scheda 2), per leggibilità. |
| Sabbia | `#F5F0E6` | Fondo pieno della scheda 2. È il **momento di sollievo** del trittico: il confronto dei numeri è l'unica cosa che il lettore deve poter leggere senza sforzo, quindi va su carta chiara. |
| Pietra/oliva | `#9A8A63`, `#8a8577` | Etichette tecniche, numerazione schede, riferimenti normativi. |
| Testi | `#d8d2c4` / `#b7ad9a` su scuro, `#26241F` / `#6f695c` su chiaro | Gerarchia di lettura a tre livelli. |

Ritmo scuro → chiaro → scuro-con-foto: il trittico ha un respiro, non tre schermate identiche.

## Formati per canale

Regola fissa 6 di `CLAUDE.md`, rispettata alla lettera.

- **Immagine 1 — `Main.dc.html`, 1080×1920 (9:16 verticale).** Gancio + il conto della riconsegna. Verticale obbligato: nel collage Facebook un 4:5 viene tagliato ai lati e il titolo si perde.
- **Immagine 2 — `Numeri.dc.html`, 1080×1080 (1:1).** Il confronto dei numeri.
- **Immagine 3 — `Offerta.dc.html`, 1080×1080 (1:1).** Come funziona + CTA, con foto reale di immobile in gestione.

Tipografia: **Archivo** 700-900 per titoli, numeri, etichette maiuscole; **Manrope** 400-600 per il corpo. Nessun terzo font.

## Elementi chiave

**Immagine 1 — cosa si nota per primo:** la headline "Dopo quattro anni ti riconsegnano **le chiavi**" (Archivo 900, 106px, con "le chiavi" in oro). Subito sotto, il colpo: due schede separate da righe sottili.
1. *Deposito cauzionale* → linea di quota oro con l'etichetta "max 3 mensilità", riferimento `art. 11 L. 392/1978` allineato a destra, e la cifra `≈ 2.550 €` in corpo 88 con a fianco "su un bilocale da 850 €".
2. *Normale usura* → descrizione a sinistra, verdetto "A CARICO TUO" in oro a destra.

Chiusura in basso a sinistra, che apre alla seconda immagine: "C'è un altro modo di far rendere la stessa casa. Senza cederla per quattro anni."

> Nota di precisione normativa: l'articolo è citato **solo** accanto al deposito cauzionale, che è ciò che l'art. 11 L. 392/1978 disciplina. La normale usura è una scheda separata, senza riferimento di legge — errore facile e verificabile in dieci secondi da chiunque in quei gruppi.

**Immagine 2 — cosa si nota per primo:** il titolo *"Stesso tipo di immobile, due modi di farlo rendere."* (allineato ai dati: la prima barra è un bilocale a Ostia, la seconda un paniere periferia e litorale — il titolo non può dire "lo stesso bilocale"), poi subito le due barre. Sono in **scala proporzionale onesta** (74% e 87% della larghezza utile, cioè ~850 contro ~1.000), non ridisegnate per esagerare il divario. Ogni barra porta due etichette non ambigue: `LORDI` sulla prima (fumè scuro), `NETTI` sulla seconda (oro). Sotto ciascuna, in corpo piccolo, cosa significa davvero — *"Lordi: le tasse le togli ancora tu"* / *"Netti della nostra commissione, di pulizie, biancheria e consumabili, e della ritenuta fiscale che versiamo noi."*

Sotto la riga "netti", con una barretta oro a sinistra e allo stesso corpo delle altre didascalie (24px, leggibile senza zoom), il **caveat fiscale obbligatorio**: *"La ritenuta non chiude ogni obbligo: la dichiarazione la chiudi con il tuo commercialista."* La grafica circola da sola, quindi il caveat che nel copy sta al punto 2 deve stare anche qui.

**La riga "utenze escluse" è trattata come un elemento di pari rango, non come una postilla:** banda piena `#2E2A25` a tutta larghezza, "UTENZE / ESCLUSE" in Archivo 900 oro, separatore verticale, e la formula ammessa dal compliance: *"Le utenze restano tue. In un affitto lungo le paga l'inquilino, in gestione no."* Nessuna formula assoluta ("una voce sola", "l'unico pezzo di conto"): TARI e oneri condominiali non sono elencati per scelta del cliente, ma la grafica non può affermare che non esistano. Davanti a questo pubblico è il pezzo che compra credibilità: chi legge sta già cercando la fregatura, e la trova dichiarata da noi prima che la trovi lui. **Non va rimpicciolita, spostata in fondo, né resa una nota in grigio.**

Chiusura: la riga di cautela ("media reale, non una simulazione e non una promessa: ogni casa fa storia a sé") e l'up-sell centro Roma/metro, **volutamente senza alcuna cifra**.

**Immagine 3 — cosa si nota per primo:** la foto reale. Banda fotografica 1080×392 in alto (`brand-assets/immobili/cucina-soggiorno-open-space.png`, ritagliata 2.57:1 e ricompressa), con gradiente fumè sopra e sotto per far reggere il testo. In basso sulla foto: "La casa che ti restituiamo" in oro, il titolo *"Pulita e controllata a ogni check-out, secondo lo standard alberghiero."* e, sotto, la riga di processo *"La manutenzione non è un conto che ti arriva tra quattro anni: è un lavoro che si fa dopo ogni soggiorno."* La foto è la prova visiva dello standard alberghiero — il punto 4 del copy diventa qualcosa che si vede. Il gradiente sulla foto è stato reso più profondo nella metà bassa (0.12 al 26%, 0.58 al 52%, 0.94 al 100%) perché la riga di processo resti leggibile.

> Nessuna promessa sullo stato futuro dell'immobile: la grafica descrive **un processo che si ripete a ogni check-out**, mai un risultato garantito. Vietato "rimessa a nuovo", "come nuova", "meglio di come l'hai lasciata".

Sotto, il quadro delle condizioni in tre righe numerate `01/02/03` separate da hairline: 15% sul fatturato senza costi fissi, bonifico il 10, report mensile. Poi la formula esatta di brand in oro, corpo 42: **"Guadagniamo solo se guadagni tu."**

CTA: banda piena oro ad angoli vivi (non una pill — coerente col linguaggio documentale), "Scrivi zona e metratura nei commenti o in privato", con sotto la **simulazione gratuita** ("quanto potrebbe rendere, senza impegno" — formula del lessico di brand, non "proiezione dei guadagni") e la promessa di onestà ("se ti conviene restare sul canone fisso, te lo diciamo noi").

**Scelta della foto:** usata `cucina-soggiorno-open-space.png`. Scartata `smart-tv-streaming-mockup.jpg` per il problema dei marchi di terzi (Netflix/Prime/Disney+ — vedi `brand-assets/README.md`). La foto è illustrativa dello standard, non prova sociale di una struttura nominata.

## Da evitare

- **Blu navy**, in qualsiasi forma. Regola fissa.
- **Toni da inserzione**: cifre giganti isolate su fondo pieno, frecce che urlano, badge "OFFERTA", countdown, emoji. In un gruppo di categoria è il segnale che fa scattare il commento "questa è pubblicità, l'admin dovrebbe cancellarla".
- **Barre non proporzionali** o assi tagliati per gonfiare il divario 850 → 1.000. Questo pubblico rifà i conti e smonta il grafico nei commenti.
- **Nascondere o attenuare le utenze.** Il valore dell'immagine 2 sta esattamente lì.
- **Formule assolute sui costi a carico del proprietario** ("una voce sola", "l'unico pezzo di conto", "tutto il resto è incluso"): TARI e oneri condominiali non sono elencati per scelta del cliente, quindi si possono omettere ma mai smentire.
- **Promesse sullo stato futuro dell'immobile** ("rimessa a nuovo", "come nuova", "meglio di come l'hai consegnata"): in grafica passa solo il processo che si ripete a ogni check-out.
- **"Netti delle tasse"** o qualunque formulazione che faccia credere che la ritenuta chiuda la posizione fiscale del proprietario: la ritenuta è ciò che versiamo noi, la dichiarazione la chiude il suo commercialista — e il caveat va scritto nell'immagine, non solo nel post.
- **Aggiungere cifre non presenti nel copy**, in particolare qualunque numero sul rendimento in centro Roma o vicino alla metro: il claim resta qualitativo per scelta (claim #9 del copy, `[DATO DA VERIFICARE]`).
- **Attribuire l'art. 11 L. 392/1978 alla normale usura**: disciplina il deposito cauzionale.
- **Rendimenti garantiti, percentuali di morosità, tempi medi di sfratto, confronti di aliquote**: nessuno di questi entra in grafica, come già nel copy.
- **Pattern già usati** nelle campagne precedenti: box citazione+risposta, carosello standard a 5 slide, confronto a due colonne, virgolette giganti, step numerati giganti, card domanda/risposta, e la griglia "scontrino/ledger" con perforazione tratteggiata di `fai-da-te-vs-gestione-professionale`. La griglia millimetrata + quote tecniche è deliberatamente altro: **le linee qui sono continue, non tratteggiate**, e i separatori sono orizzontali, non una spina verticale.
- **Foto con marchi di terzi.**

## Grafiche editabili

**Canvas Claude Design (editabile):** https://claude.ai/code/artifact/6578c0a6-83ca-4c08-9488-1fe5fe347b80

Sorgenti in `campagne/facebook-lungo-vs-breve-proprietari/grafiche/`:

| File | Formato | Contenuto |
|---|---|---|
| `Main.dc.html` | 1080×1920 | 1ª immagine — gancio + cauzione/usura |
| `Numeri.dc.html` | 1080×1080 | 2ª immagine — confronto dei numeri + utenze escluse |
| `Offerta.dc.html` | 1080×1080 | 3ª immagine — come funziona + CTA, con foto reale |
| `canvas.json` | — | Layout del canvas, titoli delle artboard e due note di lavorazione |
| `immobile-standard.jpg` | 1080×560 | Ritaglio della foto reale usato nella 3ª immagine |
| `post-facebook-lungo-vs-breve.html` | — | Canvas assemblato (file pubblicato) |

Sul canvas si modificano testo, colori, dimensioni e posizioni di ogni elemento, e si esportano le tre immagini in PNG dalla toolbar (Export). Per rigenerare il canvas dopo una modifica ai sorgenti, si ri-assembla dai `.dc.html` e si ripubblica sullo stesso link.

**Gancio da inserire nella 1ª immagine:** il testo attuale corrisponde al **gancio A** ("La cauzione non basta"), quello consigliato dal copy — verificato dopo le correzioni compliance. Se si ruota sul **gancio C** (il confronto dei numeri) per un altro gruppo, va cambiata la headline dell'artboard `Main` di conseguenza; il resto del trittico regge invariato. Il **gancio B** (tasse sui canoni non incassati) è ritirato dal consegnabile: non deve comparire in nessun artboard.

## Correzioni compliance applicate (4 settembre 2026)

Correzioni di testo, non un redesign: palette fumè, formati (1080×1920 + 2 × 1080×1080) e layout "scheda tecnica/perizia" invariati; nessuna cifra nuova e nessun numero sull'up-sell centro Roma/metro.

| Artboard | Prima | Dopo |
|---|---|---|
| `Numeri.dc.html` | "Lo stesso bilocale, due modi di farlo rendere." | "Stesso tipo di immobile, due modi di farlo rendere." |
| `Numeri.dc.html` | "…di pulizie, biancheria, consumabili e tasse." | "…di pulizie, biancheria e consumabili, e della ritenuta fiscale che versiamo noi." |
| `Numeri.dc.html` | (assente) | Nuova riga di caveat fiscale con barretta oro: "La ritenuta non chiude ogni obbligo: la dichiarazione la chiudi con il tuo commercialista." |
| `Numeri.dc.html` | "Restano a carico tuo… È l'unico pezzo di conto che devi aggiungere da solo." | "Le utenze restano tue. In un affitto lungo le paga l'inquilino, in gestione no." (banda invariata per dimensione e posizione) |
| `Offerta.dc.html` | "Pulita, controllata e rimessa a nuovo a ogni check-out." | "Pulita e controllata a ogni check-out, secondo lo standard alberghiero." + riga di processo sulla manutenzione |
| `Offerta.dc.html` | "una proiezione dei guadagni sulla tua casa" | "una simulazione gratuita sul tuo immobile: quanto potrebbe rendere, senza impegno" |
| `Main.dc.html` | — | Verificato: headline sul **gancio A** (cauzione max 3 mensilità + normale usura). Nessuna traccia del gancio B in nessun artboard. |

Micro-aggiustamenti tipografici solo per far entrare la riga di caveat senza toccare la banda utenze: titolo 58 → 54px, didascalie 25 → 24px, interlinea 1.32 → 1.28, padding del frame 52/48 → 48/44, gap tra le barre 30 → 26px. Le barre proporzionali (74% e 87%) e la banda "UTENZE ESCLUSE" restano identiche.
