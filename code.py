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
