import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AccentureNewsSpider(CrawlSpider):
    name = 'accenture_news'
    allowed_domains = ['newsroom.accenture.com']
    start_urls = ['http://newsroom.accenture.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//h4[@class='media-heading']/a")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'Title': response.xpath('//*[@id="content-details"]/div[1]/div[1]/strong/text()').get(),
            'Date': response.xpath('//*[@id="tek-wrap-centerwell"]/article/div[1]/text()').get(),
            'e-mail': response.xpath('//*[@id="content-details"]/div[1]/a[6]/text()').get(),
            'Contributors': response.xpath('//*[@id="content-details"]/div[1]/text()[28]').get()
        }
        
