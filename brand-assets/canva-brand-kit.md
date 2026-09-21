# Canva Brand Kit — come compilarlo, campo per campo

Guida operativa per il titolare. Valori pronti da copiare e incollare.
Fonte dei valori: `.claude/reference/design-system.md` (palette, tipografia) e `CLAUDE.md` (lessico).

**Premessa onesta.** Non posso compilare il Brand Kit al posto tuo: il connettore Canva che uso
legge e modifica **design**, non le impostazioni del brand. E i nomi esatti dei campi cambiano
leggermente tra versioni e piani di Canva (il Brand Kit completo richiede Canva Pro / Teams).
Se un campo che descrivo non lo trovi con quel nome, cerca quello che gli somiglia: l'ordine e il
contenuto restano validi.

**Dove si arriva**: Canva → menu a sinistra → **Brand** → **Brand Kit** (o *Brand Hub*).
Se ne hai più di uno, rinomina quello attivo: **`Hadrianus Multiservice`**.

---

## 1. Logo

Carica **tutte e quattro** le varianti da `brand-assets/logo/`, non una sola: Canva propone il
logo per primo in ogni design, e avere l'angolazione giusta evita di rifare la grafica.

| Ordine | File | Quando Canva deve proporlo |
|---|---|---|
| 1 | `logo-marmo-frontale.png` | **Logo principale.** Alta risoluzione, è quello da mettere per primo: Canva usa il primo come default. |
| 2 | `logo-bronzo-frontale.jpg` | Su fondi scuri (fumè, foto con velo scuro) |
| 3 | `logo-marmo-profilo-largo.jpg` | Copertine e aperture dove serve respiro |
| 4 | `logo-marmo-profilo-stretto.jpg` | Badge d'angolo, formati stretti |

⚠️ **Nessuna di queste ha lo sfondo trasparente.** Finché non generiamo i PNG con canale alpha
(si può fare, vedi `brand-assets/README.md`), il logo va messo **dentro una forma** — un cerchio o
un rettangolo arrotondato — non appoggiato su un fondo colorato, o si vedrà il suo riquadro.
Se vuoi, dimmelo e genero le quattro varianti trasparenti.

---

## 2. Colori — crea **tre** palette, non una

Canva permette più palette dentro lo stesso Brand Kit. Tenerle separate evita l'errore più
frequente: l'oro usato come testo su fondo chiaro, dove è illeggibile.

### Palette 1 — nome: `Hadrianus · Base`
I colori dell'identità. Sono questi sei che devono esserci sempre.

| Hex | Che cos'è |
|---|---|
| `3F3A33` | Fumè — base scura del brand |
| `2E2A25` | Fumè profondo — inchiostro titoli, estremo dei gradient |
| `C8A24B` | **Oro** — è SEMPRE il colore dell'azione |
| `F5F0E6` | Sabbia — fondi chiari e card |
| `FAF7F1` | Bianco caldo — fondo pagina (**mai** `FFFFFF`) |
| `9A8A63` | Pietra/oliva — etichette piccole maiuscole, kicker |

### Palette 2 — nome: `Hadrianus · Testo su chiaro`
Da usare quando il fondo è sabbia o bianco caldo.

| Hex | Che cos'è |
|---|---|
| `2E2A25` | Titoli — contrasto 13,3:1 |
| `3F3A33` | Corpo — 10,5:1 |
| `5A5349` | Secondario — 7,1:1, il minimo per il testo piccolo |
| `86692A` | **Oro per il testo** — 4,8:1 |

> **La regola che salva più grafiche di tutte:** `C8A24B` su fondo chiaro dà **2,25:1** — non è
> leggibile. Sul chiaro, ogni parola in oro usa **`86692A`**. `C8A24B` sul chiaro va bene solo
> come **riempimento** (pulsante, cella, filo, bordo badge) con sopra testo fumè.

### Palette 3 — nome: `Hadrianus · Testo su scuro`

| Hex | Che cos'è |
|---|---|
| `d8d2c4` | Corpo su fondo scuro |
| `b7ad9a` | Secondario, numerazione |
| `C8A24B` | Oro — **qui sì** anche come testo: sul fumè funziona |
| `a8863b` | Oro scuro, stati premuti |

**Colore vietato: il blu navy.** È una regola fissa del brand. Se Canva te lo propone in un
template, sostituiscilo con `3F3A33`.

---

## 3. Font — i tre stili di testo

Canva chiede tre livelli. Imposta così:

| Livello Canva | Font | Peso | Dimensione di riferimento | Note |
|---|---|---|---|---|
| **Titolo / Heading** | `Archivo` | **900** | 72-120 px sul 1080×1920 | Il peso 900 è ciò che rende il brand riconoscibile: non scendere sotto l'800 |
| **Sottotitolo / Subheading** | `Archivo` | **700-800** | 40-56 px | Maiuscolo + spaziatura larga per i kicker |
| **Corpo / Body** | `Manrope` | **400-600** | 32-46 px | Mai Archivo per il corpo: a peso pieno diventa illeggibile in paragrafo |

**Se Archivo o Manrope non compaiono** nella lista di Canva: sono entrambi su Google Fonts, quindi
di norma ci sono. Se il tuo piano permette il caricamento font, scaricali da Google Fonts e
caricali in **Brand Kit → Font → Carica un font**. Se non li trovi e non puoi caricarli, i ripieghi
più vicini sono **Anton** o **Archivo Black** per i titoli e **Poppins** per il corpo — ma segnalamelo,
perché cambia la resa e va allineato il `design-system.md`.

**Colore di default del testo**: titoli `2E2A25` su chiaro, `FAF7F1` su scuro. Mai nero puro.

---

## 4. Voce del brand (se il tuo piano ha il campo *Brand Voice*)

Incolla questo, è già allineato a `CLAUDE.md`:

> Tono serio e professionale, che fa pensare. Parliamo a proprietari di casa a Roma, Ostia e sul
> litorale, non a turisti. Niente entusiasmo pubblicitario, niente emoji, niente promesse di
> guadagno. Diciamo cosa facciamo e come, e lasciamo decidere. Frasi corte. Numeri solo se
> verificati.
>
> **Da usare sempre:** «Guadagniamo solo se guadagni tu» · «standard alberghiero» · «15% sull'incassato».
> **Da non usare mai:** «guadagni solo se guadagni tu» (la formula corretta è la prima) ·
> «hotel-style» · nomi di singole strutture come prova · cifre di rendimento non verificate.

---

## 5. Cosa NON mettere nel Brand Kit

- **La foto della smart TV** (`immobili/smart-tv-streaming-mockup.jpg`): mostra i loghi Netflix,
  Prime Video e Disney+. Dentro il Brand Kit diventa un asset che riappare da solo nei design, e
  quei marchi non sono nostri. Tienila fuori.
- **Foto di immobili come "Foto del brand"**: sono case reali di clienti. Nel Brand Kit stanno bene
  solo `ambientazione/tramonto-litorale-romano.jpg` e il logo.
- **Template altrui già compilati**: il Brand Kit è l'identità, non la libreria dei contenuti.

---

## 6. Ordine consigliato — quindici minuti

1. Rinomina il Brand Kit in `Hadrianus Multiservice`.
2. Carica i quattro logo nell'ordine della tabella §1.
3. Crea le tre palette §2 con i loro nomi. Sono 14 valori in tutto.
4. Imposta i tre livelli di font §3.
5. Incolla la voce del brand §4, se il campo c'è.
6. Carica `ambientazione/tramonto-litorale-romano.jpg` fra le foto del brand. Nient'altro.
7. **Verifica finale**: apri un design nuovo 1080×1920, metti un fondo `F5F0E6` e scrivi una parola
   in oro. Se Canva ti dà `C8A24B`, cambialo a mano in `86692A`. Se la palette 2 è impostata bene,
   te lo propone già lui.

---

## 7. Cosa cambia per me, dopo

Una volta compilato, quando mi mandi il link `/edit` di un progetto Canva io **vedo già i colori e
i font giusti applicati dal template**, e devo correggere meno cose a mano. Resta comunque vero
che **la famiglia tipografica non è modificabile** dal mio connettore: se un template porta un suo
font, il Brand Kit non lo sovrascrive da solo — devi applicare tu lo stile del brand dentro Canva
(**Applica Brand Kit** sul design, quando il pulsante compare).
