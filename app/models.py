from typing import List, Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    amount_max: Optional[float]
    amount_min: Optional[float]
    availability: Optional[str]
    condition: Optional[str]
    currency: Optional[str]
    date_seen: Optional[str]
    is_sale: Optional[bool]
    merchant: Optional[str]
    shipping: Optional[str]
    source_urls: Optional[str]
    asins: Optional[str]
    brand: Optional[str]
    categories: Optional[str]
    date_added: Optional[str]
    date_updated: Optional[str]
    ean: Optional[str]
    image_urls: Optional[str]
    keys: Optional[str]
    manufacturer: Optional[str]
    manufacturer_number: Optional[str]
    name: Optional[str]
    primary_categories: Optional[str]
    upc: Optional[str]
    weight: Optional[str]

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str

    class Config:
        orm_mode = True
