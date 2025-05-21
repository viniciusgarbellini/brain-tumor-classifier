import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Carregar o modelo treinado
model = load_model("modelo_brain_tumor.keras")
class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

st.title("Classificador de Tumores Cerebrais por MRI")

uploaded_file = st.file_uploader(
    "Envie uma imagem de ressonância (MRI)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Imagem Enviada", use_column_width=True)

    # Pré-processamento da imagem
    img = img.resize((256, 256))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predição
    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.subheader(f"Resultado: {predicted_class}")
    st.caption(f"Confiança: {confidence*100:.2f}%")
