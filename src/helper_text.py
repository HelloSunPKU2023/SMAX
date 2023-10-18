import re
import nltk
import pandas as pd
# nltk.download('words')
english_words = set(nltk.corpus.words.words())

# Import the stopwords corpus
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# Initialize a WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Now you can access the English stopwords
english_stopwords = stopwords.words('english')

additional_stopwords = ['bug', 
                        'country', 'customer', 'client','crush', 'case',
                        # 'data',
                        'error', 'ext', 'external',
                        'field', 'failed', 'fwd',
                        'helpdesk', 'hi', 'help',
                        'issue', 'id',
                        'message', 'msg',
                        'need',
                        'project', 'problem', 'please', 'phone',
                        'question',
                        'request', 'result', 'run', 'req',
                        'software', 'support',
                        'ticket', 'team',
                        'urgent', 'unable',
                        'warning'
                        'log',
                        # 'window',
                        'new',
                        'time',
                        'map',
                        'user',
                        'setting',
                        'create',
                        'using',
                        'report',
                        'version',
                        'work'
                        ]
english_stopwords.extend(additional_stopwords)
# print(english_stopwords)

# Initialize a Porter Stemmer
stemmer = PorterStemmer()
## Initialize a WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

def add_space_between_cjk_and_non_cjk(text):
    """
    The function adds a space between CJK (Chinese, Japanese, and Korean) characters and non-CJK
    characters in a given text.
    
    :param text: A string containing a mixture of CJK (Chinese, Japanese, Korean) characters and non-CJK
    characters
    """
    # Define a regular expression pattern to match CJK characters
    cjk_pattern = r'([\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]+)'
    white_space_pattern=r'\s+'
        
    # Use re.sub() to insert a space between CJK and non-CJK characters
    modified_text = re.sub(cjk_pattern, r' \1 ', text)
    modified_text = re.sub(white_space_pattern, ' ', modified_text).strip()
    return modified_text

# function to add space between connected capitalized words in a given string, such as "MobileNumberChange" -> "Mobile Number Change"
def add_space_between_capitalized_words(text):
    """
    The function adds a space between capitalized words in a given text.
    
    :param text: A string containing a mixture of capitalized words and non-capitalized words
    """
    # Define a regular expression pattern to match capitalized words
    pattern = r'([A-Z][a-z]+)'
    white_space_pattern=r'\s+'
        
    # Use re.sub() to insert a space between capitalized words
    modified_text = re.sub(pattern, r' \1 ', text)
    modified_text = re.sub(white_space_pattern, ' ', modified_text).strip()
    return modified_text

def remove_email(text):
    """
    Removes email addresses from a given string.
    """
    pattern = r'\S+@\S+'
    return re.sub(pattern, '', text)

def remove_uuid(text):
    """
    Removes UUIDs from a given string.
    """
    pattern = re.compile('[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}')
    return pattern.sub('', text)

def remove_date(text):
    """
    Removes date from a given string.
    """
    pattern = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
    return re.sub(pattern, '', text)

def remove_time(text):
    """
    Removes time from a given string.
    """
    pattern = r'\d{1,2}:\d{1,2}(:\d{1,2})?\s?(AM|PM|am|pm)?'
    return re.sub(pattern, '', text)

def remove_whitespace(text):
    """
    Removes whitespace from a given string.
    """
    pattern = r'^\s+|\s+$|\s+(?=\s)'
    return re.sub(pattern, '', text)

def remove_punctuation(text):
    """
    Removes punctuation from a given string, excluding "-" and "&".
    """
    pattern = r'[^\w\s\&|]'
    return re.sub(pattern, ' ', text)

def remove_brackets_content(text):
    """
    Removes content inside square brackets or angle brackets along with the brackets themselves.
    """
    pattern = r'\[.*?\]|'
    return re.sub(pattern, '', text)

exclude_words = ['1D', '2D', '3D', 'CO2', 'NH3', 'CH4', 'T1', 'T2']

def remove_word_has_alpha_and_digit(text, exclude_words=exclude_words):
    """
    Removes words that contain both alphabets and digits from a given string.
    """
    #split the words by '_' first
    text = text.replace('_', ' ')
    pattern = r'\b\w*(?:[a-zA-Z]+-?\d+|\d+-?[a-zA-Z]+)\w*\b'
    words = re.findall(pattern, text)
    words = [word for word in words if word not in exclude_words]
    for word in words:
        text = text.replace(word, '')
    return text

def remove_digits(text):
    """
    Removes digits from a given string.
    """
    pattern = r'\d+'
    return re.sub(pattern, '', text)

def remove_underline(text):
    """
    Removes underline from a given string.
    """
    pattern = r'_+'
    return re.sub(pattern, ' ', text)

def keep_text_after_last_pipe(text):
    """
    Keeps the text after the last '|' character in a given string.
    """
    if '|' in text:
        return text.split('|')[-1].strip()
    else:
        return text.strip()

    
def quick_clean_up(text):
    """
    Performs a quick clean on a given string.
    """
    # text = keep_text_after_last_pipe(text)
    text = add_space_between_cjk_and_non_cjk(text)
    text = add_space_between_capitalized_words(text)
    # text = remove_brackets_content(text)
    text = remove_email(text)
    text = remove_uuid(text)
    text = remove_date(text)
    text = remove_time(text)
    text = remove_word_has_alpha_and_digit(text)
    text = remove_punctuation(text)
    text = remove_underline(text)
    text = remove_digits(text)
    text = remove_whitespace(text)
    
    text = text.strip()
    if text == "":
        text = None
    return text

def count_words(text):
    # Define a regular expression pattern for words
    word_pattern = r"\b\w+\b"
    
    if text == None:
        text = ""
        
    # Find all matching words in the text
    words = re.findall(word_pattern, text)
    # Count the number of words
    return len(words)



def final_clean_up(text):
        # Continue with preprocessing using the translated title        

    if isinstance(text, str):
        # Remove numbers and special characters
        # text = re.sub(r'[^a-zA-Z\s]', ' ', text)

        # Convert to lowercase
        text = text.lower()

        tokens = nltk.word_tokenize(text)

        #Remove whitespace and empty tokens
        tokens = [token.strip() for token in tokens if token.strip()]

        #Remove stopwords   
        tokens = [word for word in tokens if word not in english_stopwords and len(word)>1]

        tokens = [lemmatizer.lemmatize(word) for word in tokens]


        # Join the tokens back into a string
        text = ' '.join(tokens)
        
        if count_words(text)<1 or len(text.strip())==0:
            text = pd.NA
            
    return text

def extract_abbr(texts):
    """
    Extracts abbreviations from a given list of texts.
    """
    abbrs = []
    for text in texts:
        if isinstance(text, str):
            pattern = r'\b[A-Z]+\b'
            abbr = re.findall(pattern, text)
            abbrs.extend(abbr)
    
    
    # remove english words
    abbrs = [abbr for abbr in abbrs if abbr.lower() not in english_words]

    # count the number of occurrences of each abbreviation and sort them by the occurrence descendingly and alphabetically
    abbrs = sorted([(abbr, abbrs.count(abbr)) for abbr in set(abbrs)], key=lambda x: x[0])
    
    return abbrs
