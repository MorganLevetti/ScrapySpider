import requests
from scrapy.selector import Selector

download_path = "data/"
response = requests.get("https://www.annoncesbateau.com/")
data = Selector(text=response.text)

articles = data.xpath("//div[@class='main-content-body']/section[@class='latest-boats']/ol/li/div/div[@class='description']/div/div[@class='name']/h2/text()").getall()

print(articles)