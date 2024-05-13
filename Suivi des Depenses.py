import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

depenses_df = pd.DataFrame(columns=['Date','Montant','Description'])

def ajouter_depense():
    date = entry_date.get()
    montant = entry_montant.get()
    description = entry_description.get()

    try:
        montant = float(montant)
    except ValueError:
        tk.messagebox.showerror("Erreur", "Le montant doit être un nombre valide.")
        return
    
    nouvelle_depense = pd.DataFrame({'Date': [date], 'Montant': [montant], 'Description': [description]})
    global depenses_df
    depenses_df = pd.concat([depenses_df, nouvelle_depense], ignore_index=True, sort=False)

    entry_date.delete(0, tk.END)
    entry_montant.delete(0, tk.END)
    entry_description.delete(0, tk.END)

def afficher_depenses():
    text_depenses.delete(1.0, tk.END)
    text_depenses.insert(tk.END, depenses_df.to_string(index=False))

def enregistrer():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
    if file_path:
        depenses_df.to_csv(file_path, index=False)
        messagebox.showinfo("Enregistrement", "Les dépenses ont été enregistrées avec succès.")

def visualiser_depenses():
    plt.figure(figsize=(8, 6))
    plt.bar(depenses_df['Date'], depenses_df['Montant'], color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Montant')
    plt.title('Visualisation des Dépenses')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("Gestion des Dépenses")
root.configure(background="#f0f0f0")

label_date = tk.Label(root, text="Date (JJ/MM/AAAA):", bg="#f0f0f0", fg="#333333")
label_date.grid(row=0, column=0, padx=10, pady=10)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=10, pady=10)

label_montant = tk.Label(root, text="Montant:", bg="#f0f0f0", fg="#333333")
label_montant.grid(row=1, column=0, padx=10, pady=10)
entry_montant = tk.Entry(root)
entry_montant.grid(row=1, column=1, padx=10, pady=10)

label_description = tk.Label(root, text="Description:", bg="#f0f0f0", fg="#333333")
label_description.grid(row=2, column=0, padx=10, pady=10)
entry_description = tk.Entry(root)
entry_description.grid(row=2, column=1, padx=10, pady=10)

button_ajouter = tk.Button(root, text="Ajouter Dépense", command=ajouter_depense, bg="#4CAF50", fg="white")
button_ajouter.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

button_afficher = tk.Button(root, text="Afficher Dépenses", command=afficher_depenses, bg="#008CBA", fg="white")
button_afficher.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

button_enregistrer = tk.Button(root, text="Enregistrer", command=enregistrer, bg="#f44336", fg="white")
button_enregistrer.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

button_visualiser = tk.Button(root, text="Visualiser Dépenses", command=visualiser_depenses, bg="#345F33", fg="white")
button_visualiser.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

text_depenses = tk.Text(root, width=50, height=10)
text_depenses.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
