---
name: giornata
description: Produce il pacchetto contenuti di UN giorno per Hadrianus — 1 reel, 1 carosello, 1 post Facebook, 2 storie — dall'angolo alla grafica editabile, passando per ricerca, copy, art direction, compliance e revisione. Usalo per la produzione quotidiana ricorrente; per una campagna monotematica a sé stante usa invece /nuova-campagna.
argument-hint: [data opzionale AAAA-MM-GG] [angolo o tema opzionale]
---

# Giornata — produzione quotidiana

Produce il pacchetto completo di un giorno, pronto da pubblicare, in `campagne/giornaliero/<AAAA-MM-GG>/`.

## Cosa esce ogni giorno (quantità fissa, decisa dal titolare)

| # | Contenuto | Canale | Formato | Note |
|---|---|---|---|---|
| 1 | **Reel** | Instagram + Facebook | 9:16 · 1080×1920 | 8-30 s, scene editabili + MP4/WebM montato + copertina |
| 2 | **Carosello** | Instagram + Facebook | 4:5 · 1080×1350 | 5 slide |
| 3 | **Post Facebook** | Facebook | 3 immagini: 1080×1920 + 2× 1080×1080 | formato fisso, la 1ª SEMPRE 9:16 |
| 4-5 | **2 storie** | Instagram | 9:16 · 1080×1920 | autoconclusive: ognuna problema + soluzione + CTA |

Tutte le grafiche editabili (`.dc.html` su canvas Claude Design, o Canva se collegato). PNG solo come export in più.

**Il reel si costruisce in Canva** (regola fissa n.10 di `CLAUDE.md`). Il titolare fornisce ogni volta il link `/edit`
di un progetto Canva nuovo; il reel ci va dentro come pagine 1080×1920, una per scena, con testi e forme native.
Gli altri quattro contenuti restano artboard `.dc.html`. Procedura e limiti provati sul campo:
`.claude/skills/giornata/BANCO-MONTAGGIO.md`, sezione «Canva — cosa passa e cosa no».

## Input

- **Data**: se non passata, usa la data di oggi.
- **Angolo**: se non passato, lo determina il pilastro del giorno (vedi sotto). Se passato dall'utente, quello vince.

## Passaggi

### 1 · Scegli il pilastro e l'angolo

Leggi `campagne/giornaliero/PIANO.md`: contiene la **rotazione dei pilastri per giorno della settimana** e il **registro** di ciò che è già uscito.

- Il pilastro dipende dal giorno della settimana della data richiesta.
- L'angolo specifico dev'essere **nuovo**: controlla sia il registro in `PIANO.md` sia la sezione "Angoli/ganci già usati" di `campagne/INDEX.md`. Mai ripetere un gancio già uscito.
- Crea la cartella `campagne/giornaliero/<AAAA-MM-GG>/`.

### 2 · Ricerca — `ricercatore-mercato`

Invoca `Agent` con `subagent_type: ricercatore-mercato`, passando pilastro del giorno, target e i cinque formati da produrre. Deve cercare sul web dati/trend freschi utili all'angolo (stagionalità, eventi Roma/Ostia, dinamiche affitto breve) e proporre **un angolo unico non ancora usato**.
Output atteso: `brief-mercato.md` nella cartella del giorno.

### 3 · Copy — `copywriter`

Invoca `Agent` con `subagent_type: copywriter`, indicando il brief. Scrive **tutti e cinque i contenuti** seguendo `framework-vendita`, il tono di `riferimenti/` e il lessico di `.claude/reference/lessico-brand.md`.
Ogni contenuto va consegnato nel **Master Template** (`.claude/reference/master-template.md`) — copy, layout a tabella, prompt grafico in inglese, negative, parametri, tabella claim.
Output atteso: `copy.md`.

### 4 · Grafiche — `art-director`

Invoca `Agent` con `subagent_type: art-director`, indicando brief e copy. Produce:
- `direzione-artistica.md`
- `grafiche/` con le artboard editabili `.dc.html` (11 artboard: 1 copertina reel + scene reel + 5 slide carosello + 3 immagini Facebook + 2 storie)
- `png/` con gli export
- `reel/` con `scene.json` (fonte unica), montaggio e video

**Reel → Canva.** Chiedi al titolare il link `/edit` del progetto Canva del giorno se non l'ha già dato.
Poi: `python3 .claude/skills/giornata/scene_to_canva.py <cartella>/reel/scene.json` per ricavare le scene
rappresentative, e costruiscile in Canva con `read-design` (`open_transaction: true`) + `edit-design`
(`add_page` 1080×1920 → `add_text` / `insert_shape` → `format_text`) → `finalize: "commit"`.
Le pagine devono essere create con `add_page`: quelle copiate da un altro progetto arrivano di tipo
`unsupported` e non si possono formattare. Il connettore **non imposta la famiglia di font**: colore, corpo,
peso e allineamento sì, Archivo/Manrope li applica il titolare (o si importa l'HTML). L'MP4 resta comunque
prodotto in locale come riferimento di tempi.

**Vincolo di varietà**: il layout dev'essere diverso da quello dei giorni precedenti. Prima di partire, controlla i pattern già usati in `.claude/reference/design-system.md` e negli ultimi giorni in `campagne/giornaliero/`.

### 5 · Compliance — `compliance-checker`

Invoca `Agent` con `subagent_type: compliance-checker` su tutto il pacchetto. Nessun contenuto esce senza.
Output atteso: `checklist-compliance.md`. Se torna **DA CORREGGERE**, rimanda i punti bloccanti a `copywriter` o `art-director` e ripeti — non consegnare prima.

### 6 · Revisione — `revisore-marketing-design`

Invoca `Agent` con `subagent_type: revisore-marketing-design` sul pacchetto già passato da compliance.
Output atteso: `revisione-marketing-design.md`.

### 7 · Scheda di pubblicazione

Scrivi `PUBBLICAZIONE.md` nella cartella del giorno: è **il file che il titolare apre la mattina**. Deve bastare da solo, senza leggere altro.

```
# Pubblicazione <AAAA-MM-GG> — <pilastro>

| Ora | Contenuto | File da caricare | Dove |
|---|---|---|---|
| 09:00 | Storia 1 | png/Storia1.png | Instagram storie |
| 12:00 | Carosello | png/Car01..05.png | Instagram + Facebook feed |
| 15:00 | Post Facebook | png/Fb1.png, Fb2.png, Fb3.png | Facebook (gruppi + pagina) |
| 18:00 | Reel | reel/<nome>.mp4 | Instagram + Facebook reel |
| 21:00 | Storia 2 | png/Storia2.png | Instagram storie |

## Caption pronte da copiare
### Carosello
<testo integrale>
### Post Facebook
<testo integrale>
### Reel
<testo integrale>
```

### 8 · Aggiorna la memoria

- Aggiungi la riga del giorno al **registro** in `campagne/giornaliero/PIANO.md` (data, pilastro, angolo, esito compliance/revisione).
- Aggiungi l'angolo nuovo alla sezione "Angoli/ganci già usati" di `campagne/INDEX.md`.

Questi due aggiornamenti non sono facoltativi: sono la memoria che impedisce al giorno dopo di ripetersi.

### 9 · Riporta in chat (lean)

Solo una tabella con: pilastro e angolo del giorno · esito compliance · esito revisione · percorso della cartella · eventuali blocchi. Zero preamboli, zero racconto del processo.

## Regole

- I passaggi sono sequenziali. Nessuno si salta, nemmeno quando si è in ritardo.
- Se manca un'informazione essenziale e verificabile (un claim, un numero), si scrive `[DATO DA VERIFICARE]` e si prosegue — **non** si inventa e **non** ci si ferma per questo.
- Se invece manca qualcosa che blocca l'intero pacchetto (es. nessun angolo disponibile nel pilastro), fermati e chiedi.
- Un contenuto che non passa compliance non entra in `PUBBLICAZIONE.md`.
- Se la sessione è automatica (avviata da una Routine) e nessuno può rispondere a una domanda: produci comunque il resto del pacchetto, e scrivi le domande aperte in fondo a `PUBBLICAZIONE.md` sotto "## Da confermare".
