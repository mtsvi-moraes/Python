import scrapy


class IbmSpider(scrapy.Spider):
    name = 'ibm'
    allowed_domains = ['www.newsroom.ibm.com']
    start_urls = ['https://newsroom.ibm.com/announcements']

    def parse(self, response):
        archive = response.css('#wd_printable_content .wd_title a')
        lk = response.xpath("//div[@class='wd_title']/a[@href]")
        for title, txt in archive, lk:
            file =  title.css('::text').getall(),
            link = txt.getall()

            yield response.Request(url=link, callback=self.parse_article, meta={'Article': file})
    
    def parse_article(self, response):
        article = response.request.meta['Article']
        day = response.xpath("//div[@class='wd_date']")
        for d in day:
            date = d.xpath('.//text()').get()

            yield {
                'Article': article,
                'Date': date
            }
        
        
        # next_page = response.xpath("//li[@class='wd_page_link wd_page_next']/a[@href]/text()").getall()

        # while next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse)
