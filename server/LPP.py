from nltk import download
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import re

class LPP():
    """LPP stands for Language Pre Processing."""
    
    def __init__(self):
        download('stopwords')
        download('punkt')

    def arraytostring(self, arr: list) -> str:
        """To convert an array to a string"""
        separator = ' '
        return separator.join(arr)

    def lemmatize(self, sentence: str) -> str:
        """ To clean unused characters in a sentence."""
        words = sentence.replace('\\n','').split()
        cleaned = []
        for d in words:
            w = re.sub(r'[^\x00-\x7F]+', ' ', d)
            w = re.sub(r'@\w+', ' ', w)
            w = w.lower()
            w = re.sub(r'[\'\"]', ' ', w)
            w = re.sub(r'[~`!@#$\%^&*\(\)-_+=\{\}\[\];:<>,.?/\\\|]+', ' ', w)
            w = re.sub(r'[0-9]', ' ', w)
            w = re.sub(r'\s{2,}', ' ', w)

            cleaned.append(w.strip())
        return self.arraytostring(cleaned)

    def stem(self, is_bahasa_indonesia: bool, sentence: str) -> str:
        """To convert words to the basic form."""
        if (is_bahasa_indonesia):
            factory     = StemmerFactory()
            stemmer     = factory.create_stemmer()
            output      = stemmer.stem(sentence)
            return output
        else:
            ps      = PorterStemmer()
            words   = word_tokenize(sentence)
            stemmed = []
            for w in words:
                stemmed.append(ps.stem(w))
            return self.arraytostring(stemmed)

    def stopword(self, is_bahasa_indonesia: bool, sentence: str) -> str:
        """To remove unused words."""
        if (is_bahasa_indonesia):
            factory     = StopWordRemoverFactory()
            stopword    = factory.create_stop_word_remover()
            output      = stopword.remove(sentence)
            return output
        else:
            stopword = set(stopwords.words('english'))
            words = word_tokenize(sentence)
            filtered = [w for w in words if not w in stopword]
            f = []
            for w in filtered:
                f.append(w)
            return self.arraytostring(f)
    
    def naturalize(self, is_bahasa_indonesia: bool, sentence: str) -> str:
        """Process lemmatization, stemming word, and remove stop words."""
        lemmatized = self.lemmatize(sentence)
        stemmed = self.stem(is_bahasa_indonesia, lemmatized)
        sw = self.stopword(is_bahasa_indonesia, stemmed)
        return sw