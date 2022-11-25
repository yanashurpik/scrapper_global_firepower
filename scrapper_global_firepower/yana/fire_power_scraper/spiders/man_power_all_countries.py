import scrapy
from scrapy.loader import ItemLoader
from fire_power_scraper.items import ManPowerItem


class ManPowerSpider(scrapy.Spider):
    name = "manpower-all"
    allowed_domains = ["globalfirepower.com"]
    start_urls = ["https://www.globalfirepower.com/countries.php"]

    # x-paths
    country_name = "//h1/text()"
    total_population = (
        '//span[text()="Total Population:"]/following-sibling::span/text()'
    )
    available_manpower = (
        '//span[text()="Available Manpower"]/following-sibling::span/span/text()'
    )
    fit_for_service = (
        '//span[text()="Fit-for-Service"]/following-sibling::span/span/text()'
    )
    tot_military_personnel = '//span[text()="Tot Military Personnel (est.)"]/following-sibling::span/span/text()'
    active_personnel = (
        '//span[text()="Active Personnel"]/following-sibling::span/span/text()'
    )
    reserve_personnel = (
        '//span[text()="Reserve Personnel"]/following-sibling::span/span/text()'
    )
    paramilitary = '//span[text()="Paramilitary"]/following-sibling::span/span/text()'

    def parse(self, response):
        self.logger.info("Parse function called on {}".format(response.url))
        countries = response.xpath("//body/div[9]//child::a")
        manpower = response.xpath(
            '//a[@title="Total populations listed by country"]/parent::div'
        )
        loader = ItemLoader(item=ManPowerItem(), selector=manpower)
        loader.add_xpath("country_name", self.country_name)
        loader.add_xpath("total_population", self.total_population)
        loader.add_xpath("available_manpower", self.available_manpower)
        loader.add_xpath("fit_for_service", self.fit_for_service)
        loader.add_xpath("tot_military_personnel", self.tot_military_personnel)
        loader.add_xpath("active_personnel", self.active_personnel)
        loader.add_xpath("reserve_personnel", self.reserve_personnel)
        loader.add_xpath("paramilitary", self.paramilitary)
        l = loader.load_item()
        yield l

        for country in countries:
            yield response.follow(country, self.parse)
