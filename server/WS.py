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

    def refresh(self):
        I = self.__data.readIter()
        I.next()
        while (I.hasNext()):
            now = dict(I.next())

    def getPath(self, is_bahasa_indonesia: bool, filename: str) -> str:
        return './documents/' + ('bahasa' if (is_bahasa_indonesia) else 'english')+"/" + filename

    def randomNaming(self, N: int) -> str:
        now = str(int(time.time()))
        return ''.join(random.choice(string.ascii_letters) for _ in range(((N+1)//2)))+ now[:N//2]

    def htmlScraper(self, is_bahasa_indonesia: bool, url: str) -> bool:
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
        except:
            success = False
        return success
    
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