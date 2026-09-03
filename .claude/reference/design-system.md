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

Quando parti da una nuova campagna, scegli deliberatamente un pattern NON in questa tabella (o una combinazione nuova) prima di scrivere il primo `.dc.html`.

## Asset fotografici reali disponibili

Vedi `brand-assets/README.md` per l'inventario completo (logo in 4 varianti, tramonto Litorale, foto immobile). Preferirli agli elementi puramente tipografici quando pertinenti — restano valide editabilità e palette.
