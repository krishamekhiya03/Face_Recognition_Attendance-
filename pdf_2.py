# pip install FPDF
# pip install PyPDF2
# pip install --upgrade PyPDF2

from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import RectangleObject, NameObject, DictionaryObject, ArrayObject, NumberObject
from os import path

pdf_writer = PdfWriter()
pdf_reader = PdfReader(open('pdf_1.pdf', 'rb'))

# Add each page in pdf to pdf writer
num_of_pages = len(pdf_reader.pages)

for page in range(num_of_pages):
    current_page = pdf_reader.pages[page]
    pdf_writer.add_page(current_page)

# Add link
# Create a link annotation
link_annotation = DictionaryObject()
link_annotation.update({
    NameObject("/Type"): NameObject("/Annot"),
    NameObject("/Subtype"): NameObject("/Link"),
    NameObject("/Rect"): RectangleObject([0, 0, 600, 700]),
    NameObject("/Border"): ArrayObject([NumberObject(0), NumberObject(0), NumberObject(0)]),
    NameObject("/A"): DictionaryObject({
        NameObject("/S"): NameObject("/GoTo"),
        NameObject("/D"): NumberObject(8)
    })
})

# Add the annotation to the first page
page = pdf_writer.pages[0]
if "/Annots" in page:
    page["/Annots"].append(link_annotation)
else:
    page[NameObject("/Annots")] = ArrayObject([link_annotation])

with open(path.abspath('pdf_2.pdf'), 'wb') as link_pdf:
    pdf_writer.write(link_pdf)
