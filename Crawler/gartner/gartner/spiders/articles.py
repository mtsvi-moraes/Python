import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['www.gartner.com/smarterwithgartner']
    start_urls = ['http://www.gartner.com/smarterwithgartner']

    def parse(self, response):
        articles = response.css('.rmg-t56 .h4::text').getall()
        date = response.css('.text .p-small::text').getall()

        yield {
            'Articles': articles,
            'Date': date
        }
