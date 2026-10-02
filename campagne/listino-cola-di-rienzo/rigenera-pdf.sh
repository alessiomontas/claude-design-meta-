#!/bin/bash
# Rigenera il PDF dal sorgente HTML (unica fonte di verità, autoconsistente:
# font e logo sono già dentro il file in base64).
# Uso: ./rigenera-pdf.sh
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
"$CHROME" --headless --disable-gpu --no-sandbox --virtual-time-budget=8000 \
  --no-pdf-header-footer \
  --print-to-pdf="$DIR/listino-hadrianus-cola-di-rienzo.pdf" \
  "file://$DIR/listino-hadrianus-cola-di-rienzo.html"
