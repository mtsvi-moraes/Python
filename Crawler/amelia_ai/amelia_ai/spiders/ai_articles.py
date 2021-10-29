import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AiArticlesSpider(CrawlSpider):
    name = 'ai_articles'
    allowed_domains = ['www.amelia.ai']
    start_urls = ['https://amelia.ai/blog/page/2']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='blocks post four']/li/a[@class='block-link']")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'Title': response.xpath("//p[@id='post-details']/b/text()").get()
        }
