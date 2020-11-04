import textract
import PyPDF2 

text = textract.process('./documents/001_Employee Recognition at Intuit.docx', encoding="ascii")
print(text)
print("----------------")
with open('./documents/PR08_13519044_KinantanAryaBagaspati.pdf', mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    for page in reader.pages:
        print(page.extractText().encode('unicode_escape'))
print("----------------")