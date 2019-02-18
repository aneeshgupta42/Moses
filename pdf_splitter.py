from PyPDF2 import PdfFileReader, PdfFileWriter
import os

 
 
def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_write = PdfFileWriter()
        pdf_write.addPage(pdf.getPage(page))
 
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_write.write(out)
 
        print('Created: {}'.format(output_filename))
 
if __name__ == '__main__':
  
    print("This program will create the split PDFs in the same directory as python program")
    path = input("Enter complete file path:")
    pdf_splitter(path)
