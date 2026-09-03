import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const src = path.join(__dirname, 'src');
const out = path.join(__dirname, 'out');

const jobs = [
  ['storia-1.html', 1080, 1920],
  ['storia-2.html', 1080, 1920],
  ['storia-3.html', 1080, 1920],
  ['storia-4.html', 1080, 1920],
  ['storia-5.html', 1080, 1920],
  ['carosello-1.html', 1080, 1350],
  ['carosello-2.html', 1080, 1350],
  ['carosello-3.html', 1080, 1350],
  ['carosello-4.html', 1080, 1350],
  ['carosello-5.html', 1080, 1350],
  ['post-prova.html', 1080, 1350],
  ['reel-cover.html', 1080, 1920],
];

const browser = await chromium.launch({
  executablePath: process.env.PW_CHROME || undefined,
});
for (const [file, w, h] of jobs) {
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  const url = pathToFileURL(path.join(src, file)).href;
  await page.goto(url, { waitUntil: 'load' });
  try { await page.evaluate(() => document.fonts.ready); } catch {}
  await page.waitForTimeout(400);
  const el = await page.$('.frame');
  const outFile = path.join(out, file.replace('.html', '.png'));
  await el.screenshot({ path: outFile });
  console.log('rendered', path.basename(outFile), `${w}x${h}`);
  await page.close();
}
await browser.close();
console.log('done');
