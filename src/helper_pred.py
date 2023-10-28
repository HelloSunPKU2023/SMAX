from src.helper_text import quick_clean_up, final_clean_up, convert_abbrev_in_text
from src.helper_translation import translate_to_english
# from src.helper_language import detect_language_fasttext
import pandas as pd
import numpy as np

def predict_top5(model, vectorizer, X_test, pre_processed = False):
    if not pre_processed:
        X_test = [pre_process(text) for text in X_test]
    
    try:
        texts_encoded = vectorizer.transform(X_test)

        # create empty DataFrame to store the predictions
        df_predictions = pd.DataFrame(columns=['Text', 'Pred_1', 'proba_1', 'Pred_2', 'proba_2', 'Pred_3', 'proba_3', 'Pred_4', 'proba_4', 'Pred_5', 'proba_5', 'Actual'])
        
        df_predictions['Text'] = X_test
        
        # Get the probabilities for each class
        probabilities = model.predict_proba(texts_encoded)
        
        # Define the number of top classes you want
        top_classes = 5

        # Get the indices of the top k probabilities in the order from highest to lowest
        top_k_indices = np.argsort(probabilities, axis=1)[:, -top_classes:][:,::-1]
        
        # Get the corresponding labels
        labels = np.array(model.classes_)
        top_k_labels = [labels[top_indices] for top_indices in top_k_indices]
        
        # Print the top k labels with their probabilities 
        for i, (probs, labs) in enumerate(zip(probabilities, top_k_labels)):
            for j in range(top_classes):
                df_predictions.iloc[i, j*2+1] = labs[j]
                df_predictions.iloc[i, j*2+2] = probs[top_k_indices[i][j]]
        
        return df_predictions
    except:
        print('Error: Please check the input data')
        return None

def pre_process(text):
    text = quick_clean_up(text)

    text = translate_to_english(text, 'auto')
    text = convert_abbrev_in_text(text)
    # text = final_clean_up(text)

    return text

from src.helper_pred import predict_top5

def top5_accuracy_report(model, vectorizer, X_test, y_test, pre_processed=True):
    df_pred_top5 = predict_top5(model, vectorizer, X_test, pre_processed=pre_processed)

    df_pred_top5['Actual'] = y_test

    # check if Actual is in the top 1
    df_pred_top5['in_top1'] = df_pred_top5.apply(lambda x: x['Actual'] == x['Pred_1'], axis=1)
    # check if Actual is in the top 3
    df_pred_top5['in_top3'] = df_pred_top5.apply(lambda x: x['Actual'] in [x['Pred_1'], x['Pred_2'], x['Pred_3']], axis=1)
    # check if Actual is in the top 5
    df_pred_top5['in_top5'] = df_pred_top5.apply(lambda x: x['Actual'] in [x['Pred_1'], x['Pred_2'], x['Pred_3'], x['Pred_4'], x['Pred_5']], axis=1)

    accuracy_top1 = df_pred_top5['in_top1'].mean()
    accuracy_top3 = df_pred_top5['in_top3'].mean()
    accuracy_top5 = df_pred_top5['in_top5'].mean()

    print(f'Accuracy of top 1 prediction is \033[94m{accuracy_top1:.3f}\033[0m.')
    print(f'Accuracy of top 3 prediction is \033[94m{accuracy_top3:.3f}\033[0m.')
    print(f'Accuracy of top 5 prediction is \033[94m{accuracy_top5:.3f}\033[0m.')

    return df_pred_top5
