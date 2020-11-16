from Data import Data
from DM import DM
from BDIter import biiter

"""TF-IDF stands for Term Frequency and Inverse Document Frequency.
    Source: https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/"""
class TF():

    def __init__(self, docmanager: DM):
        self.__dmanager = Data('tf', ['filename', 'language', 'term', 'tf'])
        self.__docmanager = docmanager

    def process(self, is_bahasa_indonesia: bool, filename: str):
        content         = self.__docmanager.find(is_bahasa_indonesia, filename)
        if (len(content) == 0):
            return
        lang            = 'bahasa' if (is_bahasa_indonesia) else 'english'

        words           = content.split()
        doc_length      = len(words)
        unique_words    = set(words)

        for w in unique_words:
            tf          = int(words.count(w))
            
            self.__dmanager.writenl({'filename': filename, 'language': lang, 'term': w, 'tf': tf})

        
    def getDocuments(self, is_bahasa_indonesia: bool) -> list:
        """ Get List of Document's Name """
        result = []
        I = biiter(self.__dmanager.readIter_filter(None, is_bahasa_indonesia).getList())
        while (I.hasNext()):
            now = dict(I.next())
            result.append(now['filename'])
        return result

    def refreshAll(self):
        self.refresh(True)
        self.refresh(False)

    def refresh(self, is_bahasa_indonesia):
        files = set(self.__docmanager.getDocuments(is_bahasa_indonesia))
        rfiles = set(self.getDocuments(is_bahasa_indonesia))
        process = files.difference(rfiles)

        for f in process:
            self.process(is_bahasa_indonesia, f)

class IDF():
    def __init__(self, docmanager: DM):
        self.__dmanager = Data('idf', ['language', 'term', 'count'])
        self.__idfdoc = Data('idfdoc', ['filename', 'language'])
        self.__docmanager = docmanager

    def getDocuments(self, is_bahasa_indonesia: bool) -> list:
        """ Get List of Document's Name """
        result = []
        I = biiter(self.__idfdoc.readIter_filter(None, is_bahasa_indonesia).getList())
        while (I.hasNext()):
            now = dict(I.next())
            result.append(now['filename'])
        return result

    def refreshAll(self):
        self.refresh(True)
        self.refresh(False)

    def refresh(self, is_bahasa_indonesia):
        files       = set(self.__docmanager.getDocuments(is_bahasa_indonesia))
        rfiles      = set(self.getDocuments(is_bahasa_indonesia))
        process     = files.difference(rfiles)
        lang        = 'bahasa' if (is_bahasa_indonesia) else 'english'
        
        for f in process:
            self.process(is_bahasa_indonesia, f)

    def reset(self, is_bahasa_indonesia):
        saved = []
        I = self.__dmanager.readIter_filter(None, not(is_bahasa_indonesia))
        while (I.hasNext()):
            saved.append(dict(I.next()))

        self.__dmanager.write(saved)

    def process(self, is_bahasa_indonesia: bool, filename: str):
        lang        = 'bahasa' if (is_bahasa_indonesia) else 'english'
        I           = self.__dmanager.readIter_filter(None, is_bahasa_indonesia)
        currentData = {}
        self.__idfdoc.writenl({'filename': filename, 'language': lang})
        while (I.hasNext()):
            now = dict(I.next())
            currentData[now['term']] = int(now['count'])
        
        self.reset(is_bahasa_indonesia)

        content         = self.__docmanager.find(is_bahasa_indonesia, filename)
        if (len(content) == 0):
            return

        words        = content.split()
        for w in words:
            if w in currentData.keys():
                currentData[w] += 1
            else:
                currentData[w] = 1

        for x in currentData.keys():
            self.__dmanager.writenl({'language': lang, 'term': x, 'count': currentData[x]})