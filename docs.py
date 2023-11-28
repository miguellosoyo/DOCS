# Importrar librerías de trabajo
from PIL import Image, ImageDraw, ImageFont
import streamlit as st
import pandas as pd
import io

# Definir función para agregar texto a una imagen
def add_text_to_image(image, text, position, font_path='arialbd.ttf', font_size=12):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, (0, 0, 0), font=font)
    return image

# Interfaz de Streamlit
st.title('Agregar texto a una imagen')

uploaded_file = st.file_uploader("Elige una imagen", type=["png", "jpg", "jpeg"])
text = st.text_input("Texto a insertar")
x = st.number_input("Posición X", min_value=0)
y = st.number_input("Posición Y", min_value=0)
position = (x, y)

format_option = st.selectbox("Formato de salida", ["PNG", "JPG"])

if st.button("Agregar texto a la imagen"):
    if uploaded_file is not None:
        with st.spinner('Procesando...'):
            image = Image.open(uploaded_file).convert("RGBA")
            modified_image = add_text_to_image(image, text, position)
            buffered = io.BytesIO()
            if format_option == "PNG":
                modified_image.save(buffered, format="PNG")
                st.download_button("Descargar imagen", buffered, "modified_image.png")
            else:
                modified_image_rgb = modified_image.convert("RGB")
                modified_image_rgb.save(buffered, format="JPEG")
                st.download_button("Descargar imagen", buffered, "modified_image.jpg")
