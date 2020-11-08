from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from enum import Enum
import re
import textract
import PyPDF2
from data.DataManager import DataManager

"""
    NLTK NEEDS THESE LIBRARY
    download('stopwords')
    download('punkt')
"""

class Language(Enum):
    ENGLISH = 0
    BAHASA = 1

def lemmatize(sentence):
    # Remove newline symbol
    words = sentence.replace('\\n','').split()
    cleaned = []
    for d in words:
        # Remove Unicode
        w = re.sub(r'[^\x00-\x7F]+', ' ', d)
        # Remove Mentions
        w = re.sub(r'@\w+', ' ', w)
        # Lowercase the document
        w = w.lower()
        # Remove punctuations
        w = re.sub(r'[\'\"]', ' ', w)
        # Remove symbol
        w = re.sub(r'[~`!@#$\%^&*\(\)-_+=\{\}\[\];:<>,.?/\\\|]+', ' ', w)
        # Lowercase the numbers
        w = re.sub(r'[0-9]', ' ', w)
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


def word_count(sentence):
    words = sentence.split()
    result = {}
    for w in words:
        if w in result.keys():
            result[w] += 1
        else:
            result[w] = 1
    norm = 0
    for k in result.keys():
        norm += (result[k]*result[k])
    norm **= 0.5
    result["_norm"] = norm
    result["_total"] = len(words)
    return result

def merge_sort(D: list, a:int, b:int):
    if(b-a != 1):
        mid = (a+b)//2
        merge_sort(D, a, mid)
        merge_sort(D, mid, b)
        temp = []
        P1 = a
        P2 = mid
        while(P1<mid and P2<b):
            if(D[P1] <= D[P2]):
                temp.append(D[P1])
                P1 = P1+1
            else:
                temp.append(D[P2])
                P2 = P2+1
        while(P1<mid):
            temp.append(D[P1])
            P1 = P1+1
        while(P2<b):
            temp.append(D[P2])
            P2 = P2+1
        for i in range (b-a):
            D[a+i] = temp[i]
    


class DocumentManager():

    def __init__(self):
        self.__document_path = './documents/'
        self.__document_bahasa = self.__document_path + "bahasa/"
        self.__document_english = self.__document_path + "english/"
        self.__data_manager = DataManager('documents')
        self.__data_manager.init()

    def extract(self, language, filename: str) -> str:
        path = ""
        if (language == Language.ENGLISH):
            path = self.__document_english
        elif (language == Language.BAHASA):
            path = self.__document_bahasa
        
        if (len(path) != 0):
            ext = filename.split(".")[-1]
            output = ""
            if ext == 'pdf':
                with open(path + filename, mode='rb') as f:
                    reader = PyPDF2.PdfFileReader(f)
                    for page in reader.pages:
                        if len(output) != 0:
                            output += " "
                        output += page.extractText().encode('unicode_escape').decode('utf-8')
            elif ext == 'docx' or ext == 'pptx':
                output = textract.process(path + filename, encoding='ascii').decode('utf-8')
            return output

    def process(self, language, filename: str) -> dict:
        result = self.__data_manager.read(filename)
        if (result == None):
            extracted_text = self.extract(language, filename)
            d = word_count(naturalize(language, extracted_text))
            temp = []
            for key in d:
                temp.append([key, d[key]])
            merge_sort(temp, 0, len(temp))
            sorted = {}
            for i in range (len(temp)):
                sorted[temp[i][0]] = temp[i][1]
            self.__data_manager.write({'filename': filename, 'data': sorted})
            result = d
        return result

