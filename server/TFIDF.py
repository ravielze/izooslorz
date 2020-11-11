from Data import Data
from DM import DM

"""TF-IDF stands for Term Frequency and Inverse Document Frequency"""

class TF():

    def __init__(self, docmanager: DM):
        self.__dmanager = Data('tf', ['filename', 'language', 'term', 'tf'])
        self.__docmanager = docmanager

    def refresh(self, is_bahasa_indonesia):
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

    def find(self, filename, is_bahasa_indonesia, term) -> float:
        lang = 'bahasa' if (is_bahasa_indonesia) else 'english'
        I = self.__dmanager.readIter()
        while (I.hasNext()):
            now = dict(I.next())
            if (now['filename'] == filename and now["language"] == lang and now["term"] == term):
                return float(now['tf'])
        return float(-1)
    
    def has(self, filename, is_bahasa_indonesia, term) -> bool:
        return (self.find(filename, is_bahasa_indonesia, term) >= 0)