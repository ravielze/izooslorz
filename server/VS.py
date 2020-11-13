from Data import Data
from DM import DM
from LPP import LPP
import math

class Vezz():
    """Vezz stands for Vectorizer"""

    def __init__(self):
        self.__idf = Data('idf', ['language', 'term', 'idf'])

    def dot(self, d: dict, d2: dict) -> float:
        idf = {}
        I = self.__idf.readIter()
        I.next()
        while (I.hasNext()):
            now = dict(I.next())
            idf[now["term"]] = float(now["idf"])
        
        norm = 0
        for i in d.keys():
            norm += ((d[i]*idf[i])**2)
        norm **= 0.5
        norm2 = 0
        for i in d2.keys():
            norm2 += ((d2[i]*idf[i])**2)
        norm2 **= 0.5

        result = 0
        for i in d.keys():
            if i in d2.keys():
                result += ((d[i]*idf[i])*(d2[i]*idf[i]))
        return result/(norm*norm2)

class Selch():
    """ Selch stands for Search """
    
    def __init__(self, docmanager: DM, lpp: LPP):
        self.__tf = Data('tf', ['filename', 'language', 'term', 'tf'])
        self.__idf = Data('idf', ['language', 'term', 'idf'])
        self.__docmanager = docmanager
        self.__lpp = lpp

    def search(self, query: str, is_bahasa_indonesia: bool) -> list:
        files = self.__docmanager.getDocuments(is_bahasa_indonesia)
        sorter = []
        query = self.__lpp.naturalize(is_bahasa_indonesia, query)
        q = query.split()
        query_set = set(q)
        d = {}
        for w in query_set:
            d[w] = q.count(w)
        for f in files:
            I = self.__tf.readIter_filter(f, is_bahasa_indonesia)
            cur_dict = {}
            while (I.hasNext()):
                now = dict(I.next())
                cur_dict[now["term"]] = float(now["tf"])
            sorter.append([Vezz().dot(d, cur_dict), f])
        sorter.sort(reverse=True)
        result = []
        for i in range (len(sorter)):
            d = self.__docmanager.getDocument(is_bahasa_indonesia, sorter[i][1])
            cur_dict = {"namafile": sorter[i][1], "jumlahkata": d["length"],"kecocokan": sorter[i][0], "firstsentence": d["first_sentence"]}
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
        result["kecocokan"] = Vezz().dot(d, d2)
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
        result = [["terms", "query"]]
        ad = []
        for term in terms:
            if term in d.keys():
                ad.append([term, d[term]])
            else:
                ad.append([term, 0])
        ad.sort()
        result = result + ad
        for f in files:
            result[0].append(f)
            content         = self.__docmanager.find(is_bahasa_indonesia, f)
            words           = content.split()
            for i in range(1, len(result)):
                result[i].append(words.count(result[i][0]))
        
        return result
            
        
        
        
