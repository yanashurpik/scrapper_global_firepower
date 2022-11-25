from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Date, DateTime, Float, Boolean, Text
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    country_name = Column("country_name", String(100), unique=True)


class ManPower(Base):

    __tablename__ = "man_power"

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey("country.id"), unique=True)
    total_population = Column("total_population", Text())
    available_manpower = Column("available_manpower", Text())
    fit_for_service = Column("fit_for_service", Text())
    tot_military_personnel = Column("tot_military_personnel", Text())
    active_personnel = Column("active_personnel", Text())
    reserve_personnel = Column("reserve_personnel", Text())
    paramilitary = Column("paramilitary", Text())

    country = relationship("Country", backref=backref("man_power", uselist=False))
