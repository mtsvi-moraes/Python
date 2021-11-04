import scrapy


class AzureSpider(scrapy.Spider):
    name = 'azure'
    page = 1
    allowed_domains = ['azure.microsoft.com']
    start_urls = ['https://azure.microsoft.com/en-us/blog/?page=1']

    def parse(self, response):
        for info in response.xpath(
            "//*[@class='text-heading3']/a"):
            article= info.xpath(
                "normalize-space(.//text())").get()
            link= info.xpath(
                "normalize-space(.//@href)").get()

            yield response.follow(
                url=link,
                callback=self.parse_microsoft_link, 
                meta={'Article': article}
            )

            self.page += 1
            yield scrapy.Request(
                f'https://azure.microsoft.com/en-us/blog/?page={self.page}',
                callback=self.parse
            )

    def parse_microsoft_link(self, response):
        title = response.request.meta['Article']
        Date = response.xpath(
            "//*[@class='text-body5']/text()").get()
        contributor = response.xpath(
            "//*[@class='name with-position']/a/text()").get()
        role = response.xpath(
            "//*[@class='position']/text()").get()
        yield {
            'Article': title,
            'Date': Date,
            'Contributor': contributor,
            'Role': role
        }
