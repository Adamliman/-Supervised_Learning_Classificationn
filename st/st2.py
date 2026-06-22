import streamlit as st
from PIL import Image

# -------------------------------
# 🎨 Configuration de la page
# -------------------------------
st.set_page_config(
    page_title="Image Viewer App",
    page_icon="🖼️",
    layout="wide"
)

# -------------------------------
# 🧭 En-tête
# -------------------------------
st.title("🖼️ Image Viewer App")
st.write("Cette application vous permet d'afficher une image depuis le web ou d'importer la vôtre.")

st.divider()

# -------------------------------
# 🌍 Affichage d'une image par défaut
# -------------------------------
st.subheader("📸 Image par défaut")
st.image(
    "https://picsum.photos/900/400",
    caption="Belle image aléatoire depuis le web",
    use_container_width=True
)

st.divider()

# -------------------------------
# 📁 Upload d'une image par l'utilisateur
# -------------------------------
st.subheader("📤 Importez votre propre image")

uploaded_file = st.file_uploader(
    "Choisissez un fichier image (jpg, png, jpeg)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(image, caption=f"Image importée : {uploaded_file.name}", use_container_width=True)
    with col2:
        st.success("✅ Image chargée avec succès !")
        st.write(f"**Nom :** {uploaded_file.name}")
        st.write(f"**Format :** {image.format}")
        st.write(f"**Taille :** {image.size[0]} x {image.size[1]} pixels")

else:
    st.info("Veuillez importer une image pour l'afficher ici 👆")

st.divider()

# -------------------------------
# 🧠 Pied de page
# -------------------------------
st.markdown("""
**Développé avec  par Streamlit**  
💡 *Astuce : chaque fois que vous rechargez, l'image par défaut change automatiquement !*
""")
