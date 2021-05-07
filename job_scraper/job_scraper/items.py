# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_backslashn(value):
    return value.strip()


class JobScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_backslashn), output_processor=TakeFirst())
    company = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_backslashn), output_processor=TakeFirst())
    rating = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_backslashn), output_processor=TakeFirst())
    location = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_backslashn), output_processor=TakeFirst())
    salary = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_backslashn), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_backslashn))
