import csv,os
from BDIter import biiter
from pathlib import Path

class Data:

    def __init__(self, file: str, field: list):
        self.__file = file
        self.__field = field
        if not os.path.exists('Data'):
            os.mkdir('Data')
        fileExist = Path('Data/' + self.__file + ".csv").is_file()
        if not fileExist:
            with open("Data/" + self.__file + '.csv', mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.__field,  dialect='excel')
                writer.writeheader()

    def destroy(self):
        """Delete file."""
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

    def write(self, dicts: dict):
        """Overwrite all line."""
        with open("Data/" + self.__file + '.csv', mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.__field,  dialect='excel')
            writer.writeheader()
            for x in dicts:
                writer.writerow(x)
    
    def writenl(self, x: dict):
        """Write new line."""
        with open("Data/" + self.__file + '.csv', mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.__field,  dialect='excel')
            writer.writerow(x)

    def read(self):
        """Read all data."""
        result = []
        try:
            with open("Data/" + self.__file + '.csv', mode='r', newline='') as f:
                reader = csv.DictReader(f, dialect='excel')
                for row in reader:
                    newDict = {}
                    for x in self.__field:
                        newDict[x] = row[x]
                    result.append(newDict)
        except:
            self.write({}, self.__field)
        return result

    def readIter(self) -> biiter:
        """Read all data as biiter."""
        with open("Data/" + self.__file + '.csv', mode='r', newline='') as f:
            reader = list(csv.DictReader(f, fieldnames=self.__field))
            return biiter(reader)