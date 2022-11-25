# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def remove_comma(text):
    new_text = text.replace(",", "")
    return new_text


def get_country_name(text):
    new_text = text[5:-18]
    return new_text


class ManPowerItem(scrapy.Item):
    country_name = Field(
        input_processor=MapCompose(get_country_name), output_processor=TakeFirst()
    )
    total_population = Field(
        input_processor=MapCompose(remove_comma), output_processor=TakeFirst()
    )
    available_manpower = Field(
        input_processor=MapCompose(remove_comma), output_processor=TakeFirst()
    )
    fit_for_service = Field(
        input_processor=MapCompose(remove_comma), output_processor=TakeFirst()
    )
    tot_military_personnel = Field(
        input_processor=MapCompose(remove_comma), output_processor=TakeFirst()
    )
    active_personnel = Field(
        input_processor=MapCompose(remove_comma), output_processor=TakeFirst()
    )
    reserve_personnel = Field(
        input_processor=MapCompose(remove_comma), output_processor=TakeFirst()
    )
    paramilitary = Field(
        input_processor=MapCompose(remove_comma), output_processor=TakeFirst()
    )
