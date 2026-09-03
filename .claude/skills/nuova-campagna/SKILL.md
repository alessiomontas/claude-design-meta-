---
name: nuova-campagna
description: Avvia una nuova campagna dall'inizio alla fine — ricerca di mercato, copywriting, direzione artistica e controllo compliance, in sequenza. Usa questo comando quando devi creare i contenuti per un nuovo prodotto/servizio/target/angolo, invece di richiamare gli agenti singolarmente.
argument-hint: [prodotto/servizio] [target] [canale]
---

# Nuova campagna

Orchestra i quattro agenti di `hadrianus-content-engine` in sequenza per produrre una campagna completa, pronta alla consegna, salvata in `campagne/<nome-campagna>/`.

## Input

Gli argomenti passati al comando possono contenere prodotto/servizio, target e canale in linguaggio libero, ad esempio:

```
/nuova-campagna Consulenza fiscale per PMI, target: piccoli imprenditori, canale: email
```

Se manca qualcosa di essenziale (prodotto/offerta, target, canale) **usa `AskUserQuestion` per chiederlo prima di procedere** — non presumere. Non serve chiedere tutto: solo ciò che è davvero mancante.

## Passaggi (da eseguire in ordine, senza saltarne nessuno)

1. **Determina il nome campagna**: uno slug breve derivato da prodotto+target (es. `consulenza-fiscale-pmi-email`). Crea `campagne/<nome-campagna>/` se non esiste.

2. **Ricerca di mercato** — invoca l'agente `ricercatore-mercato` (tramite lo strumento Agent, `subagent_type: ricercatore-mercato`) passando prodotto/servizio, target e canale raccolti. Attendi il brief in `campagne/<nome-campagna>/brief-mercato.md` prima di proseguire.

3. **Copywriting** — invoca l'agente `copywriter` (`subagent_type: copywriter`), indicando il percorso del brief appena prodotto. Attendi `campagne/<nome-campagna>/copy.md`.

4. **Direzione artistica** — invoca l'agente `art-director` (`subagent_type: art-director`), indicando copy e brief. Attendi `campagne/<nome-campagna>/direzione-artistica.md`.

5. **Controllo compliance** — invoca l'agente `compliance-checker` (`subagent_type: compliance-checker`) sull'intera campagna (brief + copy + direzione artistica). Attendi `campagne/<nome-campagna>/checklist-compliance.md`.

6. **Riporta all'utente**, in breve:
   - l'esito della checklist (APPROVATO / DA CORREGGERE)
   - se "DA CORREGGERE", l'elenco dei punti bloccanti in linguaggio semplice
   - dove si trovano tutti i file prodotti

## Regole

- I passaggi sono sequenziali e ognuno dipende dall'output del precedente: non eseguirli in parallelo, non saltarne nessuno anche per contenuti "semplici" o urgenti.
- Se un agente segnala che gli mancano informazioni per procedere (es. `ricercatore-mercato` non trova un'offerta chiara), fermati e chiedi all'utente prima di continuare alla fase successiva, invece di far proseguire gli agenti a valle su basi incomplete.
- Se `compliance-checker` restituisce "DA CORREGGERE", non considerare la campagna conclusa: proponi all'utente di far correggere i punti bloccanti (rilanciando `copywriter` o `art-director` sui punti specifici) prima di consegnare.
- Non consegnare mai direttamente all'utente un copy che non ha ancora superato `compliance-checker`.
