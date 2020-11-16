from Data import Data
from DM import DM
from LPP import LPP
from WS import Scraper
import math

LINK_PREFIX = 'http://localhost:5000/file/'

class Vezz():
    """Vezz stands for Vectorizer"""

    def __init__(self):
        self.__idf = Data('idf', ['language', 'term', 'count'])

    def multiplier(self, d1: dict, d2: dict):
        for i in d1.keys():
            if not(i in d2.keys()):
                continue
            d1[i] *= d2[i]

    def dot(self, d: dict, d2: dict) -> float:
        norm = 0
        for i in d.keys():
            norm += (d[i]**2)
        norm **= 0.5
        norm2 = 0
        for i in d2.keys():
            norm2 += (d2[i]**2)
        norm2 **= 0.5

        result = 0
        for i in d.keys():
            if i in d2.keys():
                result += (d[i]*d2[i])
        finalresult = 0
        try:
            finalresult = result/(norm*norm2)
        except ZeroDivisionError:
            finalresult = 0
        return finalresult

class Selch():
    """ Selch stands for Search """
    
    def __init__(self, docmanager: DM, lpp: LPP, sc: Scraper):
        self.__tf = Data('tf', ['filename', 'language', 'term', 'tf'])
        self.__idf = Data('idf', ['language', 'term', 'count'])
        self.__docmanager = docmanager
        self.__lpp = lpp
        self.__sc = sc

    def search(self, query: str, is_bahasa_indonesia: bool) -> list:
        files = self.__docmanager.getDocuments(is_bahasa_indonesia)
        documents = len(files)
        
        idf = {}
        files = self.__docmanager.getDocuments(is_bahasa_indonesia)
        documents = len(files)
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
        
        sorter = []
        query = self.__lpp.naturalize(is_bahasa_indonesia, query)
        q = query.split()
        query_set = set(q)
        d = {}
        for w in query_set:
            if w in idf.keys():
                d[w] = q.count(w)
        Vezz().multiplier(d, idf)
        for f in files:
            I = self.__tf.readIter_filter(f, is_bahasa_indonesia)
            cur_dict = {}
            while (I.hasNext()):
                now = dict(I.next())
                cur_dict[now["term"]] = float(now["tf"])
            Vezz().multiplier(cur_dict, idf)
            sorter.append([Vezz().dot(d, cur_dict), f])
        sorter.sort(reverse=True)
        result = []
        for i in range (len(sorter)):
            if sorter[i][0] <= 0.0001:
                continue
            d = self.__docmanager.getDocument(is_bahasa_indonesia, sorter[i][1])
            url = self.__sc.findUrl(sorter[i][1], is_bahasa_indonesia)
            if len(url) <= 0:
                url = LINK_PREFIX + ('bahasa/' if is_bahasa_indonesia else 'english/') + sorter[i][1]
            cur_dict = {"namafile": sorter[i][1], "jumlahkata": d["length"],"kecocokan": float('%.5f' % sorter[i][0]), "firstsentence": d["first_sentence"], "url": url}
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
        files = self.__docmanager.getDocuments(is_bahasa_indonesia)
        
        container = {}
        I = self.__tf.readIter_filter(None, is_bahasa_indonesia)
        i = 0
        while (I.hasNext()):
            i += 1
            now = dict(I.next())
            if not(now["term"] in container):
                container[now["term"]] = {}
            container[now["term"]][now["filename"]] = now["tf"]
        
        terms = set([])
        I = self.__idf.readIter_filter(None, is_bahasa_indonesia)
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
        
        result = []
        for term in terms:
            documents = []
            if term in container.keys():
                for f in files:
                    if f in container[term].keys():
                        documents.append({
                            'doc': f,
                            'value': container[term][f]
                        })
                    else:
                        documents.append({
                            'doc': f,
                            'value': 0
                        })
            else:
                for f in files:
                    documents.append({
                        'doc': f,
                        'value': 0
                    })
            if term in d.keys():
                result.append({'terms': term, 'query': d[term], 'documents': documents})
            else:
                result.append({'terms': term, 'query': 0, 'documents': documents})

        return result
            
        
        
        
