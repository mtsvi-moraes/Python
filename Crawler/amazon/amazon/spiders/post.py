import scrapy


class PostSpider(scrapy.Spider):
    name = 'post'

    payload = """

        {"resultSize":"9","pagePath":"/content/alexa-blog/en_US/blogs/alexa/device-makers","searchPath":"/content/alexa-blog/","listTags":["blogs:en-US/alexa/device-makers","blogs:en-US/alexa/connected-devices","blogs:en-US/alexa/gadgets"],"sortOrder":"desc","searchPathAuthorTag":"/content/cq:tags/blogs/tags/authors","searchPathTopicsTag":"/content/cq:tags/blogs/tags/topics","completePageUrl":"/en-US/blogs/alexa/device-makers","currentPage":1}


    """
    
    def start_requests(self):
        yield scrapy.Request(
            url= 'developer.amazon.com/alexa/alexa-skills-kit/proxy/blogs.js',
            method= 'POST',
            body= self.payload,
            headers= {
                'Content-Type': 'application/json'
            }
        )

    def parse(self, response):
        response.body()
