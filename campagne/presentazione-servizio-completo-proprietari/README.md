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
| `build-slides.mjs` · `emit.mjs` · `render.mjs` · `make-pdf.mjs` | Generatori del deck: componenti, testi, PNG, PDF |
| `preventivo/` | **Preventivo A4 per la sola messa in regola documentale** (500 € non soggetti a IVA): 2 artboard editabili, PNG 2×, PDF, checklist di compliance, generatore `build-preventivo.mjs` + `render-preventivo.mjs` |

## Rigenerare

```bash
node emit.mjs                          # testi -> 16 .dc.html
node render.mjs                        # .dc.html -> png/ (2×)
node make-pdf.mjs                      # .dc.html -> PDF 16 pagine
node preventivo/build-preventivo.mjs   # preventivo -> 2 artboard A4
node preventivo/render-preventivo.mjs  # preventivo -> PNG 2× + PDF A4
```

Il preventivo ha **tre campi da compilare prima dell'invio**: numero, data e nome della proprietaria (`[numero]`, `[gg/mm/aaaa]`, `[Nome e cognome della proprietaria]`). Mancano ancora i dati fiscali e i contatti del prestatore in calce alla seconda pagina.

I font Archivo/Manrope non sono raggiungibili da questo ambiente: `render.mjs` e `make-pdf.mjs` iniettano le copie locali scaricate nello scratchpad di sessione. Se mancano, l'export esce con i font di fallback — vanno riscaricati da Google Fonts prima di rigenerare.

## Attenzione

Il canvas pubblicato è editabile dall'utente: **prima di rilanciare `emit.mjs` su un canvas già ritoccato a mano, rileggere l'Artifact**, altrimenti le modifiche manuali vengono sovrascritte.
