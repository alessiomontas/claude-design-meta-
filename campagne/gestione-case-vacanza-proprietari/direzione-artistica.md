# Direzione artistica — Gestione case vacanza / Acquisizione proprietari

## Mood
**Elegante, rassicurante, standard alberghiero.** Deve trasmettere lo stesso livello che il copy promette: pulito, curato, premium ma accessibile — non "agenzia immobiliare aggressiva", non "cartello vendesi". Tono visivo mediterraneo/costiero (Roma, Ostia, mare) che parla di lifestyle e di rendita serena. Coerente con l'idea "il tuo immobile lavora, tu no": immagini che respirano, non affollate.

## Palette
Palette premium calda basata su un **grigio fumè** (niente blu navy — regola fissa). Il fumè è una miscela di nero, marrone e giallo: caldo, non freddo. Coerente su tutti i formati:

| Ruolo | Colore | HEX | Uso |
|---|---|---|---|
| Base scuro | Grigio fumè caldo | `#3F3A33` | Sfondi storie problema/soluzione, testi forti |
| Base scuro (profondo) | Fumè profondo | `#2E2A25` | Fondo dei gradienti, contrasto |
| Accento caldo | Oro sabbia | `#C8A24B` | Numeri chiave, CTA, dettagli premium |
| Chiaro | Bianco caldo / sabbia | `#F5F0E6` | Sfondi prova sociale, testo su scuro |
| Secondario | Pietra / oliva calda | `#9A8A63` | Etichette, icone, dettagli |
| Testo neutro | Bruno scuro | `#26241F` | Corpo su fondo chiaro |

L'oro sabbia è il colore dell'azione: appare solo su numeri-prova (183€, 5.0, 15%) e CTA, così l'occhio va sempre lì. Il fumè caldo sostituisce ovunque il vecchio navy.

## Tipografia
- **Titoli/hook:** un sans-serif geometrico e deciso (peso bold/extrabold), maiuscolo o alto contrasto, per fermare lo scroll.
- **Corpo/sottotitoli:** stesso sans in peso regular/medium, alta leggibilità su mobile.
- Coerenza assoluta tra storie, post e reel: stessa famiglia, stessa gerarchia.

## Formati per canale
- **Storie (5):** 1080x1920 px. Testo grande nella fascia centrale; **margine di sicurezza**: niente testo/CTA nei ~250px in alto (avatar/UI) e ~300px in basso (barra risposta). CTA sticker in zona pollice (basso-centro, ma sopra la barra).
- **Post feed (2):** 1080x1080 px. Overlay testo forte in alto o centro; logo Hadrianus discreto in un angolo; box numeri ad alto contrasto sul post 2.
- **Reel:** video 1080x1920 + **cover** 1080x1920 coordinata (stessa palette/typo delle storie). Testo a schermo grande, leggibile anche senza audio (molti guardano in muto).

## Gerarchia visiva (cosa si nota per primo)
1. **Hook/numero-prova** (grande, in oro o bianco su navy) → ferma lo scroll.
2. **Beneficio/sottotitolo** (medio) → spiega.
3. **CTA** (oro, riquadrata) → dice cosa fare.
Una sola CTA visibile per contenuto. Logo sempre presente ma mai protagonista.

## Elementi chiave per pezzo
- **Storie 1-2:** fondo navy, testo bianco/oro, atmosfera "problema" → contrasto forte, poco affollamento.
- **Storia 3:** 4 icone servizi (pricing, check-in H24, ospiti, pulizie) in verde-acqua/oro su navy.
- **Storia B & Post confronto:** la prova è basata su dati di mercato/differenziatori (nessuna morosità, standard alberghiero, 15%), non su singole strutture.
- **Storia 5 & Reel finale:** CTA "CALCOLO in DM" in oro, massima visibilità.
- **Post 1:** foto immobile curato + overlay "Il tuo immobile lavora. Tu no." in bianco su gradiente scuro.

## Foto
- Preferire **foto reali** di immobili in gestione: interni curati, luce naturale, taglio editoriale. Non citare il nome di singole strutture come prova (regola di brand).
- Dove non disponibili, usare placeholder chiaramente segnati e sostituirli prima della pubblicazione: **non spacciare stock generico per struttura Hadrianus**.
- Evitare: foto sgranate, grandangoli distorti, interni disordinati — contraddirebbero la promessa di standard alberghiero.

## Da evitare
- Troppo testo per schermo (soprattutto nelle storie): una idea per schermata.
- Palette incoerente tra i pezzi o colori accesi fuori palette.
- Toni "svendita/urgenza fittizia": qui l'urgenza è la simulazione gratuita, non finti countdown.
- CTA multiple nello stesso contenuto.

## Grafiche editabili
Generate come **canvas Claude Design** (`.dc.html`, artboard editabili): 5 storie + 2 post + 1 cover reel, tutte nella palette e tipografia sopra.
- Sorgenti: `campagne/gestione-case-vacanza-proprietari/grafiche/` (`Main.dc.html`, `Storia2-5.dc.html`, `Post1-2.dc.html`, `ReelCover.dc.html`, `canvas.json`).
- Artefatto modificabile pubblicato: https://claude.ai/code/artifact/4cbc01e6-0fdf-40dc-8fc9-3d87f3295e75 (modifica visiva + export PNG/PDF).
- Canva non risultava collegato in questa sessione → prodotto il kit editabile Claude Design come alternativa modificabile.
- **Foto:** tutte le artboard con immagine usano placeholder segnati `[FOTO]` da sostituire con foto reali delle strutture prima della pubblicazione.
