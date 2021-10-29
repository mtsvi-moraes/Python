import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IbmSpider(CrawlSpider):
    name = 'ibm'
    allowed_domains = ['www.research.ibm.com']
    
    def start_requests(self):
        headers = {
            'authority': 'in.hotjar.com',
            'method': 'POST',
            'path': '/api/v2/client/sites/42920/visit-data?sv=5',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-length': '129',
            'content-type': 'text/plain; charset=UTF-8',
            'origin': 'https://research.ibm.com',
            'referer': 'https://research.ibm.com/',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
        }
        yield scrapy.Request('https://research.ibm.com/publications', headers=headers)

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//h2[@class='PublicationListItem_title__2qvDX']/a")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'Title': response.xpath('//h1/text()')
        }
