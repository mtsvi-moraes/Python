import scrapy


class AmeliaSpider(scrapy.Spider):
    name = 'amelia'
    allowed_domains = ['www.amelia.ai']
    start_urls = ['https://www.amelia.ai/blog/page/1']

    def parse(self, response):
        text = response.css("#search-results-wrapper .heading-title span span")
        for x in text:
            item = x.css('::text').getall()
            
     

        yield {
            'Title': item
        }
