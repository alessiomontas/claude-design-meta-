// Deck "servizio completo" — testi definitivi da copy.md, composizione da build-slides.mjs.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as K from './build-slides.mjs';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(__dirname, 'slide');
const w = (name, html) => { fs.writeFileSync(path.join(OUT, name + '.dc.html'), html); };
const sez = (i) => `Il servizio · ${String(i).padStart(2, '0')} di 07`;

// 01 · copertina ————————————————————————————————————————————————
w('Main', K.coverSlide({
  kickerText: 'Proposta di gestione · Ostia Lido Centro',
  titleHtml: 'Da appartamento<br>a struttura.<br><span style="color: #b3892f;">Il lavoro lo facciamo noi.</span>',
  subtitle: 'Il suo bilocale a Lido Centro oggi è fermo. Qui c’è il lavoro che serve per farlo esistere per legge, come prodotto e sul mercato.',
}));

// 02 · il punto di partenza ——————————————————————————————————————
w('Immobile', K.factsSlide({
  n: 2, kickerText: 'Il punto di partenza',
  titleHtml: 'L’immobile<br>che abbiamo visto.',
  facts: [
    { label: 'Immobile', value: 'Bilocale di circa<br>50-60 mq, Lido Centro' },
    { label: 'Comune', value: 'Municipio X<br>di Roma Capitale' },
    { label: 'Vocazione', value: 'Taglio e posizione<br>da casa vacanza' },
  ],
  startLabel: 'Da dove si parte oggi',
  startText: 'Oggi mancano i due codici identificativi, la pratica comunale e i portali. Non è un errore: è semplicemente un’attività che non è mai stata aperta.',
  stacco: 'Il sopralluogo lo abbiamo già fatto. Questa presentazione parte dal punto uno.',
}));

// 03 · il percorso ———————————————————————————————————————————————
w('Percorso', K.threeUp({
  n: 3, kickerText: 'Il percorso',
  titleHtml: 'Da appartamento<br>a struttura.',
  promiseText: 'Un bilocale che si presta non è ancora una struttura che produce. In mezzo ci sono tre passaggi, e vanno fatti in quest’ordine.',
  cols: [
    { num: '01', label: 'Esistere per legge', line: 'Codici identificativi e pratica comunale: senza, l’immobile non si pubblica.' },
    { num: '02', label: 'Esistere come prodotto', line: 'Restyling, identità, foto e descrizioni: la casa diventa una proposta.' },
    { num: '03', label: 'Esistere sul mercato', line: 'Portali, sito, canali Google: la struttura si trova e si prenota.' },
  ],
  closing: 'Tre passaggi. Nessuno dei tre si può saltare, e nessuno dei tre si chiude una volta per sempre.',
}));

// 04 · slide-perno ———————————————————————————————————————————————
w('Calendario', K.calendarSlide({
  n: 4, kickerText: 'Il quadro reale',
  titleHtml: 'Non è una pratica.<br>È un calendario.',
  occhiello: 'Le pratiche si aprono una volta. Quello che viene dopo non si ferma più.',
  bands: [
    { freq: 'A ogni arrivo', items: ['Identificazione dell’ospite con documento.', 'Comunicazione alla Polizia di Stato entro 24 ore.'] },
    { freq: 'A ogni cambio ospite', items: ['Pulizia in standard alberghiero e biancheria.', 'Controllo dell’immobile stanza per stanza.'] },
    { freq: 'Ogni mese', items: ['Pagamento alla proprietà, il 10 del mese.', 'Revisione di tariffe e calendario.'] },
    { freq: 'Ogni trimestre', items: ['Comunicazione del contributo di soggiorno.', 'Versamento entro il 16 del mese successivo.'] },
    { freq: 'Ogni anno', items: ['Verifica di codici, annunci e dotazioni.', 'Dati dei soggiorni pronti per il commercialista.'] },
  ],
  closing: 'Questo calendario non si chiude. Gira finché la casa lavora.',
}));

// 05 · 01 messa in regola ————————————————————————————————————————
w('Regola', K.sectionSlide({
  n: 5, kickerText: sez(1), num: '01',
  titleHtml: 'Messa<br>in regola.',
  promiseText: 'Prima di pubblicare, l’immobile deve esistere per legge. Questa parte la seguiamo noi.',
  items: [
    { head: 'CIN — Codice Nazionale', sub: 'Senza CIN l’immobile non può essere pubblicato su nessun portale.' },
    { head: 'CIR — Codice Regionale Lazio', sub: 'Il codice che la Regione Lazio assegna alla struttura.' },
    { head: 'Pratica comunale di avvio attività', sub: 'Al SUAR di Roma Capitale, SCIA o CIA secondo la tipologia scelta.' },
    { head: 'Alloggiati Web — Polizia di Stato', sub: 'Apriamo la posizione: ogni ospite va comunicato entro 24 ore.' },
    { head: 'ROSS 1000 — flussi turistici', sub: 'Il canale con cui la Regione registra arrivi e presenze.' },
    { head: 'Dotazioni di sicurezza', sub: 'Rilevatori ed estintore: sono condizione per il CIN.' },
  ],
}));

// 06 · snodo —————————————————————————————————————————————————————
w('Responsabilita', K.statementSlide({
  n: 6, kickerText: 'La titolarità',
  statementHtml: 'Il nome sulle carte<br>resta il suo.',
  lines: [
    'I codici e la pratica sono intestati a lei, che è la proprietaria dell’immobile.',
    'Un gestore può operare su delega. La titolarità, però, non si delega.',
    'Chi fa il lavoro può cambiare. Chi risponde degli adempimenti no.',
  ],
  closing: 'Per questo non la sostituiamo: l’affianchiamo. La responsabilità resta sua, il lavoro diventa nostro.',
}));

// 07 · 02 la casa pronta —————————————————————————————————————————
w('Casa', K.sectionSlide({
  n: 7, kickerText: sez(2), num: '02',
  titleHtml: 'La casa<br>pronta.',
  promiseText: 'Un ospite prenota quello che vede. Prima delle foto, prepariamo la casa.',
  items: [
    { head: 'Piccolo restyling degli ambienti e oggettistica.' },
    { head: 'Pulizia a fondo prima del primo ospite.' },
    { head: 'Biancheria, consumabili e dotazione di base.' },
    { head: 'Pulizie in standard alberghiero a ogni cambio.' },
    { head: 'Manutenzioni seguite senza passare da lei.' },
  ],
  photo: { src: 'cucina.webp', pos: '58% 50%', caption: 'Un immobile che gestiamo oggi. Non è il suo: il suo lo prepariamo così.' },
}));

// 08 · 03 accessi ————————————————————————————————————————————————
w('Accessi', K.sectionSlide({
  n: 8, kickerText: sez(3), num: '03',
  titleHtml: 'Accessi<br>e check-in.',
  promiseText: 'L’ospite arriva a qualsiasi ora. Entra solo dopo essere stato identificato.',
  items: [
    { head: 'Identificazione dell’ospite con documento valido.' },
    { head: 'Spioncino digitale installato alla porta.' },
    { head: 'Apertura automatica del portone dal citofono.' },
    { head: 'Assistenza agli ospiti, H24, per tutto il soggiorno.' },
  ],
  noteStyle: 'band', noteLabel: 'Perché conta',
  note: 'Questi strumenti intervengono dopo il riconoscimento, non lo sostituiscono. Il check-in resta presidiato.',
}));

// 09 · 04 identità ———————————————————————————————————————————————
w('Identita', K.sectionSlide({
  n: 9, kickerText: sez(4), num: '04',
  titleHtml: 'Identità<br>dell’immobile.',
  promiseText: 'La sua casa non entra sui portali come un annuncio. Entra come una struttura con un nome.',
  items: [
    { head: 'Nome e identità dedicati all’appartamento.' },
    { head: 'Servizio fotografico a casa già pronta.' },
    { head: 'Descrizione di ogni ambiente e di ogni servizio.' },
    { head: 'Regole della casa e informazioni pratiche scritte.' },
  ],
  photo: { src: 'salotto.webp', pos: '50% 46%', caption: 'Un altro immobile che gestiamo, non il suo. Stessa luce, stessa preparazione.' },
}));

// 10 · 05 dove si vende ——————————————————————————————————————————
w('Canali', K.sectionSlide({
  n: 10, kickerText: sez(5), num: '05',
  titleHtml: 'Dove<br>si vende.',
  promiseText: 'Pubblicare su un portale non basta. La struttura deve trovarsi ovunque la cerchino.',
  items: [
    { head: 'Annunci sui principali portali di prenotazione.' },
    { head: 'Scheda Google della struttura, con mappa e recensioni.' },
    { head: 'Landing page dedicata all’appartamento.' },
    { head: 'Calendario e tariffe aggiornati su ogni canale.' },
  ],
  noteStyle: 'band', noteLabel: 'Prenotazioni dirette',
  note: 'Il sito Hadrianus raccoglie prenotazioni dirette: soggiorni che non passano da nessun portale.',
}));

// 11 · 06 gestione quotidiana ————————————————————————————————————
w('Gestione', K.denseSlide({
  n: 11, kickerText: sez(6), num: '06',
  titleHtml: 'Gestione<br>quotidiana.',
  promiseText: 'Da qui in poi il lavoro non si vede più, perché non arriva a lei. Ma c’è, ogni giorno.',
  items: [
    'Prenotazioni gestite ogni giorno.',
    'Tariffe aggiornate con pricing dinamico.',
    'Messaggi e assistenza ospiti H24.',
    'Check-in presidiato a ogni arrivo.',
    'Comunicazioni alla Polizia di Stato.',
    'Comunicazione dei flussi alla Regione.',
    'Contributo di soggiorno, ogni trimestre.',
    'Controllo stanza per stanza in uscita.',
  ],
}));

// 12 · 07 strategia ——————————————————————————————————————————————
w('Strategia', K.sectionSlide({
  n: 12, kickerText: sez(7), num: '07',
  titleHtml: 'Strategia<br>e revisione.',
  promiseText: 'La prima tariffa non è quella giusta per sempre. Si corregge guardando i dati.',
  items: [
    { head: 'Revisione periodica di tariffe e calendario.' },
    { head: 'Lettura delle recensioni e correzioni sul campo.' },
    { head: 'Posizionamento rivisto stagione per stagione.' },
  ],
  note: 'Non le promettiamo una crescita. Le promettiamo che i numeri li guardiamo, e che quando serve cambiamo.',
}));

// 13 · cosa resta alla proprietà —————————————————————————————————
w('Proprieta', K.sectionSlide({
  n: 13, kickerText: 'Il suo ruolo', num: '',
  titleHtml: 'Cosa resta<br>alla proprietà.',
  promiseText: 'Affidare la gestione non vuol dire perdere il controllo della casa: le decisioni che contano restano dove devono stare.',
  items: [
    { head: 'La titolarità della struttura, intestata a lei.' },
    { head: 'La scelta della tipologia con cui si parte.' },
    { head: 'La casa resta sua: nessun inquilino fisso.' },
    { head: 'Il pagamento del maturato, il 10 di ogni mese.' },
  ],
  note: 'Non le chiediamo di imparare niente. Le chiediamo solo le decisioni che spettano a lei.',
}));

// 14 · perimetro economico ———————————————————————————————————————
w('Condizioni', K.conditionsSlide({
  n: 14, kickerText: 'Il perimetro economico',
  titleHtml: 'Un numero solo.',
  bigNumber: '15%',
  bigLine: 'Sulle prenotazioni che generiamo. Solo su quelle.',
  conditions: [
    'Nessun costo fisso.',
    'Nessun deposito cauzionale.',
    'Pagamento il 10 di ogni mese.',
    'Sopralluogo già fatto, a costo zero.',
  ],
  outside: 'Fuori dal 15% restano i dispositivi di accesso — spioncino digitale e apertura del portone — fatturati a parte. Gli eventuali costi vivi delle pratiche glieli indichiamo prima di sostenerli.',
  formula: '«Guadagniamo solo se guadagni tu.»',
}));

// 15 · il prossimo passo —————————————————————————————————————————
w('Passo', K.stepsSlide({
  n: 15, kickerText: 'Come si parte',
  titleHtml: 'Il prossimo passo.',
  steps: [
    'Si firma il contratto di gestione.',
    'Apriamo codici, pratica e portali.',
    'Prepariamo la casa e la mettiamo sul mercato.',
  ],
  numberLine: 'La stima sul suo immobile gliela diamo quando avremo visura e planimetria. Non a occhio, e non prima di aver visto le carte.',
  cta: 'Firmiamo il contratto di gestione',
}));

// 16 · chiusura ——————————————————————————————————————————————————
w('Chiusura', K.closingSlide({
  line: 'Da appartamento<br>a struttura.',
  subline: 'Il suo bilocale a Lido Centro, e il lavoro che serve per farlo rendere.',
  contact: '351 730 5472 · info@hadrianusmultiservice.it',
}));

console.log('16 slide scritte in slide/');
