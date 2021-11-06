import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AlexaSpider(CrawlSpider):
    name = 'alexa'
    allowed_domains = ['developer.amazon.com']
    start_urls = ['https://developer.amazon.com/en-US/blogs/alexa/device-makers#!1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='blog__desc-item blog__desc-item--title']/a")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'link': response.url #xpath("//*[@class='blog-post-component__title-text mb-2']/text()").get()
        }
