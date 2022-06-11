import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="SNT",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.markdown("# Accueil 🤖")

image = Image.open('./assets/snt.png')

st.image(image, width=250, caption='https://wall.alphacoders.com/')

st.write("# Le programme de SNT")
st.write('*Voyage au pays de l\'informatique* 🤖')

st.sidebar.success("Bienvenue dans l'espace SNT  de DarkSATHI Li")

st.markdown(
    """
+ Internet 🌐
+ Le Web 🖥
+ Les réseaux sociaux 📱
+ Les données structurées et leur traitement 📉
+ Localisation, cartographie et mobilité 🛰
+ Informatique embarquée et objets connectés 🤳🏿
+ La photographie numérique 🎨
    
    """
)

st.code(
    """
    def snt(name: str) -> str:
        return f'Mon nom est {name}'
    
>>> snt('DarkSATHI')
'Mon nom est DarkSATHI'

    """
)
