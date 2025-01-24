import streamlit as st

# Sélection du modèle GPT
model_type = st.selectbox(
    "Choisissez un type de modèle GPT :",
    ["gpt-3.5-turbo", "instruction gpt-3.5-turbo", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-0125"]
)

# Affichage du modèle sélectionné
st.write(f"Modèle sélectionné : {model_type}")
