# Grafiche — Kit social proprietari

Grafiche editabili della campagna (canvas Claude Design). Ogni file `.dc.html` è un'artboard; `canvas.json` le dispone sulla canvas.

## Contenuto
- `Main.dc.html` → Storia 1 (hook)
- `Storia2.dc.html` … `Storia5.dc.html` → storie 2-5
- `Post1.dc.html` → post feed "rendita passiva"
- `Post2.dc.html` → post feed "prova sociale / case study"
- `ReelCover.dc.html` → copertina reel
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
  --artboard Main.dc.html --artboard Storia2.dc.html --artboard Storia3.dc.html \
  --artboard Storia4.dc.html --artboard Storia5.dc.html \
  --artboard Post1.dc.html --artboard Post2.dc.html --artboard ReelCover.dc.html \
  --canvas canvas.json
```
