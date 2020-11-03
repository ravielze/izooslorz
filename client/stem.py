from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from nltk import download
from enum import Enum

download()

class Language(Enum):
    ENGLISH = 0
    BAHASA = 1

def stem(language, sentence):
    if (language == Language.BAHASA):
        factory     = StemmerFactory()
        stemmer     = factory.create_stemmer()
        output      = stemmer.stem(sentence)
        return output
    elif (language == Language.ENGLISH):
        ps = PorterStemmer()
        # TODO
        return ""
    else:
        return sentence

print(stem(Language.ENGLISH, "Programers program with programing languages"))