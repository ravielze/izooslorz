
import textract
import PyPDF2
from Data import Data
from BDIter import biiter
from pathlib import Path
from LPP import LPP
import re
from pathlib import Path
import os
from threading import Thread

TEXTRACT_EXT = ['docx', 'doc', 'pptx', 'txt', 'json', 'htm', 'html', 'pdf']

class DM():
    """DM stands for Document Manager."""

    def __init__(self, lpp: LPP):
        self.__dmanager = Data('document', ['filename', 'language', 'length', 'first_sentence', 'content'])
        self.__lpp = lpp
        if not os.path.exists('Documents'):
            Path('Documents/bahasa').mkdir(parents=True, exist_ok=True)
            Path('Documents/english').mkdir(parents=True, exist_ok=True)

    def onload(self):

        def processEnglish():
            print(f"Checking Document English...")
            docenglish = self.getDocuments(False)
            for filename in os.listdir(Path('Documents/english')):
                if filename in docenglish:
                    continue
                if self.getFileExtension(filename) in TEXTRACT_EXT:
                    print(f"{filename}: Reading.")
                    self.read(False, filename)
            print(f"Checking Document English... DONE")
        
        def processBahasa():
            print(f"Checking Document Bahasa Indonesia...")
            docbahasa = self.getDocuments(True)
            for filename in os.listdir(Path('Documents/bahasa')):
                if filename in docbahasa:
                    continue
                if self.getFileExtension(filename) in TEXTRACT_EXT:
                    self.read(True, filename)
                    print(f"{filename}: Reading.")
            print(f"Checking Document Bahasa Indonesia... DONE")
            
        thread2 = Thread(target=processEnglish)
        thread2.start()
        thread = Thread(target=processBahasa)
        thread.start()

    def getFileExtension(self, filename: str) -> str:
        return filename.split(".")[-1]

    def getPath(self, is_bahasa_indonesia: bool, filename: str) -> str:
        return './Documents/' + ('bahasa' if (is_bahasa_indonesia) else 'english')+"/" + filename
    
    def find(self, is_bahasa_indonesia: bool, filename: str) -> str:
        I = self.__dmanager.readIter_filter(filename, is_bahasa_indonesia)
        if (I.hasNext()):
            now = dict(I.next())
            return now['content']
        return ""

    def getDocuments(self, is_bahasa_indonesia: bool) -> list:
        """ Get List of Document's Name """
        result = []
        I = biiter(self.__dmanager.readIter_filter(None, is_bahasa_indonesia).getList())
        while (I.hasNext()):
            now = dict(I.next())
            result.append(now['filename'])
        return result

    def getDocumentTerms(self, is_bahasa_indonesia: bool, filename: str) -> set:
        """ Return Unique Terms. """
        content = self.find(is_bahasa_indonesia, filename)
        return (set(content.split()))
    
    def arraytostring(self, arr: list) -> str:
        """To convert an array to a string"""
        separator = ' '
        return separator.join(arr)

    def getFirstSentence(self, content: str) -> str:
        content = content.replace('\n',' ').replace('\\n', ' ')
        words = content.split()
        cleaned = []
        for w in words:
            w = re.sub(r'\s{2,}', ' ', w)
            cleaned.append(w)
        content = ' '.join(cleaned)

        space_count = (content.count(' '))
        if "." in set(content):
            find = re.compile(r"^[^.]*")
            content = re.search(find, content).group(0)
        if not("." in content):
            if len(content) >= 100+space_count:
                return content[:(100+space_count)] + "..."
            else:
                return content[:(100+space_count)] + "."
        else:
            return content + "."

    def getDocument(self, is_bahasa_indonesia: bool, filename: str) -> dict:
        I = self.__dmanager.readIter_filter(filename, is_bahasa_indonesia)
        if (I.hasNext()):
            now = dict(I.next())
            return now
        return {}
    
    def read(self, is_bahasa_indonesia: bool, filename: str) -> str:
        fileExist = Path(self.getPath(is_bahasa_indonesia, filename)).is_file()
        if not fileExist:
            return ""
        content = self.find(is_bahasa_indonesia, filename)
        if (len(content) == 0):
            content = ""
            ext = self.getFileExtension(filename)
            if ext == 'pdf':
                with open(self.getPath(is_bahasa_indonesia, filename), mode='rb') as f:
                    reader = PyPDF2.PdfFileReader(f)
                    result = []
                    for page in reader.pages:
                        result.append(page.extractText().encode('unicode_escape').decode('utf-8'))
                    content = self.arraytostring(result)

            elif ext in TEXTRACT_EXT:
                content = textract.process(self.getPath(is_bahasa_indonesia, filename), encoding='ascii').decode('utf-8')

            else:
                return ""
        else:
            return content

        lang = 'bahasa' if (is_bahasa_indonesia) else 'english'
        length = len(set(content.split()))
        first_sentence = self.getFirstSentence(content)
        content = self.__lpp.naturalize(is_bahasa_indonesia, content)
        self.__dmanager.writenl({'filename': filename, 'language': lang, 'content': content, 'first_sentence': first_sentence, 'length': length})
        return content