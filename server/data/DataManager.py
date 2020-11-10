import csv
from pathlib import Path


class WordStorageManager():

    def __init__(self, data_file_name):
        self.__data = data_file_name + ".csv"
        self.__file_exist = Path(self.__data).is_file()
        self.__state = 0
        self.__maxstate = 0
        self.__fieldname = ['filename', 'data']

    def init(self, overwrite : bool = False):
        if (overwrite or not(self.__file_exist)):
            with open(self.__data, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.__fieldname)
                writer.writeheader()
        if (self.__file_exist):
            with open(self.__data, mode='r', newline='') as f:
                self.__maxstate = len(list(csv.DictReader(f, fieldnames=['filename', 'data'])))-1


    def write(self, d: dict):
        """
            d adalah dictionary dengan format sebagai berikut
            {'filename': namafile, 'data': datanf}
            dengan namafile adalah string nama file beserta extensionnya
            dan datanf adalah dictionary dengan key kata dan value jumlahnya
        """
        with open(self.__data, mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.__fieldname)
            writer.writerow(d)

            self.__maxstate += 1

    def read(self, filename: str):
        """
            Mencari data dengan filename tertentu.
        """
        with open(self.__data, mode='r', newline='') as f:
            reader = csv.DictReader(f, fieldnames=self.__fieldname)
            for row in reader:
                if row['filename'] == filename:
                    return row['data']
        return None

    def resetState(self):
        self.__state = 0
    
    def hasNext(self) -> bool:
        return self.__state+1 <= self.__maxstate

    def readNext(self) -> dict:
        if not(self.hasNext()):
            return None

        with open(self.__data, mode='r', newline='') as f:
            reader = list(csv.DictReader(f, fieldnames=['filename', 'data']))
            self.__state += 1
            return dict(reader[self.__state])