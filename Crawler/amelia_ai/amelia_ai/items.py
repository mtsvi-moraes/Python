# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmeliaAiItem(scrapy.Item):
    Title = scrapy.Field()
    Date = scrapy.Field()
    Link = scrapy.Field()
