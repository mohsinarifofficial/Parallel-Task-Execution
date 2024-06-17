import requests
from bs4 import BeautifulSoup


from celery import Celery

app = Celery('web_scraping', broker='redis://127.0.0.1', backend='redis://127.0.0.1')

app.conf.update(
    result_expires=3600,
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
)
@app.task
def scrape_page_task(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, 'lxml')
        
        # Example: Extracting all the headings (h1 tags)
        headings = soup.find_all('h2')
        
        
        return [heading.get_text() for heading in headings]
    else:
        
        return None

# # Example usage
# url = "https://www.coursera.org/articles/data-science-vs-machine-learning"
# headings = scrape_page(url)
# print(headings)



# html=requests.get("https://www.linkedin.com/pulse/poverty-pakistan-sdg-goal-1-professor-dr-qais-aslam#:~:text=SDG1%20has%20seven%20targets%20as,312)%20a%20day%E2%80%9D.")
# raw_sdg=BeautifulSoup(html.text,"lxml")
# raw_sdg=raw_sdg.find_all("div",class_="article-main__content")
# SDG1=Get_Cleaned_String(raw_sdg)
# SDG1=SDG1.replace("Professor Dr. Qais Aslam (dr.qais@ucp.edu.pk)","")
# #print(SDG1)