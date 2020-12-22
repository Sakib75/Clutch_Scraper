# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst,MapCompose

def parse_website(website):
    return website.split('?')[0]

def parse_focus(focus):
    return focus + ' Content Marketing'

def parse_loc(loc):
    return loc.replace(',','')


class ClutchItem(scrapy.Item):

    Company_Name = scrapy.Field(output_processor=TakeFirst())
    Website = scrapy.Field(input_processor= MapCompose(parse_website),output_processor=TakeFirst())
    Service_Focus = scrapy.Field(input_processor=MapCompose(parse_focus),output_processor=TakeFirst())
    Min_Project_Size = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(str.strip))
    Avg_Hourly_Rate = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(str.strip))
    Employees = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(str.strip))
    Locality = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(parse_loc))
    Region = scrapy.Field(output_processor=TakeFirst())

