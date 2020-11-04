import csv
from pathlib import Path

class DataManager():

    def __init__(self, data_file_name):
        self.__data = data_file_name + ".csv"
        self.__file_exist = Path(self.__data).is_file()

    def init(self, overwrite : bool = False):
        if (overwrite or not(self.__file_exist)):
            with open(self.__data, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['filename', 'data'])
                writer.writeheader()

    def write(self, d: dict):
        """
            d adalah dictionary dengan format sebagai berikut
            {'filename': namafile, 'data': datanf}
            dengan namafile adalah string nama file beserta extensionnya
            dan datanf adalah dictionary dengan key kata dan value jumlahnya
        """
        with open(self.__data, mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['filename', 'data'])
            writer.writerow(d)

    def read(self, filename: str):
        """
            Mencari data dengan filename tertentu.
        """
        with open(self.__data, mode='r', newline='') as f:
            reader = csv.DictReader(f, fieldnames=['filename', 'data'])
            for row in reader:
                if row['filename'] == filename:
                    return row['data']
        return None