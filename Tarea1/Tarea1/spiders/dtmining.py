import scrapy


class DtminingSpider(scrapy.Spider):
    name = "dtmining"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        products = response.css('article.product_pod')
        for product in products:
            yield {
                'nombre' : product.css('h3').css('a::attr(title)').get(),
                'precio' : product.css('article.product_pod').css('div.product_price').css('p.price_color::text').get(),
                'url' : product.css('h3').css('a::attr(href)').get()
            }
        siguiente_pag = response.css('li.next').css('a::attr(href)').get()

        if siguiente_pag is not None:
            siguiente_pag_url = "https://books.toscrape.com/catalogue/"+siguiente_pag
            yield response.follow(siguiente_pag_url,callback=self.parse)