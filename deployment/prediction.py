import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load model
with open('dt_best.pkl', 'rb') as file:
    dt_best = pickle.load(file)

def run():

    with st.form('key=default_predict'):
        person_age = st.number_input('Usia', min_value=0, max_value=120, value=0, step=1, help='Usia Peminjam')
        person_income = st.number_input('Pendapatan', min_value=0, max_value=6000000, value=0, step=1, help='Pendapatan Peminjam')
        person_home_ownership = st.selectbox('Status Tempat Tinggal', ['RENT', 'OWN', 'MORTAGE', 'OTHER'], help='Tempat tinggal Peminjam')
        person_emp_length = st.number_input('Berapa Lama Peminjam Telah Bekerja', min_value=0.0, max_value=120.0, value=0.0, step=0.01, format="%.2f", help='Lamanya bekerja dalam tahun')
        loan_intent = st.selectbox('Tujuan Peminjam', ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'], help='Tujuan pinjamnya untuk apa')
        loan_grade = st.selectbox('Tingkat Kredit Peminjam', ['A', 'B', 'C', 'D', 'E', 'F', 'G'], help='Tingkat kredit')
        loan_amnt = st.number_input('Jumlah Pinjaman', min_value=500, max_value=5000, value=1000, step=1, help='Berapa jumlah pinjaman')
        loan_int_rate = st.number_input('Tingkat Suku Bunga', min_value=5.42, max_value=23.22, value=5.42, step=0.01, format="%.2f", help='Suku bunga pinjaman')
        loan_percent_income = st.number_input('Persen Pendapatan Yang Digunakan Untuk Pembayaran Pinjaman', min_value=0.0, max_value=0.83, value=0.0, step=0.01, format="%.2f", help='Persen pendapatan yang digunakan untuk membayar/mencicil pinjaman')
        cb_person_default_on_file = st.selectbox('Riwayat Gagal Bayar Sebelumnya', ['Tidak', 'Ya'], help='Apakah sebelumnya pernah gagal bayar?')
        cb_person_cred_hist_length = st.number_input('Lama Riwayat Kredit', min_value=2, max_value=30, value=2, step=1, help='Usia Peminjam')
        
        # Konversi nilai cb_person_default_on_file
        if cb_person_default_on_file == 'Ya':
            cb_person_default_on_file = 'Y'
        else:
            cb_person_default_on_file = 'N'

        st.markdown('---')

        # Tambahkan tombol submit di dalam form
        submitted = st.form_submit_button('Predict')

    new_data = {
        'person_age': person_age,
        'person_income': person_income,
        'person_home_ownership': person_home_ownership,
        'person_emp_length': person_emp_length,
        'loan_intent': loan_intent,
        'loan_grade': loan_grade,
        'loan_amnt': loan_amnt,
        'loan_int_rate': loan_int_rate,
        'loan_percent_income': loan_percent_income,
        'cb_person_default_on_file': cb_person_default_on_file,
        'cb_person_cred_hist_length': cb_person_cred_hist_length
    }

    new_data = pd.DataFrame(new_data, index=[0])
    st.dataframe(new_data)

    if submitted:
        pred = dt_best.predict(new_data)

        # Menampilkan hasil prediksi
        st.subheader('Hasil Prediksi')
        if pred == 1:
            st.write("Kemungkinan Debitur Gagal Bayar")
        else:
            st.write("Tidak Gagal Bayar")

if __name__ == '__main__':
    run()