import re
import pandas as pd

import nltk

# Check if 'punkt' is downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Check if 'words' is downloaded
try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')

# Check if 'stopwords' is downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

english_words = set(nltk.corpus.words.words())

# Import the stopwords corpus
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# Initialize a WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

abbreviations = {
    '1D': 'one dimensional',
    '2D': 'two dimensional',
    '3D': 'three dimensional',
    '4D': 'four dimensional',
    'ADM': 'active directory manager (ADM)',
    'API': 'application programming interface (API)',
    'AMT': 'annular mechanical total (AMT)',
    'BHA': 'bottom hole assembly (BHA)',
    'BHP': 'bottom hole pressure (BHP)',
    'BR': 'drilling',
    'CCC': 'customer care center',
    'CMZ': 'commercialization',
    'CRS': 'coordinate reference system (CRS)',
    'CAMG': 'cameron',
    # 'CO2': 'carbon dioxide',
    # 'CH4': 'methane',
    'DBTM': 'drill bit total depth measurement (DBTM)',
    'DB': 'database',
    'DCA': 'decline curve analysis (DCA)',
    'DLIS': 'digital log information standard (DLIS)',
    'DOP': 'drill off test (DOP)',
    'DDR': 'daily drilling report (DDR)',
    'EXPL': 'exploration',
    'ECP': 'electronic control panel (ECP)',
    'ECL': 'eclipse',
    'FW': 'forward',
    'FW:': 'forward',
    'FM': 'forward modeling',
    'GIS': 'geographic information system (GIS)',
    'GS_': 'geoservice',
    'GSS': 'global sourcing solution (GSS)',
    'GCP': 'google cloud platform (GCP)',
    # 'HPE': 'Hewlett Packard Enterprise (HPE)',
    'HPC': 'high performance computing (HPC)',
    'IX': 'Intersect',
    'IWC': 'integrated well construction (IWC)',
    'IA': 'InterACT',
    'IAM': 'integrated asset management (IAM)',
    'KPI': 'key performance indicator (KPI)',
    'LAS': 'log ASCII standard (LAS)',
    'LGR': 'local grid refinement (LGR)',
    'ML_': 'mud logging',
    'ML': 'machine learning',
    'MWD': 'measurement while drilling (MWD)',
    'MD': 'measured depth (MD)',
    'MC': 'mud circulation',
    'MPD': 'mud pulse density (MPD)',
    'OLGA': 'oil and gas simulator (OLGA)',
    'ODRS': 'on demand reservoir simulation (ODRS)',
    'OFM': 'oil field management (OFM)',
    'OSDU': 'open subsurface data universe (OSDU)',
    # 'OML': "",
    'PTS': 'Petrotechnical Suite (PTS)',
    'PSUITE': 'Petrotechnical Suite (PTS)',
    'POC': 'proof of concept',
    'PAM': 'privileged access manager (PAM)',
    'PI': 'production index (PI)',
    'P4D': 'platform for development',
    'PROD': 'production tenant',
    'PVT': 'pressure volume temperature (PVT)',
    'PSFO': 'ProSource',
    'QC': 'quality control (QC)',
    'QI': 'quantitative interpretation (QI)',
    'RE:': 'regarding',
    'ROP5': "rate of penetration in 5-minute intervals (ROP5)",
    'RDP': 'remote desktop protocol (RDP)',
    'RTDC': 'realtime drilling center (RTDC)',
    'RT': 'realtime',
    'RPT': 'remote project transfer (RPT)',
    'ROPDSTEP': 'rate of penetration while drilling stepped intervals (ROPDSTEP)',
    'RTDS': 'real time drilling system',
    'RSDH': 'rig site data hub (RSDH)',
    'ROP': 'rate of penetration (ROP)',
    'RTC': 'real time drilling center (RTC)',
    'SLI': 'service level indicator (SLI)',
    'SLA': 'service level agreement (SLA)',
    'SSV': 'semisubmersible vessel (SSV)',
    'SEGY': 'standard exchange of geophysical data (SEGY)',
    'SWT': 'seismic well tie (SWT)',
    'SW': 'shallow water',
    'SIM': 'simulation',
    # 'SRD': "",
    'TL': 'Techlog',
    'TDR': 'time domain reflectometry (TDR)',
    'TVD': 'true vertical depth (TVD)',
    'TWT': 'two way time (TWT)',
    'U&O': 'uncertainty and optimization ',
    # 'SQL': 'structured query language (SQL)',
    'VFP': 'virtual flowmeter prediction (VFP)',
    'VSP': 'vertical seismic profile (VSP)',
    'VOL': 'volume',
    'VM': 'virtual machine (VM)',
    'VDR': 'virtual data room (VDR)',
    'WF': 'workflow',
    'WCS': 'well construction service (WCS)',
    'WSW': 'well site workstation (WSW)',
    'WITS': 'wellsite information transfer standard (WITS)',
    'WITSML': 'wellsite information transfer standard markup language (WITSML)'
}

noise_stopwords = ['co', 'cmz',
                'dp', 
                'en', 'ext',  
                'fwd', 
                're:', 're-',
                'helpdesk', 'hi', 'help', 'ha', 'hello', 
                'internal',
                'message', 'msg',
                'please', 'pd', 'ped', 
                'request', 'req', 
                'bubblesupport', 'sh', 
                'ticket', 'team', 'tr', 
                'urgent'
                ]

def remove_noise_stopwords(text):
    """
    Removes noise stopwords from a given string.
    """
    tokens = text.split()
    tokens = [token for token in tokens if token.lower() not in noise_stopwords]
    text = ' '.join(tokens)
    return text

company_names = ['eni', 'petronas', 'tpao', 'slb', 'cvx', 'equinor', 'omv', 'int', 'ecuador', 'ongc', 'bp', 'bsp', 'spic', 'chevron', "mpcl", 'schlumberger', 'santos', 'woodside']
GeoUnits = ['usl', 'sca', 'slr', 'ksa', 'ing', 'eur', 'eag', 'apg', 'chg']
Country_name = ['mexico', 'saudi', 'uk', 'algeria', 'china', 'malaysia', 'thailand']

additional_stopwords = ['add', 'able', 'adding', 'available', 'ask',
                        'bug', 
                        'commercialization', 'country', 'customer', 'create',  'collocated',
                        'department', 'discussion',
                        'error', 'errors', 
                        'fwd', 'failed',
                        'how', 'however',
                        'need', 'new', 'no',
                        'problem',
                        'question',
                        'result',  'running', 'run', 'rerun', 'required',
                        'support', 'start', 'starting', 'service',
                        'unable','use', 'using', 'updated', 'update', 
                        'your', 'i'
                        ]

# Now you can access the English stopwords
english_stopwords = stopwords.words('english')
english_stopwords.extend(additional_stopwords)
english_stopwords.extend(company_names)
english_stopwords.extend(GeoUnits)
english_stopwords.extend(Country_name)

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
    pattern = re.compile(r'[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}')
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

import string
def remove_punctuation(text):
    """
    Removes punctuation from a given string, excluding "-" and "&".
    """
    table=str.maketrans('','', string.punctuation)
    return text.translate(table)

def remove_brackets_content(text):
    """
    Removes content inside square brackets or angle brackets along with the brackets themselves.
    """
    pattern = r'\[.*?\]|'
    return re.sub(pattern, '', text)

exclude_words = ['1d', '2d', '3d', 'co2', 'nh3', 'ch4', 't1', 't2']

def remove_word_has_alpha_and_digit(text, exclude_words=exclude_words):
    """
    Removes words that contain both alphabets and digits from a given string.
    """
    #split the words by '_' first
    text = text.replace('_', ' ')
    pattern = r'\b\w*(?:[a-zA-Z]+-?\d+|\d+-?[a-zA-Z]+)\w*\b'
    words = re.findall(pattern, text)
    words = [word for word in words if word.lower() not in exclude_words]
    for word in words:
        text = text.replace(word, '')
    return text

def remove_digits(text):
    """
    Removes digits only words from a given string.
    """
    pattern = r'\b\d+\b'
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

# Thanks to https://www.kaggle.com/rftexas/text-only-kfold-bert
def convert_abbrev(word):
    return abbreviations[word.upper()] if word.upper() in abbreviations.keys() else word

# Thanks to https://www.kaggle.com/rftexas/text-only-kfold-bert

from nltk.tokenize import word_tokenize
def convert_abbrev_in_text(text):
    text = text.replace('U&O', ' uncertainty and optimization')
    tokens = word_tokenize(text)
    tokens = [convert_abbrev(word) for word in tokens]
    text = ' '.join(tokens)
    return text

special_characters = ['"', '#', '$', '%', "'", '(', ')', '[', ']', '{', '}','*', '+', '-', '/', '<', '>', '=', '|', ':', '~', '`', '@', '^']

def remove_special_characters(text, special_characters=special_characters):
    """
    Removes special characters from a given string.
    """
    for character in special_characters:
        text = text.replace(character, ' ')
    return text
def quick_clean_up(text):
    """
    Performs a quick clean on a given string.
    """
    # text = keep_text_after_last_pipe(text)
    text = add_space_between_cjk_and_non_cjk(text)
    # text = add_space_between_capitalized_words(text)
    # text = remove_brackets_content(text)
    text = remove_uuid(text)
    text = remove_email(text)
    
    text = remove_date(text)
    text = remove_time(text)
    
    text = remove_word_has_alpha_and_digit(text)
    text = remove_underline(text)
    
    text = remove_noise_stopwords(text)
    text = remove_special_characters(text)
    text = remove_noise_stopwords(text)
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

def extract_keywords(text):
    """
    Extracts keywords from a given string.
    """
    if isinstance(text, str):
        # Remove numbers and special characters
        # text = re.sub(r'[^a-zA-Z\s]', ' ', text)

        # Convert to lowercase
        text = text.lower()

        # text = convert_abbrev_in_text(text)
        # text = remove_word_has_alpha_and_digit(text)
        text = remove_punctuation(text)
        
        tokens = nltk.word_tokenize(text)

        #Remove whitespace and empty tokens
        tokens = [token.strip() for token in tokens if token.strip()]

        #Remove stopwords   
        tokens = [word for word in tokens if word.lower() not in additional_stopwords]

        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        
        #stem the tokens
        # tokens = [stemmer.stem(word) for word in tokens]

        #remove duplicated words
        tokens = list(set(tokens))
        
        # #sort the tokens alphabetically
        # tokens = sorted(tokens)
        
        # Join the tokens back into a string
        text = ' '.join(tokens)
        
        if count_words(text)<1 or len(text.strip())==0:
            text = pd.NA
            
    return text

def enhance_title(text):
        # Continue with preprocessing using the translated title        

    if isinstance(text, str):
        text = remove_punctuation(text)
        text = convert_abbrev_in_text(text)        
        tokens = nltk.word_tokenize(text)
        tokens = [word for word in tokens if word.lower() not in english_stopwords]            
        text = ' '.join(tokens)
        tokens = [token.strip() for token in tokens if token.strip()]

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

# list top n most frequent words in the Title_translated column
from sklearn.feature_extraction.text import CountVectorizer

def get_top_n_words(corpus, n=100):
    vec = CountVectorizer(stop_words = 'english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]