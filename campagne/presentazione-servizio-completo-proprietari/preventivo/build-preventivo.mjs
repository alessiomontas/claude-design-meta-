// Preventivo A4 — messa in regola documentale. Due artboard editabili.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const C = {
  cream: '#FAF6EC', paper: '#FFFDF8', ink: '#26241F', body: '#46423a', note: '#6f695c',
  stone: '#9A8A63', gold: '#C8A24B', goldText: '#b3892f', dark: '#3F3A33',
  hair: 'rgba(38,36,31,0.13)', hairStrong: 'rgba(38,36,31,0.22)',
};
const F = { d: "'Archivo', 'Arial Black', Arial, sans-serif", t: "'Manrope', 'Helvetica Neue', Arial, sans-serif" };
const W = 794, H = 1123;

const HELMET = `<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
  <style>
    body { margin: 0; font-family: 'Manrope', 'Helvetica Neue', Arial, sans-serif; }
    a { color: #b3892f; } a:hover { color: #a8863b; }
  </style>
</helmet>`;

const page = (inner) => `<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
${HELMET}
<div class="frame" style="width: ${W}px; height: ${H}px; box-sizing: border-box; position: relative; overflow: hidden; background: ${C.cream}; color: ${C.ink}; font-family: ${F.t};">
${inner}
</div>
</x-dc>
</body>
</html>
`;

// intestazione comune
const header = (right) => `  <div style="position: absolute; left: 56px; right: 56px; top: 50px; display: flex; align-items: flex-start; justify-content: space-between;">
    <div style="display: flex; flex-direction: column; gap: 7px;">
      <span style="font-family: ${F.d}; font-weight: 800; font-size: 16px; letter-spacing: 5.4px; text-transform: uppercase; color: ${C.ink};">Hadrianus</span>
      <span style="font-size: 10.5px; letter-spacing: 1.7px; text-transform: uppercase; color: ${C.note};">Multiservice · Property management · Roma · Ostia</span>
    </div>
    ${right}
  </div>
  <div style="position: absolute; left: 56px; right: 56px; top: 116px; height: 2px; background: ${C.gold};"></div>`;

const foot = (n, txt) => `  <div style="position: absolute; left: 56px; right: 56px; bottom: 40px; padding-top: 12px; border-top: 1px solid ${C.hair}; display: flex; align-items: center; justify-content: space-between;">
    <span style="font-size: 10px; letter-spacing: 1.2px; color: ${C.note};">${txt}</span>
    <span style="font-family: ${F.d}; font-weight: 600; font-size: 10px; letter-spacing: 2px; color: rgba(38,36,31,0.38);">${n} / 2</span>
  </div>`;

const label = (t) => `<span style="font-family: ${F.d}; font-weight: 700; font-size: 10.5px; letter-spacing: 2.4px; text-transform: uppercase; color: ${C.stone};">${t}</span>`;

// ————————————————————————————————————————————————— pagina 1
const voci = [
  ['Verifica preliminare dell’immobile', 'Controllo di visura catastale, planimetria e dati dell’unità, per accertare che l’immobile possa essere destinato a locazione turistica.'],
  ['CIR — Codice Identificativo Regionale', 'Richiesta e ottenimento del codice della Regione Lazio, intestato alla proprietà.'],
  ['CIN — Codice Identificativo Nazionale', 'Richiesta e ottenimento del codice della Banca Dati Strutture Ricettive: senza, l’immobile non può essere pubblicato su nessun portale.'],
  ['Pratica comunale di avvio attività', 'Predisposizione e presentazione al SUAR di Roma Capitale, nella forma prevista per la tipologia scelta (SCIA o CIA).'],
  ['Alloggiati Web — Polizia di Stato', 'Apertura della posizione e attivazione delle credenziali per la comunicazione degli ospiti.'],
  ['ROSS 1000 — Regione Lazio', 'Apertura della posizione per la rilevazione dei flussi turistici.'],
  ['Contributo di soggiorno — Roma Capitale', 'Registrazione della struttura presso il Comune, per gli adempimenti successivi.'],
  ['Consegna del fascicolo', 'Codici, credenziali, ricevute e copia di ogni pratica, raccolti in un unico fascicolo intestato a lei.'],
];

const listaVoci = voci.map(([h, s], i) => `      <div style="display: flex; gap: 16px; align-items: flex-start; padding: 9.5px 0; ${i === voci.length - 1 ? '' : `border-bottom: 1px solid ${C.hair};`}">
        <span style="font-family: ${F.d}; font-weight: 900; font-size: 14px; line-height: 1.35; color: ${C.goldText}; width: 26px; flex-shrink: 0;">${String(i + 1).padStart(2, '0')}</span>
        <div style="display: flex; flex-direction: column; gap: 3px;">
          <span style="font-size: 14px; font-weight: 700; line-height: 1.3; color: ${C.ink};">${h}</span>
          <span style="font-size: 12px; line-height: 1.42; color: ${C.note};">${s}</span>
        </div>
      </div>`).join('\n');

const p1 = page(`${header(`    <img src="hadrianus-tempio-220.webp" alt="Hadrianus" style="height: 74px; width: auto; margin-top: -6px;">`)}

  <div style="position: absolute; left: 56px; top: 156px; width: 420px; display: flex; flex-direction: column; gap: 10px;">
    ${label('Preventivo')}
    <h1 style="font-family: ${F.d}; font-weight: 900; font-size: 33px; line-height: 1.06; letter-spacing: -0.8px; margin: 0; color: ${C.ink};">Messa in regola<br>documentale.</h1>
  </div>
  <div style="position: absolute; right: 56px; top: 160px; width: 230px; display: flex; flex-direction: column; gap: 9px; text-align: right;">
    <span style="font-size: 12px; line-height: 1.5; color: ${C.body};">Preventivo n. <b>[numero]</b></span>
    <span style="font-size: 12px; line-height: 1.5; color: ${C.body};">Data <b>[gg/mm/aaaa]</b></span>
    <span style="font-size: 12px; line-height: 1.5; color: ${C.body};">Valido 30 giorni dall’emissione</span>
  </div>

  <div style="position: absolute; left: 56px; right: 56px; top: 276px; display: flex; gap: 34px; padding: 16px 0; border-top: 1px solid ${C.hair}; border-bottom: 1px solid ${C.hair};">
    <div style="flex: 1; display: flex; flex-direction: column; gap: 5px;">
      ${label('Intestato a')}
      <span style="font-size: 13.5px; font-weight: 700; line-height: 1.35; color: ${C.ink};">[Nome e cognome della proprietaria]</span>
    </div>
    <div style="flex: 1; display: flex; flex-direction: column; gap: 5px;">
      ${label('Immobile')}
      <span style="font-size: 13.5px; font-weight: 700; line-height: 1.35; color: ${C.ink};">Bilocale, Ostia Lido Centro</span>
    </div>
  </div>

  <p style="position: absolute; left: 56px; top: 352px; width: 682px; margin: 0; font-size: 13.5px; line-height: 1.55; color: ${C.body};">Oggetto del preventivo è <b>la sola messa in regola documentale</b> dell’immobile: al termine, l’appartamento è in regola per essere affittato e pubblicato.</p>

  <div style="position: absolute; left: 56px; top: 432px; width: 682px; display: flex; flex-direction: column; gap: 2px;">
    ${label('Cosa comprende')}
    <div style="display: flex; flex-direction: column; margin-top: 6px;">
${listaVoci}
    </div>
  </div>

  <div style="position: absolute; left: 56px; right: 56px; bottom: 88px; background: ${C.gold}; color: #2E2A25; padding: 20px 26px; display: flex; align-items: center; justify-content: space-between; gap: 20px;">
    <div style="display: flex; flex-direction: column; gap: 4px;">
      <span style="font-family: ${F.d}; font-weight: 800; font-size: 11px; letter-spacing: 2.4px; text-transform: uppercase;">Totale</span>
      <span style="font-size: 12px; line-height: 1.35;">Importo non soggetto a IVA · costi vivi delle pratiche esclusi</span>
    </div>
    <span style="font-family: ${F.d}; font-weight: 900; font-size: 42px; line-height: 1; letter-spacing: -1.4px;">500,00 €</span>
  </div>
${foot(1, 'Preventivo — messa in regola documentale · Bilocale, Ostia Lido Centro')}`);

// ————————————————————————————————————————————————— pagina 2
const esclusi = [
  'Servizio fotografico, testi dell’annuncio, pubblicazione sui portali e landing page.',
  'Gestione dell’immobile e adempimenti ricorrenti: comunicazioni a ogni arrivo, flussi statistici, contributo di soggiorno.',
  'Dotazioni di sicurezza richieste per i codici (rilevatori ed estintore): le indichiamo, la fornitura resta alla proprietà.',
  'Interventi tecnici o di conformità sull’immobile, se dalla verifica preliminare dovessero emergere.',
  'Adempimenti fiscali e dichiarativi, che restano al suo commercialista.',
];

const serve = [
  'Visura catastale e planimetria dell’immobile.',
  'Documento d’identità e codice fiscale della proprietaria.',
  'Dati dell’unità: metratura, vani, posti letto, servizi.',
  'Delega per la presentazione delle pratiche a suo nome.',
];

const riga = (t) => `      <div style="display: flex; gap: 12px; align-items: flex-start;">
        <div style="width: 11px; height: 2px; background: ${C.gold}; margin-top: 8px; flex-shrink: 0;"></div>
        <span style="font-size: 12.5px; line-height: 1.45; color: ${C.body};">${t}</span>
      </div>`;

const condizioni = [
  ['Costi delle pratiche', 'Diritti di segreteria, imposte di bollo ed eventuali oneri comunali sono a carico della proprietà. Vengono quantificati e comunicati <b>prima</b> di procedere: nessuna spesa viene sostenuta senza il suo consenso.'],
  ['Pagamento', 'Alla conferma del preventivo si sostengono i soli costi delle pratiche. I <b>500,00 €</b> si pagano a lavoro concluso, alla consegna del fascicolo.'],
  ['Tempi', 'L’avvio è immediato alla ricezione dei documenti. I tempi di rilascio dipendono dagli enti competenti e non sono nella nostra disponibilità: la teniamo aggiornata a ogni passaggio.'],
  ['Esito delle pratiche', 'L’esito dipende dai requisiti dell’immobile. Se dalla verifica preliminare emerge un impedimento, glielo diciamo prima di procedere e il preventivo si ferma, senza alcun costo di onorario.'],
];

const p2 = page(`${header(`    <div style="text-align: right; display: flex; flex-direction: column; gap: 6px;">
      <span style="font-size: 11px; letter-spacing: 1.6px; text-transform: uppercase; color: ${C.note};">Preventivo n. [numero]</span>
      <span style="font-size: 11px; letter-spacing: 1.6px; text-transform: uppercase; color: ${C.note};">Pagina 2 di 2</span>
    </div>`)}

  <div style="position: absolute; left: 56px; top: 156px; width: 682px; display: flex; flex-direction: column; gap: 12px;">
    ${label('Cosa non comprende')}
    <div style="display: flex; flex-direction: column; gap: 9px;">
${esclusi.map(riga).join('\n')}
    </div>
  </div>

  <div style="position: absolute; left: 56px; top: 358px; width: 682px; display: flex; flex-direction: column; gap: 12px;">
    ${label('Condizioni')}
    <div style="display: flex; flex-direction: column;">
${condizioni.map(([h, t], i) => `      <div style="display: flex; gap: 22px; align-items: flex-start; padding: 13px 0; ${i === condizioni.length - 1 ? '' : `border-bottom: 1px solid ${C.hair};`}">
        <span style="width: 152px; flex-shrink: 0; font-family: ${F.d}; font-weight: 800; font-size: 12.5px; line-height: 1.35; color: ${C.ink};">${h}</span>
        <span style="font-size: 12.5px; line-height: 1.45; color: ${C.body};">${t}</span>
      </div>`).join('\n')}
    </div>
  </div>

  <div style="position: absolute; left: 56px; top: 712px; width: 682px; display: flex; flex-direction: column; gap: 12px;">
    ${label('Cosa ci serve da lei')}
    <div style="display: flex; flex-direction: column; gap: 9px;">
${serve.map(riga).join('\n')}
    </div>
  </div>

  <div style="position: absolute; left: 56px; right: 56px; bottom: 96px; border: 1px solid ${C.hairStrong}; padding: 22px 26px; display: flex; flex-direction: column; gap: 20px; background: ${C.paper};">
    <span style="font-family: ${F.d}; font-weight: 800; font-size: 13px; line-height: 1.35; color: ${C.ink};">Per accettazione del preventivo</span>
    <div style="display: flex; gap: 40px;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 26px;">
        <div style="height: 1px; background: ${C.hairStrong};"></div>
        <span style="font-size: 10.5px; letter-spacing: 1.6px; text-transform: uppercase; color: ${C.note}; margin-top: -18px;">Luogo e data</span>
      </div>
      <div style="flex: 1; display: flex; flex-direction: column; gap: 26px;">
        <div style="height: 1px; background: ${C.hairStrong};"></div>
        <span style="font-size: 10.5px; letter-spacing: 1.6px; text-transform: uppercase; color: ${C.note}; margin-top: -18px;">Firma della proprietaria</span>
      </div>
    </div>
  </div>
${foot(2, 'Hadrianus Multiservice · hadrianusmultiservice.it')}`);

fs.writeFileSync(path.join(__dirname, 'Main.dc.html'), p1);
fs.writeFileSync(path.join(__dirname, 'Pagina2.dc.html'), p2);
fs.writeFileSync(path.join(__dirname, 'canvas.json'), JSON.stringify({
  artboards: [
    { file: 'Main.dc.html', title: 'Preventivo · pagina 1', x: 0, y: 0, w: W, h: H, print: 'fixed' },
    { file: 'Pagina2.dc.html', title: 'Preventivo · pagina 2', x: W + 120, y: 0, w: W, h: H, print: 'fixed' },
  ],
  annotations: [{ id: 'nota-preventivo', x: 0, y: -190, w: 900,
    text: 'Preventivo Hadrianus — sola messa in regola documentale del bilocale di Ostia Lido Centro.\nDue pagine A4 (794×1123 px = 210×297 mm a 96 px/pollice).\nDa compilare prima dell’invio: numero del preventivo, data, nome della proprietaria.\nExport PDF dalla barra in alto = due pagine A4.' }],
  launch: { view: 'canvas' },
}, null, 2));
console.log('preventivo: 2 artboard + canvas.json');
