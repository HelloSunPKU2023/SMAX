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
There is a `90%` chance that the correct product name is in the top 3 predictions.

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
title = st.text_area('Title/Description of a SMAX Ticket (type in the box below):', '')
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
            for i in range(top_num):
                if prediction[i*2+1]>0:
                    st.markdown(f"<font color='green'>{i+1}. {prediction[i*2]}</font>: <font color='red'>{prediction[i*2+1]*100:.4f}%</font>", unsafe_allow_html=True)
    # # Model 1
    # # predict
    # df1 = predict_top5(model = model1, vectorizer = vectorizer1, X_test = [title])
    # # display the prediction
    # if df1 is None:
    #     st.write(f"Cannot predict by{MODEL_1} model")
    # else:
    #     predictions1 = df1.iloc[0, 1:11].tolist()
    #     title = df1.iloc[0, 0]
    #     # display the tile in blue and bold font and larger size
    #     st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title}</b></font>", unsafe_allow_html=True)
    #     st.markdown(f"Predicted by: {MODEL_1} model")
    #     # # display the predictions in green, one line per prediction
    #     for i in range(top_num):
    #         if predictions1[i*2+1]>0:
    #             st.markdown(f"<font color='green'>{i+1}. {predictions1[i*2]}</font>: <font color='red'>{predictions1[i*2+1]*100:.4f}%</font>", unsafe_allow_html=True)
    
    # # Model 2
    # st.markdown(f"Predicted by: {MODEL_2} model")
    # # predict
    # df2 = predict_top5(model = model2, vectorizer = vectorizer2, X_test = [title])
    # # display the prediction
    # if df2 is None:
    #     st.write(f"Cannot predict by {MODEL_2} model")
    # else:
    #     predictions2 = df2.iloc[0, 1:11].tolist()
    #     if df1 is None:
    #         title = df2.iloc[0, 0]
    #         st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title}</b></font>", unsafe_allow_html=True)
    #     for i in range(top_num):
    #         if predictions2[i*2+1]>0:
    #             st.markdown(f"<font color='green'>{i+1}. {predictions2[i*2]}</font>: <font color='red'>{predictions2[i*2+1]*100:.4f}%</font>", unsafe_allow_html=True)
                
    
    # # Model 3
    # st.markdown(f"Predicted by: {MODEL_3} model")
    # # predict
    # df3 = predict_top5(model = model3, vectorizer = vectorizer3, X_test = [title])
    # # display the prediction
    # if df3 is None:
    #     st.write(f"Cannot predict by {MODEL_3} model")
    # else:
    #     predictions3 = df3.iloc[0, 1:11].tolist()
    #     if df1 is None:
    #         title = df3.iloc[0, 0]
    #         st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title}</b></font>", unsafe_allow_html=True)
    #     for i in range(top_num):
    #         if predictions3[i*2+1]>0:
    #             st.markdown(f"<font color='green'>{i+1}. {predictions3[i*2]}</font>: <font color='red'>{predictions3[i*2+1]*100:.4f}%</font>", unsafe_allow_html=True)
    
    # # Model 4
    # st.markdown(f"Predicted by: {MODEL_4} model")
    # # predict
    # df4 = predict_top5(model = model4, vectorizer = vectorizer4, X_test = [title])
    # # display the prediction
    # if df4 is None:
    #     st.write(f"Cannot predict by {MODEL_4} model")
    # else:
    #     predictions4 = df4.iloc[0, 1:11].tolist()
    #     if df1 is None:
    #         title = df4.iloc[0, 0]
    #         st.markdown(f"Title cleaned: <font color='blue' size=5 ><b>{title}</b></font>", unsafe_allow_html=True)
    #     for i in range(top_num):
    #         if predictions4[i*2+1]>0:
    #             st.markdown(f"<font color='green'>{i+1}. {predictions4[i*2]}</font>: <font color='red'>{predictions4[i*2+1]*100:.4f}%</font>", unsafe_allow_html=True)