import re
import fasttext
from langdetect import detect, detect_langs

fasttext.FastText.eprint = lambda x: None
model_path = "/Users/Haitao/fasttext/lid.176.bin"
model = fasttext.load_model(model_path)
LANGUAGE_DETECTION_THRESHOLD = 0.45

def is_fasttext_installed():
    """
    The `is_fasttext_installed` function is used to check if the `fasttext` library is installed.
    """
    try:
        import fasttext
        # print location of fasttext module
        print(fasttext.__file__)
        return True
    except ImportError:
        return False

def is_utf8(text):
    """
    The `is_text_utf8` function is used to determine if a given text is encoded in UTF-8 format.
    
    :param text: The text parameter is the input text that you want to check the encoding of
    """
    if isinstance(text, bytes) or text is None:
        return False
    try:
        text.encode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
    

# Function to detect language 
# with confidence level = 45%
# fasttext performance is better than the other solutions for short text (ref: https://medium.com/besedo-engineering/language-identification-for-very-short-texts-a-review-c9f2756773ad
def detect_language_fasttext(text, threshold=LANGUAGE_DETECTION_THRESHOLD):
    """
    The function `detect_language_fasttext` uses a pre-trained model to predict the language of a given
    text, removing numbers and special characters before making the prediction.
    
    :param text: The `text` parameter is the input text that you want to detect the language of. It
    should be a string
    :param threshold: The `threshold` parameter is used to determine the confidence level required for a
    language to be detected. If the predicted confidence level for a language is below the threshold,
    the function will return 'unknown' instead of the detected language
    :return: The function `detect_language_fasttext` returns the detected language of the input text. If
    the language cannot be detected or if there is an error, it returns 'unknown'.
    """
    # Remove numbers and special characters
    if not is_utf8(text) or len(text)==0 or text is None:
        return 'unknown'
    
    text = text.lower()
    
    # Detect korean characters
    if re.search(r'[\uac00-\ud7af]+', text):
        return 'ko'

    # Detect japanese Hiragana and Katakana characters
    if re.search(r'[\u3040-\u309f\u30a0-\u30ff]+', text):
            return 'ja'
    
    # Detect chinese characters both simplified and traditional
    if re.search(r'[\u4e00-\u9fff]+', text):
        return 'zh'
        
    
    try:
        lang_detected = model.predict(text, k=1, threshold=threshold)
        return lang_detected[0][0].replace('__label__', '')
    except Exception as e:
        # print("An error occurred:", e)
        return 'unknown'
    


def detect_language_langdetect(text, threshold=LANGUAGE_DETECTION_THRESHOLD):
    """
    The `detect_language_langdetect` function is used to detect the language of a given text using the
    langdetect library, with an optional threshold parameter.
    
    :param text: The text parameter is the input text that you want to detect the language of
    :param threshold: The threshold parameter is used to determine the minimum confidence level required
    for a language to be considered as the detected language. If the confidence level of the detected
    language is below the threshold, the function will return None
    """
    if not is_utf8(text) or len(text)==0 or text is None:
        return 'unknown'
    
    text = text.lower()

    # Detect korean characters
    if re.search(r'[\uac00-\ud7af]+', text):
        return 'ko'

    # Detect japanese Hiragana and Katakana characters
    if re.search(r'[\u3040-\u309f\u30a0-\u30ff]+', text):
            return 'ja'
    
    # Detect chinese characters both simplified and traditional
    if re.search(r'[\u4e00-\u9fff]+', text):
        return 'zh'
        

    
    # Detect the languages and their confidence scores
    langs = detect_langs(text)


    # Check if the top detected language's confidence score is above the threshold
    if langs[0].prob > threshold:
        detected_language = langs[0].lang
        confidence = langs[0].prob
    else:
        detected_language = "unknown"
        confidence = 0.0
    return detected_language
