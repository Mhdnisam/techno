# file = input("enter your file name:")
# search = input("search word:")
# try:
#     with open(file, "r", encoding='utf-8') as file:
#         found = False
#         for line in file:
#             if search in line:
#                 print(line.strip())
#                 found = True
#         if not found:
#             print("word not found")
# except FileNotFoundError:
#     print("file note found")
import pdfplumber

file = input("Enter your PDF file name: ")
search = input("Search word: ")

try:
    with pdfplumber.open(file) as pdf:
        found = False
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    if search in line:
                        print(line.strip())
                        found = True
        if not found:
            print("Word not found")
except FileNotFoundError:
    print("File not found")

