#Description: This programs scrapes FAKE and REAL news data from a website
import requests
from bs4 import BeautifulSoup


URL = "https://www.politifact.com/factchecks/list/?page=2"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
tag = soup.body
results = soup.find(id="top")
job_elements = results.find_all("article", class_="m-statement")

for job_element in job_elements:
    author_element = job_element.find("div", class_="m-statement__meta")
    # location_element = job_element.find("p", class_="location")
    print(author_element, end="\n"*4)





