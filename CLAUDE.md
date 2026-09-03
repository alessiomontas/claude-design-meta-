# Hadrianus Content Engine

Questo repository è il motore di generazione contenuti di vendita di **Hadrianus**. Claude Code legge questo file a ogni avvio: contiene il contesto, le regole e il flusso di lavoro che ogni agente deve rispettare.

## Cos'è questo sistema

Un team di agenti specializzati che, dato un prodotto/servizio, un target e un canale, produce contenuti di vendita pronti alla consegna (ads, email, landing page, script) seguendo sempre lo stesso metodo, calibrato sugli esempi reali in `riferimenti/`.

Non si scrive mai copy "a braccio": prima si studia il mercato, poi si scrive seguendo il framework, poi si dà direzione grafica, infine si controlla tutto prima di consegnare.

## Struttura del progetto

```
CLAUDE.md                      → questo file, contesto globale
README.md                      → istruzioni rapide d'uso
riferimenti/                   → contenuti reali di esempio (il "tono di voce" da imitare)
.claude/agents/
├── ricercatore-mercato.md     → studia target/angolo prima di scrivere
├── copywriter.md              → scrive i testi seguendo il metodo
├── art-director.md            → direzione grafica (+ Canva, se collegato)
└── compliance-checker.md      → controllo finale prima della consegna
.claude/skills/
├── framework-vendita/         → il metodo di vendita, richiamato da ogni agente
└── nuova-campagna/            → comando che orchestra gli agenti in sequenza
```

## Flusso di lavoro standard

Per ogni nuova campagna, l'ordine è sempre lo stesso e va rispettato:

1. **`ricercatore-mercato`** — analizza prodotto, target, concorrenza e angolo di vendita. Produce un brief scritto.
2. **`copywriter`** — scrive i testi partendo dal brief, seguendo la skill `framework-vendita` e lo stile di `riferimenti/`.
3. **`art-director`** — definisce la direzione visiva coerente col copy (e genera bozze su Canva, se il connettore è attivo).
4. **`compliance-checker`** — ultimo controllo prima della consegna: claim verificabili, tono coerente, refusi, formattazione.

Il comando `/nuova-campagna` esegue questi quattro passaggi in sequenza. Non saltare mai un passaggio, anche per contenuti "veloci": è il motivo per cui questo sistema esiste.

## Regole non negoziabili

- **Mai inventare claim, numeri, risultati o testimonianze.** Se un dato non è verificato, va segnalato come tale (es. "[DATO DA VERIFICARE]"), mai scritto come fatto.
- **Il tono di voce si calibra sempre su `riferimenti/`**, non su preferenze generiche di stile. Se `riferimenti/` è vuoto o incompleto, chiedilo esplicitamente all'utente prima di scrivere copy definitivo.
- **Niente contenuto esce senza passare da `compliance-checker`.** Anche una singola email o un singolo post.
- **Ogni campagna produce output tracciabile**: salvare brief, copy, direzione artistica e checklist di compliance in `campagne/<nome-campagna>/` (la cartella viene creata al bisogno).
- Se mancano informazioni essenziali (chi è il target, qual è l'offerta, quali claim sono verificati) **fermarsi e chiederle**, non presumerle.

## Come aggiungere/aggiornare i riferimenti

`riferimenti/` deve contenere contenuti reali già scritti (o performanti) da Hadrianus: sono l'unico modo per gli agenti di imparare il vero tono di voce, non un'imitazione generica di "buon copywriting". Vedi `riferimenti/README.md` per il formato.

## Note tecniche

- Gli agenti in `.claude/agents/` sono richiamabili singolarmente (per interventi mirati, es. "usa compliance-checker su questo testo") oppure in sequenza tramite `/nuova-campagna`.
- La skill `framework-vendita` è il "manuale del metodo": è un punto di partenza strutturato, va raffinata via via che si aggiungono riferimenti reali e si osserva cosa funziona meglio per Hadrianus.
- L'integrazione Canva (agente `art-director`) è opzionale: se il connettore Canva non è collegato, l'agente produce comunque un brief visivo testuale dettagliato invece delle bozze grafiche.
