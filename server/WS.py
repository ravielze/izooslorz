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

class Scraper():
    def __init__(self, lpp: LPP):
        self.__lpp = lpp

    def getPath(self, is_bahasa_indonesia: bool, filename: str) -> str:
        return './documents/' + ('bahasa' if (is_bahasa_indonesia) else 'english')+"/" + filename

    def randomNaming(self, N: int) -> str:
        now = str(int(time.time()))
        return ''.join(random.choice(string.ascii_letters) for _ in range(((N+1)//2)))+ now[:N//2]

    def htmlScraper(self, is_bahasa_indonesia: bool, url: str) -> bool:
        success = True
        try:
            response = urllib.request.urlopen(url)
            webContent = response.read()
            soup = BeautifulSoup(webContent.decode('utf8'), 'html.parser')
            title = self.__lpp.lemmatize(soup.find('title').string).replace(' ', '')

            f = open(self.getPath(is_bahasa_indonesia, title + "_" + self.randomNaming(9) + ".html"), 'wb')
            f.write(webContent)
            f.close()
        except:
            success = False
        return success

lpp = LPP()
s = Scraper(lpp)
print(s.htmlScraper(False, 'https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/'))