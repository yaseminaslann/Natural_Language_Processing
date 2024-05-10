# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader

input_pdf = PdfFileReader("tıp.pdf")

for i in range(10):
    output = PdfFileWriter()
    for j in range(10):
        output.addPage(input_pdf.getPage((i*10)+j))
    name = "{}_tıp.pdf".format(i)
    with open(name, "wb") as output_stream:
        output.write(output_stream)