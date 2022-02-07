# Import libraries
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from collections import OrderedDict
import json
import pandas as pd

pdf_list = pd.read_csv('Data Engineer Task - Data Engineer Task.csv')
for i in pdf_list:
    print(i)


# # Path of the pdf
# PDF_file = r"https://www.mpscmaterial.com/wp-content/uploads/2021/09/3.-Polity-Book-for-Class-11th-in-Marathi-21.pdf"
  
# '''
# Part #1 : Converting PDF to images
# '''
# # Store all the pages of the PDF in a variable
# from pdf2image import pdfinfo_from_path,convert_from_path
# info = pdfinfo_from_path(PDF_file, userpw=None, poppler_path=r"C:\Users\Chanchal Agrawal\Downloads\Release-22.01.0-0\poppler-22.01.0\Library\bin")
# outfile = "out_text.txt"
# # open file 
# f = open(outfile, "r+") 
# # absolute file positioning
# f.seek(0) 
# # to erase all data 
# f.truncate() 
# maxPages = info["Pages"]
# for page in range(1, maxPages//2, 10) : 
#     pages = convert_from_path(PDF_file, dpi=200, first_page=page, last_page = min(page+10-1,maxPages), poppler_path=r"C:\Users\Chanchal Agrawal\Downloads\Release-22.01.0-0\poppler-22.01.0\Library\bin")
#     # Iterate through all the pages stored above
#     for page in pages:
#         filename = "temp.jpg"
#         # Save the image of the page in system
#         page.save(filename, 'JPEG')
#         # Recognize the text as string in image using pytesserct
#         pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
#         text = str((pytesseract.image_to_string(Image.open(filename),lang='hin')))
#         text = text.replace('-\n', '')    
#         with open(outfile, "a", encoding="utf-8") as f:
#             f.write(text)
#         # print(text)

#     c = OrderedDict()
#     c["page-url"] = "https://tjsbbank.co.in/pdf/English_Marathi_Notice.pdf"
#     c["pdf-url"] = "https://tjsbbank.co.in/pdf/English_Marathi_Notice.pdf"
#     c["paragraph"] = text
#     json_object = json.dumps(c, indent = 2) 
#     # Writing to json
#     with open("final.json", "w",encoding="utf-8") as f:
#         f.write(json_object)
#     f.close()
