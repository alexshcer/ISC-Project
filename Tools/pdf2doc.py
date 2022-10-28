"""author: alexshcer"""

from pdf2docx import Converter

x=1
for x in range(1, 31):
    if x==1 or x==2 or x==3 or x==4 or x==5 or x==6 or x==7 or x==8 or x==9:
        y = str(x).zfill(2)
        pdf_file  = f'../Final/avo_{y}.pdf'# source file 
        docx_file = f'../Final/avo_docx/avo_{y}.docx'  # destination file
    else:
        pdf_file  = f'../Final/avo_{x}.pdf'# source file 
        docx_file = f'../Final/avo_docx/avo_{x}.docx'  # destination file
    
    # convert pdf to docx
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

    x = x + 1