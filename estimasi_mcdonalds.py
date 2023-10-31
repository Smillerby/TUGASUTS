import pickle
import streamlit as st

model = pickle.load(open('estimasi_mcdonalds.sav', 'rb'))

st.title('Estimasi Jumlah Nutrisi Di Menu McDonalds')
Cholesterols = st.number_input('Input Kolesterol (mg)')
Total_carbohydrate = st.number_input('Input Total Karbohidrat (g)')
Total_Sugars = st.number_input('Input Jumlah Gula (g)')
Protein = st.number_input('Input Jumlah Protein (g)')
Trans_fat = st.number_input('Input Jumlah Lemak(Lemak Jenuh)')
Sat_Fat = st.number_input('Input Total Sat Fat(Lemak Padat)')
Added_Sugars = st.number_input('Input Jumlah Gula Yang Di Tambahkan')
Total_fat = st.number_input('Input Jumlah Total Lemak')


predict = ''

if st.button('Estimasi Energi'):
    predict = model.predict(
        [[Cholesterols, Total_carbohydrate, Total_Sugars, Protein, Trans_fat, Added_Sugars, Total_fat, Sat_Fat]]
        )
    st.write ('Estimasi Jumlah Energi di setiap ukuran makanan McDonalds : ', predict)
