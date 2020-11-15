import csv,os
from BDIter import biiter
from pathlib import Path

class Data:

    def __init__(self, file: str, field: list):
        self.__file = file
        self.__field = field
        self.__cache = [[],[],[],[]]
        self.__isChanged = True
        if not os.path.exists('Data'):
            os.mkdir('Data')
        fileExist = Path('Data/' + self.__file + ".csv").is_file()
        if not fileExist:
            with open("Data/" + self.__file + '.csv', mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.__field,  dialect='excel')
                writer.writeheader()

    def isChanged(self) -> bool:
        return self.__isChanged

    def destroy(self):
        """Delete file."""
        self.__isChanged = True
        if os.path.exists('Data/' + self.__file + ".csv"):
            os.remove('Data/' + self.__file + ".csv")
        del self

    def rename(self, file: str):
        """Rename filename."""
        d= 'Data/' + self.__file + ".csv"
        dnew= 'Data/' + file + ".csv"
        if os.path.exists(d):
            os.rename(d, dnew)
        self.__file = file

    def write(self, dicts: list):
        """Overwrite all line."""
        self.__isChanged = True
        with open("Data/" + self.__file + '.csv', mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.__field,  dialect='excel')
            writer.writeheader()
            for x in dicts:
                writer.writerow(x)

    def reset(self):
        """Reset."""
        self.__isChanged = True
        with open("Data/" + self.__file + '.csv', mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.__field,  dialect='excel')
            writer.writeheader()
    
    def writenl(self, x: dict):
        """Write new line."""
        self.__isChanged = True
        with open("Data/" + self.__file + '.csv', mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.__field,  dialect='excel')
            writer.writerow(x)

    def read(self):
        """Read all data."""
        result = []
        if len(self.__cache[0]) != 0 and self.__isChanged == False:
            return self.__cache[0]
        try:
            with open("Data/" + self.__file + '.csv', mode='r', newline='') as f:
                reader = csv.DictReader(f, dialect='excel')
                for row in reader:
                    newDict = {}
                    for x in self.__field:
                        newDict[x] = row[x]
                    result.append(newDict)
            self.__cache[0] = result
        except:
            self.write({}, self.__field)
        return result

    def readIter(self) -> biiter:
        """Read all data as biiter."""
        if len(self.__cache[0]) != 0 and self.__isChanged == False:
            print("T")
            return biiter(self.__cache[0])
        try:
            with open("Data/" + self.__file + '.csv', mode='r', newline='') as f:
                self.__cache[0] = list(csv.DictReader(f, fieldnames=self.__field))
                return biiter(self.__cache[0])
        except:
            return biiter([])
    
    def readIter_filter(self, filename=None, is_bahasa_indonesia=None) -> biiter:
        """Read all data as biiter with filename filter."""
        if filename != None and is_bahasa_indonesia != None:
            if "language" in self.__field and "filename" in self.__field:
                if len(self.__cache[1]) != 0 and self.__isChanged == False:
                    print("T")
                    return biiter(self.__cache[1])
                result = []
                lang = 'bahasa' if (is_bahasa_indonesia) else 'english'

                I = self.readIter()

                while (I.hasNext()):
                    now = dict(I.next())

                    if (now['filename'] == filename and now["language"] == lang):
                        result.append(now)
                self.__cache[1] = result
                return biiter(self.__cache[1])
            else:
                return biiter([])
        elif filename != None:
            if "filename" in self.__field:
                if len(self.__cache[2]) != 0 and self.__isChanged == False:
                    print("T")
                    return biiter(self.__cache[2])
                result = []

                I = self.readIter()

                while (I.hasNext()):
                    now = dict(I.next())

                    if (now['filename'] == filename):
                        result.append(now)
                
                self.__cache[2] = result
                return biiter(self.__cache[2])
            else:
                return biiter([])
        else:
            if "language" in self.__field:
                if len(self.__cache[3]) != 0 and self.__isChanged == False:
                    print("T")
                    return biiter(self.__cache[3])
                result = []

                I = self.readIter()
                lang = 'bahasa' if (is_bahasa_indonesia) else 'english'

                while (I.hasNext()):
                    now = dict(I.next())

                    if (now["language"] == lang):
                        result.append(now)
                
                self.__cache[3] = result
                return biiter(self.__cache[3])
            else:
                return biiter([])