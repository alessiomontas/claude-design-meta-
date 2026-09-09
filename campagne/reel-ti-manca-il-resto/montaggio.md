# Pubblicare il reel — cosa serve fare

`reel/reel-ti-manca-il-resto.mp4` è già pronto: 1080×1920, 30 fps, 15,0 secondi, H.264, **muto**.
Si carica direttamente su Instagram Reels, Facebook Reels e TikTok.

## Musica (2 minuti in CapCut)

1. CapCut → Nuovo progetto → Importa il file. Non toccare le proporzioni.
2. **Audio → Suoni**: strumentale senza voce, 95-105 BPM. Filtra per uso commerciale.
3. Allinea i colpi forti a **0:02,6** (entra "Ti manca il resto"), **0:11,0** (la presa in carico) e
   **0:13,0** (la chiusura). La lista fra 4,0 e 11,0 sta su un tempo regolare: se la traccia ha un beat
   costante, i cinque stacchi ci cadono sopra da soli.
4. Esporta 1080×1920, 30 fps, qualità alta. Niente filigrana.

## Copertina

`reel/copertina.jpg` — il fotogramma con il gancio completo ("non ti serve un'altra casa" + "Ti manca il resto").
È l'immagine che ferma lo scroll nel feed: si legge tutto senza far partire il video.

## Dove e quando pubblicarlo

Instagram Reels e Facebook Reels. Nei gruppi Facebook di proprietari solo dove il regolamento consente la
promozione: chiedi prima all'admin.

**Ordine consigliato con gli altri due reel** (sono tre messaggi diversi sullo stesso pubblico, non tre versioni
della stessa cosa):

1. `reel-cosa-cerca-un-proprietario` (8 s) — posiziona: dice che cosa vuole davvero un proprietario.
2. **questo (15 s)** — argomenta: dice che cosa manca alla sua casa e quanto costa averlo.
3. `reel-superhost-acquisizione` (23 s) — dimostra: Superhost e recensioni reali.

Distanza consigliata: 4-6 giorni l'uno dall'altro.

## Se vuoi rifarlo

Le nove scene sono artboard modificabili in `grafiche/`. Cambia il testo, riesporta, rimonta: la ricetta tecnica
(overlay PNG con alpha + `overlay` di ffmpeg scena per scena + `concat`) è in `direzione-artistica.md` del reel
da 8 secondi.
