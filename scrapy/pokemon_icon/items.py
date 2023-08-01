# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonIconItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()#num of the pokemon
    icon_src = scrapy.Field()#src of the pokemon icon
    name = scrapy.Field()#name of the pokemon

    
