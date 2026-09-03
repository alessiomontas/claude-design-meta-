# Direzione artistica — Fai-da-te vs gestione professionale

## Mood

**Riconoscente, concreto, mai da SaaS.** Tre aggettivi guida:

- **Concreto** — l'angolo è il costo-opportunità del tempo, quindi la grafica deve mostrare *scene* (il messaggio a cena, il calendario fermo), non concetti astratti o icone generiche.
- **Riconoscente della fatica**, non paternalistico — il target ha già imparato a fare tutto da solo. Niente toni "ti salviamo noi", niente esclamativi da urgenza. Il busto di Adriano in Storia 3 fa da "sigillo" di autorevolezza, non da badge trionfalistico.
- **Sobrio, mai da tabella comparativa** — il brief vieta esplicitamente il linguaggio "noi vs loro" da property-management SaaS (già lo standard del settore). Niente check/cross a due colonne, niente elenco di feature con icone ripetute: la metafora visiva scelta (lo "scontrino"/il conto) sostituisce la tabella comparativa con qualcosa di più personale e coerente col titolo del carosello.

## Palette

Fumè caldo + oro, invariata rispetto al design system (mai blu navy):

- **Base scura** `#3F3A33` / `#2E2A25` (gradient radiale nelle slide "hero" e di chiusura) — usata per le scene di tensione (problema, agitazione, hook, CTA).
- **Oro** `#C8A24B` — CTA, spina verticale del "ledger", cifra "15%", bordo del sigillo circolare, dettagli check.
- **Sabbia chiara** `#F5F0E6` — riservata **a una sola slide** (Carosello 4, "Soluzione"): il passaggio a sfondo chiaro in mezzo a quattro slide scure è la mossa deliberata per segnare il momento di sollievo ("lo facciamo noi"), invece di tenere tutto uniformemente scuro come nelle campagne precedenti.

Motivazione: il target non ha bisogno di essere rassicurato con toni chiari e pastello (non è un principiante impaurito) — la base resta scura/istituzionale per quasi tutta la sequenza, e il chiaro si guadagna solo nel momento in cui il messaggio lo giustifica.

## Formati per canale

- **3 storie Instagram** (autoconclusive, mai a carosello): 1080×1920, ciascuna con gancio + risoluzione + CTA sullo stesso frame.
- **Carosello feed "Il conto che non hai mai fatto"**: 5 slide, 1080×1350.

## Pattern scelto (nuovo rispetto alle campagne precedenti)

Consultata la tabella "Pattern di layout già usati" in `.claude/reference/design-system.md` prima di iniziare — `gestione-case-vacanza-proprietari` usa box citazione+risposta e griglie 2×2/checklist; `instagram-fiducia-proprietari` usa virgolette giganti e step numerati. Per differenziarsi, questa campagna introduce due dispositivi nuovi:

**Storie — un "device" concreto diverso per ognuna, mai il box con bordo sinistro oro già usato due volte:**
- **Storia 1** — mockup di notifica (card "Ospite · 22:47") sopra il gancio, per rendere fisico "hai risposto mentre eri a cena".
- **Storia 2** — striscia calendario 7 giorni (grid CSS), un giorno cerchiato in oro con icona "pausa" per il prezzo fermo — nessun numero/prezzo inventato, solo il segnale visivo di stagnazione.
- **Storia 3** — sigillo circolare con la foto reale del busto di Adriano (`brand-assets/logo/logo-bronzo-frontale.jpg`, ritagliato e ricompresso in `grafiche/hadrianus-bust.jpg`), bordo oro, leggermente ruotato: il momento in cui il proprietario "passa il testimone" a un metodo autorevole, non a un tool.

**Carosello — griglia "scontrino/ledger":** ogni slide ha una riga tratteggiata (perforazione) in alto e in basso, un'etichetta "Voce 0X / 05" al posto del solito "01/05 + Scorri" in basso, e una spina verticale oro a sinistra del blocco di testo (invece del box a bordo sinistro). Slide 2 (problema) usa leader tratteggiati orizzontali come voci di conto; Slide 4 (soluzione) inverte la palette a sfondo chiaro; Slide 5 chiude con una doppia riga oro (il "totale" del conto) sopra il "15%" gigante. La metafora resta coerente con il titolo "Il conto che non hai mai fatto" senza mai diventare una tabella comparativa.

## Elementi chiave (gerarchia)

- **Storie**: il "device" concreto (notifica/calendario/sigillo) è il primo punto di attenzione, subito sopra il gancio in Archivo 900; la risoluzione resta testo semplice su sfondo (niente card), la CTA oro piena chiude ogni frame.
- **Carosello**: la spina oro guida l'occhio dall'alto in basso su ogni slide; l'etichetta "Voce 0X/05" in alto a destra sostituisce la paginazione classica; l'ultima slide porta il "15%" come punto focale assoluto, preceduto dalla doppia riga che lo presenta come "il conto finale".
- **CTA**: sempre 'Scrivi "CALCOLO" in DM' — pillola oro piena, mai outline, per restare l'unica azione richiesta su ogni frame.

## Da evitare

- Box con bordo sinistro oro (già pattern ricorrente in `gestione-case-vacanza-proprietari` e implicito nel design system) — qui sostituito dalla spina verticale e dai leader tratteggiati.
- Tabelle comparative "noi vs loro" o liste di feature con icone ripetute in griglia — il brief lo segnala come linguaggio già saturo nel settore.
- Numeri di tempo risparmiato o percentuali di fatturato non verificati in grafica (es. "risparmi X ore") — nessuna cifra di questo tipo è stata inserita, coerente con `copy.md` e `brief-mercato.md`.
- Tono "hotel-style" nei testi eventualmente aggiunti in fase di editing — sempre "standard alberghiero".
- "Guadagniamo solo se guadagni tu" mai in apertura — resta in Storia 3 e nella slide 5 di chiusura, coerente col copy.

## Grafiche editabili

Canvas Claude Design pubblicato: **https://claude.ai/code/artifact/5eb14ede-98c5-49da-9141-8da2cf491dd2**

8 artboard editabili (canvas pan/zoom, click-to-select, testo modificabile inline):

- `Main.dc.html` — Storia 1 "Il tempo che non ti paga nessuno"
- `Storia2.dc.html` — Storia 2 "Il margine che non vedi"
- `Storia3.dc.html` — Storia 3 "Hai già imparato. Non devi più farlo per sempre" (con `hadrianus-bust.jpg`, ritaglio del logo reale)
- `Slide1.dc.html` … `Slide5.dc.html` — Carosello "Il conto che non hai mai fatto"
- `canvas.json` — layout del canvas (storie in riga sopra, carosello in riga sotto)

Sorgenti in `campagne/fai-da-te-vs-gestione-professionale/grafiche/` (inclusa l'immagine ritagliata `hadrianus-bust.jpg`, 460×460, ~30KB, derivata da `brand-assets/logo/logo-bronzo-frontale.jpg`).
