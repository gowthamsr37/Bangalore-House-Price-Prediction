import streamlit as st
import pandas as pd
import pickle
import numpy as np

pipe = pickle.load(open('house_price-model.pkl', 'rb'))
data = pd.read_csv('cleaned_data.csv')
st.header('Bangalore House Price Prediction')


location = st.selectbox('Select the Location' ,(data['location'].unique()))
bath = st.selectbox('Select the number of bathrooms' ,(sorted(data['bath'].unique())))
bhk = st.selectbox('Select the BHK' ,(sorted(data['bhk'].unique())))
total_sqft = st.selectbox('Select the area in sqft' ,(sorted(data['total_sqft'].unique())))

button = st.button('Predict the Price')

if button:
    prediction = pipe.predict(pd.DataFrame(np.array([location, total_sqft, bath, bhk]).reshape(1, 4),
                                      columns=['location', 'total_sqft', 'bath', 'bhk']))
    st.header('This property will cost around {} lakhs'.format(str(round(prediction[0],2))))


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSoak5PPPqR12DffIkfzcCFx4N9O33-_HV6w&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

