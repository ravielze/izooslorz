from LPP import LPP
from DM import DM
from TFIDF import TF, IDF
from WS import Scraper
from VS import Selch

class IZOOSLORZ():

    def __init__(self):
        IZOOSLORZ._instance = self
        self.lpp = LPP()
        self.dm = DM(self.lpp)
        self.dm.onload()
        self.tf = TF(self.dm)
        self.tf.refreshAll()
        self.idf = IDF(self.dm)
        self.idf.refreshAll()
        self.sc = Scraper(self.lpp)
        self.ss = Selch(self.dm, self.lpp, self.sc)