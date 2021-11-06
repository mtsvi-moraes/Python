import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from parsel import Selector


class BlogSpider(CrawlSpider):
    name = 'blog'
    allowed_domains = ['ai.googleblog.com']
    start_urls = ['https://ai.googleblog.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//h2[@class='title']/a")), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//span[@id='blog-pager-older-link']/a")))
    )

    def parse_item(self, response):
        yield {
            'Title': response.xpath("normalize-space(/html/head/title/text())").get(),
            'Date': response.xpath("normalize-space(//span[@class='publishdate']/text())").get(),
            'Contributor': response.xpath("normalize-space(//*[@class='byline-author']/text())").get(),
            'Link': response.url
        }
