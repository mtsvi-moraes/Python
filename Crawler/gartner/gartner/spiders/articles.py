import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['www.gartner.com/smarterwithgartner/archive']
    start_urls = ['http://www.gartner.com/smarterwithgartner/archive/']

    def parse(self, response):
        articles = response.xpath('//div/h4/text()').getall()
        title = response.xpath('//*[@id="gartnerinternalpage-b3a76c580b"]/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div/h2/text()').get()

        yield {
            'Title': title,
            'Articles': articles
        }
