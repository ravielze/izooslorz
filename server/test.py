from data.DataManager import WordStorageManager

"""
wsm = WordStorageManager('test')
wsm.init()
wsm.resetState()
while (wsm.hasNext()):
    print(wsm.readNext())"""

from DocProcessing import DocumentManager, Language
from data.TFManager import NormalizedTFManager
dm = DocumentManager()
doc = dm.process(Language.BAHASA, 'PR08_13519044_KinantanAryaBagaspati.pdf')
print(doc)

wsm = WordStorageManager('documents')
wsm.init()

tfm = NormalizedTFManager('tf')
tfm.init()
tfm.clear()
tfm.process(wsm)