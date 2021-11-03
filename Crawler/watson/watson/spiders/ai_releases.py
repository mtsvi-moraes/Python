import scrapy


class AiReleasesSpider(scrapy.Spider):
    name = 'ai_releases'
    allowed_domains = ['research.ibm.com']
    start_urls = ['https://research.ibm.com/blog?tag=artificial-intelligence']

    def parse(self, response):
        yield {
            'Title': [title.getall() for title in response.css("//h2[@class='PostCard_title__2emhy']/a/span/text() | //h2[@class='PostCard_title__2emhy']/a/text()")]
        }
        