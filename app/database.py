from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

DATABASE_URL = "postgresql://metoo:metoo@db:5432/db_product"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    amount_max = Column(Float)
    amount_min = Column(Float)
    availability = Column(String)
    condition = Column(String)
    currency = Column(String)
    date_seen = Column(String)
    is_sale = Column(Boolean)
    merchant = Column(String)
    shipping = Column(String)
    source_urls = Column(String)
    asins = Column(String)
    brand = Column(String)
    categories = Column(String)
    date_added = Column(String)
    date_updated = Column(String)
    ean = Column(String)
    image_urls = Column(String)
    keys = Column(String)
    manufacturer = Column(String)
    manufacturer_number = Column(String)
    name = Column(String)
    primary_categories = Column(String)
    upc = Column(String)
    weight = Column(String)
