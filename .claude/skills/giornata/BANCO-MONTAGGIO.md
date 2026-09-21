# Banco di montaggio — come funziona

Il reel non è più codice: è un **file di scene**. Questo cambia chi può modificarlo.

```
scene.json  ──►  scene_to_html.py  ──►  reel.html  ──►  anima_reel.py  ──►  reel.mp4
     ▲
     │
  banco-montaggio.html   ← il titolare modifica qui
```

## Il file di scene

`campagne/giornaliero/<data>/reel/scene.json`:

```json
{
  "titolo": "Il costo del vuoto", "durata": 25.0, "fondo": "#FAF7F1",
  "sfondo_immagine": null,
  "elementi": [
    {"id": "gancio", "nome": "Gancio · la frase negata", "tipo": "testo",
     "testo": "Una casa vuota non costa niente.",
     "x": 64, "y": 820, "w": 952,
     "font": "Archivo", "peso": 900, "size": 70, "colore": "#2E2A25",
     "t_in": 0.0, "t_out": 1.45,
     "anim_in": "maschera-basso", "anim_out": "esce-alto", "dur_in": 0.18}
  ]
}
```

`tipo`: `testo` · `fascia` · `immagine`.
Un elemento con `fondo` e `h` diventa una card o una banda con il testo centrato dentro.

## Vocabolario delle animazioni

| Entrata | Uscita |
|---|---|
| `nessuna` (già presente) | `taglio` (secco, 0 ms) |
| `sfuma` | `sfuma` |
| `maschera-basso` · `maschera-alto` · `maschera-sinistra` | `maschera-chiude` |
| `entra-basso` · `entra-alto` · `entra-sinistra` · `entra-destra` | `esce-alto` · `esce-basso` |
| `scatto` | |

Stessa curva ovunque: `cubic-bezier(.16,1,.3,1)`, che decelera forte.
L'anteprima nel banco usa la stessa matematica del montatore, quindi quello che si vede a schermo
è quello che esce nel video.

## Il giro completo

1. Il titolare apre il banco, sposta, riscrive, cambia tempi e animazioni, preme **Salva**.
2. Io rileggo l'artifact, estraggo `scene.json` dal blocco `<script id="scena">` e lo salvo nel repo.
3. `python3 .claude/skills/giornata/scene_to_html.py <scene.json> reel.html`
4. `python3 .claude/skills/giornata/anima_reel.py reel.html reel.mp4 <durata> 30`

## Perché l'MP4 non lo fa il browser

Il montaggio in H.264 richiede ffmpeg, che nella pagina non c'è. L'anteprima si guarda nel banco;
il file finale lo genero io dal `scene.json` salvato. Il vantaggio resta: **le scelte le fa il
titolare**, non servono richieste di modifica a voce.

## Tempi minimi di lettura

Rispettarli sempre — la tabella completa sta in `.claude/reference/reel-virali.md`.
Riga di lista 1,2 s · frase di due righe 1,8 s · parola di svolta 1,1 s · CTA 2,0 s.

---

## Canva — cosa passa e cosa no (provato il 16/09/2026)

Il connettore Canva **è collegato** e costruisce davvero: pagine 1080×1920, forme,
rettangoli con angoli arrotondati, cerchi, testi posizionati al pixel, corpo, peso, colore,
allineamento, interlinea. Il reel del 16/09 è stato ricostruito lì in otto pagine.

### I tre limiti, verificati sull'elenco completo delle operazioni

| Limite | Conseguenza pratica |
|---|---|
| **Nessun comando per il tipo di carattere** | Ogni testo atterra nel font predefinito di Canva. Archivo e Manrope vanno rimessi a mano, testo per testo |
| **Nessun comando per la spaziatura fra lettere** | Il lockup `H A D R I A N U S` perde la spaziatura larga |
| **Nessun comando di animazione** | Entrate, uscite e tempi si rifanno tutti a mano dentro Canva |

### Altri inciampi incontrati

- Una pagina **copiata** da un progetto esistente può risultare di tipo `unsupported`:
  Canva non ne espone gli elementi, quindi non si possono formattare né spostare. Le pagine
  create con `add_page` sono invece di tipo `fixed` e si gestiscono bene. **Costruire sempre
  su pagine nuove.**
- Il ridimensionamento di un documento (`resize-design`) consuma un **uso Pro a consumo**.
- I link `/watch` e i "link pubblici di visualizzazione" danno accesso in sola lettura:
  serve il link di **modifica**, e il documento deve stare su un account raggiungibile dal
  connettore (una cartella di team può non esserlo).
- Il collegamento può scadere a metà lavoro: le modifiche restano in una transazione aperta
  e vanno confermate con `finalize: commit`, altrimenti si perdono.

### Regola

Il reel **resta sul banco di montaggio**: lì tipografia e tempi sono già a posto e sono
esattamente le due cose che a Canva non arrivano. Canva serve quando il titolare vuole
ritoccare dal telefono o pubblicare da lì.

## Immagini dentro Canva — cosa serve al titolare (16/09/2026)

Il connettore Canva **non sa elencare i Caricamenti**: `get-assets` vuole già gli `asset_id`, e non esiste
uno strumento «mostrami le mie immagini». `upload-asset-from-url` accetta solo URL già pubblici, quindi le
foto private o generate qui non si possono caricare per quella strada.

Resta una via sola, e va usata così:

1. Il titolare trascina **una volta** ogni foto da Caricamenti su una pagina qualsiasi del progetto Canva
   (anche una pagina di servizio in fondo, da cancellare poi).
2. `read-design` con `open_transaction: true` restituisce gli elementi immagine con il loro `asset_id`.
3. Da lì l'`asset_id` si riusa dove serve: `insert_fill` per metterla su un'altra pagina,
   `update_fill` per sostituire il contenuto di un riquadro esistente, `crop_media` per l'inquadratura.

Quindi: **sì, le foto dei caroselli si possono mettere in Canva** — ma le foto devono comparire su una
pagina, non solo nei Caricamenti. In alternativa il carosello resta dov'è oggi, sulle artboard `.dc.html`,
dove le foto si gestiscono senza passaggi manuali.

**Verificato il 16/09/2026.** Un `asset_id` letto in un progetto funziona anche in un progetto **diverso**:
`MAHUsauQ_cs`, letto dalla pagina 1 di «MULTISERVICE», si inserisce senza errori nel progetto del reel.
Quindi basta che una foto stia su una pagina qualsiasi di un qualsiasi progetto del titolare: da lì in poi
è riusabile ovunque. L'`asset_id` dell'immagine compare in `fill.media.mediaId`; i video in `fill.media.videoId`.

### Le pagine ritoccate a mano possono diventare illeggibili

Le otto pagine del reel erano tutte `fixed`. Dopo che il titolare ha lavorato nel progetto, la **pagina 2 è
diventata `unsupported`**: il collegamento non ne espone più gli elementi e lì non si può più correggere
niente. Le altre sette sono rimaste `fixed` e modificabili.

Conseguenza operativa: **prima si costruisce tutto, poi il titolare ritocca.** Se serve rimettere mano a una
pagina diventata `unsupported`, l'unica strada è rifarla con `add_page` e cancellare la vecchia.

## Canva — modelli: cosa posso seguire e cosa no

**Provato il 20/09/2026.** Il titolare ha condiviso un template video animato (`DAHVxjBJbDU`).
Risultato: la pagina torna come **`type: "unsupported"`**. Non se ne leggono gli elementi, non se ne
ottiene nemmeno la miniatura, non si sostituisce un testo. Il connettore non sa rappresentare
quella pagina, quindi per me è cieca.

**Corretto il 21/09.** La prima stesura diceva «vale sempre»: era una generalizzazione da **un
solo campione**, e non regge. Quello che sappiamo davvero:

> **Dipende dal modello, e si scopre solo provando.** Un modello costruito su una **clip video a
> tutto schermo** (come `DAHVxjBJbDU`) torna `unsupported`. Un modello fatto di **testo e forme con
> animazioni applicate** ha buone probabilità di essere leggibile e modificabile — da verificare.

**La prova costa una chiamata:** `read-design` sul link, e si vede subito se la pagina è
`unsupported`. Farla sempre **prima** di promettere qualsiasi cosa al titolare.

**Le anteprime invece funzionano.** Il 20/09 la miniatura risultava assente; il 21/09 la stessa
pagina l'ha restituita. Canva la genera con ritardo: se manca, **non significa che non arriverà** —
si riprova più tardi. Quindi **un modello lo posso vedere**, anche quando non lo posso modificare.

### Cosa riesco a fare, in ordine di quanto funziona

| Cosa mi dai | Posso leggerlo | Posso modificarlo | Note |
|---|---|---|---|
| **Progetto vuoto 1080×1920** | — | ✅ tutto | È il caso che uso: costruisco le pagine da zero |
| **Pagine che ho creato io con `add_page`** | ✅ | ✅ tutto | Restano modificabili finché nessuno le ritocca a mano |
| **Template statico semplice** (testo + forme) | ✅ di solito | ✅ sostituisco i testi | Va provato caso per caso |
| **Template su clip video a tutto schermo** | ❌ | ❌ | `unsupported`. Provato su `DAHVxjBJbDU` |
| **Template di testo animato** (testo + forme) | da provare | da provare | Il caso con più probabilità di funzionare: consigliarlo al titolare |
| **Pagina ritoccata a mano dal titolare** | spesso ❌ | spesso ❌ | Può diventare `unsupported` dopo l'editing manuale |
| **Miniatura di un modello** | ✅ la vedo | — | Anche di pagine `unsupported`. Può richiedere tempo perché Canva la generi |

### Cosa non posso fare in nessun caso, anche su pagine mie

- **Animazioni e transizioni**: il connettore non le espone. Si mettono a mano in Canva.
- **Durata della pagina**: non la imposto. Nel video la decide il titolare.
- **Famiglia di font**: imposto corpo, peso, colore e allineamento, **non il carattere**.
  Archivo e Manrope li applica il titolare.
- **Audio**, **taglio dei video**, **spaziatura fra le lettere**.
- **Sfogliare la libreria pubblica di Canva**: vedo solo i progetti dell'account e i *brand
  template*, che su questo account sono zero.

### Come darmi un modello, in pratica

1. **Mandami uno screenshot** della pagina o delle pagine. È l'unico modo che ho per vederlo
   davvero e dirti se regge il copione.
2. Se lo vuoi usare **con le sue animazioni**: lo duplichi tu in Canva, io ti consegno il testo
   pagina per pagina e i codici colore, e il copia-incolla lo fai tu. Animazioni e font restano
   intatti. È la strada per il risultato più professionale.
3. Se vuoi che **lo riempia io**: deve essere un modello **statico**, e va provato prima — se
   torna `unsupported` non c'è modo di aggirarlo.

**Non promettere mai di riempire un template prima di averlo aperto.** È successo il 20/09 ed era
sbagliato. La promessa giusta è: «mandami il link, lo provo e ti dico sì o no».

### Come il titolare consegna un modello

Una via sola, ed è la più semplice: **applica il template a un progetto e manda il link `/edit` di
quel progetto.** Tre accortezze che cambiano l'esito:

1. **Applica tutte le pagine che servono** (10-12), non una sola. Il primo tentativo ne aveva una.
2. **Non ritoccarlo a mano prima di mandarmelo**: l'editing manuale può rendere `unsupported` una
   pagina che prima non lo era.
3. **Preferisci i template di testo animato** a quelli costruiti su clip video: hanno molte più
   probabilità di essere modificabili da qui.
