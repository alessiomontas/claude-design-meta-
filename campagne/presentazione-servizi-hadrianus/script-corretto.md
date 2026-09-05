# Reel "Presentazione servizi Hadrianus" — revisione

Fonte: video caricato dall'utente (37.5s, 1080×1920, girato/montato fuori da questa pipeline — non tracciato prima d'ora). Angolo: **presentazione dei 4 pilastri del servizio** (trasparenza, fisco, cura, rendita) → non ancora usato nelle campagne esistenti (vedi `INDEX.md`), diverso da "rischio affitto tradizionale" e da "fiducia/come funziona".

## Cosa funziona (tenere)

- Hook diretto nei primi 2s: "Hai un appartamento a Roma o sul litorale?" — buona domanda di qualificazione.
- Struttura a pilastri (Trasparenza → Fisco & Regolamenti → Cura Totale → Rendita → Senza Stress → CTA): logica, facile da seguire.
- Foto reali del brand (cartellina in pelle, chiavetta, olio, cartoncino "Welcome to Ostia", busto/tempio) — coerente con la preferenza di usare asset reali invece di elementi solo tipografici.
- Palette fumè scuro + oro/giallo sulle pillole di testo: coerente col design system, nessun blu navy.
- CTA finale chiaro con numero di telefono ripetuto e leggibile.
- Formato 9:16 corretto per Reel.

## Problemi trovati

1. **[COMPLIANCE — bloccante]** Headline "RENDITA ALTA GARANTITA" (~t=24-27s). `lessico-brand.md` vieta esplicitamente il "rendimento garantito": *"Mai promettere un risultato garantito — rischio di pubblicità ingannevole"*. Va riscritta.
2. **[COMPLIANCE — bloccante, trovato dal compliance-checker]** "Legalità 100%" (~t=14-16s): percentuale presentata come fatto, non supportata da una fonte verificata → riformulare senza cifra: **"Piena legalità"**.
3. **[COMPLIANCE — da correggere, trovato dal compliance-checker]** "Massima visibilità" (~t=24-27s): superlativo assoluto senza prova → **"Visibilità ottimizzata"** (coerente con "Tariffe ottimizzate" nella stessa pillola).
4. **Refuso sull'asset brandizzato**: la cartellina in pelle mostrata più volte (t≈12-20s) riporta "HADRIANUS **Multtservce**" invece di "Hadrianus Multiservice". Se è un mockup grafico va corretto alla fonte prima di riusarlo; se è un oggetto fisico stampato, segnalarlo per la ristampa.
5. **Battuta morta** a t≈6-7s: 3 pallini bianchi (indicatore da carosello/slide) sopra il tramonto, senza testo né contenuto — sembra un residuo di template non pensato per un reel (dove non si può "swipare"). Costa ~1.5s subito dopo l'hook, il momento più delicato per la ritenzione.

**Verificato da `compliance-checker`**: via libera su "Rendita Ottimizzata", "Burocrazia zero", "Zero pensieri", "Gestione tasse" (impegni di servizio, non risultati economici promessi al cliente); nessun case study nominato, nessuna testimonianza, nessun "hotel-style".

## Script corretto (timeline)

| t | Testo a schermo | Immagine | Nota |
|---|---|---|---|
| 0-4s | "Hai un appartamento a Roma o sul litorale? E vuoi guadagnare senza pensieri?" | Tramonto/silhouette piante (invariata) | Tenere l'hook; completare la seconda domanda invece di lasciarla troncata su "E VUOI" |
| 4-6s | *(taglio diretto, niente pallini)* | Ingresso arco + scrivania home office | Rimuovere lo stacco a pallini: tagliare diretto sulla scena successiva |
| 6-10s | "Trasparenza" + pillole "Report chiari" / "Pagamenti puntuali" | Scrivania/ufficio (invariata) | Invariata |
| 10-16s | "Fisco & Regolamenti" + pillole "Burocrazia zero" / "Gestione tasse" / **"Piena legalità"** (sostituisce "Legalità 100%") | Documenti brandizzati Hadrianus (invariata, **correggere il refuso "Multtservce" sulla cartellina prima di rigirare/riesportare**) | Fix compliance: nessuna percentuale non verificata |
| 16-20s | "Cura Totale" + pillole "Pulizie professionali" / "Personale addestrato" / "Manutenzione interna" | Mani che aprono il vassoio con cartellina, olio, chiavetta (invariata) | — |
| 20-27s | **"Rendita Ottimizzata"** (sostituisce "Rendita Alta Garantita") + pillole **"Visibilità ottimizzata"** (sostituisce "Massima visibilità") / "Tariffe ottimizzate" / "Zero pensieri" | Terrazzo vista mare, poltrona sospesa, cartoncino "Welcome to Ostia" (invariata) | Fix compliance: nessuna promessa di rendimento garantito, nessun superlativo senza prova |
| 27-30s | "Senza Stress" | Uomo con spritz al tramonto (invariata) | — |
| 30-32s | "Scopri come" | Aperitivo + menu brandizzato (invariata) | — |
| 32-37s | "Gestione case vacanze — Scopri i nostri servizi, contattaci ora" + numero "+39 351 730 5472" | Mockup telefono + busto/tempio Hadrianus (invariata) | Valutare aggiungere in chiusura "Guadagniamo solo se guadagni tu" (leva di fiducia ricorrente del brand) come sottotitolo prima del numero |

## Claim verificati per questa versione (confermato da `compliance-checker`)

- "Burocrazia zero", "Gestione tasse", "Piena legalità", "Zero pensieri": promesse sul **servizio** che Hadrianus si impegna a fornire (non sul risultato economico del cliente) → consentite, coerenti con "gestione documentale & pratiche amministrative" già in brief.
- "Rendita Ottimizzata": sostituisce un claim di risultato garantito con un claim di processo (ottimizzazione tariffe/visibilità), verificabile e coerente con "pricing dinamico" già in `brand-identity.md`.
- "Visibilità ottimizzata": sostituisce il superlativo assoluto "Massima visibilità" (non provato) con un claim di processo, coerente con "Tariffe ottimizzate" nella stessa pillola.
- Nessun nome di struttura specifica, nessuna testimonianza, nessun numero di rendimento inventato, nessuna percentuale non supportata: OK.
