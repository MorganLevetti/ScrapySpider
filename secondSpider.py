import requests
from scrapy.selector import Selector

response = requests.get('https://www.annoncesbateau.com/')
data = Selector(text=response.text)

# divs = data.xpath('//*[@class="content"]/p')
divs = data.xpath("//ol/li/div/div[@class='description']/div/div[@class='name']/h2/text()").getall()


print(divs)

    