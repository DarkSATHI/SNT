import streamlit as st
from PIL import Image

image = Image.open('/assets/snt.png')

st.image(image, width=250, caption='https://wall.alphacoders.com/')

st.title("Internet 🌐")
st.sidebar.markdown("# Internet 🌐")
