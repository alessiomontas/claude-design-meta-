// PNG (2×) + PDF A4 del preventivo, dalle stesse artboard editabili.
import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const tmp = path.join(__dirname, '_render');
fs.mkdirSync(tmp, { recursive: true });
const W = 794, H = 1123;
const FONT_DIR = '/tmp/claude-0/-home-user-claude-design-meta-/51e09ff2-f7f1-5c62-9221-a8c1b5015230/scratchpad/fonts';
let FONT_CSS = '';
try {
  FONT_CSS = fs.readFileSync(path.join(FONT_DIR, 'local-fonts.css'), 'utf8')
    .replace(/url\((?!https?:)([^)]+)\)/g, (m, f) => `url(file://${FONT_DIR}/${f.trim()})`);
} catch { console.warn('!! font locali non trovati'); }

const frame = (f) => {
  const dc = fs.readFileSync(path.join(__dirname, f), 'utf8');
  return (dc.match(/<\/helmet>([\s\S]*?)<\/x-dc>/) || [, ''])[1].trim()
    .replace(/src="(?!https?:|data:|\.\.\/)([^"]+)"/g, 'src="../$1"');
};
const head = `<meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
<style>${FONT_CSS}
@page { size: ${W}px ${H}px; margin: 0; }
html, body { margin: 0; padding: 0; background: #fff; font-family: 'Manrope', 'Helvetica Neue', Arial, sans-serif; }
.frame { page-break-after: always; break-after: page; }
.frame:last-child { page-break-after: auto; break-after: auto; }
</style>`;

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
// PNG singoli
for (const [f, name] of [['Main.dc.html', 'preventivo-1'], ['Pagina2.dc.html', 'preventivo-2']]) {
  const file = path.join(tmp, name + '.html');
  fs.writeFileSync(file, `<!doctype html><html><head>${head}</head><body>${frame(f)}</body></html>`);
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  await page.goto(pathToFileURL(file).href, { waitUntil: 'load' });
  try { await page.evaluate(() => document.fonts.ready); } catch {}
  await page.waitForTimeout(300);
  await (await page.$('.frame')).screenshot({ path: path.join(__dirname, name + '.png') });
  console.log('ok', name);
  await page.close();
}
// PDF a due pagine
const file = path.join(tmp, '_preventivo.html');
fs.writeFileSync(file, `<!doctype html><html><head>${head}</head><body>${frame('Main.dc.html')}\n${frame('Pagina2.dc.html')}</body></html>`);
const page = await browser.newPage({ viewport: { width: W, height: H } });
await page.goto(pathToFileURL(file).href, { waitUntil: 'load' });
try { await page.evaluate(() => document.fonts.ready); } catch {}
await page.waitForTimeout(400);
const out = path.join(__dirname, 'Hadrianus-Preventivo-Messa-in-Regola.pdf');
await page.pdf({ path: out, width: `${W}px`, height: `${H}px`, printBackground: true, pageRanges: '1-2' });
await browser.close();
console.log('PDF:', out, (fs.statSync(out).size / 1024).toFixed(0) + ' KB');
