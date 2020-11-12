from Data import Data
from DM import DM
from LPP import LPP
from BDIter import biiter
import math

"""TF-IDF stands for Term Frequency and Inverse Document Frequency.
    Source: https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/"""

class TF():

    def __init__(self, docmanager: DM, lpp: LPP):
        self.__dmanager = Data('tf', ['filename', 'language', 'term', 'tf'])
        self.__docmanager = docmanager
        self.__lpp = lpp
        self.__cache = (str('filename.empty'), biiter([]))

    def query(self, is_bahasa_indonesia: bool, query: str) -> dict:
        content = self.__lpp.naturalize(is_bahasa_indonesia, query)
        if (len(content) == 0):
            return {}
        
        result          = {}
        words           = content.split()
        doc_length      = len(words)
        unique_words    = set(words)

        for w in unique_words:
            tf          = float(words.count(w))/float(doc_length)
            result[w]   = tf
        return result

    def refresh(self, is_bahasa_indonesia: bool):
        lang = 'bahasa' if (is_bahasa_indonesia) else 'english'
        files = self.__docmanager.getDocuments(is_bahasa_indonesia)

        for f in files:
            content         = self.__docmanager.find(is_bahasa_indonesia, f)

            if (len(content) == 0):
                continue

            words           = content.split()
            doc_length      = len(words)
            unique_words    = set(words)

            for w in unique_words:
                tf          = float(words.count(w))/float(doc_length)
                
                self.__dmanager.writenl({'filename': f, 'language': lang, 'term': w, 'tf': tf})

    def find(self, filename: str, is_bahasa_indonesia: bool, term: str) -> float:
        if (self.__cache[0] == filename):
            I = (self.__cache[1]).copy()
        else:
            I = self.__dmanager.readIter_filter(filename, is_bahasa_indonesia)
            self.__cache = (str(filename), I.copy())

        while (I.hasNext()):
            now = dict(I.next())
            if (now["term"] == term):
                return float(now['tf'])
        return float(-1)
    
    def has(self, filename: str, is_bahasa_indonesia: bool, term: str) -> bool:
        return (self.find(filename, is_bahasa_indonesia, term) >= 0)

class IDF():
    def __init__(self, docmanager: DM, lpp: LPP):
        self.__dmanager = Data('idf', ['language', 'term', 'idf'])
        self.__docmanager = docmanager
        self.__lpp = lpp
    
    def refresh(self, is_bahasa_indonesia: bool):
        lang = 'bahasa' if (is_bahasa_indonesia) else 'english'
        files = self.__docmanager.getDocuments(is_bahasa_indonesia)
        all_documents = float(len(files))
        processed_terms = set()

        for f in files:
            unique_terms = self.__docmanager.getDocumentTerms(is_bahasa_indonesia, f)

            for term in unique_terms:

                if term in processed_terms:
                    continue

                term_count = float(0)
                for g in files:
                    unique_terms_g = self.__docmanager.getDocumentTerms(is_bahasa_indonesia, g)
                    if term in processed_terms:
                        continue
                    if term in unique_terms_g:
                        term_count += float(1)
                
                idf = 1+math.log(all_documents/term_count)
                self.__dmanager.writenl({'language': lang, 'term': term, 'idf': idf})
                processed_terms.add(term)

    def find(self, is_bahasa_indonesia: bool, term: str) -> float:
        I = self.__dmanager.readIter_filter(None, is_bahasa_indonesia)

        while (I.hasNext()):
            now = dict(I.next())
            if (now["term"] == term):
                return float(now['idf'])
        return float(-1)

    def query(self, is_bahasa_indonesia: bool, query: str) -> dict:
        content = self.__lpp.naturalize(is_bahasa_indonesia, query)
        if (len(content) == 0):
            return {}
        
        result          = {}
        words           = content.split()
        unique_words    = set(words)

        for w in unique_words:
            result[w] = self.find(is_bahasa_indonesia, w)
        return result