import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image



def run():

    # title
    st.title('Default Prediction')

    # sub header
    st.subheader('Kemungkinan Gagal Bayar atau Tidak Pada Debitur')

    # gambar
    image = Image.open('image.jpg')
    st.image(image, caption='')

    # deskripsi
    st.write('Created by: [Dwi Putra Satria Utama](https://www.linkedin.com/in/dwiputra3500/)')

    # garis pembatas
    st.markdown('---')

    # dataframe
    df = pd.read_csv('credit_risk_dataset.csv')

    # sub header
    st.subheader('Data yang paling berpengaruh terhadap kemungkinan gagal bayar Debitur')

    # Membuat clustered bar plot untuk korelasi antara loan_status dan person_home_ownership
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(x='person_home_ownership', hue='loan_status', data=df, palette='viridis')
    plt.legend(title='Status Pinjaman', loc='upper right', labels=['Tidak gagal bayar', 'Gagal bayar'])
    plt.title('Korelasi antara Status Pinjaman dan Status Tempat Tinggal')
    plt.xlabel('Status tempat tinggal')
    plt.ylabel('Jumlah')
    st.pyplot(fig)

    st.write('Berdasarkan grafik tersebut, status tempat tinggal mempengaruhi tingkat gagal bayar, dimana status tempat tinggal yang masih RENT memiliki tingkat gagal bayar tertinggi diantara yang lain.')
    
    # garis pembatas
    st.markdown('---')

    # Membuat kolom baru untuk range pendapatan berdasarkan deskripsi yang diberikan
    income_bins = [0, 39500, 56000, 66500, 6000000]
    income_labels = ['Rendah', 'Menengah', 'Tinggi', 'Sangat Tinggi']
    df['income_range'] = pd.cut(df['person_income'], bins=income_bins, labels=income_labels)

    # Mengurutkan kategori range pendapatan secara berurutan
    df['income_range'] = pd.Categorical(df['income_range'], categories=income_labels, ordered=True)

    # Membuat bar plot untuk korelasi antara loan_status dan income_range
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(x='income_range', hue='loan_status', data=df, palette='viridis')
    plt.legend(title='Status Pinjaman', loc='upper right', labels=['Tidak gagal bayar', 'Gagal bayar'])
    plt.title('Korelasi antara Status Pinjaman dan Range Pendapatan')
    plt.xlabel('Range Pendapatan')
    plt.ylabel('Jumlah')
    st.pyplot(fig)

    # Deskripsi nominal range
    st.write('Deskripsi nominal range pendapatan:')
    st.write('Rendah        : ≤ 39.500')
    st.write('Menengah      : 39.501 - 56.000')
    st.write('Tinggi        : 56.001 - 66.500')
    st.write('Sangat Tinggi : ≥ 66.501')

    st.write('Berdasarkan grafik tersebut, tinggi atau rendahnya pendapatan mempengaruhi tingkat gagal bayar, dimana orang orang yang berpendapatan rendah memiliki tingkat gagal bayar tertinggi diantara yang lain.')


    # garis pembatas
    st.markdown('---')

    # Membuat histogram untuk korelasi antara loan_percent_income dan loan_status
    fig = plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='loan_percent_income', hue='loan_status', bins=20, kde=True, palette='viridis')
    plt.legend(title='Status Pinjaman', loc='upper right', labels=['Gagal bayar', 'Tidak gagal bayar'])
    plt.title('Korelasi antara loan_percent_income dan Status Pinjaman')
    plt.xlabel('Persentase pendapatan yang digunakan untuk pembayaran pinjaman')
    plt.ylabel('Jumlah')
    st.pyplot(fig)

    st.write('Berdasarkan grafik tersebut, persentase pendapat yang digunakan untuk membayar pinjaman mempengaruhi tingkat gagal bayar, dimana semakin tinggi nilai persentasenya semakin berkemungkinan memiliki resiko gagal bayar, dimana titik puncak berda pada angka 0.3, setelah itu landai kembali.')
    
    # garis pembatas
    st.markdown('---')

if __name__ == '__main__':
    run()
