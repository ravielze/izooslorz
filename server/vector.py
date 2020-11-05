from DocProcessing import DocumentManager, Language

dm = DocumentManager()
a = dm.process(Language.BAHASA, "mapresrika.docx")
print(a[1])