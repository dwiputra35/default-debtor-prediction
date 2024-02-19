import streamlit as st
import home
import eda
import prediction

st.set_page_config(page_title='Default Prediction', layout='wide', initial_sidebar_state='expanded')

navigation = st.sidebar.selectbox('Pilih Halaman:', ('Home', 'Exploratory Data Analysis', 'Predict'))

if navigation == 'Home':
    home.run()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()