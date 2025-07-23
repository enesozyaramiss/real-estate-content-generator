from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class ListingType(str, Enum):
    SALE = "sale"
    RENT = "rent"

class Language(str, Enum):
    ENGLISH = "en"
    PORTUGUESE = "pt"

class Location(BaseModel):
    city: str
    neighborhood: str
    
class Features(BaseModel):
    bedrooms: int
    bathrooms: int
    area_sqm: int
    balcony: bool = False
    parking: bool = False
    elevator: bool = False
    floor: Optional[int] = None
    year_built: Optional[int] = None

class PropertyData(BaseModel):
    title: str
    location: Location
    features: Features
    price: int
    listing_type: ListingType
    language: Language

class ContentSection(BaseModel):
    tag: str
    content: str
    
class GeneratedContent(BaseModel):
    property_id: Optional[str] = None
    language: Language
    sections: List[ContentSection]

class APIResponse(BaseModel):
    success: bool
    data: Optional[GeneratedContent] = None
    message: Optional[str] = None
    error: Optional[str] = None