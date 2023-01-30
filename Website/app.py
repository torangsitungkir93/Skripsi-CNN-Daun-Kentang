import streamlit as st
import matplotlib.pyplot as plt
import time
import os
import cv2
import numpy as np
from PIL import Image, ImageOps
from img_classification import teachable_machine_classification, probabilitas
from remover import removeBg, ubahRGB


# Background and CSS
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #28BF78;
    border: none;
    padding: 13px 17px;
    border-radius: 10px;
    font-family:&#39;Muli&#39;, sans-serif;
    color: white;
    display: inline-block;
    cursor: pointer;
    text-decoration: none;
    align-items: center;
}
div.stButton > button:hover {
    background-color: #67c99b;
    color:##ff99ff;
    }
div.block-container {
    padding :32px;
}
</style>""", unsafe_allow_html=True)
background = Image.open('static/logo.png')
# background = background.resize((1600, 700))
st.image(background, use_column_width=False)
x = 20

uploaded_file = st.file_uploader(
    "Pilih Gambar yang akan diprediksi", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    #------ save image -------#
    with open(os.path.join("tempDir", "uploadFile.jpg"), "wb") as f:
        f.write(uploaded_file.getbuffer())
    uploadedPath = r"E:\\Mata Kuliah\Semester 8\Tugas Akhir\Website\\tempDir\\uploadFile.jpg"
    # ----------------------- #

    remover = removeBg(uploadedPath)
    ubahRGB()
    image = Image.open(
        "E:\Mata Kuliah\Semester 8\Tugas Akhir\Website\\out.jpg")

    # image_np = np.asarray(image)
    # st.write(image_np)
    # image = Image.open(uploaded_file)
    st.image(image, caption=None,
             width=250, use_column_width=False)

    #------ Klasifikasi -------#
    result = st.button("Prediksi Penyakit")
    if result:
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.007)
            progress.progress(i+1)
        label = teachable_machine_classification(
            image, 'Models/Kombinasi6.hdf5')
        if label == 0:
            st.warning("Prediksi gambar ini adalah Kentang Early Blight")
        if label == 1:
            st.success("Prediksi gambar ini adalah Kentang Healthy")
        if label == 2:
            st.warning("Prediksi gambar ini adalah Kentang Late Blight")
        hasil = probabilitas(image, 'Models/Kombinasi5Fix.hdf5')
        preds, persentase = probabilitas(image, 'Models/Model_2Bagus.hdf5')
        # preds
        # persentase
        # cekArray = np.asarray(image)
        # cekArray
else:
    result = st.button("Prediksi Penyakit ", disabled=True)
