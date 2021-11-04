import scrapy


class AccentureNewsroomSpider(scrapy.Spider):
    name = 'accenture_newsroom'
    allowed_domains = ['newsroom.accenture.com']
    Page = 1
    INCREMENTED_BY = 1
    start_urls = ['https://newsroom.accenture.com']

    def parse(self, response):
        title = response.xpath("//h4[@class='media-heading']")
        for answer in title:
            heading = answer.xpath('normalize-space(.//a/text())').get(),
            link = answer.xpath('.//@href').get()

            yield response.follow(url=link, callback=self.parse_article, meta={'Title': heading})
            
            self.Page += self.INCREMENTED_BY
            yield scrapy.Request(
                url= f'https://newsroom.accenture.com/?page={self.Page}',
                callback= self.parse
            )
            

    
    def parse_article(self, response):
        name = response.request.meta['Title']
        date2 = response.xpath("normalize-space(//div[@class='col-xs-12 rel-date']/text())").get(),
        for day in response.xpath("normalize-space(//div[@id='tek-wrap-centerwell']/article/div[1]/text())"):
                   
            date = day.get()

            yield {
                'Title': name,
                'Date': (date) or (date2),
                'Link': response.url
            }


        # self.Page += self.INCREMENTED_BY
        # page = response.xpath("//li[@class='next ']/a")
        # url_base = 'https://newsroom.accenture.com'
        # for req in page:
        #     next_page = req.xpath(".//@href").extract_first()
        #     if next_page:
        #             yield scrapy.Request(url=url_base+next_page+'l', dont_filter=True, callback=self.parse)
