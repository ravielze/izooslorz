import csv
from pathlib import Path
from data.DataManager import WordStorageManager


class NormalizedTFManager():

    def __init__(self, data_file_name):
        self.__data = data_file_name + ".csv"
        self.__file_exist = Path(self.__data).is_file()
        self.__fieldname = ['filename', 'data']

    def init(self, overwrite : bool = False):
        if (overwrite or not(self.__file_exist)):
            with open(self.__data, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.__fieldname)
                writer.writeheader()

    def clear(self):
        with open(self.__data, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.__fieldname)
            writer.writeheader()

    def write(self, d: dict):
        with open(self.__data, mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.__fieldname)
            writer.writerow(d)

    def read(self, filename: str):
        with open(self.__data, mode='r', newline='') as f:
            reader = csv.DictReader(f, fieldnames=self.__fieldname)
            for row in reader:
                if row['filename'] == filename:
                    return row['data']
        return None

    def process(self, wm: WordStorageManager):
        wm.resetState()
        while (wm.hasNext()):
            data = wm.readNext()
            d = eval(data['data'])
            for term in d.keys():
                if term.startswith("_"):
                    continue
                d[term] = float(d[term])/float(d['_total'])
            self.write({'filename': data['filename'], 'data': d})