# create a streamlit app to take a user input and return a prediction

import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

from src.helper_pred import predict_top5
"""
# Welcome to Product Name Predictor!

Put a `Title of a SMAX Ticket` then click the `Predict` button to get the top 5 predicted product names.

"""

# load the model
# MODEL_SELECTED =  'logistic_regression'
MODEL_SELECTED =  'sgc_classifier'

model = joblib.load(f'models/model_{MODEL_SELECTED}.pkl', 'rb')
vectorizer = joblib.load(f'models/vectorizer_{MODEL_SELECTED}.pkl', 'rb')

# add a text area
title = st.text_area('Title of a SMAX Ticket:', 'Type here ...')

# add a button
if st.button('Predict'):
    # predict
    df = predict_top5(model = model, vectorizer = vectorizer, X_test = [title])
    
    # display the prediction
    if df is None:
        st.write("Cannot predict")
    else:
        predictions = df.iloc[0, 1:11].tolist()
        title = df.iloc[0, 0]
        # display the tile in blue and bold font and larger size
        st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title}</b></font>", unsafe_allow_html=True)
        
        # # display the predictions in green, one line per prediction
        for i in range(5):
            st.markdown(f"<font color='green'>{i+1}. {predictions[i*2]}</font>: <font color='red'>{predictions[i*2+1]*100:.2f}%</font>", unsafe_allow_html=True)
            # st.write(f"{i+1}. {prediction}")

        # st.write(f"Title Cleaned: {title}")
        # st.write(f"Product Name should be: {predictions}")   
        