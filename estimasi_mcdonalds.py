import pickle
import streamlit as st

model = pickle.load(open('estimasi_mcdonalds.sav', 'rb'))

st.title('Estimasi Jumlah Energi Di Menu McDonalds')
Cholesterols = st.number_input('Input Kolesterol (mg)')
Total_carbohydrate = st.number_input('Input Total Karbohidrat (g)')
Total_Sugars = st.number_input('Input Jumlah Gula (g)')
Protein = st.number_input('Input Jumlah Protein (g)')

predict = ''

if st.button('Estimasi Energi'):
    predict = model.predict(
        [[Cholesterols, Total_carbohydrate, Total_Sugars, Protein]]
        )
    st.write ('Estimasi Jumlah Energi di setiap ukuran makanan McDonalds : ', predict)