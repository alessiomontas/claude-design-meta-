# Patong — rimando al brain su Google Drive

Questo repository è **pubblico**: la memoria del progetto Hadrianus Patong (Phuket) NON sta qui.

Brain privato su Google Drive, cartella `PATONG` → `_CLAUDE_BRAIN` (id cartella `1vQwQEV0anVnWSaQrWwgL1z6dOdu3Qw6P`).

All'avvio di una sessione su Patong, usa il connettore Google Drive (`read_file_content`) e leggi in quest'ordine:
1. `00_ISTRUZIONI_CLAUDE` (id `1J0TqPqc3rX8lcIcxS06bKSqY9cNj48dequXn1fZ5ccE`) — protocollo di lettura e aggiornamento
2. `01_MEMORIA` (id `1LYi3GrdqNf04Lf7KfnH932yiAy9ycK7Xa-UmcrHtYpw`)
3. `02_CRONOLOGIA` (id `1Us5FORahxDvWcLT3phKlr4Io4T3thd0_P782moIzLLU`) — solo le prime 5 voci
4. `03_CONOSCENZA_Fiscale_Burocrazia` e `04_INVENTARIO_Documenti` solo se servono

Gli id cambiano a ogni aggiornamento: se non vengono trovati, cerca per titolo nella cartella.
Non copiare in questo repository contratti, dati di clienti o analisi fiscali e legali.
