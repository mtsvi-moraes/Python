import scrapy
import chromedriver_autoinstaller
import selenium
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector


class AlexaSpider(scrapy.Spider):
    name = 'alexa'
    
    def start_requests(self):
        yield SeleniumRequest(
            url = 'https://developer.amazon.com/en-US/blogs/alexa/device-makers',
            wait_time= 3,
            callback= self.parse,
            screenshot= True
        )



    def parse(self, response):
        # img = response.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)
        items = response.xpath("//*[@class='blog__desc-item blog__desc-item--title']/a")
        for item in items:
            title = item.xpath("normalize-space(.//text())").get()
            links = item.xpath(".//@href").get()

            yield response.follow(
                url = links,
                callback= self.parse_articles,
                meta = {
                    'Title': title
                }
            )
       
        next_page: response.xpath("//*[@id='#!+1']/@href").get()
        if next_page:
            absolute_url = f'https://developer.amazon.com/en-US/blogs/alexa/device-makers{next_page}'
            yield SeleniumRequest(
                url = absolute_url,
                wait_time= 3,
                callback= self.parse
            )

    
    def parse_articles(self, response):
        article = response.meta['Title']
        date = response.xpath(
            "//*[@class='blog-post-component__date']/text()").get()
        contributor = response.xpath(
            "normalize-space(//*[@class='blog__desc-item blog__desc-item--author mr-2']/a/text())").get()
        yield {
            'Title': article,
            'Date': date,
            'Contributor': contributor
        }


