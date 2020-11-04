from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from enum import Enum
import re

"""
    NLTK NEEDS THESE LIBRARY
    download('stopwords')
    download('punkt')
"""

class Language(Enum):
    ENGLISH = 0
    BAHASA = 1

def lemmatize(sentence):
    words = sentence.split()
    cleaned = []
    for d in words:
        # Remove Unicode
        w = re.sub(r'[^\x00-\x7F]+', ' ', d)
        # Remove Mentions
        w = re.sub(r'@\w+', '', w)
        # Lowercase the document
        w = w.lower()
        # Remove punctuations
        w = re.sub(r'[\'\"]', ' ', w)
        w = re.sub(r'[~`!@#$\%^&*\(\)-_+=\{\}\[\];:<>,.?/\\\|]+', '', w)
        # Lowercase the numbers
        w = re.sub(r'[0-9]', '', w)
        # Remove the doubled space
        w = re.sub(r'\s{2,}', ' ', w)
        cleaned.append(w)
    output  = ""
    for w in cleaned:
        if len(output) != 0:
            output += " "
        output += w
    return output

def stem(language, sentence):
    if (language == Language.BAHASA):
        factory     = StemmerFactory()
        stemmer     = factory.create_stemmer()
        output      = stemmer.stem(sentence)
        return output
    elif (language == Language.ENGLISH):
        ps      = PorterStemmer()
        words   = word_tokenize(sentence)
        output  = ""
        for w in words:
            if len(output) != 0:
                output += " "
            output += ps.stem(w)
        return output
    else:
        return sentence

def stopword(language, sentence):
    if (language == Language.BAHASA):
        factory     = StopWordRemoverFactory()
        stopword    = factory.create_stop_word_remover()
        output      = stopword.remove(sentence)
        return output
    if (language == Language.ENGLISH):
        stopword = set(stopwords.words('english'))
        words = word_tokenize(sentence)
        filtered = [w for w in words if not w in stopword]
        output  = ""
        for w in filtered:
            if len(output) != 0:
                output += " "
            output += w
        return output


def naturalize(language, sentence):
    lemmatized = lemmatize(sentence)
    stemmed = stem(language, lemmatized)
    sw = stopword(language, stemmed)
    return sw
