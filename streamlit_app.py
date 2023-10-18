# create a streamlit app to take a user input and return a prediction

import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

# from src.helper_pred import predict_top5
"""
# Welcome to Product Name Predictor!

Put a `Title of a SMAX Ticket` then click the `Predict` button to get the top 5 predicted product names.

"""
model = joblib.load('models/model_logistic_regression.pkl', 'rb')
vectorizer = joblib.load('models/vectorizer_logistic_regression.pkl', 'rb')

# add a text area
title = st.text_area('Title of a SMAX Ticket:', 'Type here ...')

# # add a button
# if st.button('Predict'):
#     # load the model

    
#     # predict
#     df = predict_top5(model = model, vectorizer = vectorizer, X_test = [title])
    
#     # display the prediction
#     if df is None:
#         st.write("Cannot predict")
#     else:
#         predictions = df.iloc[0, 1:11].tolist()
#         title = df.iloc[0, 0]
#         st.write(f"Title Cleaned: {title}")
#         st.write(f"Product Name: {predictions}")
        