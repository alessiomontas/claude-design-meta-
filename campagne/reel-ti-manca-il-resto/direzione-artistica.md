# Direzione artistica — reel "Ti manca il resto"

**Nove scene editabili:** https://claude.ai/code/artifact/0c676336-1e90-4f3a-98bc-e26e6488f059
Ogni scena è un artboard 1080×1920 con sfondo, velo, marchio, barra di avanzamento e testi separati.
`grafiche/Main.dc.html` è la scena 1, poi `S2` … `S9`.

## Stesso stile, seconda voce

È il secondo contenuto della serie: identità grafica identica al reel da 8 secondi — fotografia reale a pieno
fotogramma, velo fumè a tre strati, una frase bianca al centro esatto in Archivo 800/900 a 72 px, marchio fisso
in alto, chiusura in oro. Chi vede i due reel di fila deve riconoscerli come dello stesso studio.

**Cosa cambia, e perché.** Un reel da 15 secondi ha un problema che quello da 8 non ha: la gente se ne va a
metà. Quindi:

- **Barra di avanzamento oro sotto il marchio.** Il filo bianco del lockup diventa un binario: una barra oro
  (`#C8A24B`, 3 px, 322 px di corsa) si riempie da sinistra a destra sui 15 secondi. Dice quanto manca senza
  rubare un pixel al centro del fotogramma. È la firma che distingue questo reel dal precedente.
- **Ritmo a lista.** Cinque battute identiche per struttura e durata (1,4 s l'una), tutte con la stessa
  impaginazione: l'occhio smette di rileggere e comincia a contare. È il ritmo che tiene fino alla fine.
- **Due scene finali più lunghe** (2 s ciascuna) per far leggere prima la presa in carico, poi il prezzo.

## Palette e tipografia

Identiche al reel da 8 secondi — vedi `campagne/reel-cosa-cerca-un-proprietario/direzione-artistica.md`.
In più, un solo elemento nuovo:

| Elemento | Valore |
|---|---|
| Binario barra | `rgba(255,255,255,0.28)`, 3 px, larghezza 322 px, `left: 379px`, `top: 168px` |
| Riempimento barra | `#C8A24B`, stessa geometria, larghezza proporzionale al tempo trascorso |
| Sottotitolo di scena 8 | Manrope 600, 40 px, `rgba(255,255,255,0.92)`, 30 px sotto il titolo |

Nel video la barra è disegnata da ffmpeg con `drawbox` e larghezza `322*min((t+offset)/15,1)`, così avanza in
modo continuo dentro ogni scena e non "scatta" agli stacchi.

## Le fonti visive, scena per scena

| Scena | Sorgente | Perché lì |
|---|---|---|
| 1-2 | `brand-assets/ambientazione/tramonto-litorale-romano.jpg` | il gancio parla di **comprare un'altra casa**: serve un'immagine di territorio, non di stanza. È anche l'unica scena che dichiara dove lavoriamo |
| 3 | `brand-assets/immobili/balcone-terrazzo.jpeg` | l'annuncio che ti fa trovare è la foto che ferma lo scroll: questa lo è |
| 4 | `brand-assets/immobili/cucina-soggiorno-open-space.png` (ritaglio zona pranzo) | scena ordinata, neutra, adatta a una frase sul prezzo |
| 5 | `brand-assets/video/clean/interno-cucina.mp4` | l'unico video in mezzo alla lista: rompe la sequenza di fermi immagine a metà |
| 6 | `brand-assets/immobili/salotto-divano-azzurro.jpg` (ritaglio divano) | tessuto e superfici: è la scena delle pulizie |
| 7 | `brand-assets/video/clean/balcone.mp4` | secondo video, chiude la lista in movimento |
| 8 | `brand-assets/immobili/salotto-divano-azzurro.jpg` (ritaglio tenda) | luce alta e calma: è il momento in cui il reel smette di elencare |
| 9 | `brand-assets/video/clean/busto-profilo.mp4` | la firma. Angolazione diversa dal reel precedente, che chiudeva sul busto frontale |

Alternanza: foto · foto · foto · **video** · foto · **video** · foto · **video**. I due video in mezzo e uno in
chiusura evitano che quindici secondi di fermi immagine sembrino una presentazione.

**Nessuna immagine generata.** Il materiale reale bastava, e un interno inventato in un contenuto di
acquisizione clienti è un rischio che non vale la pena correre: chi risponde poi visita quelle case.

## Attenzione sui marchi di terzi

Il primo montaggio della scena 8 usava un ritaglio dell'open space in cui comparivano un tostapane e una
macchina a capsule sul piano. Ritaglio cambiato. `smart-tv-streaming-mockup.jpg` resta **inutilizzabile** in
qualsiasi ritaglio: i loghi delle piattaforme sullo schermo sono leggibili anche di taglio.

## Pattern grafico

**"Una frase al centro sul reale" + barra di avanzamento.** Registrato in `.claude/reference/design-system.md`.
Il prossimo contenuto lungo può riusare la barra; un contenuto corto no, altrimenti la serie perde la differenza
tra il formato breve e quello lungo.
