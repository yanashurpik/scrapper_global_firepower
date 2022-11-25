from fire_power_scraper.models import db_connect
from sqlalchemy.orm import sessionmaker

from fire_power_scraper.models import create_table, Country, ManPower


class SaveQuotesPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        country = Country()
        manpower_metrics = ManPower()
        country.country_name = item["country_name"]
        manpower_metrics.total_population = item["total_population"]
        manpower_metrics.available_manpower = item["available_manpower"]
        manpower_metrics.tot_military_personnel = item["tot_military_personnel"]
        manpower_metrics.fit_for_service = item["fit_for_service"]
        manpower_metrics.active_personnel = item["active_personnel"]
        manpower_metrics.reserve_personnel = item["reserve_personnel"]
        manpower_metrics.paramilitary = item["paramilitary"]

        # check whether the country exists
        exist_country = (
            session.query(Country).filter_by(country_name=country.country_name).first()
        )
        if exist_country is not None:  # the current country exists
            country = exist_country
            manpower_metrics.country_id = exist_country.id
        else:
            country = country
            manpower_metrics.country_id = country.id

        exist_country = session.query(ManPower).filter_by(country_id=country.id).first()
        if exist_country is not None:  # the current country exists
            manpower_metrics = exist_country

        try:
            session.add(manpower_metrics)
            session.add(country)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
