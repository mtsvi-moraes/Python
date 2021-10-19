import scrapy

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['www.gartner.com']
    start_urls = ['http://www.gartner.com/smarterwithgartner']

    def parse(self, response):
        link = response.xpath('//a[contains(@data-elem-attr, "href=url;data-type=tags")]')
        for site in link:
            website = site.xpath('.//@href').get()
            yield response.follow(url=website, callback=self.get_information, meta={'Link': website})

    def get_information(self, response):
        link = response.request.meta['Link']
        title = response.xpath('//h1/text()').get()
        pub = response.xpath('(//p/span[@class="p-small"])[1]')
        for day in pub:
            publication_date = day.xpath('.//text()').get()
        #journalist = response.xpath('//p/span[@class="p-small"])[2]')
        #for publication in journalist:
            #contributor = publication.xpath('.//text()').get()
        
            yield {
                'Title': title,
                'Date': publication_date,
                'Link': link
                #'Contributor': contributor
            }