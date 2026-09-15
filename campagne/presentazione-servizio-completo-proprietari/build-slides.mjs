// Generatore delle slide editabili (.dc.html) del deck "servizio completo".
// Fonte di verità dei testi: copy.md. Qui vivono griglia, tipografia e componenti.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(__dirname, 'slide');

export const C = {
  cream: '#FAF6EC', paper: '#FFFDF8', ink: '#26241F', body: '#46423a', note: '#6f695c',
  stone: '#9A8A63', gold: '#C8A24B', goldText: '#b3892f', dark: '#3F3A33', darkDeep: '#2E2A25',
  onDark: '#E8E1D2', noteDark: '#b7ad9a', hair: 'rgba(38,36,31,0.13)', hairDark: 'rgba(232,225,210,0.18)',
  wash: '#F1E9D6',
};
const F = { d: "'Archivo', 'Arial Black', Arial, sans-serif", t: "'Manrope', 'Helvetica Neue', Arial, sans-serif" };

const HELMET = `<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
  <style>
    body { margin: 0; font-family: 'Manrope', 'Helvetica Neue', Arial, sans-serif; }
    a { color: #b3892f; } a:hover { color: #a8863b; }
  </style>
</helmet>`;

export function page(inner, { darkBg = false } = {}) {
  const bg = darkBg
    ? `radial-gradient(120% 90% at 22% 8%, #4a443a 0%, ${C.dark} 52%, ${C.darkDeep} 100%)`
    : C.cream;
  return `<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
${HELMET}
<div class="frame" style="width: 1280px; height: 720px; box-sizing: border-box; position: relative; overflow: hidden; background: ${bg}; color: ${darkBg ? C.onDark : C.ink};">
${inner}
</div>
</x-dc>
</body>
</html>
`;
}

// ---- componenti ------------------------------------------------------------

export function kicker(text, { dark = false } = {}) {
  return `  <div style="position: absolute; left: 88px; top: 58px; display: flex; align-items: center; gap: 13px;">
    <div style="width: 30px; height: 2px; background: ${C.gold};"></div>
    <span style="font-family: ${F.d}; font-weight: 700; font-size: 12.5px; letter-spacing: 3.2px; text-transform: uppercase; color: ${dark ? C.noteDark : C.stone};">${text}</span>
  </div>`;
}

export function mark({ dark = false } = {}) {
  return `  <span style="position: absolute; right: 88px; top: 56px; font-family: ${F.d}; font-weight: 800; font-size: 12.5px; letter-spacing: 4.4px; text-transform: uppercase; color: ${dark ? 'rgba(232,225,210,0.55)' : 'rgba(38,36,31,0.40)'};">Hadrianus</span>`;
}

export function foot(n, { dark = false } = {}) {
  return `  <div style="position: absolute; left: 88px; right: 88px; bottom: 44px; display: flex; align-items: center; justify-content: space-between;">
    <div style="width: 26px; height: 2px; background: ${dark ? 'rgba(200,162,75,0.75)' : 'rgba(200,162,75,0.85)'};"></div>
    <span style="font-family: ${F.d}; font-weight: 600; font-size: 11.5px; letter-spacing: 2.4px; color: ${dark ? 'rgba(232,225,210,0.45)' : 'rgba(38,36,31,0.34)'};">${String(n).padStart(2, '0')} / 16</span>
  </div>`;
}

export function watermark(num, { dark = false } = {}) {
  if (!num) return '';
  return `  <span style="position: absolute; left: 78px; bottom: 74px; font-family: ${F.d}; font-weight: 900; font-size: 168px; line-height: 0.78; letter-spacing: -6px; color: ${dark ? 'rgba(232,225,210,0.055)' : '#F0E7D3'};">${num}</span>`;
}

export function title(text, { size = 40, color = C.ink, width = 420 } = {}) {
  return `<h2 style="font-family: ${F.d}; font-weight: 900; font-size: ${size}px; line-height: 1.04; letter-spacing: -1px; margin: 0; color: ${color}; max-width: ${width}px; text-wrap: pretty;">${text}</h2>`;
}

export function promise(text, { dark = false, width = 380 } = {}) {
  return `<p style="font-size: 17.5px; line-height: 1.52; margin: 0; color: ${dark ? C.noteDark : C.body}; max-width: ${width}px;">${text}</p>`;
}

// voce di elenco: trattino oro + riga forte + riga secondaria
export function item({ head, sub }, { dark = false } = {}) {
  return `      <div style="display: flex; gap: 16px; align-items: flex-start;">
        <div style="width: 14px; height: 2px; background: ${C.gold}; margin-top: 11px; flex-shrink: 0;"></div>
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <span style="font-size: ${sub ? 17.5 : 19}px; font-weight: 700; line-height: 1.32; color: ${dark ? C.onDark : C.ink};">${head}</span>
          ${sub ? `<span style="font-size: 15.5px; line-height: 1.42; color: ${dark ? C.noteDark : C.note};">${sub}</span>` : ''}
        </div>
      </div>`;
}

export function rule(x, y, w, h, { dark = false } = {}) {
  return `  <div style="position: absolute; left: ${x}px; top: ${y}px; width: ${w}px; height: ${h}px; background: ${dark ? C.hairDark : C.hair};"></div>`;
}

// ---- layout A: sezione numerata (colonna sinistra + elenco a destra) -------

export function sectionSlide({ n, kickerText, num, titleHtml, promiseText, items, photo, note, dark = false }) {
  const left = [];
  left.push(`    <div style="position: absolute; left: 88px; top: 150px; width: 400px; display: flex; flex-direction: column; gap: 20px;">
      ${title(titleHtml, { color: dark ? '#FFFFFF' : C.ink, width: 400 })}
      ${promise(promiseText, { dark, width: 370 })}
    </div>`);
  if (photo) {
    left.push(`    <div style="position: absolute; left: 88px; top: ${photo.top || 392}px; width: 400px; display: flex; flex-direction: column; gap: 11px;">
      <img src="${photo.src}" alt="" style="width: 400px; height: ${photo.h || 208}px; object-fit: cover; display: block;">
      <span style="font-size: 12.5px; line-height: 1.4; color: ${dark ? 'rgba(232,225,210,0.55)' : 'rgba(38,36,31,0.45)'};">${photo.caption}</span>
    </div>`);
  } else {
    left.push(watermark(num, { dark }));
  }
  const list = items.map((it) => item(it, { dark })).join('\n');
  const noteBlock = note
    ? `\n  <div style="position: absolute; left: 600px; right: 88px; bottom: 96px; display: flex; gap: 14px; align-items: flex-start; border-top: 1px solid ${dark ? C.hairDark : C.hair}; padding-top: 16px;">
    <span style="font-family: ${F.d}; font-weight: 700; font-size: 11.5px; letter-spacing: 2.2px; text-transform: uppercase; color: ${C.goldText}; flex-shrink: 0; margin-top: 2px;">Nota</span>
    <span style="font-size: 14.5px; line-height: 1.45; color: ${dark ? C.noteDark : C.body};">${note}</span>
  </div>`
    : '';
  return page(`${kicker(kickerText, { dark })}
${mark({ dark })}
${rule(552, 148, 1, 440, { dark })}
${left.join('\n')}
  <div style="position: absolute; left: 600px; top: 148px; width: 592px; height: ${note ? 384 : 440}px; display: flex; flex-direction: column; justify-content: center; gap: ${items.length > 5 ? 18 : (items.some((i) => i.sub) ? 22 : 30)}px;">
${list}
  </div>${noteBlock}
${foot(n, { dark })}`, { darkBg: dark });
}

export default { C, F, page, kicker, mark, foot, watermark, title, promise, item, rule, sectionSlide };

// ---- layout B: tre passaggi affiancati -------------------------------------

export function threeUp({ n, kickerText, titleHtml, promiseText, cols, closing }) {
  const cells = cols.map((c) => `      <div style="flex: 1; display: flex; flex-direction: column; gap: 14px; border-top: 2px solid ${C.gold}; padding-top: 22px;">
        <span style="font-family: ${F.d}; font-weight: 900; font-size: 42px; line-height: 1; color: ${C.goldText};">${c.num}</span>
        <span style="font-family: ${F.d}; font-weight: 800; font-size: 19px; line-height: 1.2; letter-spacing: -0.2px; color: ${C.ink};">${c.label}</span>
        <span style="font-size: 15.5px; line-height: 1.5; color: ${C.note};">${c.line}</span>
      </div>`).join('\n');
  return page(`${kicker(kickerText)}
${mark()}
  <div style="position: absolute; left: 88px; top: 140px; right: 88px; display: flex; align-items: flex-end; justify-content: space-between; gap: 40px;">
    ${title(titleHtml, { width: 560 })}
    <p style="font-size: 17px; line-height: 1.55; margin: 0 0 6px 0; color: ${C.body}; max-width: 430px;">${promiseText}</p>
  </div>
  <div style="position: absolute; left: 88px; right: 88px; top: 350px; display: flex; gap: 44px;">
${cells}
  </div>
  <div style="position: absolute; left: 88px; right: 88px; bottom: 112px; border-top: 1px solid ${C.hair}; padding-top: 18px;">
    <span style="font-family: ${F.d}; font-weight: 800; font-size: 19px; line-height: 1.35; color: ${C.ink};">${closing}</span>
  </div>
${foot(n)}`);
}

// ---- layout C: il calendario (slide-perno, fondo scuro) --------------------

export function calendarSlide({ n, kickerText, titleHtml, occhiello, bands, closing }) {
  const rows = bands.map((b, i) => `    <div style="display: flex; gap: 34px; align-items: flex-start; padding: ${i === 0 ? '0' : '11px'} 0 11px 0; ${i === bands.length - 1 ? '' : `border-bottom: 1px solid ${C.hairDark};`}">
      <div style="width: 210px; flex-shrink: 0; display: flex; align-items: baseline; gap: 12px;">
        <div style="width: 12px; height: 2px; background: ${C.gold}; transform: translateY(-5px);"></div>
        <span style="font-family: ${F.d}; font-weight: 800; font-size: 14px; letter-spacing: 1.5px; text-transform: uppercase; color: ${C.gold}; line-height: 1.3;">${b.freq}</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 4px;">
        ${b.items.map((t) => `<span style="font-size: 15px; line-height: 1.4; color: ${C.onDark};">${t}</span>`).join('\n        ')}
      </div>
    </div>`).join('\n');
  return page(`${kicker(kickerText, { dark: true })}
${mark({ dark: true })}
  <div style="position: absolute; left: 88px; top: 124px; width: 1104px; display: flex; align-items: flex-end; justify-content: space-between; gap: 48px;">
    ${title(titleHtml, { color: '#FFFFFF', width: 580, size: 34 })}
    <p style="font-size: 16.5px; line-height: 1.5; margin: 0 0 4px 0; color: ${C.noteDark}; max-width: 420px;">${occhiello}</p>
  </div>
  <div style="position: absolute; left: 88px; right: 88px; top: 258px; display: flex; flex-direction: column;">
${rows}
  </div>
  <div style="position: absolute; left: 88px; bottom: 82px; display: flex; align-items: center; gap: 16px;">
    <div style="width: 26px; height: 2px; background: ${C.gold};"></div>
    <span style="font-family: ${F.d}; font-weight: 800; font-size: 19px; line-height: 1.3; color: #FFFFFF;">${closing}</span>
  </div>
${foot(n, { dark: true })}`, { darkBg: true });
}

// ---- layout D: elenco denso su due colonne --------------------------------

export function denseSlide({ n, kickerText, num, titleHtml, promiseText, items, closing }) {
  const half = Math.ceil(items.length / 2);
  const col = (arr) => `      <div style="flex: 1; display: flex; flex-direction: column; gap: 15px;">
${arr.map((t) => `        <div style="display: flex; gap: 14px; align-items: flex-start;">
          <div style="width: 12px; height: 2px; background: ${C.gold}; margin-top: 10px; flex-shrink: 0;"></div>
          <span style="font-size: 16.5px; line-height: 1.35; font-weight: 600; color: ${C.ink};">${t}</span>
        </div>`).join('\n')}
      </div>`;
  return page(`${kicker(kickerText)}
${mark()}
  <div style="position: absolute; left: 88px; top: 140px; right: 88px; display: flex; align-items: flex-end; justify-content: space-between; gap: 40px;">
    ${title(titleHtml, { width: 520 })}
    <p style="font-size: 17px; line-height: 1.55; margin: 0 0 6px 0; color: ${C.body}; max-width: 430px;">${promiseText}</p>
  </div>
${rule(88, 318, 1104, 1)}
  <div style="position: absolute; left: 88px; right: 88px; top: 356px; display: flex; gap: 64px;">
${col(items.slice(0, half))}
${col(items.slice(half))}
  </div>
  ${closing ? `<div style="position: absolute; left: 88px; right: 88px; bottom: 106px; border-top: 1px solid ${C.hair}; padding-top: 16px;">
    <span style="font-family: ${F.d}; font-weight: 800; font-size: 18px; line-height: 1.35; color: ${C.ink};">${closing}</span>
  </div>` : watermark(num)}
${foot(n)}`);
}

// ---- layout E: copertina ---------------------------------------------------

export function coverSlide({ kickerText, titleHtml, subtitle }) {
  return page(`  <img src="hadrianus-logo-900.webp" alt="Hadrianus" style="position: absolute; right: 40px; bottom: 44px; height: 556px; width: auto;">
  <div style="position: absolute; right: 0; top: 0; width: 560px; height: 720px; background: linear-gradient(90deg, ${C.cream} 0%, rgba(250,246,236,0.72) 26%, rgba(250,246,236,0) 55%);"></div>
  <div style="position: absolute; left: 44px; top: 44px; right: 44px; bottom: 44px; border: 1px solid rgba(200,162,75,0.40);"></div>
  <div style="position: absolute; left: 92px; top: 168px; width: 650px; display: flex; flex-direction: column; gap: 24px;">
    <div style="display: flex; align-items: center; gap: 14px;">
      <div style="width: 34px; height: 2px; background: ${C.gold};"></div>
      <span style="font-family: ${F.d}; font-weight: 700; font-size: 13px; letter-spacing: 3.4px; text-transform: uppercase; color: ${C.stone};">${kickerText}</span>
    </div>
    <h1 style="font-family: ${F.d}; font-weight: 900; font-size: 50px; line-height: 1.04; letter-spacing: -1.1px; margin: 0; color: ${C.ink}; text-wrap: pretty;">${titleHtml}</h1>
    <p style="font-size: 18px; line-height: 1.55; margin: 0; color: ${C.body}; max-width: 500px;">${subtitle}</p>
  </div>
  <div style="position: absolute; left: 92px; bottom: 86px; display: flex; align-items: center; gap: 22px;">
    <span style="font-family: ${F.d}; font-weight: 800; font-size: 17px; letter-spacing: 5px; text-transform: uppercase; color: ${C.ink};">Hadrianus</span>
    <div style="width: 1px; height: 18px; background: rgba(38,36,31,0.25);"></div>
    <span style="font-size: 13px; letter-spacing: 1.6px; text-transform: uppercase; color: ${C.note};">Multiservice · Roma · Ostia</span>
  </div>`);
}

// ---- layout F: l'immobile (tre dati + blocco di partenza) ------------------

export function factsSlide({ n, kickerText, titleHtml, facts, startLabel, startText, stacco }) {
  const cells = facts.map((f, i) => `      <div style="flex: 1; padding: 0 30px 0 ${i === 0 ? '0' : '30px'}; ${i === 0 ? '' : `border-left: 1px solid ${C.hair};`} display: flex; flex-direction: column; gap: 10px;">
        <span style="font-family: ${F.d}; font-weight: 700; font-size: 11.5px; letter-spacing: 2.4px; text-transform: uppercase; color: ${C.stone};">${f.label}</span>
        <span style="font-family: ${F.d}; font-weight: 800; font-size: 22px; line-height: 1.22; color: ${C.ink};">${f.value}</span>
      </div>`).join('\n');
  return page(`${kicker(kickerText)}
${mark()}
  <div style="position: absolute; left: 88px; top: 150px; width: 520px;">
    ${title(titleHtml, { width: 520 })}
  </div>
  <div style="position: absolute; left: 648px; top: 156px; width: 544px; display: flex; flex-direction: column; gap: 12px;">
    <span style="font-family: ${F.d}; font-weight: 700; font-size: 11.5px; letter-spacing: 2.4px; text-transform: uppercase; color: ${C.goldText};">${startLabel}</span>
    <p style="font-size: 17px; line-height: 1.55; margin: 0; color: ${C.body};">${startText}</p>
  </div>
${rule(88, 392, 1104, 1)}
  <div style="position: absolute; left: 88px; right: 88px; top: 438px; display: flex;">
${cells}
  </div>
  <div style="position: absolute; left: 88px; right: 88px; bottom: 92px; background: rgba(200,162,75,0.16); border-left: 3px solid ${C.gold}; padding: 20px 26px;">
    <span style="font-family: ${F.d}; font-weight: 800; font-size: 19px; line-height: 1.3; color: ${C.ink};">${stacco}</span>
  </div>
${foot(n)}`);
}

// ---- layout G: slide di snodo (affermazione centrale) ---------------------

export function statementSlide({ n, kickerText, statementHtml, lines, closing }) {
  const cells = lines.map((t) => `      <div style="flex: 1; display: flex; gap: 13px; align-items: flex-start;">
        <div style="width: 12px; height: 2px; background: ${C.gold}; margin-top: 10px; flex-shrink: 0;"></div>
        <span style="font-size: 15.5px; line-height: 1.45; color: ${C.body};">${t}</span>
      </div>`).join('\n');
  return page(`${kicker(kickerText)}
${mark()}
  <div style="position: absolute; left: 88px; right: 88px; top: 190px; display: flex; flex-direction: column; gap: 30px;">
    <h2 style="font-family: ${F.d}; font-weight: 900; font-size: 52px; line-height: 1.06; letter-spacing: -1.2px; margin: 0; color: ${C.ink}; max-width: 900px; text-wrap: pretty;">${statementHtml}</h2>
  </div>
${rule(88, 408, 1104, 1)}
  <div style="position: absolute; left: 88px; right: 88px; top: 446px; display: flex; gap: 46px;">
${cells}
  </div>
  <div style="position: absolute; left: 88px; right: 88px; bottom: 96px; background: ${C.paper}; border: 1px solid ${C.hair}; border-left: 3px solid ${C.gold}; padding: 20px 26px;">
    <span style="font-family: ${F.d}; font-weight: 800; font-size: 19px; line-height: 1.35; color: ${C.ink};">${closing}</span>
  </div>
${foot(n)}`);
}

// ---- layout H: condizioni economiche (fondo scuro, 15% protagonista) ------

export function conditionsSlide({ n, kickerText, titleHtml, bigNumber, bigLine, conditions, outside, formula }) {
  const cells = conditions.map((t) => `      <div style="display: flex; gap: 13px; align-items: flex-start;">
        <div style="width: 12px; height: 2px; background: ${C.gold}; margin-top: 10px; flex-shrink: 0;"></div>
        <span style="font-size: 16.5px; line-height: 1.4; color: ${C.onDark};">${t}</span>
      </div>`).join('\n');
  return page(`${kicker(kickerText, { dark: true })}
${mark({ dark: true })}
  <div style="position: absolute; left: 88px; top: 160px; width: 470px; display: flex; flex-direction: column; gap: 18px;">
    ${title(titleHtml, { color: '#FFFFFF', width: 440, size: 38 })}
    <div style="display: flex; flex-direction: column; gap: 14px; margin-top: 18px;">
      <span style="font-family: ${F.d}; font-weight: 900; font-size: 158px; line-height: 0.78; letter-spacing: -7px; color: ${C.gold};">${bigNumber}</span>
      <span style="font-size: 17px; line-height: 1.45; color: ${C.noteDark}; max-width: 420px;">${bigLine}</span>
    </div>
  </div>
${rule(600, 148, 1, 396, { dark: true })}
  <div style="position: absolute; left: 648px; top: 150px; width: 544px; display: flex; flex-direction: column; gap: 17px;">
${cells}
  </div>
  <div style="position: absolute; left: 648px; top: 418px; width: 544px; border-top: 1px solid ${C.hairDark}; padding-top: 18px; display: flex; gap: 14px; align-items: flex-start;">
    <span style="font-family: ${F.d}; font-weight: 700; font-size: 11.5px; letter-spacing: 2.2px; text-transform: uppercase; color: ${C.gold}; flex-shrink: 0; margin-top: 3px;">Fuori</span>
    <span style="font-size: 15px; line-height: 1.45; color: ${C.noteDark};">${outside}</span>
  </div>
  <div style="position: absolute; left: 88px; right: 88px; bottom: 96px; border-top: 1px solid ${C.hairDark}; padding-top: 22px;">
    <span style="font-family: ${F.d}; font-weight: 900; font-size: 30px; line-height: 1.2; letter-spacing: -0.6px; color: #FFFFFF;">${formula}</span>
  </div>
${foot(n, { dark: true })}`, { darkBg: true });
}

// ---- layout I: il prossimo passo (tre passi + CTA) ------------------------

export function stepsSlide({ n, kickerText, titleHtml, steps, numberLine, cta }) {
  const cells = steps.map((s, i) => `      <div style="flex: 1; display: flex; flex-direction: column; gap: 12px; border-top: 2px solid ${C.gold}; padding-top: 20px;">
        <span style="font-family: ${F.d}; font-weight: 900; font-size: 34px; line-height: 1; color: ${C.goldText};">0${i + 1}</span>
        <span style="font-size: 16.5px; line-height: 1.45; font-weight: 600; color: ${C.ink};">${s}</span>
      </div>`).join('\n');
  return page(`${kicker(kickerText)}
${mark()}
  <div style="position: absolute; left: 88px; top: 146px; width: 760px;">
    ${title(titleHtml, { width: 760, size: 44 })}
  </div>
  <div style="position: absolute; left: 88px; right: 88px; top: 300px; display: flex; gap: 44px;">
${cells}
  </div>
  <div style="position: absolute; left: 88px; right: 88px; top: 486px; border-top: 1px solid ${C.hair}; padding-top: 18px;">
    <span style="font-size: 16px; line-height: 1.5; color: ${C.body};">${numberLine}</span>
  </div>
  <div style="position: absolute; left: 88px; bottom: 92px; display: flex; align-items: center; gap: 0;">
    <div style="background: ${C.gold}; color: ${C.darkDeep}; padding: 18px 34px; font-family: ${F.d}; font-weight: 800; font-size: 20px; letter-spacing: 0.2px;">${cta}</div>
  </div>
${foot(n)}`);
}

// ---- layout L: chiusura di marca ------------------------------------------

export function closingSlide({ line, subline, contact }) {
  return page(`  <img src="tramonto.webp" alt="" style="position: absolute; inset: 0; width: 1280px; height: 720px; object-fit: cover; object-position: 50% 42%;">
  <div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(34,30,25,0.93) 0%, rgba(34,30,25,0.74) 44%, rgba(34,30,25,0.20) 100%);"></div>
  <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(34,30,25,0.55) 0%, rgba(34,30,25,0.10) 34%, rgba(34,30,25,0.62) 100%);"></div>
  <div style="position: absolute; left: 88px; top: 258px; width: 640px; display: flex; flex-direction: column; gap: 22px;">
    <div style="width: 34px; height: 2px; background: ${C.gold};"></div>
    <h2 style="font-family: ${F.d}; font-weight: 900; font-size: 50px; line-height: 1.05; letter-spacing: -1.2px; margin: 0; color: #FFFFFF; max-width: 600px; text-wrap: pretty;">${line}</h2>
    <p style="font-size: 17.5px; line-height: 1.5; margin: 0; color: rgba(255,255,255,0.80); max-width: 520px;">${subline}</p>
  </div>
  <div style="position: absolute; left: 88px; bottom: 88px; display: flex; align-items: center; gap: 22px;">
    <span style="font-family: ${F.d}; font-weight: 800; font-size: 17px; letter-spacing: 5px; text-transform: uppercase; color: #FFFFFF;">Hadrianus</span>
    <div style="width: 1px; height: 18px; background: rgba(255,255,255,0.40);"></div>
    <span style="font-size: 13px; letter-spacing: 1.6px; text-transform: uppercase; color: rgba(255,255,255,0.72);">${contact}</span>
  </div>`);
}
