#txt files
def read(file_path):
    file=open(file_path,"r",encoding="utf-8")
    return file.read()
def write(file_path,text):
    file=open(file_path,"a",encoding="utf-8")
    file.write(text)

# csv file

import csv

def write(file_path,data):
    file=open(file_path,"a",newline='')
    csv.writer(file).writerows(data)

def read(file_path):
    file=open(file_path,"r")
    return csv.reader(file)

data=[['Name', 'Age', 'City'],
    ['Alice', 30],
    ['Bob', 25, 'Los Angeles']]
write("new.csv",data)
csv_file=read("new.csv")

for i in csv_file:
    print(i)

# pdf
import PyPDF2
from fpdf import FPDF
def read_pdf(file_path):
    file=open(file_path,"rb")
    reader = PyPDF2.PdfReader(file)
    text = ""
    # Iterate through each page and extract text
    for page in reader.pages:
        text += page.extract_text()
    return text

def write(file_path,data):
    data=data.encode("latin-1","ignore").decode("latin-1")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data)
    pdf.output(file_path)

text = read_pdf("3_1_8_Gajski_137-147_accepted_31.10.2023.pdf")
print(text)
write("my.pdf",text)

