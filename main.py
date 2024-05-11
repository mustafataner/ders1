import streamlit as st
import pandas as pd

# Veri setini yükle
data = pd.read_csv('nufus_verileri.csv')

# Streamlit başlığı
st.title('Türkiye Şehir Nüfus Bilgileri')

# Şehir seçimi için dropdown menüsü
selected_city = st.selectbox('Şehir Seçiniz:', data['Sütun2'].unique())

# Seçilen şehir ile ilgili verileri göster
city_data = data[data['Sütun2'] == selected_city]
st.table(city_data[['Sütun2', 'Sütun3', 'Sütun4', 'Sütun5']])
