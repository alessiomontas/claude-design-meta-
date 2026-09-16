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
