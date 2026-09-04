# Direzione artistica — Post Facebook: affitto lungo vs gestione totale (versione 2)

> Questa è la **versione 2**, rifatta il 4 settembre 2026 dopo che il titolare ha bocciato la v1.
> La v1 (impianto "scheda tecnica / perizia su carta millimetrata", gancio su usura e deposito cauzionale, barre proporzionali) **non va più ripresa**: registro sbagliato per quello che il titolare vuole comunicare.

**Canvas editabile:** https://claude.ai/code/artifact/6578c0a6-83ca-4c08-9488-1fe5fe347b80
**Sorgenti:** `grafiche/Main.dc.html`, `grafiche/Numeri.dc.html`, `grafiche/Offerta.dc.html`, `grafiche/canvas.json`, `grafiche/immobile-standard.jpg`

## Mood

**Diretto, sicuro di sé, a contrasto secco.** Il titolare ha chiesto un registro marketing, non documentale: il post deve colpire in mezzo secondo nello scroll di un gruppo Facebook e chiudersi con una sfida ("Valuta tu"), non con una spiegazione. Meno righe, corpi più grandi, blocchi pieni al posto delle griglie.

## Palette

Palette fumè di brand invariata (hex esatti in `.claude/reference/design-system.md`), usata qui in modo **binario**: fondo scuro `#3F3A33` / `#2E2A25` per tutto ciò che è problema o contesto, blocchi pieni `#F5F0E6` e oro `#C8A24B` per tutto ciò che è soluzione, numero positivo o chiamata all'azione. Nessun blu navy. È il contrasto stesso a fare il lavoro persuasivo: l'occhio capisce da che parte stare prima di leggere.

## Formati (obbligati — regola fissa 6 di CLAUDE.md, solo Facebook)

| # | File | Formato | Contenuto |
|---|---|---|---|
| 1 | `Main.dc.html` | **1080×1920 (9:16)** | Il gancio: promessa sui 5 anni + sfida finale |
| 2 | `Numeri.dc.html` | 1080×1080 | Tabella di paragone a due colonne, 3 righe |
| 3 | `Offerta.dc.html` | 1080×1080 | Come si parte + nessun deposito + 15% + CTA |

La prima **deve** restare 9:16: nel collage Facebook un 4:5 viene tagliato ai lati (verificato su pubblicazione reale).

## Pattern visivo — "blocchi invertiti a piena larghezza"

Nuovo rispetto a tutte le campagne precedenti (vedi tabella pattern in `design-system.md`): niente card, niente griglia tecnica, niente tratteggi. Ogni immagine è una pila di **fasce piene a tutta larghezza** che si alternano scuro/chiaro, ognuna con un solo messaggio. L'evidenziatore oro sul testo (`background: #C8A24B` inline sulla frase chiave) è la firma grafica di questa campagna.

- **Scheda 01** — tre fasce: contesto scuro con la promessa, fascia chiara piena con "Non è una speranza. È l'impegno che ci prendiamo noi.", fascia scura di chiusura con "Valuta tu." in oro grande. La sfida è staccata e leggibile: è il tono voluto dal titolare, non va annegata.
- **Scheda 02** — intestazioni di colonna (✕ Affitto lungo / ✓ Con Hadrianus), poi 3 righe a due celle affiancate: cella scura opaca a sinistra, cella chiara piena a destra. In fondo, banda con barretta oro: **"Le utenze restano tue."**
- **Scheda 03** — foto reale dell'immobile sotto un gradiente profondo, processo numerato 01→04 in oro, fascia chiara piena con le quattro negazioni sui costi, poi CTA in banda oro piena.

## Elementi chiave

- Cosa si nota per primo: la frase evidenziata in oro (scheda 01), il numero `1.000-1.100 €` a destra (scheda 02), la banda oro della CTA (scheda 03).
- Le formule obbligate da compliance sono in grafica alla lettera: **"Media, non una promessa: ogni casa fa storia a sé."**, **"Le utenze restano tue."**, **"tasse e spese"** (mai "tasse e utenze"), **"Guadagniamo solo se guadagni tu."**, **"standard alberghiero"**.

## Da evitare

- Formule assolute sui costi ("tutto incluso", "l'unica spesa", "nessun altro costo"): TARI e oneri condominiali restano al proprietario e si possono omettere, **mai negare**.
- Cifre non presenti nel copy — in particolare qualunque numero sull'up-sell centro Roma / vicinanza metro.
- Percentuali di morosità e tempi medi di sfratto: indifendibili davanti a questo pubblico.
- Strutture nominate come prova; "hotel-style" al posto di "standard alberghiero".
- Impaginare l'assicurazione come garanzia più assertiva di quanto dica il copy: in grafica si scrive **"eventuali danni causati dagli ospiti"**.

## Correzioni applicate dopo il secondo giro di compliance

| Dove | Prima | Dopo |
|---|---|---|
| `Numeri.dc.html` titolo | "Bilocale a Ostia. Stesso immobile, due strade." | "Stesso tipo di immobile, due strade." (la media è sugli immobili in gestione, non su un bilocale a Ostia) |
| `Numeri.dc.html` colonna destra | "con le procedure di gestione già pagate" | "al netto delle procedure di gestione: commissione, pulizie, biancheria, consumabili" (perimetro esplicito, nessuna negazione implicita su tasse e condominio) |
| `Numeri.dc.html` colonna sinistra | "Tolte tasse e spese — condominio, TARI, manutenzione —" | "Tolte tasse e spese" (l'elenco solo a sinistra rendeva il confronto non omogeneo) |
| `Numeri.dc.html` e `Offerta.dc.html` | "copre i danni causati dagli ospiti" | "copre gli **eventuali** danni causati dagli ospiti" |

## Aperto prima della pubblicazione

Dettagli dell'assicurazione (chi la emette, cosa copre, massimali/franchigie): non bloccano l'impaginazione, ma vanno avuti pronti per rispondere nei commenti — in un gruppo di proprietari la domanda arriva.
