# Video di brand — inventario

Cinque clip caricate dal titolare, lette e catalogate il 9 settembre 2026. Durano tutte 4-5 secondi: sono **materiale di sfondo e di stacco**, non filmati narrativi.

| File | Durata | Formato | Cosa si vede | Uso consigliato |
|---|---|---|---|---|
| `multiservice-brand.mp4` | 4,1 s · 1080×1350 (4:5) · 30 fps | h264 | **Logo animato**: la scritta `HADRIANUS MULTISERVICE` che si compone su fondo sabbia mentre entra il busto di Adriano | **Intro o outro** di ogni reel. È l'unico file senza filigrana: usalo come firma del brand |
| `clip-1.mov` | 5,2 s | h264 + audio | Busto di Adriano in marmo davanti al tempio, **zoom lento in avanti** fino al primo piano del volto; alla base la scritta HADRIANUS | Apertura o chiusura solenne, sotto un velo scuro con il testo sopra |
| `clip-2.mov` | 5,2 s | h264 + audio | **Balcone reale** con poltrona sospesa, piante, luce piena; movimento di camera lentissimo | Scena "casa vera": funziona dove si parla dell'immobile, non del brand |
| `clip-3.mov` | 5,2 s | h264 + audio | Stesso busto **di profilo**, zoom molto lento, inquadratura più larga | Stacco tra due blocchi di testo, o sfondo per la frase di chiusura |
| `logo-animato.mp4` | 5,2 s · 768×1344 · 24 fps | h264 | **Interno reale**: cucina e zona pranzo, tavolo apparecchiato, movimento appena percettibile | Sfondo per numeri e condizioni economiche: è ordinato e non ruba attenzione al testo |

*(i nomi originali sono fuorvianti: `logo-animato.mp4` è un interno, non il logo — il logo animato vero è `multiservice-brand.mp4` — e `clip-2`/`clip-3` sono l'opposto di come erano stati catalogati la prima volta. Usa la cartella `clean/`, dove i nomi dicono cosa si vede.)*

## ⚠️ Filigrana CapCut

**Quattro clip su cinque hanno la scritta `CapCut Ai` in alto a sinistra**, ben visibile su `clip-1` e `clip-2`, più tenue su `clip-3` e `logo-animato`. In un contenuto di acquisizione clienti è un problema: comunica "fatto con un'app gratuita", che è l'opposto del posizionamento professionale.

**Risolta il 9 settembre**: le quattro clip sono state ingrandite leggermente e ricentrate, così la filigrana
esce dal fotogramma. Le versioni pulite sono in `clean/` (tabella in fondo) e sono quelle da usare nei
montaggi. Resta comunque preferibile, quando possibile, **riesportare le clip da CapCut Pro senza filigrana**:
è l'unico modo di recuperare anche i pixel che il ritaglio ha tolto.

`multiservice-brand.mp4` è pulito e si può usare così com'è.

## Nota sull'origine

Le clip del busto sono immagini animate (movimento generato, non ripresa reale) e anche l'interno ha un movimento artificiale. Non è un problema di per sé — sono materiale di brand, non prove di risultato — ma **non vanno mai presentate come "il nostro immobile" o "il nostro lavoro"** se non ritraggono una casa realmente in gestione. Il balcone di `clip-2` corrisponde alla foto reale già in `brand-assets/immobili/balcone-terrazzo.jpeg`: quello sì è un immobile vero.

## Cosa si può fare con questi file, ora

L'ambiente ha un ffmpeg completo (h264): le clip si decodificano, si possono estrarre fotogrammi, tagliare, montare in sequenza con i testi sopra ed esportare direttamente in **MP4 pronto per Instagram**. Non serve più passare da CapCut per la conversione — serve solo se si vuole aggiungere musica scelta a mano.

## `clean/` — le versioni senza filigrana, pronte al montaggio

Il 9 settembre le quattro clip con filigrana sono state **ingrandite leggermente e ricentrate**, in modo che la
scritta `CapCut Ai` finisca fuori dal fotogramma. Nessuna toppa sopra, nessuna banda: il marchio esce dal bordo.

| File pulito | Da | Cosa si vede | Ingrandimento |
|---|---|---|---|
| `clean/busto-frontale.mp4` | `clip-1.mov` | busto di Adriano, zoom lento sul volto | +6,7% (tagliati 90 px in alto) |
| `clean/balcone.mp4` | `clip-2.mov` | balcone con poltrona sospesa | +42% (il formato 3:4 va comunque ritagliato per il 9:16) |
| `clean/busto-profilo.mp4` | `clip-3.mov` | busto di profilo | +6,7% |
| `clean/interno-cucina.mp4` | `logo-animato.mp4` | cucina e zona pranzo reali | +50% (sorgente 768 px, resta un po' morbida: usala sotto velo) |

Tutte in **1080×1920 (9:16), 30 fps, H.264, senza audio**, pronte per essere montate o caricate in CapCut.
Gli originali restano dove sono: non sono stati toccati.

`multiservice-brand.mp4` è pulito in partenza e non è stato ritoccato — ma è 4:5, va ritagliato o incorniciato
se serve dentro un 9:16.
