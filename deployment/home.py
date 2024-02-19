import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def run():


    # Membuat Sub Header
    st.subheader('Default Prediction')

    # Menambahkan Deskripsi
    st.write('''Project ini dibuat untuk memenuhi tugas Milestone 2 Phase 1 di Hacktiv8 
             Indonesia dengan tujuan membangun sebuah model klasifikasi yang dapat memprediksi apakah 
             seorang debitur akan gagal membayar pada bulan berikutnya. Menggunakan dataset yang mencakup 
             informasi hubungan antara fitur-fitur dengan status default pembayaran. Dengan demikian, model 
             yang dihasilkan dapat digunakan untuk memberikan insight kepada institusi keuangan dalam mengidentifikasi 
             risiko kredit yang lebih tinggi dan mengambil langkah-langkah pencegahan yang sesuai untuk mengelola risiko.
             ''')

    # Membuat pembatas
    st.markdown('---')


    st.write('Created by: [Dwi Putra Satria Utama](https://www.linkedin.com/in/dwiputra3500/)')

if __name__ == '__main__':
    run()