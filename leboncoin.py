#Description: This programs scrapes FAKE and REAL news data from a website
import requests
from bs4 import BeautifulSoup

# Web URL
URL = "https://immobilierneuf.leboncoin.fr/recherche?locations=2-93&type=2&page=1"
# Get the web URL in page
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="__next")
tag = soup.body
job_elements = results.find_all("div", class_="lieiNA")

# requests.get('https://api.github.com')
# Boucle for, get all string in body
for string in tag.strings:
    print(string)
