# Presentazione "servizio completo" — bilocale Ostia Lido Centro

Presentazione commerciale **1-a-1** (non contenuto social): 16 slide 16:9 per una proprietaria già incontrata di persona — bilocale ~50-60 mq a Lido Centro, nessun adempimento ancora aperto.

## Cosa c'è qui

| File / cartella | Cos'è |
|---|---|
| `brief-mercato.md` | Brief di `ricercatore-mercato`: decisori, angolo, ricerca normativa con fonti e stato, elenco dei 28 servizi con CONFERMATO/NUOVO, divieti |
| `copy.md` | Copy definitivo slide per slide (Master Template) + tabella claim + note per l'art director |
| `direzione-artistica.md` | Griglia, palette chiara, tipografia, firma visiva, uso delle immagini |
| `checklist-compliance.md` | Verifica di `compliance-checker` sul testo montato nelle artboard |
| `slide/` | Le 16 artboard editabili `.dc.html` + `canvas.json` + immagini |
| `png/` | Export PNG 2560×1440 (2×) di ogni slide |
| `Hadrianus-Presentazione-Bilocale-Lido-Centro.pdf` | PDF pronto da inviare — 16 pagine, misura PowerPoint 16:9 |
| `build-slides.mjs` · `emit.mjs` · `render.mjs` · `make-pdf.mjs` | Generatori: componenti, testi, PNG, PDF |

## Rigenerare

```bash
node emit.mjs        # testi -> 16 .dc.html
node render.mjs      # .dc.html -> png/ (2×)
node make-pdf.mjs    # .dc.html -> PDF 16 pagine
```

I font Archivo/Manrope non sono raggiungibili da questo ambiente: `render.mjs` e `make-pdf.mjs` iniettano le copie locali scaricate nello scratchpad di sessione. Se mancano, l'export esce con i font di fallback — vanno riscaricati da Google Fonts prima di rigenerare.

## Attenzione

Il canvas pubblicato è editabile dall'utente: **prima di rilanciare `emit.mjs` su un canvas già ritoccato a mano, rileggere l'Artifact**, altrimenti le modifiche manuali vengono sovrascritte.
