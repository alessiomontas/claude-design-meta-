# Listino pulizie e housekeeping — Via Cola di Rienzo

Documento **commerciale per il cliente** (non contenuto social): il listino delle tre unità di Via
Cola di Rienzo, da inviare come **secondo documento** dopo la proposta di servizio in slide
(`Preventivo-pulizie-Cola-di-Rienzo.pdf`, 3 slide 16:9, inviata al cliente il 2 ottobre 2026).

| | |
|---|---|
| **Formato** | PDF A4 verticale, 3 pagine |
| **Sorgente editabile** | `listino-hadrianus-cola-di-rienzo.html` (autoconsistente: font e logo in base64) |
| **Consegna** | `listino-hadrianus-cola-di-rienzo.pdf` |
| **Anteprime** | `anteprime/pagina-0X.png` |
| **Stato** | 🟢 Pronto — compliance passata |

## Continuità con le slide già inviate

Il documento riprende la grafica delle slide, non la reinventa:

- **Palette campionata dai PNG delle slide**: fumè `#1B1712`, sabbia `#F7F3EB`, oro `#C8A24B`,
  oro chiaro su scuro `#E0BE6C`, oro scuro su chiaro `#A8823A`, bianco card `#FFFFFF`.
- **Barra oro in testa a ogni pagina**: `linear-gradient(90deg,#A8823A,#C8A24B 52%,#DFBD6B)` —
  è la firma visiva delle slide.
- **Tipografia**: le slide erano composte in Palatino + Optima (font di sistema macOS).
  Qui si usano i cloni liberi, incorporati nel file così che il PDF sia identico su qualunque
  macchina: **URW P052** (clone di Palatino) per titoli e numeri, **Alegreya Sans** (umanista
  flared, sostituto di Optima) per il testo corrente.
- **Logo**: estratto in trasparenza dal PDF delle slide (immagine + smask ricomposte in RGBA) e
  salvato anche in `brand-assets/logo/trasparenti/logo-crema-trasparente.png`.

Nota: questa è la **prima palette "documento"** del brand — non usa Archivo/Manrope del
design system social, perché deve stare accanto alle slide già in mano al cliente.

## Impianto delle 3 pagine

| Pagina | Contenuto | Perché |
|---|---|---|
| 01 | Hero scuro + **tabella listino** (3 unità × pulizia/refill/kit → totale a check-out) + nota kit + banda "un solo numero per unità" | Il prezzo si vede subito, già scomposto: nessuna voce resta implicita |
| 02 | "Cosa comprende la tariffa": 5 voci numerate (magazzino, refill, pulizia, biancheria, letti) + card "kit aggiuntivi 15 €" e "come si fattura" | Giustifica il prezzo con il lavoro, non con aggettivi |
| 03 | "Che cosa cambia per lei": confronto *non entra più in conto* / *è già dentro la tariffa*, esempio su una settimana (245 €), prossimo passo | Chiude sul risparmio di gestione, non sullo sconto |

## Le tariffe (come dettate dal titolare)

| Unità | Pulizia | Refill | Kit biancheria | A check-out |
|---|---|---|---|---|
| Double Deluxe · bilocale 70 m² | 70 € | 10 € | 15 € | **95 €** |
| Superior Double Room · bilocale 45 m² | 60 € | 10 € | 15 € | **85 €** |
| Small Double Room · camera 16 m² | 40 € | 10 € | 15 € | **65 €** |

Kit biancheria aggiuntivo (secondo letto, letto singolo, ospite in più): **15 € a kit**.

## Decisioni prese con il titolare prima di scrivere

1. **IVA inclusa** — gli importi mostrati sono finali (nota a piè di pagina su tutte e 3 le pagine).
2. **Refill e kit si addebitano sempre**, insieme alla pulizia: il documento mostra il totale pieno
   a check-out con il dettaglio delle tre voci.
3. **Fatturazione mensile a consuntivo** sui check-out effettivamente eseguiti, senza canone fisso
   né minimo mensile.

## Riformulazione chiesta dal titolare

Le cinque cose dette a voce ("magazzino e stoccaggio con la compra dei prodotti, ricarica dei
refill, pulizie complete e professionali, gestione e ordini dei kit biancheria, preparazione dei
letti") non sono state trascritte come elenco operativo: sono diventate **le cinque voci numerate
di pagina 02**, ognuna detta dal punto di vista del cliente (cosa smette di fare lui), e il prezzo
è stato riformulato come **"una tariffa a check-out, tutto compreso"** invece che come somma di tre
addendi. È la differenza fra un preventivo e un listino che si legge in dieci secondi.

## Rigenerare il PDF

```bash
./rigenera-pdf.sh        # richiede Chromium headless (percorso in CHROME=)
```

Per cambiare un prezzo o una riga di testo si modifica direttamente l'HTML (è testo normale,
niente build step) e si rilancia lo script.
