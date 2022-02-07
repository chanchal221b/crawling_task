# Internship_tasks

Task 1 - Wikipedia Extractor

For this task I have used the pytohn library - wikipedia.



We take user inputs which are 

- keywords (string argument to define the query string
- num_urls (integer argument for number of wikipedia pages to extract from)
- output (output json-file name)

The script searches the keyword, stores the related urls and fianlly writes the extarcted information on a json file.


Task 2 - PDF content extractor

This task required alot of dependencies. It lookes like a basic pdf content extraction task but actually was quite tricky. 

All the pdf files had marathi content which is difficult to extract using normal libraries like pdfminer etc.

So I switched to using OCR- Optical Character Recognition. 

For that the first step was to convert all teh pages from a pdf into images.Then we use tesseract to perform OCR. This extracts texts from the images. Finally I stored this data in a json file as was requested.

I faced alot of issues while performing this task. It involved dealing with alot of libraries and dependencies hence I faced installation issues.

Another issue was related to the language of the pdf files. Since it was Marathi some language packages were required to be downloaded for the tesseract library to recognize the text and extract it.

Final issue was related to the size of the files.

Currently I have written a script which takes in the pdf url and extracts text from a limited number of pages from the pdf. Then it stores the content in the prescribed format in a json file.
