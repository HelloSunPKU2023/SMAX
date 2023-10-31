# create a streamlit app to take a user input and return a prediction

import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

from src.helper_pred import predict_top5
"""
# Guess what product are you talking about...

Put a `SMAX ticket Title or Description` then click the `Guess` button. \n
`95%` chance of top 3 product match ...

"""

# load the model
MODEL_1 =  'svc_linear'
# Configuration: Classify top 25 products; Text column: Title_Translated, Title words length: (4, 15);
# Records/product caped at 6000; Class weight factor: -1; class weight power: 0.5.
# # Accuracy of top 1 prediction is 0.819.
# Accuracy of top 3 prediction is 0.952.
# Accuracy of top 5 prediction is 0.978.

MODEL_2 =  'logistic_regression'
# Configuration: Classify top 25 products; Text column: Title_Translated, Title words length: (4, 15);
# Records/product caped at 6000; Class weight factor: -1; class weight power: 0.5.
# Accuracy of top 1 prediction is 0.819.
# Accuracy of top 3 prediction is 0.951.
# Accuracy of top 5 prediction is 0.974.

MODEL_3 =  'sgc_classifier'
# Configuration: Classify top 25 products; Text column: Title_Translated, Title words length: (4, 15);
# Records/product caped at 6000; Class weight factor: -1; class weight power: 0.5.
# Accuracy of top 1 prediction is 0.828.
# Accuracy of top 3 prediction is 0.947.
# Accuracy of top 5 prediction is 0.972.

top_num = 3
other_products = [
    'VISAGE', 'eSearch', 'Drillbench', 'Engine Ecosystem, Sim Cluster Mgr.', 
    'MEPO', 'FDPlan', 'Enterprise Data Solution', 'Flaresim', 'Developer Portal', 
    'Cameron Supplier Portal', 'Drilling Insights'
    ]

@st.cache_resource
def load_models(): 
    model1 = joblib.load(f'models/model_{MODEL_1}.pkl', 'rb')
    vectorizer1 = joblib.load(f'models/vectorizer_{MODEL_1}.pkl', 'rb')

    model2 = joblib.load(f'models/model_{MODEL_2}.pkl', 'rb')
    vectorizer2 = joblib.load(f'models/vectorizer_{MODEL_2}.pkl', 'rb')

    model3 = joblib.load(f'models/model_{MODEL_3}.pkl', 'rb')
    vectorizer3 = joblib.load(f'models/vectorizer_{MODEL_3}.pkl', 'rb')

    # model4 = joblib.load(f'models/model_{MODEL_4}.pkl', 'rb')
    # vectorizer4 = joblib.load(f'models/vectorizer_{MODEL_4}.pkl', 'rb')

    MODEL_NNAMES = [MODEL_1, MODEL_2, MODEL_3]
    models = [model1, model2, model3]
    vectorizers = [vectorizer1, vectorizer2, vectorizer3]
    return MODEL_NNAMES, models, vectorizers

# load the models into the cache
MODEL_NNAMES, models, vectorizers = load_models()

# add a text area
title = st.text_area('SMAX ticket Title or Description:', height=50)
title_cleaned = ""
# add a disclaimer
st.markdown(f"<font color='red' size=3 ><b>Disclaimer: For demonstration purposes only; predictions may be inaccurate.</b></font>", unsafe_allow_html=True)

# add a button
if st.button('Guess'):
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
            st.markdown(f"Predicted by: {MODEL_NNAMES[i]} model")
            for i in range(top_num):
                if prediction[i*2+1]>0:
                    st.markdown(f"<font color='green'>{i+1}. {prediction[i*2]}</font>: <font color='red'>{prediction[i*2+1]*100:.1f}%</font>", unsafe_allow_html=True)
    st.markdown(f"<font color='green' size=3 ><b>Other Products (not in top 25)</b></font>: <font color='white' size=3 >{', '.join(other_products)}</font>", unsafe_allow_html=True)