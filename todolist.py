import tkinter as tk

def add_item():
    item = entry.get()
    if item != "":
        listbox.insert(tk.END, item)  # Aggiungi l'elemento alla lista
        entry.delete(0, tk.END)  # Pulisci il campo di input

def remove_item():
    try:
        selected_item_index = listbox.curselection()  # Ottieni l'indice dell'elemento selezionato
        listbox.delete(selected_item_index)  # Rimuovi l'elemento
    except IndexError:
        pass  # Se non è stato selezionato nessun elemento, ignora

def complete_item():
    try:
        selected_item_index = listbox.curselection()
        item = listbox.get(selected_item_index)  # Ottieni l'elemento selezionato
        listbox.delete(selected_item_index)  # Rimuovi l'elemento dalla lista
        listbox.insert(tk.END, f"✔ {item}")  # Aggiungi l'elemento come "completato"
    except IndexError:
        pass  # Se non è stato selezionato nessun elemento, ignora

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Aggiungi", width=20, command=add_item)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10)

remove_button = tk.Button(root, text="Rimuovi", width=20, command=remove_item)
remove_button.pack(pady=5)

complete_button = tk.Button(root, text="Completato", width=20, command=complete_item)
complete_button.pack(pady=5)

root.mainloop()
