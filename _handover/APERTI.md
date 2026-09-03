# APERTI — problemi noti, dubbi irrisolti, cose fragili, TODO

## Problemi noti / inconsistenze già identificate e MAI risolte

1. **I documenti "di processo" della Campagna 1 sono disallineati dal contenuto pubblicato finale.**
   `brief-mercato.md`, `checklist-compliance.md`, `revisione-marketing-design.md` e `copy.md` (quest'ultimo marcato esplicitamente come superato) citano ancora "Rome Smart Sea" come case study e "hotel-style" in più punti, nonostante queste due cose siano ora **vietate** da regola di brand (vedi REGOLE.md). Solo i file effettivamente pubblicati (grafiche `.dc.html`, PNG, `direzione-artistica.md`, `PIANO-PUBBLICAZIONE.md`, `grafiche/README.md`) sono stati corretti. Questo è stato segnalato esplicitamente all'utente in chat ("i documenti interni di analisi... conservano ancora riferimenti storici... non sono contenuti pubblicati. Se preferisci li ripulisco anche lì...") ma **non è mai arrivata una risposta/conferma dall'utente**, quindi la pulizia non è stata fatta. Un revisore che apra `brief-mercato.md` senza questo contesto rischia di pensare che il case study sia ancora usato.

2. **La Campagna 2 (fiducia) non ha un `checklist-compliance.md` né una `revisione-marketing-design.md` dedicati.**
   A differenza della Campagna 1, la conformità (nessun rendimento garantito, nessun case study, lessico corretto) è stata verificata "a vista" dall'assistente e dichiarata solo nella chat, non prodotta come documento tracciabile nella cartella della campagna. Questo viola, in senso stretto, la regola fissa "Niente contenuto esce senza passare da `compliance-checker`" e "Ogni campagna produce output tracciabile: salvare... checklist di compliance in `campagne/<nome-campagna>/`".

3. **`/nuova-campagna` non è mai stata invocata come comando reale in questa sessione.**
   Entrambe le campagne sono state prodotte "a mano" dall'assistente seguendo lo stesso schema concettuale (ricerca→copy→grafica→compliance→revisione), ma senza passare dal meccanismo di orchestrazione a sub-agenti descritto nella skill. Non c'è quindi la controprova che il comando funzioni davvero end-to-end così com'è scritto oggi. Rischio concreto: se in futuro qualcuno lancia `/nuova-campagna` aspettandosi lo stesso risultato ottenuto in questa chat, il comportamento reale degli agenti-subagente potrebbe divergere (tono, struttura dei file prodotti) da quanto visto qui, perché non è mai stato testato.

4. **Il flusso Playwright per il rendering PNG si è interrotto a metà almeno due volte durante la sessione** (il processo in background veniva chiuso prima di completare tutti i file), richiedendo di rilanciare manualmente il rendering per i file mancanti con uno script "one-off" scritto al volo. Lo script definitivo salvato nel repo (`build-and-render.mjs`) NON ha mai fallito da solo in un singolo run pulito e verificato interamente: è stato sempre completato con l'aiuto di run parziali aggiuntivi. Chi riesegue questo script in futuro dovrebbe verificare che tutti i PNG attesi siano stati effettivamente scritti in `out/`, non fidarsi ciecamente dell'exit code.

5. **Nessuna foto reale è mai stata fornita dal cliente.**
   Tutte le grafiche di entrambe le campagne sono composizioni tipografiche pure. Questo era segnalato come limite nella prima revisione ("Sostituire i placeholder `[FOTO]` con foto reali... è l'intervento a più alto impatto") ma nel frattempo il design è stato rifatto per non dipendere più da foto/placeholder (le versioni attuali funzionano senza foto). Resta comunque vero che, se il cliente fornisse foto reali, oggi nessuna grafica le userebbe — sarebbe un lavoro di redesign, non di semplice sostituzione.

## Dubbi non risolti (mai chiesti esplicitamente all'utente, o chiesti e rimasti in sospeso)

6. **Nessun feedback del cliente Hadrianus reale è mai stato raccolto** su nessuno dei contenuti prodotti (né copy né grafiche). Ogni validazione (compliance, revisione esperta) è simulata dall'assistente sulla base delle regole scritte, non da una persona lato cliente. Prima di pubblicare qualunque contenuto realmente sui canali social di Hadrianus, andrebbe fatto un giro di validazione umana.

7. **Il gruppo Facebook target non è mai stato specificato**: tutti i testi usano il placeholder `[Nome Città/Quartiere]` da compilare manualmente prima della pubblicazione. Non è chiaro se l'utente abbia già in mente i gruppi specifici o se vada fatta una ricerca di gruppi locali pertinenti.

8. **Follow-up proposti dall'assistente e mai confermati dall'utente**, sospesi al momento dell'handover:
   - generare caption dedicate per ciascuna delle 3 storie della Campagna 2 (oggi `copy-e-piano.md` ha caption solo per i 2 caroselli);
   - generare un post Facebook a 3 immagini abbinato alla Campagna 2 (fiducia) — oggi il post Facebook a 3 immagini esiste solo per la Campagna 1.

9. **Rendiconti/trasparenza economica menzionati nel copy** ("Rendiconti chiari, tutto tracciato" — Storia 2 della Campagna 2) non sono un servizio verificato in `riferimenti/`: è un'estensione plausibile del claim "guadagniamo solo se guadagni tu / 15% sul fatturato", ma non è stata segnalata come `[DATO DA VERIFICARE]` né esplicitamente confermata dall'utente come servizio realmente offerto. Andrebbe verificato con il cliente prima della pubblicazione.

10. **Le meccaniche di verifica ospiti ("ospiti verificati sulle piattaforme")** citate nella Campagna 2 come rassicurazione sono descritte nell'agente `art-director`/`compliance-checker` come "verifica standard sulle piattaforme (processo), non una garanzia assoluta" — questa distinzione è scritta nel copy interno ma **non compare nel testo pubblico** delle grafiche/caption. Se un proprietario la interpretasse come garanzia assoluta e succedesse un incidente con un ospite, il claim potrebbe essere contestato. Da valutare se aggiungere un disclaimer visibile.

## Cose fragili (funzionano ma con dipendenze poco robuste)

11. **Il rendering PNG dipende da un percorso hard-coded fuori dal repository**: `/opt/pw-browsers/chromium-1194/chrome-linux/chrome` (binario Chromium) e `/opt/node22/lib/node_modules/playwright/index.js` (libreria Playwright), entrambi impostati come variabile d'ambiente o import assoluto negli script. Se questo progetto viene spostato su un'altra macchina/ambiente, questi percorsi vanno adattati o gli script falliscono silenziosamente/con errore di modulo non trovato.

12. **Il canvas editabile pubblicato (Artifact) non ha una wake-subscription attiva**: durante la sessione, ogni tentativo di registrare un "watch" sull'Artifact per essere notificati di modifiche esterne è stato rifiutato dal servizio ("subscribe_forbidden"). Questo significa che se qualcuno modifica il canvas online (es. l'utente stesso, editando visivamente), **questa sessione non lo saprebbe** e un futuro aggiornamento da codice rischierebbe di sovrascrivere le modifiche fatte a mano nell'editor, a meno di rileggere esplicitamente l'Artifact prima di ripubblicare.

13. **Le due campagne condividono lo stesso schema di script (`build-and-render.mjs`) ma sono due copie indipendenti**, non un modulo condiviso: una correzione allo script di rendering fatta in una campagna (es. bugfix nella conversione `.dc.html`→HTML standalone) non si propaga automaticamente all'altra. Se in futuro si trova un bug nel rendering, va corretto in entrambi i file.

## TODO espliciti (cose da fare, non solo da verificare)

- [ ] Decidere se e come allineare i documenti storici della Campagna 1 (punto 1) — riscriverli o marcarli chiaramente come archivio.
- [ ] Produrre `checklist-compliance.md` e (se voluto) `revisione-marketing-design.md` per la Campagna 2, per pareggiare lo standard della Campagna 1.
- [ ] Decidere se testare `/nuova-campagna` end-to-end almeno una volta, per validare che il comando descritto funzioni davvero come scritto.
- [ ] Raccogliere feedback reale dal cliente Hadrianus su almeno un pezzo di contenuto prima di considerare qualunque campagna "pronta alla pubblicazione" definitiva.
- [ ] Decidere sui due follow-up sospesi (punto 8: caption storie Campagna 2, post Facebook Campagna 2).
- [ ] Se il cliente fornirà foto reali in futuro, prevedere un giro di redesign delle grafiche per integrarle (oggi nessun artboard ha uno spazio-immagine pensato apposta).
