# Hadrianus Content Engine

Motore di generazione contenuti di vendita di **Hadrianus** (property management case vacanza, Roma/Ostia). Claude Code legge questo file a ogni avvio: contiene **solo ciò che deve sempre essere in memoria** — identità minima, flusso, regole fisse, lessico. Il resto (contesto esteso, palette/componenti, glossario con esempi) sta in `.claude/reference/` e va letto on-demand, non è precaricato: tienilo così, non spostarci dentro le regole fisse.

Un team di agenti produce contenuti (storie, post, caroselli, reel, Facebook) sempre con lo stesso metodo: ricerca → copy → grafica → compliance → revisione. Mai copy "a braccio". Per chi è Hadrianus, target, offerta e angoli già usati → **`.claude/reference/brand-identity.md`**.

## Struttura del progetto

```
CLAUDE.md                       → questo file: nucleo sempre caricato
README.md                       → istruzioni rapide d'uso
riferimenti/                    → contenuti reali del cliente (tono di voce da imitare)
brand-assets/                   → logo, foto ambientazione, foto immobili reali (vedi brand-assets/README.md)
campagne/
├── INDEX.md                    → indice campagne: angoli/ganci già usati, da consultare prima di una nuova
├── giornaliero/                → produzione quotidiana
│   ├── PIANO.md                →   pilastri per giorno della settimana + registro di ciò che è già uscito
│   └── <AAAA-MM-GG>/           →   pacchetto del giorno (reel, carosello, post FB, 2 storie) + PUBBLICAZIONE.md
└── <nome-campagna>/            → output tracciabile di ogni campagna monotematica
_handover/                      → snapshot per revisore esterno (stato, decisioni, regole, inventario, aperti)
.claude/agents/                 → i 5 agenti (ricercatore-mercato, copywriter, art-director, compliance-checker, revisore-marketing-design)
.claude/skills/                 → framework-vendita (metodo), nuova-campagna (campagna), giornata (produzione quotidiana)
.claude/reference/              → approfondimenti on-demand, NON precaricati:
├── brand-identity.md           →   chi è Hadrianus, target/pain-point, cosa si può usare come prova
├── design-system.md            →   palette hex, tipografia, formati canale, componenti .dc.html riutilizzabili
├── lessico-brand.md            →   glossario esteso corretto/vietato, con esempi
├── modello-reel-8-secondi.md   →   telaio dei reel brevi (negazione + desideri), tempi e tipografia
├── reel-virali.md              →   manuale di montaggio reel: formati senza volto/voce, ritmo, loop, 3 strutture al secondo
├── prompt-immagini.md          →   framework prompt Midjourney/DALL·E/Leonardo: 5 blocchi, negative, lock di brand
└── master-template.md          →   formato fisso di ogni contenuto + griglia + controllo qualità
```

## Flusso di lavoro standard

1. **`ricercatore-mercato`** — analizza prodotto, target, concorrenza, angolo (legge `brand-identity.md` + `campagne/INDEX.md` per non ripetere un angolo già usato). Produce un brief.
2. **`copywriter`** — scrive seguendo `framework-vendita` e lo stile di `riferimenti/` (consulta `lessico-brand.md` per i termini corretti).
3. **`art-director`** — direzione visiva + **grafiche editabili** (canvas Claude Design, o Canva se collegato), usando `design-system.md` come fonte di palette/componenti.
4. **`compliance-checker`** — claim verificabili, tono, refusi, marchi di terzi nelle foto.
5. **`revisore-marketing-design`** — revisione esperta finale prima della consegna.

Il comando `/nuova-campagna` orchestra questi passaggi. Non saltarne mai uno, anche per contenuti "veloci".

## Produzione quotidiana

Oltre alle campagne monotematiche, il brand produce **ogni giorno** un pacchetto fisso: 1 reel, 1 carosello (5 slide), 1 post Facebook (3 immagini), 2 storie autoconclusive. Lo orchestra il comando **`/giornata`**, che usa lo stesso flusso a 5 agenti e salva in `campagne/giornaliero/<AAAA-MM-GG>/`.

Il pilastro del giorno e il registro di ciò che è già uscito stanno in **`campagne/giornaliero/PIANO.md`** — va letto prima di scegliere l'angolo e aggiornato dopo, sempre. La pubblicazione resta manuale (nessuno strumento qui pubblica su Instagram/Facebook): ogni giorno esce un `PUBBLICAZIONE.md` con orari, file e caption pronte.

## Preferenze fisse di output (SEMPRE — decise dall'utente)

1. **Ogni grafica deve essere EDITABILE come su Canva.** Mai solo immagini piatte. L'utente deve poter aggiungere elementi, spostarli, ridimensionarli, cambiare font, modificare testo inline. Default: **canvas Claude Design** (skill `design`) o Canva se collegato. PNG solo come export aggiuntivo, mai sostitutivo.
2. **Vietato il blu navy.** Base scura brand = **grigio fumè caldo**. Palette esatta in `.claude/reference/design-system.md`.
3. **Le storie sono autoconclusive, mai a carosello.** Ogni storia dà da sola problema E soluzione in poche frasi + CTA. Il carosello resta valido solo per i POST del feed.
4. **Genera SEMPRE anche la grafica, di default.** Ogni contenuto (post, storia, reel, annuncio) ha la sua grafica editabile abbinata, senza che l'utente la chieda.
5. **Varia il design tra un contenuto/campagna e l'altro.** Stessa identità (fumè + oro, Archivo/Manrope), layout sempre diverso — controlla i pattern già usati in `design-system.md` prima di iniziare.
6. **Post Facebook — formato fisso (SOLO Facebook).** Sempre 3 immagini: 1ª **verticale 1080×1920 (9:16)** (gancio+problema), 2ª e 3ª **quadrate 1080×1080** (soluzione, offerta/CTA). La 1ª deve essere 9:16 — nel collage Facebook un 4:5 viene tagliato ai lati.
7. **Ogni contenuto esce nel Master Template.** Copy + layout a tabella + prompt grafico in inglese + negative + parametri + tabella claim. Formato fisso in `.claude/reference/master-template.md`. Niente template, niente consegna.
8. **Output lean.** In chat: liste e tabelle, zero preamboli, zero spiegazioni di processo. Il ragionamento sta nei documenti di campagna. Una modifica tocca solo l'elemento richiesto, mai l'intera campagna.
9. **Controllo qualità prima della consegna, non dopo.** I sei controlli di `master-template.md` si fanno sul PNG renderizzato, guardato a dimensione telefono, prima di mostrare qualcosa.
10. **Il reel si costruisce dentro Canva, sempre.** Da ogni campagna in poi il reel — e solo il reel — nasce direttamente in un progetto Canva che il titolare indica con un link `/edit`: pagine 1080×1920, una pagina per scena, testi e forme native Canva (nessuna immagine necessaria). Le animazioni le mette il titolare dentro Canva. Tutto il resto del pacchetto — carosello, post Facebook, storie — resta sul flusso esistente (artboard `.dc.html` su canvas Claude Design). Il `scene.json` resta la fonte unica: `.claude/skills/giornata/scene_to_canva.py` lo traduce in pagine, e il banco di montaggio resta valido per chi vuole rivedere tempi e animazioni prima di portarle in Canva.

## Lessico di brand (SEMPRE)

- **"Guadagniamo solo se guadagni tu"** — mai "guadagni solo se guadagni tu".
- **Mai "hotel-style"** → **"standard alberghiero"** (o "metodo/livello alberghiero").
- **Niente case study su singole strutture nominate** come prova nei contenuti di acquisizione clienti — usa processo, standard alberghiero, allineamento 15%, o dati di mercato generali.

Glossario esteso con esempi ed edge case → `.claude/reference/lessico-brand.md`.

## Asset di brand reali

Logo (4 varianti), foto tramonto Litorale, foto immobile reale — in `brand-assets/` (inventario e note d'uso in `brand-assets/README.md`). L'`art-director` li preferisce agli elementi tipografici quando pertinenti. Varianti trasparenti del logo non ancora disponibili (nessuno strumento di rimozione sfondo in questo ambiente).

## Regole non negoziabili

- **Mai inventare claim, numeri, risultati o testimonianze.** Non verificato → `[DATO DA VERIFICARE]`, mai scritto come fatto.
- **Il tono si calibra sempre su `riferimenti/`**, non su preferenze generiche di stile. Se vuoto/incompleto, chiedilo prima di scrivere copy definitivo.
- **Niente contenuto esce senza `compliance-checker`.** Anche un singolo post. Campagna completa → serve poi `revisore-marketing-design`.
- **Le grafiche si consegnano sempre in formato modificabile**, mai come immagini piatte non editabili.
- **Ogni campagna produce output tracciabile** in `campagne/<nome-campagna>/` — e va aggiunta a `campagne/INDEX.md`.
- Se mancano informazioni essenziali (target, offerta, claim verificati) **fermarsi e chiederle**, non presumerle.

## Note tecniche

- Gli agenti in `.claude/agents/` sono richiamabili singolarmente o in sequenza via `/nuova-campagna`.
- `framework-vendita` è il manuale del metodo di copywriting: va raffinato osservando cosa funziona per Hadrianus.
- Canva (`art-director`) è opzionale: se non collegato, l'agente produce comunque grafiche via canvas Claude Design (mai solo un brief testuale — vedi preferenza fissa 1).
