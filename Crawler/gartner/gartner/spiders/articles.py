import scrapy

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['www.gartner.com']
    start_urls = ['http://www.gartner.com/smarterwithgartner']

    def parse(self, response):
        articles = [item.strip() for item in response.css('.rmg-t56 .h4::text').getall()]
        date = [item.strip() for item in response.css('.text .p-small::text').getall()]
        link = response.xpath('//a[contains(@data-elem-attr, "href=url;data-type=tags")]')
        for site in link:
            website = site.xpath('.//@href').get()
            yield response.follow(url=website)
