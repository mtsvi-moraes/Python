import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class IbmAnnouncements(CrawlSpider):
    name = 'ibm_announcements'
    allowed_domains = ['newsroom.ibm.com']
    start_urls = ['https://newsroom.ibm.com/announcements']
    

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//*[@class='wd_title']/a")), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//*[@aria-label='Show next page']")))
    )

    def parse_item(self, response):
        yield {
            'Title': response.xpath("(//h1)[2]/text()").get(),
            'Date': response.xpath("//div[@class='wd_date']/text()").get(),
            'Link': response.url
        }
