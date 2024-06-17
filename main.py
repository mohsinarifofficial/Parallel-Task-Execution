from celery import group
import web_Scraping
from web_Scraping import scrape_page_task


# List of URLs to scrape
urls = [
    'https://www.coursera.org/articles/data-science-vs-machine-learning',
    'https://www.coursera.org/degrees/global-mph-imperial'
    
    # Add more URLs as needed
]

# Dispatch tasks in parallel

task_group = group(scrape_page_task.s(url) for url in urls)

result = task_group.apply_async()

# Wait for tasks to complete and gather results
results = result.get(timeout=120)
print("hy")
# Print results
for i, headings in enumerate(results):
    print(f'Headings from {urls[i]}: {headings}')
