// PDF della presentazione: una pagina per slide, misura PowerPoint 16:9 (13,333 × 7,5 pollici).
import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const slideDir = path.join(__dirname, 'slide');
const tmpDir = path.join(slideDir, '_render');
fs.mkdirSync(tmpDir, { recursive: true });

const ORDER = ['Main','Immobile','Percorso','Calendario','Regola','Responsabilita','Casa','Accessi',
  'Identita','Canali','Gestione','Strategia','Proprieta','Condizioni','Passo','Chiusura'];

const FONT_DIR = '/tmp/claude-0/-home-user-claude-design-meta-/51e09ff2-f7f1-5c62-9221-a8c1b5015230/scratchpad/fonts';
let FONT_CSS = '';
try {
  FONT_CSS = fs.readFileSync(path.join(FONT_DIR, 'local-fonts.css'), 'utf8')
    .replace(/url\((?!https?:)([^)]+)\)/g, (m, f) => `url(file://${FONT_DIR}/${f.trim()})`);
} catch { console.warn('!! font locali non trovati'); }

const frames = ORDER.map((n) => {
  const dc = fs.readFileSync(path.join(slideDir, n + '.dc.html'), 'utf8');
  return (dc.match(/<\/helmet>([\s\S]*?)<\/x-dc>/) || [, ''])[1].trim()
    .replace(/src="(?!https?:|data:|\.\.\/)([^"]+)"/g, 'src="../$1"');
});

const html = `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap">
<style>${FONT_CSS}
  @page { size: 1280px 720px; margin: 0; }
  html, body { margin: 0; padding: 0; background: #fff; font-family: 'Manrope', Arial, sans-serif; }
  .frame { page-break-after: always; break-after: page; }
  .frame:last-child { page-break-after: auto; break-after: auto; }
</style></head><body>
${frames.join('\n')}
</body></html>`;

const file = path.join(tmpDir, '_deck.html');
fs.writeFileSync(file, html);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
await page.goto(pathToFileURL(file).href, { waitUntil: 'load' });
try { await page.evaluate(() => document.fonts.ready); } catch {}
await page.waitForTimeout(600);
const out = path.join(__dirname, 'Hadrianus-Presentazione-Bilocale-Lido-Centro.pdf');
await page.pdf({ path: out, width: '1280px', height: '720px', printBackground: true, pageRanges: '1-16' });
await browser.close();
console.log('PDF:', out, (fs.statSync(out).size / 1024 / 1024).toFixed(2) + ' MB');
