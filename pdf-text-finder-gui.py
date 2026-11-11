import tkinter as tk
from tkinter import filedialog, messagebox
#import fitz  # PyMuPDF
import pymupdf
import os
import threading
import platform
import subprocess

class PDFSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recherche de mots dans des PDF")
        self.root.geometry("700x570")

        # Widgets
        self.label_dossier = tk.Label(root, text="Dossier PDF :")
        self.label_dossier.pack(anchor='w', padx=10, pady=(10, 0))

        self.entry_dossier = tk.Entry(root, width=70)
        self.entry_dossier.pack(padx=10)

        self.btn_parcourir = tk.Button(root, text="Parcourir...", command=self.choisir_dossier)
        self.btn_parcourir.pack(pady=5)

        self.label_mot = tk.Label(root, text="Mot ou phrase à rechercher :")
        self.label_mot.pack(anchor='w', padx=10, pady=(10, 0))

        self.entry_mot = tk.Entry(root, width=50)
        self.entry_mot.pack(padx=10)

        self.btn_rechercher = tk.Button(root, text="Rechercher", command=self.lancer_recherche)
        self.btn_rechercher.pack(pady=10)

        self.liste_resultats = tk.Listbox(root, width=100, height=20)
        self.liste_resultats.pack(padx=10, pady=10)
        self.liste_resultats.bind('<Double-1>', self.ouvrir_pdf)

        self.label_status = tk.Label(root, text="", fg="gray")
        self.label_status.pack(padx=10, pady=(0, 10))

        self.fichiers_trouves = []

    def choisir_dossier(self):
        dossier = filedialog.askdirectory()
        if dossier:
            self.entry_dossier.delete(0, tk.END)
            self.entry_dossier.insert(0, dossier)

    def lancer_recherche(self):
        self.btn_rechercher.config(state=tk.DISABLED)
        self.label_status.config(text="Recherche en cours...")
        self.liste_resultats.delete(0, tk.END)
        self.fichiers_trouves = []

        # Thread pour ne pas bloquer l'interface
        thread = threading.Thread(target=self.recherche_en_arriere_plan)
        thread.start()

    def recherche_en_arriere_plan(self):
        dossier = self.entry_dossier.get()
        mot_cle = self.entry_mot.get().strip().lower()

        if not os.path.isdir(dossier):
            self.afficher_erreur("Le dossier spécifié n'existe pas.")
            return
        if not mot_cle:
            self.afficher_erreur("Veuillez entrer un mot ou une phrase à rechercher.")
            return

        fichiers_temp = []
        labels_temp = []
        total_resultats = 0

        for fichier in os.listdir(dossier):
            if fichier.lower().endswith(".pdf"):
                chemin_complet = os.path.join(dossier, fichier)
                try:
                    with pymupdf.open(chemin_complet) as doc:
                        texte = ""
                        for page in doc:
                            texte += page.get_text()
                        occurrences = texte.lower().count(mot_cle)
                        if occurrences > 0:
                            affichage = f"{fichier} ({occurrences} occurrence{'s' if occurrences > 1 else ''})"
                            fichiers_temp.append(chemin_complet)
                            labels_temp.append(affichage)
                            total_resultats += 1
                except Exception as e:
                    print(f"Erreur avec {fichier} : {e}")

        self.root.after(0, self.afficher_resultats, fichiers_temp, labels_temp, total_resultats)

    def afficher_resultats(self, fichiers, labels, total):
        self.fichiers_trouves = fichiers
        self.liste_resultats.delete(0, tk.END)
        for label in labels:
            self.liste_resultats.insert(tk.END, label)
        if total == 0:
            self.label_status.config(text="Aucun fichier trouvé.")
        else:
            self.label_status.config(text=f"{total} fichier(s) trouvé(s).")
        self.btn_rechercher.config(state=tk.NORMAL)

    def afficher_erreur(self, message):
        self.root.after(0, lambda: [
            messagebox.showerror("Erreur", message),
            self.btn_rechercher.config(state=tk.NORMAL),
            self.label_status.config(text="")
        ])

    def ouvrir_pdf(self, event):
        selection = self.liste_resultats.curselection()
        if selection:
            index = selection[0]
            chemin = self.fichiers_trouves[index]
            try:
                if platform.system() == "Windows":
                    os.startfile(chemin)  # Compatible avec chemins SMB \\serveur\...
                else:
                    subprocess.Popen(["xdg-open", chemin])
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier :\n{e}")

# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFSearchApp(root)
    root.mainloop()
