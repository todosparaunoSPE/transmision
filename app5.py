# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:35:00 2024

@author: jperezr
"""

import streamlit as st
import cv2
import numpy as np

# Configurar la página de Streamlit
st.title("Transmisión en Vivo con Streamlit y OpenCV")

# Inicializar la cámara
camera = cv2.VideoCapture(0)

# Función para capturar el video
def get_frame():
    ret, frame = camera.read()
    if not ret:
        st.error("No se pudo acceder a la cámara.")
        return None
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

# Crear un contenedor en Streamlit para mostrar el video
stframe = st.empty()

try:
    while True:
        frame = get_frame()
        if frame is not None:
            stframe.image(frame, channels="RGB")
        else:
            break
except KeyboardInterrupt:
    st.write("Transmisión detenida.")
finally:
    # Liberar la cámara al finalizar
    camera.release()