# create a streamlit app to take a user input and return a prediction

import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

from src.helper_pred import predict_top5
"""
# Predict Product by Ticket Title

Put a `Title of a SMAX Ticket` then click the `Predict` button. \n
There is a `95%` chance that the correct product name is in the top 5 predictions.

"""

# load the model
MODEL_2 =  'sgc_classifier'
MODEL_1 =  'logistic_regression'
MODEL_3 = 'multinomialNB'

model1 = joblib.load(f'models/model_{MODEL_1}.pkl', 'rb')
vectorizer1 = joblib.load(f'models/vectorizer_{MODEL_1}.pkl', 'rb')

model2 = joblib.load(f'models/model_{MODEL_2}.pkl', 'rb')
vectorizer2 = joblib.load(f'models/vectorizer_{MODEL_2}.pkl', 'rb')

model3 = joblib.load(f'models/model_{MODEL_3}.pkl', 'rb')
vectorizer3 = joblib.load(f'models/vectorizer_{MODEL_3}.pkl', 'rb')

# add a text area
title = st.text_area('Title of a SMAX Ticket (type in the box below):', '')

# add a button
if st.button('Predict'):
    # check if the user has entered a title
    if title.strip() == '':
        st.write("Please enter a title")
        st.stop()
    
    # Model 1
    # predict
    df1 = predict_top5(model = model1, vectorizer = vectorizer1, X_test = [title])
    # display the prediction
    if df1 is None:
        st.write(f"Cannot predict by{MODEL_1} model")
    else:
        predictions1 = df1.iloc[0, 1:11].tolist()
        title = df1.iloc[0, 0]
        # display the tile in blue and bold font and larger size
        st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title}</b></font>", unsafe_allow_html=True)
        st.markdown(f"Predicted by: {MODEL_1} model")
        # # display the predictions in green, one line per prediction
        for i in range(5):
            if predictions1[i*2+1]>0:
                st.markdown(f"<font color='green'>{i+1}. {predictions1[i*2]}</font>: <font color='red'>{predictions1[i*2+1]*100:.4f}%</font>", unsafe_allow_html=True)
    
    # Model 2
    st.markdown(f"Predicted by: {MODEL_2} model")
    # predict
    df2 = predict_top5(model = model2, vectorizer = vectorizer2, X_test = [title])
    # display the prediction
    if df2 is None:
        st.write(f"Cannot predict by {MODEL_2} model")
    else:
        predictions2 = df2.iloc[0, 1:11].tolist()
        if df1 is None:
            title = df2.iloc[0, 0]
            st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title}</b></font>", unsafe_allow_html=True)
        for i in range(5):
            if predictions2[i*2+1]>0:
                st.markdown(f"<font color='green'>{i+1}. {predictions2[i*2]}</font>: <font color='red'>{predictions2[i*2+1]*100:.4f}%</font>", unsafe_allow_html=True)
                
    # Model 3
    st.markdown(f"Predicted by: {MODEL_3} model")
    # predict
    df3 = predict_top5(model = model3, vectorizer = vectorizer3, X_test = [title])
    # display the prediction
    if df3 is None:
        st.write(f"Cannot predict by {MODEL_3} model")
    else:
        predictions2 = df3.iloc[0, 1:11].tolist()
        if df1 is None:
            title = df3.iloc[0, 0]
            st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title}</b></font>", unsafe_allow_html=True)
        for i in range(5):
            if predictions3[i*2+1]>0:
                st.markdown(f"<font color='green'>{i+1}. {predictions3[i*2]}</font>: <font color='red'>{predictions3[i*2+1]*100:.4f}%</font>", unsafe_allow_html=True)
        