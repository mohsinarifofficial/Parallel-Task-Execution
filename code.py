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
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login")

# Login
driver.find_element(By.ID, "email").send_keys("your_email")
driver.find_element(By.ID, "pass").send_keys("your_password")
driver.find_element(By.NAME, "login").click()

# Navigate to Marketplace
time.sleep(5)
driver.get("https://www.facebook.com/marketplace")
time.sleep(5)

# Scroll and Collect Ads
ad_links = set()  # Use a set to avoid duplicates
scroll_pause_time = 2  # Pause to allow loading
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Find ad elements
    ads = driver.find_elements(By.XPATH, "//a[contains(@href, '/marketplace/item/')]")
    for ad in ads:
        ad_links.add(ad.get_attribute("href"))

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

    # Check if new content loaded
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # Exit loop if no new content is loaded
    last_height = new_height

# Print all collected ad links
print(f"Collected {len(ad_links)} ads:")
for link in ad_links:
    print(link)

# Close WebDriver
driver.quit()
