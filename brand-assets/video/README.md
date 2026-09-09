# Video di brand — inventario

Cinque clip caricate dal titolare, lette e catalogate il 9 settembre 2026. Durano tutte 4-5 secondi: sono **materiale di sfondo e di stacco**, non filmati narrativi.

| File | Durata | Formato | Cosa si vede | Uso consigliato |
|---|---|---|---|---|
| `multiservice-brand.mp4` | 4,1 s · 1080×1350 (4:5) · 30 fps | h264 | **Logo animato**: la scritta `HADRIANUS MULTISERVICE` che si compone su fondo sabbia mentre entra il busto di Adriano | **Intro o outro** di ogni reel. È l'unico file senza filigrana: usalo come firma del brand |
| `clip-1.mov` | 5,2 s | h264 + audio | Busto di Adriano in marmo davanti al tempio, **zoom lento in avanti** fino al primo piano del volto; alla base la scritta HADRIANUS | Apertura solenne, sotto un velo scuro con il testo del gancio sopra |
| `clip-2.mov` | 5,2 s | h264 + audio | Stesso busto **di profilo**, zoom molto lento, inquadratura più larga | Stacco tra due blocchi di testo, o sfondo per la frase di chiusura |
| `clip-3.mov` | 5,2 s | h264 + audio | **Balcone reale** con poltrona sospesa, piante, luce piena; movimento di camera lentissimo | Scena "casa vera": funziona dove si parla dell'immobile, non del brand |
| `logo-animato.mp4` | 5,2 s · 768×1344 · 24 fps | h264 | **Interno reale**: cucina e zona pranzo, tavolo apparecchiato, movimento appena percettibile | Sfondo per numeri e condizioni economiche: è ordinato e non ruba attenzione al testo |

*(il nome `logo-animato.mp4` è fuorviante: è un interno, non il logo. Il logo animato vero è `multiservice-brand.mp4`. Nomi da sistemare alla prossima occasione.)*

## ⚠️ Filigrana CapCut

**Quattro clip su cinque hanno la scritta `CapCut Ai` in alto a sinistra**, ben visibile su `clip-1` e `clip-2`, più tenue su `clip-3` e `logo-animato`. In un contenuto di acquisizione clienti è un problema: comunica "fatto con un'app gratuita", che è l'opposto del posizionamento professionale.

Tre modi per gestirla, in ordine di preferenza:

1. **Rigenerare le clip senza filigrana** (CapCut Pro le esporta pulite): è la soluzione vera.
2. **Coprirla**: la filigrana sta nell'angolo alto a sinistra, dove nelle nostre grafiche c'è già il marchio `— HADRIANUS`. Una banda o il logo posizionato lì la nasconde senza sembrare una toppa.
3. **Ritagliare l'alto** del fotogramma: si perde composizione, va valutato clip per clip.

`multiservice-brand.mp4` è pulito e si può usare così com'è.

## Nota sull'origine

Le clip del busto sono immagini animate (movimento generato, non ripresa reale) e anche l'interno ha un movimento artificiale. Non è un problema di per sé — sono materiale di brand, non prove di risultato — ma **non vanno mai presentate come "il nostro immobile" o "il nostro lavoro"** se non ritraggono una casa realmente in gestione. Il balcone di `clip-3` corrisponde alla foto reale già in `brand-assets/immobili/balcone-terrazzo.jpeg`: quello sì è un immobile vero.

## Cosa si può fare con questi file, ora

L'ambiente ha un ffmpeg completo (h264): le clip si decodificano, si possono estrarre fotogrammi, tagliare, montare in sequenza con i testi sopra ed esportare direttamente in **MP4 pronto per Instagram**. Non serve più passare da CapCut per la conversione — serve solo se si vuole aggiungere musica scelta a mano.
