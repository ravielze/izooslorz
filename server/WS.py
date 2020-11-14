"""

url = 'https://github.com/microsoft/pylance-release/blob/master/TROUBLESHOOTING.md#unresolved-import-warnings'

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('test.html', 'wb')
f.write(webContent)
f.close"""

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import time, string, random
from LPP import LPP
from Data import Data
from BDIter import biiter

class Scraper():
    def __init__(self, lpp: LPP):
        self.__lpp = lpp
        self.__data = Data('webscraping', ['filename', 'language', 'url'])

    def getPath(self, is_bahasa_indonesia: bool, filename: str) -> str:
        return './Documents/' + ('bahasa' if (is_bahasa_indonesia) else 'english')+"/" + filename

    def randomNaming(self, N: int) -> str:
        now = str(int(time.time()))
        return ''.join(random.choice(string.ascii_letters) for _ in range(((N+1)//2)))+ now[:N//2]

    def htmlScraper(self, is_bahasa_indonesia: bool, url: str) -> tuple:
        success = True
        lang = 'bahasa' if (is_bahasa_indonesia) else 'english'
        try:
            response        = urllib.request.urlopen(url)
            webContent      = response.read()
            soup            = BeautifulSoup(webContent.decode('utf8'), 'html.parser')

            title           = self.__lpp.lemmatize(soup.find('title').string).replace(' ', '')
            fname           = title + "_" + self.randomNaming(9) + ".html"
            f               = open(self.getPath(is_bahasa_indonesia, fname), 'wb')
            f.write(webContent)
            f.close()
            self.__data.writenl({'filename': fname, 'language': lang, 'url': url})
        except Exception as e:
            success = False
            fname = str(e)
        return (success, fname)
    
    def findUrl(self, filename: str, is_bahasa_indonesia: bool) -> str:
        I = self.__data.readIter_filter(filename, is_bahasa_indonesia)
        if I.hasNext():
            now = dict(I.next())
            return now['url']
        else:
            return ""

    def getDocuments(self, is_bahasa_indonesia: bool) -> list:
        result = []
        I = biiter(self.__data.readIter_filter(None, is_bahasa_indonesia).getList())
        while (I.hasNext()):
            now = dict(I.next())
            result.append(now['filename'])
        return result

    def getUrl(self, is_bahasa_indonesia: bool, filename: str) -> float:
        I = self.__dmanager.readIter_filter(filename, is_bahasa_indonesia)

        if (I.hasNext()):
            now = dict(I.next())
            return now['url']
        return None