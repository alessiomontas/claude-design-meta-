# Design system — Hadrianus

Fonte unica di verità per palette, tipografia, formati e componenti. Leggilo (o fanne `grep`) ogni volta che l'`art-director` costruisce artboard `.dc.html`, invece di ridefinire i colori a memoria — evita drift tra campagne e refusi come il navy che si reintroduce per errore.

## Palette (grigio fumè caldo — MAI blu navy)

| Ruolo | Hex | Uso |
|---|---|---|
| Base scura (fumè) | `#3F3A33` | Sfondi pieni scuri (storie problema/soluzione, card scure) |
| Base scura profonda | `#2E2A25` | Estremo scuro nei gradient radiali |
| Fumè intermedio (gradient) | `#4a443a` | Punto chiaro dei gradient radiali su sfondo scuro |
| Oro accento | `#C8A24B` | CTA, numeri chiave, badge, bordi in evidenza — è SEMPRE il colore dell'azione |
| Oro hover/scuro | `#a8863b` | Hover dei link, varianti pressed |
| Oro scuro per testo su chiaro | `#b3892f` | Testo enfatizzato oro su sfondo chiaro (leggibilità) |
| Chiaro/sabbia (fondo) | `#F5F0E6` | Sfondi chiari, card chiare su sfondo scuro |
| Pietra/oliva (label) | `#9A8A63` | Etichette piccole maiuscolo, kicker |
| Testo scuro su chiaro | `#26241F` | Corpo testo su sfondo chiaro |
| Testo scuro secondario | `#46423a` | Corpo meno enfatizzato su chiaro |
| Testo scuro terziario | `#6f695c` / `#8a8577` | Didascalie, note piccole su chiaro |
| Testo chiaro su scuro | `#d8d2c4` | Corpo testo su sfondo scuro |
| Testo chiaro secondario | `#b7ad9a` | Numerazione slide, note piccole su scuro |
| Testo chiaro terziario | `#cfc7b8` / `#9a8f7c` | Colonna "cosa NON abbiamo" nei confronti, contrasto ridotto |

Gradient scuro standard per sfondi "hero": `radial-gradient(120% 80% at 50% 10%, #4a443a 0%, #3F3A33 55%, #2E2A25 100%)` (angolo/percentuali variano leggermente per artboard, mai il set di colori).

## Tipografia

- **Titoli, CTA, badge, numeri**: `Archivo` (peso 600-900), spesso `text-transform: uppercase` + `letter-spacing` largo per i kicker, peso 900 per headline e numeri giganti.
- **Corpo testo**: `Manrope` (peso 400-700).
- Import standard da includere in ogni `.dc.html` (dentro `<helmet><link>`):
  `https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap`
- Link color di default: `a { color: #C8A24B; } a:hover { color: #a8863b; }`

## Griglia e safe area

Margine laterale 64 px · colonna utile 952 px · safe area 180 px in alto e 320 px in basso (interfaccia dei
social) · passo verticale 20 px · scala tipografica 70·62·50·45·40·33·31·17 su 1080 px di larghezza.
Dettaglio e controllo qualità in `.claude/reference/master-template.md`.

## Formati per canale (dimensioni artboard in px)

| Contenuto | Dimensioni | Rapporto |
|---|---|---|
| Storia Instagram | 1080×1920 | 9:16 |
| Post/slide carosello Instagram | 1080×1350 | 4:5 |
| Cover reel | 1080×1920 | 9:16 |
| Post Facebook — 1ª immagine | 1080×1920 | 9:16 (MAI 4:5, viene tagliata nel collage) |
| Post Facebook — 2ª e 3ª immagine | 1080×1080 | 1:1 |

## Componenti riutilizzabili (snippet pronti)

Header/logo mark (in cima a ogni artboard):
```html
<div style="display: flex; align-items: center; gap: 16px;">
  <div style="width: 40px; height: 3px; background: #C8A24B;"></div>
  <span style="font-family: 'Archivo', sans-serif; font-weight: 800; letter-spacing: 6px; font-size: 30px; text-transform: uppercase;">Hadrianus</span>
</div>
```

CTA pill (piena, oro):
```html
<div style="width: 100%; box-sizing: border-box; text-align: center; background: #C8A24B; color: #2E2A25; border-radius: 999px; padding: 32px; font-family: 'Archivo', sans-serif; font-weight: 800; font-size: 44px;">Scrivi "CALCOLO" in DM</div>
```

CTA pill (outline, per CTA secondaria/"continua"):
```html
<div style="display: flex; align-items: center; gap: 16px; background: rgba(200,162,75,0.16); border: 2px solid #C8A24B; border-radius: 999px; padding: 20px 34px; width: fit-content;">
  <span style="font-family: 'Archivo', sans-serif; font-weight: 700; font-size: 34px;">Scorri</span>
  <span style="font-size: 36px; color: #C8A24B;">→</span>
</div>
```

Box "risposta"/callout (bordo sinistro oro, su sfondo scuro):
```html
<div style="background: rgba(245,240,230,0.06); border-left: 6px solid #C8A24B; border-radius: 14px; padding: 40px 44px;">
  <p style="font-size: 46px; line-height: 1.25; margin: 0; font-weight: 700;">Testo risposta.</p>
</div>
```

Check/cross list item:
```html
<div style="display: flex; align-items: center; gap: 20px;">
  <svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#C8A24B" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
  <span style="font-size: 42px; line-height: 1.2;">Testo punto di forza</span>
</div>
```
(per una "✕" usare `<span style="color:#C8A24B; font-weight:800;">✕</span>` invece dell'svg check)

Badge step numerato (carosello "come funziona"):
```html
<span style="font-family: 'Archivo', sans-serif; font-weight: 900; font-size: 240px; line-height: 0.8; color: #C8A24B;">01</span>
```

Confronto a due colonne (scuro "cosa evitare" / chiaro "cosa abbiamo"):
```html
<div style="display: flex; gap: 26px;">
  <div style="flex: 1; background: rgba(245,240,230,0.05); border: 1px solid rgba(245,240,230,0.14); border-radius: 24px; padding: 40px 34px;">...</div>
  <div style="flex: 1; background: #F5F0E6; border-radius: 24px; padding: 40px 34px;">...</div>
</div>
```

## Pattern di layout già usati (varia rispetto a questi — regola fissa "varia il design")

| Campagna | Storie | Carosello/post |
|---|---|---|
| `gestione-case-vacanza-proprietari` | box citazione+risposta, box checklist scuro | carosello 5 slide standard (intro→problema X-list→servizi grid 2×2→differenza check-list→CTA), confronto 2 colonne |
| `instagram-fiducia-proprietari` | "virgolette" grandi + risposta in card, icona lucchetto | step numerati giganti (Carosello A), card domanda/risposta (Carosello B) |
| `facebook-lungo-vs-breve-proprietari` | — (campagna solo Facebook) | **"blocchi invertiti a piena larghezza"** (versione 2 — la v1 "scheda tecnica/perizia" è stata bocciata dal titolare e non va ripresa): niente card e niente griglia tecnica, ogni immagine è una pila di fasce piene a tutta larghezza che si alternano scuro/chiaro, una fascia = un messaggio; **evidenziatore oro inline** sulla frase chiave come firma grafica; scheda 02 a due colonne secche (cella scura opaca a sinistra ✕, cella chiara piena a destra ✓, 3 righe) con numeri giganti e banda finale con barretta oro; scheda 03 con foto reale sotto gradiente leggibile, processo numerato 01→04 in oro, fascia chiara con le negazioni sui costi, CTA in banda oro piena |
| `fai-da-te-vs-gestione-professionale` | devices per storia (notifica ospite mockup, calendario 7 giorni con giorno "fermo", sigillo circolare con foto reale busto Adriano ruotato), niente box con bordo sinistro | griglia "scontrino/ledger": header logo+"Voce 0X/05" + riga tratteggiata (perforazione) in cima e in fondo a ogni slide, spina verticale oro a sinistra del testo, leader tratteggiati orizzontali sulle voci, slide soluzione a sfondo chiaro (sabbia) come "sollievo" tra due slide scure, slide finale come "totale" con doppia riga e "15%" gigante |

| `facebook-stagionalita-reel-proprietari` | — | **"calendario a 12 caselle"**: dodici riquadri (i mesi) con i sei di ottobre-marzo accesi in oro e gli altri spenti in fumè — striscia piccola in fondo alla verticale, griglia grande nella quadrata, e nel reel una casella che si accende per battuta. Apertura a citazione desaturata (freddo) che stacca su interno caldo, schede "una tipologia per scena" con numero oro fisso in alto a destra e filo che si allunga sotto il titolo, chiusura a fondo pieno con banda oro che sale |
| `reel-cosa-cerca-un-proprietario` | — | **"una frase al centro sul reale"**: nessuna card, nessun blocco, nessun numero grande. Fotografia o video reale a pieno fotogramma + velo fumè a tre strati (radiale centrale + verticale alto/basso + tinta piatta) + **una sola riga bianca al centro esatto**, Archivo 800/900 a 72 px con ombra tripla; marchio `HADRIANUS · MULTISERVICE` fisso in alto per tutta la durata; chiusura con riga oro `#E2BE6C` e CTA maiuscola spaziata. È il pattern per i contenuti dove l'immagine è la protagonista e il testo commenta |
| `reel-ti-manca-il-resto` | — | **"una frase al centro sul reale" + barra di avanzamento**: stesso impianto del reel da 8 s (foto reale a pieno fotogramma, velo fumè a tre strati, una riga bianca al centro, marchio fisso in alto), con in più il filo bianco del lockup che diventa un **binario** dove una barra oro `#C8A24B` da 3 px e 322 px di corsa si riempie sui 15 secondi. Serve a tenere lo spettatore su un formato lungo: usala solo sui contenuti oltre i 10 secondi, altrimenti la serie perde la differenza fra breve e lungo |
| `reel-standard-alberghiero` | — | **"testo nello spazio vuoto misurato" + ritmo a due tempi**: si parte da un video già finito e **non lo si copre**. Le posizioni si misurano — differenza fra fotogrammi per trovare le finestre ferme, energia dei bordi in otto fasce orizzontali per trovare le fasce vuote — e il testo va solo lì (in alto sugli interni, al centro sul mosaico scuro, in basso sul busto). Tre veli diversi secondo la posizione del testo, incrociati in dissolvenza sulle transizioni. Ogni inquadratura porta **due entrate**: la riga grande subito, la secondaria 1,8 s dopo. Audio originale conservato senza ricodifica |

Quando parti da una nuova campagna, scegli deliberatamente un pattern NON in questa tabella (o una combinazione nuova) prima di scrivere il primo `.dc.html`.

**Video / reel.** Un reel si consegna come: artboard `.dc.html` una per scena (editabili), video montato pronto e copertina. Dal 9 settembre l'ambiente ha un **ffmpeg completo con H.264** (`pip3 install imageio-ffmpeg`, percorso in `/tmp/claude-0/ffpath`): si decodificano mp4/mov, si estraggono fotogrammi, si compone testo su video e **si esporta direttamente in MP4 1080×1920 caricabile su Instagram**. CapCut serve solo per la musica. La ricetta di montaggio (overlay PNG con alpha renderizzati da Chromium + `overlay` di ffmpeg battuta per battuta, poi `concat`) è documentata in `campagne/reel-cosa-cerca-un-proprietario/direzione-artistica.md`.

**Clip di brand pulite.** Le clip caricate dal titolare avevano la filigrana `CapCut Ai`: le versioni ingrandite e ricentrate senza filigrana sono in `brand-assets/video/clean/` (`busto-frontale`, `busto-profilo`, `balcone`, `interno-cucina`), tutte 1080×1920 30 fps. Usa sempre quelle.

## Asset fotografici reali disponibili

Vedi `brand-assets/README.md` per l'inventario completo (logo in 4 varianti, tramonto Litorale, foto immobile). Preferirli agli elementi puramente tipografici quando pertinenti — restano valide editabilità e palette.

## I 3 strumenti grafici — chi fa cosa

Ogni strumento ha una mansione precisa. Non si sovrappongono: si passano il lavoro in sequenza quando serve.

| Strumento | Mansione | Quando |
|---|---|---|
| **Claude Design** (canvas `.dc.html`) | Motore di **default** per ogni artboard testo+layout: storie, post, caroselli, cover reel, post Facebook. Costruisce la grafica finita con palette fumè, tipografia Archivo/Manrope, componenti di questo file. | Sempre, per qualunque grafica social da zero. Non richiede connessione, è sempre disponibile — resta il motore principale anche quando Adobe è collegato, per non duplicare la pipeline esistente (artboard → `canvas.json` → export Playwright). |
| **Canva** | Editing manuale/collaborativo del workspace dell'utente, quando vuole rifinire o lavorare direttamente lì. | Solo su richiesta esplicita dell'utente, come alternativa a Claude Design. |
| **Adobe for creativity** | **Post-produzione delle foto/video reali** prima che entrino negli artboard — non genera artboard testo+layout da zero (eviterebbe di duplicare Claude Design con un secondo motore parallelo). | Vedi elenco compiti sotto. |

### Compiti reali assegnati ad Adobe for creativity

- **Ritocco foto reali** (`brand-assets/immobili/`, `brand-assets/ambientazione/`) prima di inserirle in un artboard: correzione tono/esposizione (`image_apply_adjustments`, `image_apply_auto_tone`), raddrizzamento (`image_auto_straighten`).
- **Crop sul formato esatto del canale** con rilevamento soggetto, usando i rapporti di questa tabella (es. `"9:16"` per una storia, `"1:1"` per Facebook 2ª/3ª immagine): `image_crop_and_resize`. Per un crop più preciso e verificato visivamente: `image_crop_to_bounds`.
- **Estensione del canvas** quando una foto reale non copre il formato verticale richiesto (es. il tramonto del Litorale in un formato 9:16 più alto dell'originale): `image_generative_expand`.
- **Varianti trasparenti del logo** (richieste dall'utente, finora bloccate per mancanza di strumento): `image_remove_background` su ciascuna delle 4 angolazioni in `brand-assets/logo/`. Ora producibile — vedi `brand-assets/README.md`.
- **Video per i Reel**: `video_resize` per il formato corretto, `video_create_quick_cut` per montaggi rapidi da più clip, `media_enhance_speech` per pulire l'audio del parlato.

### Flusso combinato (i 3 insieme, quando serve)

Adobe prepara/pulisce la foto o il video reale (ritocco, crop, sfondo rimosso) → Claude Design la inserisce nell'artboard finale con testo, CTA e palette → se l'utente vuole rifinire a mano il risultato, Canva come ultimo passaggio opzionale. Non tutti i passaggi servono sempre: per una grafica solo testuale, Claude Design da solo basta.

---

## Variante CHIARA (fondo bianco caldo) — dal 16/09/2026

Stessa identità di marca, fondo ribaltato. Introdotta su richiesta del titolare: *"scale di colori
con lo sfondo bianco invece che nero, sempre con le stesse palette di colore"*. Non sostituisce la
base fumè: sono **due registri della stessa palette**, si alternano fra un contenuto e l'altro
(preferenza fissa 5 — il layout varia sempre).

| Ruolo | Hex | Note |
|---|---|---|
| Fondo pagina | `#FAF7F1` | Bianco **caldo**, mai `#FFFFFF`: il bianco puro stacca dal marchio e abbaglia sul telefono |
| Fondo card / fascia | `#F5F0E6` | Sabbia, per separare blocchi senza disegnare bordi |
| Inchiostro titoli | `#2E2A25` | Fumè profondo — 13,3:1 sul fondo |
| Inchiostro corpo | `#3F3A33` | 10,5:1 |
| Inchiostro secondario | `#5A5349` | 7,1:1 — il minimo per il testo piccolo |
| **Oro per il TESTO** | `#86692A` | 4,8:1 |
| Oro pieno (CTA, celle, fili, badge) | `#C8A24B` | Solo come **riempimento**, con sopra testo fumè (5,9:1) |

### La regola che conta

**`#C8A24B` su fondo chiaro dà 2,25:1: non è leggibile come testo.** Sul fumè l'oro è
perfetto e si usa ovunque; sul chiaro va usato **solo come superficie** (banda CTA, celle piene,
fili, bordo dei badge). Ogni parola in oro su fondo chiaro usa **`#86692A`**.

Corollario: sul chiaro sparisce il problema del velo. Le foto non stanno più *sotto* il testo ma
**accanto**, in blocchi pieni o pannelli ritagliati — niente veli, niente ombre sul testo.
Il `text-shadow` a tre strati della variante fumè qui **non si usa mai**: su fondo chiaro sporca.

### Separazione

Sul fumè le gerarchie si fanno con la luce (velo, ombra, oro acceso). Sul chiaro si fanno con
**peso, spazio e superficie**: fascia sabbia contro fondo bianco, filo oro da 3 px, Archivo 900
contro Manrope 500. Niente ombre morbide sotto le card: al massimo `rgba(46,42,37,0.06)` per
staccare una card dal fondo, mai di più.
