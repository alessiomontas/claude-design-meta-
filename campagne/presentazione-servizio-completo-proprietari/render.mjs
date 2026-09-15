// Render delle slide editabili (.dc.html) in PNG 2x — stessa fonte di verità del canvas.
import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const slideDir = path.join(__dirname, 'slide');
const outDir = path.join(__dirname, 'png');
const tmpDir = path.join(slideDir, '_render');
fs.mkdirSync(outDir, { recursive: true });
fs.mkdirSync(tmpDir, { recursive: true });

const W = 1280, H = 720, SCALE = 2;

// I webfont di Google non sono raggiungibili da questo ambiente (proxy TLS):
// per il render si iniettano gli stessi file scaricati in locale, così il PNG
// mostra davvero Archivo/Manrope come il canvas online.
const FONT_DIR = '/tmp/claude-0/-home-user-claude-design-meta-/51e09ff2-f7f1-5c62-9221-a8c1b5015230/scratchpad/fonts';
let FONT_CSS = '';
try {
  FONT_CSS = fs.readFileSync(path.join(FONT_DIR, 'local-fonts.css'), 'utf8')
    .replace(/url\((?!https?:)([^)]+)\)/g, (m, f) => `url(file://${FONT_DIR}/${f.trim()})`);
} catch { console.warn('!! font locali non trovati: il PNG userà i font di fallback'); }

function toStandalone(dc) {
  const helmet = (dc.match(/<helmet>([\s\S]*?)<\/helmet>/) || [, ''])[1].trim();
  const frame = (dc.match(/<\/helmet>([\s\S]*?)<\/x-dc>/) || [, ''])[1].trim();
  // le immagini stanno una cartella sopra rispetto a slide/_render/
  const fixed = frame.replace(/src="(?!https?:|data:|\.\.\/)([^"]+)"/g, 'src="../$1"')
                     .replace(/url\((['"]?)(?!https?:|data:|\.\.\/)([^)'"]+)\1\)/g, 'url($1../$2$1)');
  return `<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n${helmet}\n<style>${FONT_CSS}</style>\n</head>\n<body style="margin:0">\n${fixed}\n</body>\n</html>\n`;
}

const only = process.argv.slice(2);
const files = fs.readdirSync(slideDir).filter(f => f.endsWith('.dc.html'))
  .filter(f => !only.length || only.includes(f) || only.includes(f.replace('.dc.html', '')))
  .sort();

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
for (const f of files) {
  const name = f.replace('.dc.html', '');
  const html = toStandalone(fs.readFileSync(path.join(slideDir, f), 'utf8'));
  const tmp = path.join(tmpDir, `${name}.html`);
  fs.writeFileSync(tmp, html);
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: SCALE });
  await page.goto(pathToFileURL(tmp).href, { waitUntil: 'load' });
  try { await page.evaluate(() => document.fonts.ready); } catch {}
  await page.waitForTimeout(350);
  const el = await page.$('.frame');
  await el.screenshot({ path: path.join(outDir, `${name}.png`) });
  const box = await el.boundingBox();
  console.log('ok', name, `${Math.round(box.width)}x${Math.round(box.height)}`);
  await page.close();
}
await browser.close();
