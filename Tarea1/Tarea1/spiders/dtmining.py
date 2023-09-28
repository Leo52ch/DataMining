import scrapy


class DtminingSpider(scrapy.Spider):
    name = "dtmining"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/index.html"]

    def parse(self, response):
        pass
