import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor

model = pickle.load(open('RandomForestRegressor.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))


st.title('Gold_Price_Prediction')

SPX = st.number_input('SPX:')
USO = st.number_input('USO:')
SLV = st.number_input('SLV:')
EUR_USD = st.number_input('EUR/USD:')

prediction=''
if st.button('Predict'):
    input = pd.DataFrame([[SPX, USO, SLV, EUR_USD]], columns=['SPX', 'USO', 'SLV', 'EUR/USD'])
    prediction += str(model.predict(input)[0])

st.success(prediction)
