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

Put a `Title/Description of a SMAX Ticket` then click the `Predict` button. \n
There is a `94%` chance that the correct product name is in the top 3 predictions.

"""

# load the model
MODEL_1 =  'voting'
MODEL_2 =  'svc_linear'
MODEL_3 =  'logistic_regression'
MODEL_4 =  'sgc_classifier'

top_num = 3

model1 = joblib.load(f'models/model_{MODEL_1}.pkl', 'rb')
vectorizer1 = joblib.load(f'models/vectorizer_{MODEL_1}.pkl', 'rb')

model2 = joblib.load(f'models/model_{MODEL_2}.pkl', 'rb')
vectorizer2 = joblib.load(f'models/vectorizer_{MODEL_2}.pkl', 'rb')

model3 = joblib.load(f'models/model_{MODEL_3}.pkl', 'rb')
vectorizer3 = joblib.load(f'models/vectorizer_{MODEL_3}.pkl', 'rb')

model4 = joblib.load(f'models/model_{MODEL_4}.pkl', 'rb')
vectorizer4 = joblib.load(f'models/vectorizer_{MODEL_4}.pkl', 'rb')

MODEL_NNAMES = [MODEL_1, MODEL_2, MODEL_3, MODEL_4]
models = [model1, model2, model3, model4]
vectorizers = [vectorizer1, vectorizer2, vectorizer3, vectorizer4]

# add a text area
title = st.text_area('Type in the box below:', height=50)
title_cleaned = ""
# add a disclaimer
st.markdown(f"<font color='red' size=4 ><b>Disclaimer: For demonstration purposes only; predictions may be inaccurate.</b></font>", unsafe_allow_html=True)

# add a button
if st.button('Predict'):
    # check if the user has entered a title
    if title.strip() == '':
        st.write("Please enter a title or a short description of the issue.")
        st.stop()
    
    for i in range(len(models)):
        df = predict_top5(model = models[i], vectorizer = vectorizers[i], X_test = [title])
        if df is None:
            st.write(f"Cannot predict by {MODEL_NNAMES[i]} model")
        else:
            prediction = df.iloc[0, 1:11].tolist()
            
            if title_cleaned == "":
                title_cleaned = df.iloc[0, 0]
                st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title_cleaned}</b></font>", unsafe_allow_html=True)
            st.markdown(f"Predicted by: {MODEL_NNAMES[i]} model：")
            for i in range(top_num):
                if prediction[i*2+1]>0:
                    st.markdown(f"<font color='green'>{i+1}. {prediction[i*2]}</font>: <font color='red'>{prediction[i*2+1]*100:.1f}%</font>", unsafe_allow_html=True)