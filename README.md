# EXTRACTEUR-DE-FACTURES-PDF

Application **Streamlit** pour l'extraction de données depuis des factures PDF scannées à l'aide de **EasyOCR**.

## ✅ Fonctionnalités
- Téléversement d'un fichier PDF scanné
- Extraction automatique des informations :
  - Date
  - Immatriculation du véhicule
  - Net à Payer
  - Désignation et Prix Unitaire
- Affichage des résultats dans une interface web
- Export des données en Excel (.xlsx)

## 🛠️ Prérequis
- Python 3.9 ou supérieur

## 📦 Installation locale
```bash
git clone https://github.com/votre-utilisateur/EXTRACTEUR-DE-FACTURES-PDF.git
cd EXTRACTEUR-DE-FACTURES-PDF
pip install -r requirements.txt
streamlit run app_streamlit_easyocr.py
```

## ☁️ Déploiement sur Streamlit Cloud
1. Créez un compte sur [Streamlit Cloud](https://streamlit.io/cloud)
2. Connectez votre dépôt GitHub
3. Déployez l'application → obtenez un lien public

## 📂 Structure du projet
```
📂 EXTRACTEUR-DE-FACTURES-PDF
 ├── app_streamlit_easyocr.py   # Script principal Streamlit
 ├── requirements.txt           # Dépendances
 ├── README.md                  # Documentation
 ├── .gitignore                 # Fichiers à ignorer
```

## 📸 Capture d'écran (exemple)
![Interface Streamlit](https://streamlit.io/images/brand/streamlit-mark-color.png)

## ✅ Auteur
Projet développé pour automatiser l'extraction des données de factures PDF scannées.
