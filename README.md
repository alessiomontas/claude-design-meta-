# Hadrianus Content Engine

Sistema di generazione contenuti di vendita per Hadrianus, basato su Claude Code: un team di agenti specializzati che porta un'idea di campagna dal brief al contenuto pronto per la consegna, sempre nello stesso ordine e con lo stesso metodo.

## Avvio rapido

1. Apri questa cartella con Claude Code (in locale o su claude.ai/code).
2. Al primo utilizzo, popola `riferimenti/` con 2-3 contenuti reali di Hadrianus (vedi `riferimenti/README.md`) — è da lì che gli agenti imparano il tono di voce.
3. Lancia una nuova campagna:

   ```
   /nuova-campagna
   ```

   e rispondi alle domande su prodotto/servizio, target e canale. In alternativa puoi passare le informazioni direttamente:

   ```
   /nuova-campagna Consulenza fiscale per PMI, target: piccoli imprenditori, canale: email
   ```

4. Il risultato viene salvato in `campagne/<nome-campagna>/`: brief di mercato, copy, direzione artistica e checklist di compliance.

## Cosa fa ogni agente

| Agente | Quando entra in gioco | Cosa produce |
|---|---|---|
| `ricercatore-mercato` | Sempre per primo | Brief: target, dolori/desideri, concorrenza, angolo di vendita consigliato |
| `copywriter` | Dopo il brief | Bozze di testo (ads, email, landing, script) secondo il metodo Hadrianus |
| `art-director` | Dopo che il copy è stabile | Direzione visiva (mood, palette, formati) + bozze Canva se collegato |
| `compliance-checker` | Sempre per ultimo | Verifica claim, tono, refusi; approva o segnala cosa correggere prima della consegna |

Puoi anche richiamare un singolo agente fuori dal flusso completo, ad esempio:

```
Usa l'agente compliance-checker su questo testo: [...]
```

## Le due skill

- **`framework-vendita`** — il metodo di scrittura persuasiva usato da tutti gli agenti che producono o valutano testo. È il "manuale interno": aggiornalo man mano che capisci cosa funziona davvero per Hadrianus.
- **`nuova-campagna`** — il comando che orchestra i quattro agenti in sequenza per produrre una campagna completa.

## Struttura cartelle

```
CLAUDE.md                      contesto letto a ogni avvio
README.md                      questo file
riferimenti/                   contenuti reali di esempio, per calibrare il tono
campagne/                      output delle campagne generate (creata al primo uso)
.claude/agents/                i 4 agenti specializzati
.claude/skills/                framework-vendita e nuova-campagna
```

## Collegamento Canva (opzionale)

Se colleghi il connettore Canva a Claude Code, l'agente `art-director` può generare bozze visive direttamente nel tuo workspace Canva. Senza Canva collegato, produce comunque un brief visivo testuale completo (mood board descrittiva, palette, formati per canale) che puoi passare a un grafico o usare tu stesso in Canva.

## Manutenzione del sistema

- Aggiungi nuovi `riferimenti/` ogni volta che un contenuto performa particolarmente bene: è il segnale più forte per affinare il metodo.
- Se noti che il copy prodotto si allontana dal tono Hadrianus, il problema quasi sempre è in `riferimenti/` (pochi esempi, o non rappresentativi) più che negli agenti stessi.
- Le regole "dure" (mai inventare claim, sempre passare da compliance) sono in `CLAUDE.md` e valgono per tutti gli agenti: non vanno duplicate né contraddette nei singoli file agente/skill.
