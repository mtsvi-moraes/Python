import scrapy
from amazon.items import AmazonItem


class AlexaBlogSpider(scrapy.Spider):
    name = 'alexa_blog'
    allowed_domains = ['developer.amazon.com']
    start_urls = ['https://developer.amazon.com/en-US/blogs/alexa/device-makers#!1']

    def parse(self, response):
        item = response.xpath("//*[@class='blog__desc-item blog__desc-item--title']/a/text()").get()
        yield {
            'title': item
        }
