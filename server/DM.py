
import textract
import PyPDF2
from Data import Data
from BDIter import biiter
from pathlib import Path
from LPP import LPP

TEXTRACT_EXT = ['docx', 'doc', 'pptx', 'txt', 'json', 'htm', 'html']

class DM():
    """DM stands for Document Manager."""

    def __init__(self):
        self.__dmanager = Data('document', ['filename', 'language', 'content'])
        self.__lpp = LPP()

    def getFileExtension(self, filename: str) -> str:
        return filename.split(".")[-1]

    def getPath(self, is_bahasa_indonesia: bool, filename: str) -> str:
        document_path = './documents/'
        if (is_bahasa_indonesia):
            return document_path + "bahasa/" + filename
        else:
            return document_path + "english/" + filename
    
    def find(self, is_bahasa_indonesia: bool, filename: str) -> str:
        if (is_bahasa_indonesia):
            lang = 'bahasa'
        else:
            lang = 'english'
        I = self.__dmanager.readIter()
        while (I.hasNext()):
            now = dict(I.next())
            if (now['filename'] == filename and now["language"] == lang):
                print("skip")
                return now['content']
        return None
    
    def arraytostring(self, arr: list) -> str:
        """To convert an array to a string"""
        separator = ' '
        return separator.join(arr)
    
    def read(self, is_bahasa_indonesia: bool, filename: str):
        fileExist = Path(self.getPath(is_bahasa_indonesia, filename)).is_file()
        if not fileExist:
            return ""
        content = self.find(is_bahasa_indonesia, filename)
        if (content == None):
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

        if (is_bahasa_indonesia):
            lang = 'bahasa'
        else:
            lang = 'english'
        content = self.__lpp.naturalize(is_bahasa_indonesia, content)
        self.__dmanager.writenl({'filename': filename, 'language': lang, 'content': content})
        return content