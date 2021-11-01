import scrapy


class AmeliaSpider(scrapy.Spider):
    name = 'amelia'
    allowed_domains = ['amelia.ai']
    start_urls = ['https://amelia.ai/media/page/1']

    def parse(self, response):
        title = response.xpath("//span[@class='selectorgadget_suggested']/span/text()")
        for element in title:
            t = element.xpath.get()
      
            
     

        yield {
            'Title': t
        }
