from Data import Data
from DM import DM
from LPP import LPP
from WS import Scraper
from TFIDF import TF, IDF
import math

LINK_PREFIX = 'http://localhost:5000/file/'

class Selch():
    """ Selch stands for Search """
    
    def __init__(self, docmanager: DM, lpp: LPP, sc: Scraper, tf: TF, idf: IDF):
        self.__tf = tf.getDataManager()
        self.__idf = idf.getDataManager()
        self.__docmanager = docmanager
        self.__lpp = lpp
        self.__sc = sc
        self.__isChanged = True
        self.__cache = {}

    def dot(self, d: dict, d2: dict, idf: dict, documents: float) -> float:
        norm = 0
        for i in d.keys():
            norm += ((d[i]*idf[i])**2)
        norm **= 0.5
        norm2 = 0
        for i in d2.keys():
            if i in d.keys():
                norm2 += ((d2[i]*idf[i])**2)
        norm2 **= 0.5

        result = 0
        for i in d.keys():
            if i in d2.keys() and i in idf.keys():
                result += ((d[i]*idf[i])*(d2[i]*idf[i]))
        finalresult = 0
        try:
            finalresult = result/(norm*norm2)
        except ZeroDivisionError:
            finalresult = 0
        return finalresult

    def getIDF(self, documents: int, is_bahasa_indonesia: bool) -> dict:
        idf = {}
        if self.__isChanged == False:
            self.__isChanged = (self.__tf.isChanged()) or (self.__idf.isChanged())

        if self.__isChanged == False:
            print("T")
            return self.__cache

        if self.__isChanged:
            I = self.__idf.readIter_filter(None, is_bahasa_indonesia)
            i = 0
            while (I.hasNext()):
                i += 1
                now = dict(I.next())
                try:
                    idf[now["term"]] = 1 + math.log(documents/float(now["count"]))
                except:
                    print(f"Line {i} Error.")
                    continue
        self.__cache = idf
        return idf

    def search(self, query: str, is_bahasa_indonesia: bool) -> list:
        files = self.__docmanager.getDocuments(is_bahasa_indonesia)
        documents = len(files)
        idf = self.getIDF(documents, is_bahasa_indonesia)
        sorter = []
        query = self.__lpp.naturalize(is_bahasa_indonesia, query)
        q = query.split()
        query_set = set(q)
        d = {}
        for w in query_set:
            if not(w in idf.keys()):
                continue
            d[w] = q.count(w)
        for f in files:
            I = self.__tf.readIter_filter(f, is_bahasa_indonesia)
            cur_dict = {}
            while (I.hasNext()):
                now = dict(I.next())
                cur_dict[now["term"]] = float(now["tf"])
            sorter.append([self.dot(d, cur_dict, idf, float(documents)), f])
        sorter.sort(reverse=True)
        result = []
        for i in range (len(sorter)):
            if sorter[i][0] <= 0.0001:
                continue
            d = self.__docmanager.getDocument(is_bahasa_indonesia, sorter[i][1])
            url = self.__sc.findUrl(sorter[i][1], is_bahasa_indonesia)
            if len(url) <= 0:
                url = LINK_PREFIX+ ('bahasa/' if is_bahasa_indonesia else 'english/') + sorter[i][1]
            cur_dict = {"namafile": sorter[i][1], "jumlahkata": d["length"],"kecocokan": sorter[i][0], "firstsentence": d["first_sentence"], "url": url}
            result.append(cur_dict)
            
        return result

    def documentComparing(self, is_bahasa_indonesia: bool, filename: str, filename2: str) -> dict:
        result = {"dokumen_1": filename, "dokumen_2": filename2}
        I = self.__tf.readIter_filter(filename, is_bahasa_indonesia)
        d = {}
        while (I.hasNext()):
            now = dict(I.next())
            d[now["term"]] = float(now["tf"])
        I = self.__tf.readIter_filter(filename2, is_bahasa_indonesia)
        d2 = {}
        while (I.hasNext()):
            now = dict(I.next())
            d2[now["term"]] = float(now["tf"])
        result["kecocokan"] = self.dot(d, d2)
        return result
    
    def termTable(self, query: str, is_bahasa_indonesia: bool) -> list:
        terms = set([])
        I = self.__idf.readIter()
        I.next()
        while (I.hasNext()):
            now = dict(I.next())
            terms.add(now["term"])
        
        query = self.__lpp.naturalize(is_bahasa_indonesia, query)
        q = query.split()
        query_set = set(q)
        d = {}
        for w in query_set:
            d[w] = q.count(w)
            terms.add(w)
        
        files = self.__docmanager.getDocuments(is_bahasa_indonesia)
        documents = len(files)
        result = []
        for term in terms:
            if term in d.keys():
                result.append({'terms': term, 'query': d[term], 'documents': []})
            else:
                result.append({'terms': term, 'query': 0, 'documents': []})
        for f in files:
            content         = self.__docmanager.find(is_bahasa_indonesia, f)
            if (len(content) == 0):
                continue
            words           = content.split()
            for i in range(len(result)):
                result[i]['documents'].append({
                    'doc': f,
                    'value': words.count(result[i]['terms'])
                })
        
        return result
            
        
        
        
