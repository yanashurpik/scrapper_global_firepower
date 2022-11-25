from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from fire_power_scraper.spiders.man_power_all_countries import ManPowerSpider


process = CrawlerProcess(get_project_settings())
process.crawl(ManPowerSpider)
process.start()
