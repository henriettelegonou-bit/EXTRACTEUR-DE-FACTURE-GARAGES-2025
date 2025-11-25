import streamlit as st
import fitz  # PyMuPDF
import easyocr
from PIL import Image
import io
import re
import pandas as pd

st.title("Application d'extraction de données depuis factures PDF scannées")
st.write("Téléversez un fichier PDF scanné pour extraire les informations clés.")

uploaded_file = st.file_uploader("Choisir un fichier PDF", type=["pdf"])

if uploaded_file:
    st.info("Traitement en cours... Cela peut prendre quelques secondes.")

    # Charger le PDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    # Initialiser EasyOCR
    reader = easyocr.Reader(['fr'])

    # Liste pour stocker les données
    factures = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes()))

        # OCR avec EasyOCR
        result = reader.readtext(io.BytesIO(pix.tobytes()), detail=0)
        text = "
".join(result)

        # Extraction des données clés
        date_match = re.search(r"\d{2}/\d{2}/\d{4}", text)
        immat_match = re.search(r"[A-Z0-9-]{6,}", text)
        net_match = re.search(r"(NET À PAYER|Net à payer)[^\d]*(\d+[\.,]\d+)", text)

        # Extraction des lignes de désignation et prix unitaire
        lignes = []
        for line in text.splitlines():
            if re.search(r".+\s+(\d+[\.,]\d+)$", line):
                designation = re.sub(r"\s+(\d+[\.,]\d+)$", "", line)
                prix = re.search(r"(\d+[\.,]\d+)$", line).group()
                lignes.append({"Désignation": designation, "Prix Unitaire": prix})

        factures.append({
            "Page": page_num + 1,
            "Date": date_match.group() if date_match else "Non trouvée",
            "Immatriculation": immat_match.group() if immat_match else "Non trouvée",
            "Net à Payer": net_match.group(2) if net_match else "Non trouvé",
            "Lignes": lignes
        })

    # Affichage des résultats
    st.success("Extraction terminée !")
    for f in factures:
        st.subheader(f"Facture - Page {f['Page']}")
        st.write(f"Date : {f['Date']}")
        st.write(f"Immatriculation : {f['Immatriculation']}")
        st.write(f"Net à Payer : {f['Net à Payer']}")
        st.write("Désignations et Prix :")
        st.table(pd.DataFrame(f['Lignes']))

    # Préparer export Excel
    all_rows = []
    for f in factures:
        for ligne in f['Lignes']:
            all_rows.append({
                "Page": f['Page'],
                "Date": f['Date'],
                "Immatriculation": f['Immatriculation'],
                "Désignation": ligne['Désignation'],
                "Prix Unitaire": ligne['Prix Unitaire'],
                "Net à Payer": f['Net à Payer']
            })

    df_export = pd.DataFrame(all_rows)
    st.download_button(
        label="Télécharger en Excel",
        data=df_export.to_excel(index=False, engine='openpyxl'),
        file_name="factures_extraites.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )