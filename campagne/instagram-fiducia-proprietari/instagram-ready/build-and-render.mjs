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

const manifest = [
  ['Main.dc.html', 'storia-1', 1080, 1920],
  ['Storia2.dc.html', 'storia-2', 1080, 1920],
  ['Storia3.dc.html', 'storia-3', 1080, 1920],
  ['CarA1.dc.html', 'carosello-A-1', 1080, 1350],
  ['CarA2.dc.html', 'carosello-A-2', 1080, 1350],
  ['CarA3.dc.html', 'carosello-A-3', 1080, 1350],
  ['CarA4.dc.html', 'carosello-A-4', 1080, 1350],
  ['CarA5.dc.html', 'carosello-A-5', 1080, 1350],
  ['CarB1.dc.html', 'carosello-B-1', 1080, 1350],
  ['CarB2.dc.html', 'carosello-B-2', 1080, 1350],
  ['CarB3.dc.html', 'carosello-B-3', 1080, 1350],
  ['CarB4.dc.html', 'carosello-B-4', 1080, 1350],
  ['CarB5.dc.html', 'carosello-B-5', 1080, 1350],
];

function toStandalone(dc) {
  const helmet = (dc.match(/<helmet>([\s\S]*?)<\/helmet>/) || [,''])[1].trim();
  const frame = (dc.match(/<\/helmet>([\s\S]*?)<\/x-dc>/) || [,''])[1].trim();
  return `<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n${helmet}\n</head>\n<body>\n${frame}\n</body>\n</html>\n`;
}

const browser = await chromium.launch({ executablePath: process.env.PW_CHROME || undefined });
for (const [dcFile, name, w, h] of manifest) {
  const dc = fs.readFileSync(path.join(grafiche, dcFile), 'utf8');
  const srcFile = path.join(src, `${name}.html`);
  fs.writeFileSync(srcFile, toStandalone(dc));
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
