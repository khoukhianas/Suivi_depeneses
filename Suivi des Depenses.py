import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter import filedialog
# Créer une DataFrame pour stocker les dépenses
depenses_df = pd.DataFrame(columns=['Date', 'Montant', 'Description'])

def ajouter_depense():
    # Récupérer les valeurs saisies
    date = entry_date.get()
    montant = entry_montant.get()
    description = entry_description.get()

    # Vérifier si le montant est un nombre valide
    try:
        montant = float(montant)
    except ValueError:
        # Afficher un message d'erreur si le montant n'est pas valide
        tk.messagebox.showerror("Erreur", "Le montant doit être un nombre valide.")
        return
    
    # Créer une nouvelle ligne à ajouter
    nouvelle_depense = pd.DataFrame({'Date': [date], 'Montant': [montant], 'Description': [description]})
    
    # Concaténer la nouvelle ligne avec la DataFrame existante
    global depenses_df
    depenses_df = pd.concat([depenses_df, nouvelle_depense], ignore_index=True, sort=False)

    # Effacer les champs de saisie après ajout
    entry_date.delete(0, tk.END)
    entry_montant.delete(0, tk.END)
    entry_description.delete(0, tk.END)

def afficher_depenses():
   
    # Afficher toutes les dépenses enregistrées dans la DataFrame
    for index, row in depenses_df.iterrows():
        # Effacer le contenu actuel de la zone d'affichage des dépenses
        text_depenses.delete(1.0, tk.END)
        text_depenses.insert(tk.END,depenses_df)
        # Ajouter une ligne vide entre chaque dépense
        text_depenses.insert(tk.END, "\n")
def enregistrer():
    # Demander à l'utilisateur de choisir un emplacement pour enregistrer le fichier
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
    
    if file_path:
        # Enregistrer la DataFrame dans le fichier CSV
        depenses_df.to_csv(file_path, index=True)
        messagebox.showinfo("Enregistrement", "Les dépenses ont été enregistrées avec succès.")
    
# Créer une fenêtre principale
root = tk.Tk()
root.title("Gestion des Dépenses")

# Créer les widgets
label_date = tk.Label(root, text="Date (JJ/MM/AAAA):")
label_date.grid(row=0, column=0, padx=10, pady=10)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=10, pady=10)

label_montant = tk.Label(root, text="Montant:")
label_montant.grid(row=1, column=0, padx=10, pady=10)
entry_montant = tk.Entry(root)
entry_montant.grid(row=1, column=1, padx=10, pady=10)

label_description = tk.Label(root, text="Description:")
label_description.grid(row=2, column=0, padx=10, pady=10)
entry_description = tk.Entry(root)
entry_description.grid(row=2, column=1, padx=10, pady=10)

button_ajouter = tk.Button(root, text="Ajouter Dépense", command=ajouter_depense)
button_ajouter.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

button_afficher = tk.Button(root, text="Afficher Dépenses", command=afficher_depenses)
button_afficher.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

button_enregistrer = tk.Button(root, text="Enregistrer", command=enregistrer)
button_enregistrer.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

text_depenses = tk.Text(root, width=50, height=10)
text_depenses.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Lancer la boucle principale
root.mainloop()
