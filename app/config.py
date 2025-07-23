import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # Google Gemini Configuration (FREE)
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    gemini_temperature: float = float(os.getenv("GEMINI_TEMPERATURE", "0.7"))
    gemini_max_output_tokens: int = int(os.getenv("GEMINI_MAX_OUTPUT_TOKENS", "8192"))
    
    # Application Settings
    app_name: str = os.getenv("APP_NAME", "Real Estate Content Generator")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"

# Global settings instance
settings = Settings()

# Content generation limits
CONTENT_LIMITS = {
    "title_max_chars": 60,
    "meta_description_max_chars": 155,
    "description_min_chars": 500,
    "description_max_chars": 700,
    "key_features_count": 5,
    "neighborhood_min_chars": 150,
    "neighborhood_max_chars": 300,
    "call_to_action_max_chars": 100
}

# SEO Keywords by language
SEO_KEYWORDS = {
    "en": {
        "base_terms": ["apartment", "property", "real estate", "for sale", "for rent"],
        "location_templates": ["{property_type} in {city}", "{property_type} {neighborhood}"],
        "action_words": ["buy", "rent", "schedule", "visit", "discover", "explore"],
        "features": ["bedrooms", "bathrooms", "balcony", "parking", "elevator", "modern"]
    },
    "pt": {
        "base_terms": ["apartamento", "propriedade", "imóvel", "venda", "arrendamento"],
        "location_templates": ["{property_type} em {city}", "{property_type} {neighborhood}"],
        "action_words": ["comprar", "arrendar", "agendar", "visitar", "descobrir", "explorar"],
        "features": ["quartos", "casas de banho", "varanda", "estacionamento", "elevador", "moderno"]
    }
}