import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const grafiche = path.join(__dirname, '..', 'grafiche');
const src = path.join(__dirname, 'src');
const out = path.join(__dirname, 'out');
fs.mkdirSync(src, { recursive: true });
fs.mkdirSync(out, { recursive: true });

// mappa: sorgente editabile .dc.html -> nome file finale + dimensioni IG
const manifest = [
  ['Main.dc.html', 'storia-a', 1080, 1920],
  ['StoriaB.dc.html', 'storia-b', 1080, 1920],
  ['StoriaC.dc.html', 'storia-c', 1080, 1920],
  ['Carosello1.dc.html', 'carosello-1', 1080, 1350],
  ['Carosello2.dc.html', 'carosello-2', 1080, 1350],
  ['Carosello3.dc.html', 'carosello-3', 1080, 1350],
  ['Carosello4.dc.html', 'carosello-4', 1080, 1350],
  ['Carosello5.dc.html', 'carosello-5', 1080, 1350],
  ['PostProva.dc.html', 'post-prova', 1080, 1350],
  ['ReelCover.dc.html', 'reel-cover', 1080, 1920],
  ['FbPost1.dc.html', 'fb-1', 1080, 1920],
  ['FbPost2.dc.html', 'fb-2', 1080, 1080],
  ['FbPost3.dc.html', 'fb-3', 1080, 1080],
];

// Deriva un HTML standalone (renderizzabile) da un .dc.html editabile
function toStandalone(dc) {
  const helmet = (dc.match(/<helmet>([\s\S]*?)<\/helmet>/) || [,''])[1].trim();
  const frame = (dc.match(/<\/helmet>([\s\S]*?)<\/x-dc>/) || [,''])[1].trim();
  return `<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n${helmet}\n</head>\n<body>\n${frame}\n</body>\n</html>\n`;
}

const browser = await chromium.launch({ executablePath: process.env.PW_CHROME || undefined });
for (const [dcFile, name, w, h] of manifest) {
  const dc = fs.readFileSync(path.join(grafiche, dcFile), 'utf8');
  const html = toStandalone(dc);
  const srcFile = path.join(src, `${name}.html`);
  fs.writeFileSync(srcFile, html);

  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(srcFile).href, { waitUntil: 'load' });
  try { await page.evaluate(() => document.fonts.ready); } catch {}
  await page.waitForTimeout(400);
  const el = await page.$('.frame');
  await el.screenshot({ path: path.join(out, `${name}.png`) });
  console.log('rendered', `${name}.png`, `${w}x${h}`);
  await page.close();
}
await browser.close();
console.log('done');
