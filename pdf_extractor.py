# Import libraries
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from collections import OrderedDict
import json
import pandas as pd

pdf = pd.read_csv("Data Engineer Task - Data Engineer Task.csv",header=None)
pdf_df = pd.DataFrame(pdf)

finalfile = "pdf_extract.json"
# open file 
f = open(finalfile, "r+") 
# absolute file positioning
f.seek(0) 
# to erase all data 
f.truncate() 

for index, row in pdf_df.iterrows():
    # Path of the pdf
    url = row[0]
    PDF_file = row[0]
    
    '''
    Part #1 : Converting PDF to images
    '''
    if(PDF_file.endswith('.pdf')):
        # Store all the pages of the PDF in a variable
        from pdf2image import pdfinfo_from_path,convert_from_path
        info = pdfinfo_from_path(PDF_file, userpw=None, poppler_path=r"C:\Users\Chanchal Agrawal\Downloads\Release-22.01.0-0\poppler-22.01.0\Library\bin")
        outfile = "sample_output.txt"
        # open file 
        f = open(outfile, "r+") 
        # absolute file positioning
        f.seek(0) 
        # to erase all data 
        f.truncate() 
        maxPages = info["Pages"]

        #Iterating 10 pages of a pdf at a time
        for page in range(1, maxPages-1, 10) : 
            pages = convert_from_path(PDF_file, dpi=200, first_page=page, last_page = min(page+10-1,maxPages), poppler_path=r"C:\Users\Chanchal Agrawal\Downloads\Release-22.01.0-0\poppler-22.01.0\Library\bin")
            # Iterate through all the pages stored above
            for page in pages:
                filename = "temp.jpg"
                # Save the image of the page in system
                page.save(filename, 'JPEG')
                # Recognize the text as string in image using pytesserct
                pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
                text = str((pytesseract.image_to_string(Image.open(filename),lang='hin')))
                text = text.replace('-\n', '')    
                with open(outfile, "a", encoding="utf-8") as f:
                    f.write(text)
                # print(text)
        
        with open(finalfile, 'a', encoding='utf8') as json_file:
            c = OrderedDict()
            c["page-url"] = url
            c["pdf-url"] = url
            c["paragraph"] = text
            json_object = json.dumps(c, indent = 2,ensure_ascii=False) 
            json_file.write(json_object)
        # f.close()
