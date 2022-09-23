import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['https://www.annoncesbateau.com/']
    start_urls = ['https://www.annoncesbateau.com/']

    def parse(self, response):

        boats = response.xpath("//div[@class='content nav-slide']") 

        for boat in boats:
            boat_name = boat.xpath("//ol/li/div/div[@class='description']/div/div[@class='name']/h2/text()").getall()
            boat_adress = boat.xpath("//ol/li/div/div[@class='description']/div/div[@class='location']/text()").getall()
            boat_price = boat.xpath("//ol/li/div/div[@class='description']/div/div[@class='price']/text()").getall()
        
        yield{
            "boat name": boat_name ,"boat adress": boat_adress, "boat price": boat_price
        }
        
