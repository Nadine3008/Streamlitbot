import streamlit as st

# Sélection du modèle GPT
model_type = st.selectbox(
    "Choisissez un type de modèle GPT :",
    ["gpt-3.5-turbo", "instruction gpt-3.5-turbo", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-0125"]
)

# Affichage du modèle sélectionné
st.write(f"Modèle sélectionné : {model_type}")

# Ajouter un slider pour le nombre maximum de jetons
max_tokens = st.slider(
    "Choisissez le nombre maximum de jetons :",
    min_value=0,
    max_value=500,
    value=100  # Valeur par défaut
)

# Affichage de la valeur sélectionnée
st.write(f"Nombre maximum de jetons : {max_tokens}")
