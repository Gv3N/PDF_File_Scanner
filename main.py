# A PDF to text scanner. Planned to use as resume recommendation system.

# references:
# Links to all possible libs about pdf to text :
# https://stackabuse.com/working-with-pdfs-in-python-reading-and-splitting-pages/
# links to working system, using pypdf2, textract & nltk libs:
# https://medium.com/better-programming/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f
# Links to other related things:
# https://automatetheboringstuff.com/chapter13/
# https://stackoverflow.com/questions/17098675/searching-text-in-a-pdf-using-python

# import libs
import PyPDF2  # using this to convert text based pdf into text
import textract  # using this to convert scanned pdf files into text

# import nltk  # using this to clean[remove punctuation] & convert phrases into keywords
# if any error prompt if required then follow as it says. for me it is download >>>nltk.download('punkt') & stopwords
# The word_tokenize() function will break our text phrases into individual words.
from nltk.tokenize import word_tokenize

# We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc.
# that don't hold much value as keywords.
from nltk.corpus import stopwords


# PART 1 : Read PDF file  # if there many files use for loops

filename = r'C:\Users\bakta\Desktop\testzone\testpdf.pdf'  # for better efficient use pathlib (python 3.4 & above)

pdfFileObj = open(filename, 'rb')  # rb: Opens a file for reading only in binary format.

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # a readable obj that will be parsed

# checks for number of pages that needed to be parsed
num_pages = pdfReader.numPages
count = 0
text = ""

# while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)  # create a obj to store the page
    count += 1
    text += pageObj.extractText()  # store all the text elements into text as string

# This if statement exists to check if the above library returned words.
# It's done because PyPDF2 cannot read scanned files.

if text != "":
    text = text
else :
    text = textract.process(filename, method='tesseract', language='eng')  # (file path, method,encoding)

# print(text)
# text variable contains all the text elements & contains lot of spaces & junk etc.
# we clean our text and return it as a list of keywords
# -------------------------------FOR FAR LOOPS WORKS, TESTED

# PART 2: Convert text into keywords
tokens = word_tokenize(text)  # breaks text phrases into words

punctuations = ['(',')',';',':','[',']',',']  # list of punctuations to clean

stop_words = stopwords.words('english')  # removes useless word , refer import for more details

# We create a list comprehension that only returns a list of words that are
# NOT IN stop_words and NOT IN punctuations.

keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
print(keywords)

# based on pdf format some text may distorted. So not 100% accurate as expected.
# Just need to format the pdf the way it able to detect accurately.
