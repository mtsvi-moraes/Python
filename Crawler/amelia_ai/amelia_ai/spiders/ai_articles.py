import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AiArticlesSpider(CrawlSpider):
    name = 'ai_articles'
    allowed_domains = ['amelia.ai']
    start_urls = ['https://amelia.ai/media/page/1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='blocks post four']/li/a[@class='block-link']")), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="ai-load-more"]')), follow=True),
    )

    def parse_item(self, response):
        yield {
            'Title': response.xpath("(//span[@class='heading-title']/span/span)[1]/text()").get(),
            'Date': response.xpath('//*[@id="post-details"]/text()').get(),
            'Link': response.url
        }
