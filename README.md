# PDF Text Finder Suite

Une collection d'outils Python permettant de rechercher rapidement des mots ou des expressions dans des fichiers PDF.

Ces applications utilisent la bibliothèque **PyMuPDF (fitz/pymupdf)** pour extraire le texte des documents PDF et effectuer des recherches rapides, même sur de grandes quantités de fichiers.

---

# 🚀 Fonctionnalités

- Recherche de mots ou d'expressions dans des fichiers PDF
- Recherche insensible à la casse
- Comptage du nombre d'occurrences trouvées
- Affichage détaillé des résultats
- Ouverture directe des fichiers trouvés
- Interface graphique conviviale
- Recherche dans les sous-répertoires
- Compatible avec les dossiers locaux et les partages réseau Windows (SMB)

---

# 📦 Applications incluses

## 1. pdf-text-finder.py

Version console minimaliste destinée à l'automatisation et aux utilisateurs avancés.

### Fonctionnement

- Analyse les fichiers PDF d'un dossier prédéfini.
- Recherche un mot ou une expression définie dans le script.
- Affiche dans la console les fichiers contenant le texte recherché.

### Avantages

✅ Très léger  
✅ Rapide à exécuter  
✅ Facile à intégrer dans des scripts automatisés

### Limites

❌ Pas d'interface graphique  
❌ Paramètres à modifier directement dans le code

---

## 2. pdf-text-finder-gui.py

Version graphique standard basée sur Tkinter.

### Fonctionnement

- Sélection du dossier PDF via une boîte de dialogue.
- Saisie dynamique du texte recherché.
- Analyse des PDF présents uniquement dans le dossier sélectionné.
- Affiche le nombre d'occurrences trouvées.
- Ouvre le document PDF sur double-clic.

### Avantages

✅ Utilisation simple  
✅ Aucune modification du code nécessaire  
✅ Interface conviviale

### Limites

❌ Ne parcourt pas automatiquement les sous-dossiers

---

## 3. pdf-text-deepfinder-gui.py

Version graphique avancée pour les recherches documentaires de grande ampleur.

### Fonctionnement

- Parcours récursif complet d'une arborescence.
- Analyse automatique des sous-répertoires.
- Affiche les chemins relatifs des fichiers trouvés.
- Comptage détaillé des occurrences.
- Ouverture directe des PDF trouvés.

### Avantages

✅ Recherche dans des bibliothèques documentaires complètes  
✅ Compatible avec les serveurs de fichiers  
✅ Affichage détaillé des résultats  
✅ Recherche récursive automatique

### Limites

❌ Temps de recherche plus important sur des dossiers volumineux

---

# 📊 Comparatif

| Fonction | Console | GUI Standard | GUI DeepFinder |
|-----------|----------|-------------|----------------|
| Interface graphique | ❌ | ✅ | ✅ |
| Sélection du dossier | ❌ | ✅ | ✅ |
| Recherche récursive | ❌ | ❌ | ✅ |
| Comptage des occurrences | ✅ | ✅ | ✅ |
| Ouverture des PDF | ❌ | ✅ | ✅ |
| Compatible partage réseau | ✅ | ✅ | ✅ |
| Utilisation sans modifier le code | ❌ | ✅ | ✅ |

---

# 🖥️ Prérequis

- Python 3.10 ou supérieur
- Windows 10/11, Linux ou macOS

---

# ⚙️ Installation

## Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/PDF-Text-Finder.git
cd PDF-Text-Finder
```

## Créer un environnement virtuel

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Installer les dépendances

```bash
pip install pymupdf
```

ou

```bash
pip install PyMuPDF
```

---

# ▶️ Utilisation

## Version console

```bash
python pdf-text-finder.py
```

## Interface graphique standard

```bash
python pdf-text-finder-gui.py
```

## Interface graphique DeepFinder

```bash
python pdf-text-deepfinder-gui.py
```

---

# 📦 Création d'un exécutable Windows

## Avec PyInstaller

```bash
python -m PyInstaller --onefile --noconsole nom_du_script.py
```

### Exemples

```bash
python -m PyInstaller --onefile --noconsole pdf-text-finder-gui.py
```

```bash
python -m PyInstaller --onefile --noconsole pdf-text-deepfinder-gui.py
```

---

## Compression avec UPX

Téléchargement :

https://github.com/upx/upx/releases

Commande :

```bash
pyinstaller --onefile --noconsole --upx-dir="C:\Program Files\upx" ton_script.py
```

L'outil UPX permet de réduire significativement la taille finale de l'exécutable.

---

# 💡 Cas d'utilisation

- Recherche dans des publications scientifiques
- Exploration de bibliothèques documentaires
- Recherche de mots-clés dans des rapports PDF
- Vérification documentaire
- Audit de documents techniques
- Recherche dans des archives PDF volumineuses
- Analyse de documents stockés sur un serveur de fichiers

---

# 📚 Dépendances

- Python
- PyMuPDF (fitz / pymupdf)
- Tkinter (généralement inclus avec Python)

---

# 📄 Licence

MIT License

Copyright (c) 2026 Guy-Olivier Gétaz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# 👤 Auteur

**Guy-Olivier Gétaz**

Développé en Python avec **PyMuPDF** et **Tkinter** pour faciliter la recherche textuelle dans des collections de fichiers PDF.
