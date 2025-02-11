# To-Do List

## Descrizione
Questa applicazione "To-Do List" ti permette di creare e gestire una lista di attività (o una lista della spesa) tramite un'interfaccia grafica semplice e intuitiva, utilizzando la libreria Tkinter di Python. Puoi aggiungere, rimuovere e segnare come completati gli elementi della lista.

### Funzionalità:
- **Aggiungi attività**: Inserisci nuovi elementi nella lista.
- **Rimuovi attività**: Rimuovi un elemento selezionato dalla lista.
- **Segna come completato**: Segna un'attività come completata aggiungendo un'icona "✔" davanti all'elemento.

## Prerequisiti

### Ambiente di esecuzione:
Per eseguire questa applicazione, è necessario avere un ambiente Python configurato correttamente. Si consiglia di utilizzare un server Linux (ad esempio CentOS, Ubuntu, ecc.) e un applicativo come **MobaXterm** per facilitare l'interazione con il server tramite terminale e interfaccia grafica.

### Software richiesti:
- **Python** (versione 3.x)
- **pip** (gestore di pacchetti Python)
- **Tkinter** (libreria per l'interfaccia grafica)

### Installazione e configurazione dell'ambiente:

1. **Installa Python**:
   Se non hai già Python installato, puoi installarlo eseguendo il comando:

   - Su Ubuntu/Debian:

     ```bash
     sudo apt-get install python3
     ```

   - Su CentOS:

     ```bash
     sudo yum install python3
     ```

2. **Installa pip**:
   Se pip non è installato, puoi farlo con il comando:

   - Su Ubuntu/Debian:

     ```bash
     sudo apt-get install python3-pip
     ```

   - Su CentOS:

     ```bash
     sudo yum install python3-pip
     ```

3. **Installa le dipendenze**:
   Installa le librerie necessarie per eseguire il progetto. Usa `pip` per installare Tkinter:

   - Su Ubuntu/Debian:

     ```bash
     pip install tk
     ```

   - Su CentOS (Tkinter potrebbe essere già incluso, altrimenti):

     ```bash
     sudo yum install python3-tkinter
     ```

4. **Verifica che Tkinter sia installato correttamente**:
   Dopo aver installato Tkinter, puoi verificarne l'installazione avviando Python e cercando di importarlo:

   ```bash
   python3 -c "import tkinter"
