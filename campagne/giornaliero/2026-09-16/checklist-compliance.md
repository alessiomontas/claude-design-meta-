# Checklist compliance — Giornaliero 2026-09-16 "Il costo del vuoto"

## Esito
DA CORREGGERE

## Bloccanti (da correggere prima della consegna)

1. **Claim non verificato e vietato: "Simulazione gratuita del rendimento."**
   - `grafiche/build.py:222` (C5) e `grafiche/build.py:326` (S2) → propagato in `grafiche/C5.dc.html:26`, `grafiche/S2.dc.html:25`, `png/C5.png`, `png/S2.png`.
   - Non esiste in `copy.md` (divergenza non autorizzata), promette un servizio gratuito mai confermato dal titolare e introduce la parola **rendimento**, vietata dal brief (punto 11, vincoli riga 121) e dalla nota di perimetro di `copy.md:10`.
   - Correzione: **rimuovere la riga** da entrambe le slide (nessuna sostituzione: sotto la CTA non serve nulla). Se serve una riga di chiusura, l'unica ammessa è `Guadagniamo solo se guadagni tu.` — già presente sopra la CTA.

2. **Refuso grammaticale ripetuto: "Anche senza nessuno residente"**
   - `grafiche/build.py:14` (voce 02 delle VOCI) → stampato in C3, F2, S1 (`png/C3.png`, `png/S1.png`) e presente in `copy.md:34`, `copy.md:67` (reel 3,6-4,6 s), `copy.md:234`, `copy.md:412`.
   - "nessuno" davanti a un sostantivo è errato.
   - Correzione: `Anche senza nessuno residente` → **`Anche se non risiede nessuno`** (in `copy.md:34` e caption: `Si paga anche se in casa non risiede nessuno` — già corretto nelle caption, allineare le grafiche).

3. **Marcatore `[DATO DA VERIFICARE]` ancora aperto nel pacchetto**
   - `brief-mercato.md:67` (spesa condominiale media annua).
   - Il dato non viene usato in nessun contenuto: correzione = riscrivere la cella come **`⛔ NESSUNA FONTE AFFIDABILE — non stimare, non pubblicabile. Nominata solo come voce.`**, eliminando il marcatore.

4. **"nessun costo fisso" ancora presente nel brief** (doveva essere rimosso da tutto il pacchetto, domanda aperta al titolare dal 14/09)
   - `brief-mercato.md:24`: `**15% sul fatturato generato**, nessun costo fisso noto oltre questo.` → **`**15% sul fatturato generato**. (Eventuali costi una tantum d'avvio: domanda aperta al titolare, non comunicabile.)`**
   - `brief-mercato.md:26`: `Hadrianus non aggiunge un costo fisso a un problema di costi fissi` → **`la nostra voce esiste solo se la casa ha incassato`**.
   - `brief-mercato.md:125`: `il 15% senza costi fissi` → **`il 15% sul fatturato generato`**.
   - `brief-mercato.md:34`: `senza spendere soldi per farla partire` → **`senza doverci pensare`** (implica spesa d'avvio zero, non confermata).

5. **Nota di demerito verso il proprietario in `copy.md:552` (S2, punto 3)**
   - Testo attuale: `Gestire da soli non dà gli strumenti per tenere un calendario aperto tutto l'anno. Non è una questione di impegno: è che quel lavoro è un mestiere a parte.`
   - "Gestire da soli non dà gli strumenti" giudica il modo di fare del proprietario.
   - Correzione: allineare `copy.md` al testo già corretto in grafica (`build.py:314-315`): **`Tenere un calendario aperto tutto l'anno è un mestiere a parte.`**

6. **F1: manca la firma di brand prevista dal layout**
   - `copy.md:397` prevede `firma | Guadagniamo solo se guadagni tu.` in F1; in `build.py` (F1, righe 233-247) non c'è.
   - Correzione: aggiungere `blocco(['Guadagniamo solo se guadagni tu.'], …)` sopra la CTA di F1, oppure eliminare la riga dal layout di `copy.md`. La formula è **"Guadagniamo solo se guadagni tu"** (verificata corretta ovunque nel pacchetto).

7. **Il reel R1 non esiste come artboard**
   - `copy.md` §1 descrive un reel da 17 s, ma in `grafiche/` non c'è nessun file R1/reel e in `png/` non c'è nessun frame. Il pacchetto giornaliero richiede 5 contenuti: oggi ne sono prodotti 4.
   - Correzione: produrre gli artboard del reel (o almeno i key-frame editabili) prima della consegna.

## Osservazioni (non bloccanti, ma da considerare)

- **Aritmetica ISTAT verificata**: 9.581.772 / 35.271.829 = 27,166% → 27,2% corretto; fonte `ISTAT, Censimento permanente 2021` visibile a video in C2 (`build.py:179`) e F1 (`build.py:244`). ✔
- **"1 casa su 4" sottostima il dato**: in C2 (`build.py:174`) il titolo dice `1 casa su 4 in Italia non è occupata.` mentre il display dice 27,2% e le caption dicono correttamente "più di una su quattro". Difendibile, ma incoerente: consigliato `Più di 1 casa su 4 in Italia non è occupata.` (la barra 1/4 può restare).
- **`TOTALE ALL'ANNO`** (C3, `build.py:63`): forma zoppa. Meglio **`TOTALE IN UN ANNO`** o `TOTALE ANNUO`.
- **Divergenze minori copy.md ↔ build.py** (da riallineare in `copy.md`, il testo stampato è accettabile):
  - voce 03: copy `Quote condominiali ordinarie` → grafica `Quote condominiali` (l'aggettivo "ordinarie" è sostanziale, esclude le straordinarie: preferibile tenerlo almeno nel dettaglio);
  - voce 05: copy `Quota fissa dei contatori` → grafica `Quota fissa contatori`;
  - C1/F1/S2: gancio su 3 righe invece di 2 (scelta motivata a commento, ok);
  - F1: la grafica aggiunge la CTA `Scrivi CALCOLO in DM` oltre a `Salva questo post` (ok, la 1ª del collage deve avere la CTA) — aggiornare `copy.md:381`;
  - C5: la riga di corpo `La nostra voce compare solo a incasso avvenuto.` (`copy.md:313`) non è in grafica;
  - S1: i servizi e `Si parte da com'è` (`copy.md:519`) non sono in grafica.
  - `fonte()` rende a 22 px, `copy.md` dichiara 17: allineare la tabella di layout.
- **Foto F1 (`pranzo-banda.jpg`)**: dalla finestra si vedono **palme tropicali** e l'insieme ha un aspetto da render. Nessun marchio di terzi visibile (nessun logo, elettrodomestico o schermo brandizzato in F1/S1/C1), quindi non è bloccante, ma in un post che parla di case a Roma e Ostia mina la credibilità: sostituire con un'immagine senza vegetazione tropicale.
- **Barra dei 12 mesi in S2** (`build.py:304`, piene=[5,6,7,9]): 4 celle su 12 possono essere lette come un tasso di occupazione del 33%. Nessuna percentuale è scritta, quindi resta un simbolo di stato; se si vuole azzerare il rischio, rendere le celle piene in numero irregolare e non allineate a una frazione leggibile.
- **Verificato conforme**: nessuna aliquota IMU, nessun totale del costo del vuoto, nessuna tariffa/occupazione/rendimento stampati; scadenze IMU 16 giugno / 16 dicembre corrette; TARI dovuta senza residenti coerente col regolamento citato; "standard alberghiero" usato ovunque, mai "hotel-style"; nessun case study su strutture nominate; nessun confronto con concorrenti nominati nei contenuti; formula "nessuno te l'ha mai messo su una riga sola" presente in F2 e S1; accenti e apostrofi corretti nei PNG (`è`, `È`, `com'è`, `Perché`, `l'anno`).

## Coerenza col tono Hadrianus
In linea. Registro concreto da bollettini e scadenze, nessun gergo da consulente, il 15% arriva in chiusura come conseguenza e non come pitch. L'unica frattura di tono è la riga **"Simulazione gratuita del rendimento."**: è linguaggio da lead magnet generico, opposto all'intero impianto del giorno ("Non ci sono cifre nostre: questo conto è solo tuo") — motivo in più per toglierla.
