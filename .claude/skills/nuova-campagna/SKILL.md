---
name: nuova-campagna
description: Avvia una nuova campagna dall'inizio alla fine — ricerca di mercato, copywriting, direzione artistica e controllo compliance, in sequenza. Usa questo comando quando devi creare i contenuti per un nuovo prodotto/servizio/target/angolo, invece di richiamare gli agenti singolarmente.
argument-hint: [prodotto/servizio] [target] [canale]
---

# Nuova campagna

Orchestra gli agenti di `hadrianus-content-engine` in sequenza per produrre una campagna completa, pronta alla consegna, salvata in `campagne/<nome-campagna>/`: ricerca di mercato → copy → direzione artistica e grafiche editabili → compliance → revisione esperta marketing/design.

## Input

Gli argomenti passati al comando possono contenere prodotto/servizio, target e canale in linguaggio libero, ad esempio:

```
/nuova-campagna Consulenza fiscale per PMI, target: piccoli imprenditori, canale: email
```

Se manca qualcosa di essenziale (prodotto/offerta, target, canale) **usa `AskUserQuestion` per chiederlo prima di procedere** — non presumere. Non serve chiedere tutto: solo ciò che è davvero mancante.

## Passaggi (da eseguire in ordine, senza saltarne nessuno)

1. **Determina il nome campagna**: uno slug breve derivato da prodotto+target (es. `consulenza-fiscale-pmi-email`). Crea `campagne/<nome-campagna>/` se non esiste. Controlla `campagne/INDEX.md` per gli angoli/ganci già usati, così il `ricercatore-mercato` non ne ripropone uno identico.

2. **Ricerca di mercato** — invoca l'agente `ricercatore-mercato` (tramite lo strumento Agent, `subagent_type: ricercatore-mercato`) passando prodotto/servizio, target e canale raccolti. Attendi il brief in `campagne/<nome-campagna>/brief-mercato.md` prima di proseguire.

3. **Copywriting** — invoca l'agente `copywriter` (`subagent_type: copywriter`), indicando il percorso del brief appena prodotto. Attendi `campagne/<nome-campagna>/copy.md`.

4. **Direzione artistica + grafiche editabili** — invoca l'agente `art-director` (`subagent_type: art-director`), indicando copy e brief. Produce `campagne/<nome-campagna>/direzione-artistica.md` e, quando possibile, le **grafiche editabili** (canvas Claude Design con la skill `design`, o Canva se collegato) — una artboard per ogni contenuto richiesto, nei formati corretti. I sorgenti/link vanno in `campagne/<nome-campagna>/grafiche/` o riferiti nella direzione artistica.

5. **Controllo compliance** — invoca l'agente `compliance-checker` (`subagent_type: compliance-checker`) sull'intera campagna (brief + copy + direzione artistica). Attendi `campagne/<nome-campagna>/checklist-compliance.md`.

6. **Revisione esperta marketing/design** — invoca l'agente `revisore-marketing-design` (`subagent_type: revisore-marketing-design`) sull'intera campagna già passata da compliance. Valuta impaginazione, contenuti, grafiche/foto, testi ed efficacia commerciale. Attendi `campagne/<nome-campagna>/revisione-marketing-design.md`.

7. **Aggiorna `campagne/INDEX.md`** con la nuova riga (angolo, target/leva, formati, stato).

8. **Riporta all'utente**, in breve:
   - l'esito della checklist compliance (APPROVATO / DA CORREGGERE)
   - il giudizio della revisione esperta (PRONTA / PRONTA CON RITOCCHI / DA RILAVORARE) e gli interventi prioritari
   - dove si trovano tutti i file e le grafiche prodotte

## Regole

- I passaggi sono sequenziali e ognuno dipende dall'output del precedente: non eseguirli in parallelo, non saltarne nessuno anche per contenuti "semplici" o urgenti.
- Se un agente segnala che gli mancano informazioni per procedere (es. `ricercatore-mercato` non trova un'offerta chiara), fermati e chiedi all'utente prima di continuare alla fase successiva, invece di far proseguire gli agenti a valle su basi incomplete.
- Se `compliance-checker` restituisce "DA CORREGGERE", non considerare la campagna conclusa: proponi all'utente di far correggere i punti bloccanti (rilanciando `copywriter` o `art-director` sui punti specifici) prima di consegnare.
- Non consegnare mai direttamente all'utente un copy che non ha ancora superato `compliance-checker`.
