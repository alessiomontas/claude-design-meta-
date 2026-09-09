# Modello reel 8 secondi — "la negazione + i desideri"

Schema di reel verticale indicato dal titolare come riferimento (video di un team immobiliare americano,
The Matheson Team · RE/MAX) e **riadattato al mestiere del property manager**. Prima applicazione:
`campagne/reel-cosa-cerca-un-proprietario/`. Leggilo prima di costruire un nuovo reel breve: è un telaio, non
un contenuto — il testo cambia ogni volta, la struttura no.

## Perché funziona

Il reel non mostra un prodotto: **nega la cosa che il pubblico si aspetta di sentire** ("i clienti non dicono
X") e poi elenca, una per inquadratura, le cose che vogliono davvero. Chi guarda si riconosce in una delle
righe e resta fino alla fine. Otto secondi bastano perché ogni battuta è una frase sola.

## Il telaio, battuta per battuta

| Battuta | Durata | Cosa contiene | Lunghezza indicativa |
|---|---|---|---|
| 1 · gancio | 0,0 → 2,0 s | la negazione: riga piccola di impostazione + frase grossa negata | 45-50 caratteri in tutto |
| 2 · svolta | 2,0 → 3,0 s | **stessa inquadratura**, entra una riga nuova che apre l'elenco | 15-20 caratteri |
| 3 | 3,0 → 4,0 s | primo desiderio | 30-40 caratteri |
| 4 | 4,0 → 5,0 s | secondo desiderio | 30-40 caratteri |
| 5 | 5,0 → 6,0 s | terzo desiderio | 30-40 caratteri |
| 6 · chiusura | 6,0 → 8,0 s | la firma commerciale: chi sei e perché quelle righe ti riguardano | 40-50 caratteri + riga oro |

Regole di ritmo: **stacchi netti** sui secondi esatti, nessuna dissolvenza tranne una sola — la riga della
battuta 2, che entra in 0,3 s sulla stessa scena. L'ultima battuta dura il doppio perché deve far leggere due
righe. Il video finisce di colpo: in loop riparte pulito.

## Regole tipografiche

- Testo **al centro esatto** del fotogramma. Mai in alto, mai in basso, mai allineato a sinistra.
- Sans grassetto (Archivo 800/900), **~72 px su 1080×1920** — circa il 20% più grande del modello originale,
  perché il pubblico Hadrianus è più anziano di quello di un reel di design.
- Massimo due righe per battuta, con le interruzioni di riga decise a mano.
- Ombra scura stratificata sotto ogni riga + velo circolare al centro: il bianco deve reggere anche sulle
  scene chiare.
- Marchio fisso in alto per tutta la durata (nome + filo + sottotitolo), come nel modello.
- Italiano. Una parola inglese si usa solo se è **quella che il reel nega**.

## La versione lunga (15 secondi)

Lo stesso telaio regge un formato lungo cambiando solo la parte centrale: il gancio resta 2,6 s, la svolta 1,4 s,
poi **cinque battute uguali da 1,4 s** invece di tre, e due scene finali da 2 s (prima la presa in carico, poi il
prezzo). Applicato in `campagne/reel-ti-manca-il-resto/`. Su un formato lungo aggiungi una **barra di
avanzamento** oro sotto il marchio: sopra i 10 secondi la gente se ne va a metà, e sapere quanto manca la
trattiene. Sotto i 10 secondi non serve e toglie carattere al formato breve.

## Cosa cambiare a ogni nuovo reel

La negazione e i tre desideri. Il telaio, i tempi e la tipografia restano: sono ciò che rende riconoscibile
la serie. Se serve un reel che **dimostra** invece che posizionare, questo schema non va bene — usa la
struttura a prove di `campagne/reel-superhost-acquisizione/`.

## Come si monta, tecnicamente

Overlay PNG con canale alpha renderizzati da Chromium (velo, marchio, testi in file separati), poi `overlay`
di ffmpeg battuta per battuta e `concat` finale. Export MP4 H.264 1080×1920 30 fps direttamente qui — vedi la
nota "Video / reel" in `design-system.md` e la ricetta in
`campagne/reel-cosa-cerca-un-proprietario/direzione-artistica.md`.
