import fitz  # PyMuPDF
import os

# 📁 Dossier contenant les PDF
dossier = r"\\192.168.0.60\Projets\E200312 - Elaboration d'un BioSensor (BioCapteur) avec système de mesure\Documentation\Publications\EIS"

# 🔍 Mot ou phrase à rechercher (insensible à la casse)
mot_cle = "trunk".lower()

# 📄 Liste des fichiers trouvés
resultats = []

# 🔄 Parcours de tous les fichiers PDF
for fichier in os.listdir(dossier):
    if fichier.lower().endswith(".pdf"):
        chemin_pdf = os.path.join(dossier, fichier)
        try:
            with fitz.open(chemin_pdf) as doc:
                texte = ""
                for page in doc:
                    texte += page.get_text()
                if mot_cle in texte.lower():
                    resultats.append(fichier)
        except Exception as e:
            print(f"Erreur dans {fichier} : {e}")

# ✅ Résultats
print("\n🔍 Mot-clé trouvé dans les fichiers suivants :")
for f in resultats:
    print("•", f)

if not resultats:
    print("Aucun fichier trouvé contenant ce mot ou cette phrase.")
