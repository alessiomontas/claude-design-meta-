# Grafiche — Kit social proprietari

Grafiche editabili della campagna (canvas Claude Design). Ogni file `.dc.html` è un'artboard; `canvas.json` le dispone sulla canvas.

Palette: **grigio fumè caldo** (niente blu navy). Tutto editabile come su Canva (sposta, ridimensiona, cambia font, aggiungi immagini).

## Contenuto
- `Main.dc.html` → Storia A (rendita / anti-stress) — autoconclusiva
- `StoriaB.dc.html` → Storia B (rischio affitto tradizionale → terza strada) — autoconclusiva
- `StoriaC.dc.html` → Storia C (15% / fiducia) — autoconclusiva
- `Carosello1.dc.html` … `Carosello5.dc.html` → carosello feed (5 slide)
- `PostProva.dc.html` → post feed "affitto tradizionale vs casa vacanza" (confronto)
- `ReelCover.dc.html` → copertina reel
- `FbPost1.dc.html` (verticale) · `FbPost2.dc.html` · `FbPost3.dc.html` (quadrate) → post Facebook a 3 immagini
- `canvas.json` → layout della canvas

## Artefatto pubblicato (modificabile)
https://claude.ai/code/artifact/4cbc01e6-0fdf-40dc-8fc9-3d87f3295e75
(modifica visiva degli elementi + export PNG/PDF per ogni formato)

## Foto
Tutte le artboard con immagine usano **placeholder `[FOTO]`**: vanno sostituiti con foto reali delle strutture prima della pubblicazione.

## Rigenerare il file canvas (se serve ripubblicare)
Il file `social-kit-proprietari.html` (~2.4MB) è generato e **non versionato** (vedi `.gitignore`). Per rigenerarlo dai sorgenti serve la skill `design` di Claude Code:

```
node "<base-dir-skill-design>/seed-canvas.mjs" \
  --template "<base-dir-skill-design>/payload.template.html" \
  --out social-kit-proprietari.html \
  --title "Kit Social Proprietari — Case Vacanza" \
  --artboard Main.dc.html --artboard StoriaB.dc.html --artboard StoriaC.dc.html \
  --artboard Carosello1.dc.html --artboard Carosello2.dc.html --artboard Carosello3.dc.html \
  --artboard Carosello4.dc.html --artboard Carosello5.dc.html \
  --artboard PostProva.dc.html --artboard ReelCover.dc.html \
  --canvas canvas.json
```
