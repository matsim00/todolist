# To-Do List (Lista delle cose da fare)

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
   
   ```bash
   sudo apt-get install python3

2. **Installa pip**:
   Se pip non è installato, puoi farlo con il comando:

   ```bash
   sudo apt-get install python3-pip

   O su CentOS:

   ```bash
sudo yum install python3-pip

3. **Installa le dipendenze**:
Installa le librerie necessarie per eseguire il progetto:

   ```bash
pip install tkinter

4. **Test di Tkinter**:
Tkinter dovrebbe essere già incluso con Python, ma se non lo hai, puoi installarlo separatamente. Per esempio, su Ubuntu puoi farlo con:

   ```bash
sudo apt-get install python3-tk

5. **Clona il repository**:
Clona questo progetto sul tuo server Linux utilizzando git:

   ```bash
git clone https://github.com/tuo-utente/to-do-list.git

6. **Esegui il programma**:
Una volta che hai clonato il repository e installato tutte le dipendenze, puoi eseguire l'applicazione con il seguente comando:

   ```bash
python3 todo_list.py

Questo avvierà l'applicazione con l'interfaccia grafica di Tkinter, dove potrai aggiungere, rimuovere e completare le attività.
