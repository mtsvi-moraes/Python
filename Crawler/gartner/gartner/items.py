# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import Compose, MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def get_all_items(item):
    return item.get_all()



class GartnerItem(scrapy.Item):
    # define the fields for your item here like:
    #article = scrapy.Field(input_processor=MapCompose(remove_tags, get_all_items), output_processor=Join())
    #date = scrapy.Field(input_processor=MapCompose(remove_tags, get_all_items), output_processor=Join())