import streamlit as st

st.title("cars shoroom")

st.header('cars')


st.write('ertyuio')

st.subheader("Sous-section")

st.markdown("**Texte en gras** et *italique*")

if st.button('clique me'):
    st.write('adam khir mn cr7')

nom = st.text_input('votre nom')
if nom :
    st.success(f'bonjour {nom}')


col1 ,col2 = st.columns(2)
col1.write('AZERTYUI')
col2.write('DFGHJKL')

with st.sidebar :
    st.header ("Menu latéral")
    choix = st.selectbox("Choisir :", ["Accueil", "Analyse", "Contact"])


nom = st.text_input("Entrez votre nom")
age = st.number_input("Votre âge", min_value=0, max_value=100)
st.button("Valider")
choix = st.selectbox("Choisissez une option", ["A", "B", "C"])
multi = st.multiselect("Options multiples", ["Python", "R", "SQL"])



import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["col1", "col2"]
)

st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)


if "compteur" not in st.session_state:
    st.session_state.compteur = 0

if st.button("Ajouter 1"):
    st.session_state.compteur += 1

st.write("Compteur :", st.session_state.compteur)


checkbox = st.checkbox("I agree")
radio = st.radio("Pick one", ["Option A", "Option B", "Option C"])
select = st.selectbox("Choose one", ["MCA", "JSK", "USMA"])

multiselect = st.multiselect("Choose multiple", ["A", "B", "C"])
toggle = st.toggle("Enable feature")


st.image("https://picsum.photos/800/400", caption="Belle image", use_container_width=True)


progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

