#  Real Estate Content Generator

AI-powered content generator for real estate property listings using Google Gemini 1.5 Flash API. Generates SEO-optimized, multilingual HTML content for property listing pages.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Gemini](https://img.shields.io/badge/Google-Gemini_1.5_Flash-orange.svg)](https://ai.google.dev/)

##  Features

- ** AI-Powered Content** - Uses Google Gemini 1.5 Flash 
- ** Multilingual** - English & Portuguese with proper localization
- ** SEO Optimized** - Keyword-rich, search engine ready content
- ** Fast & Async** - Non-blocking API architecture
- ** Structured Output** - 7 HTML sections ready for web integration
- ** Auto Documentation** - Interactive Swagger UI

## Generated Content Sections

| Section | HTML Tag | Purpose | Limit |
|---------|----------|---------|-------|
| Page Title | `<title>` | Browser tab & SEO | 60 chars |
| Meta Description | `<meta name="description">` | Search snippet | 155 chars |
| Main Headline | `<h1>` | Visible page title | - |
| Property Description | `<section id="description">` | Rich content | 500-700 chars |
| Key Features | `<ul id="key-features">` | Bullet points | 3-5 items |
| Neighborhood Info | `<section id="neighborhood">` | Area description | 150-300 chars |
| Call to Action | `<p class="call-to-action">` | Conversion message | 100 chars |

##  Installation & Setup

### Prerequisites
- Python 3.8+
- Google Gemini API Key (free from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Quick Start

```bash
# 1. Clone and setup environment
git clone <repository-url>
cd real-estate-content-generator
python -m venv venv

# Activate virtual environment
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env with your Gemini API key
```

### Environment Configuration

Create `.env` file:

```env
# Google Gemini Configuration (FREE)
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-flash
GEMINI_TEMPERATURE=0.7
GEMINI_MAX_OUTPUT_TOKENS=8192

# Application Settings
DEBUG=True
APP_NAME=Real Estate Content Generator
```

### Run the Application

```bash
uvicorn main:app --reload --port 8000

# Server starts at: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## API Usage

### Health Check

```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy",
  "gemini_configured": true,
  "model": "gemini-1.5-flash"
}
```

### Generate Complete Content

**Endpoint:** `POST /generate-content`

```bash
curl -X POST "http://localhost:8000/generate-content" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "T3 apartment in Lisbon",
       "location": {
         "city": "Lisbon",
         "neighborhood": "Campo de Ourique"
       },
       "features": {
         "bedrooms": 3,
         "bathrooms": 2,
         "area_sqm": 120,
         "balcony": true,
         "parking": false,
         "elevator": true,
         "floor": 2,
         "year_built": 2005
       },
       "price": 650000,
       "listing_type": "sale",
       "language": "en"
     }'
```

**Response:**
```json
{
  "success": true,
  "data": {
    "language": "en",
    "sections": [
      {
        "tag": "title",
        "content": "<title>T3 Apartment for Sale in Campo de Ourique, Lisbon</title>"
      },
      {
        "tag": "meta_description",
        "content": "<meta name=\"description\" content=\"Spacious 3-bedroom apartment in Lisbon with balcony and elevator, located in Campo de Ourique. Ideal for families.\">"
      },
      {
        "tag": "headline",
        "content": "<h1>Modern T3 Apartment with Balcony in Campo de Ourique, Lisbon</h1>"
      }
      // ... 4 more sections
    ]
  },
  "message": "Content generated successfully"
}
```

### Generate Single Section

```bash
curl -X POST "http://localhost:8000/generate-section?section_name=title" \
     -H "Content-Type: application/json" \
     -d @tests/sample_data/sample_en.json
```

Available sections: `title`, `meta_description`, `headline`, `description`, `key_features`, `neighborhood`, `call_to_action`

## Multilingual Support

### Supported Languages

- **English:** `"language": "en"`
- **Portuguese:** `"language": "pt"`

### Language Features

- **Localized Grammar** - Natural expressions for each language
- **SEO Keywords** - Language-appropriate search terms  
- **Real Estate Terms** - "apartment" vs "apartamento", "sale" vs "venda"
- **Cultural Adaptation** - Local market terminology

### Portuguese Example

```json
{
  "title": "Apartamento T3 em Lisboa",
  "location": {
    "city": "Lisboa", 
    "neighborhood": "Campo de Ourique"
  },
  "language": "pt"
  // ... rest of the data
}
```

## System Architecture

### How It Works

```
JSON Property Data → FastAPI → AI Prompts → Gemini API → HTML Content → User
```

**Flow Breakdown:**
1. **Input:** User sends property data in JSON format
2. **Validation:** FastAPI + Pydantic validates the data structure
3. **Processing:** System builds context and selects language-specific prompts
4. **AI Generation:** 7 separate calls to Gemini API (one per HTML section)
5. **Output:** Returns structured JSON with HTML-tagged content sections

### Project Structure

```
real-estate-content-generator/
├── main.py                       # FastAPI application
├── requirements.txt              # Dependencies
├── .env.example                  # Environment template
├── app/
│   ├── models.py                 # Pydantic data models
│   ├── config.py                 # Configuration & constants
│   └── services/
│       └── content_generator.py  # AI content generation
├── templates/
│   └── prompts/
│       ├── english_prompts.py    # English AI prompts
│       └── portuguese_prompts.py # Portuguese AI prompts
└── tests/
    ├── test_api.py              # API tests
    └── sample_data/
        ├── sample_en.json       # Test data (English)
        └── sample_pt.json       # Test data (Portuguese)
```

## Technical Details

### Architecture

- **FastAPI** - Modern Python web framework with automatic API docs
- **Pydantic** - Data validation and serialization
- **Google Gemini 1.5 Flash** - Free AI model for content generation
- **Async/Await** - Non-blocking architecture for better performance

```json
// Example error response
{
  "success": false,
  "error": "Failed to generate content",
  "message": "Please try again later"
}
```

## Testing

Test the API with sample data:

```bash
# Test English content generation
curl -X POST "http://localhost:8000/generate-content" \
     -H "Content-Type: application/json" \
     -d @tests/sample_data/sample_en.json

# Test Portuguese content generation
curl -X POST "http://localhost:8000/generate-content" \
     -H "Content-Type: application/json" \
     -d @tests/sample_data/sample_pt.json

# Test single section generation
curl -X POST "http://localhost:8000/generate-section?section_name=title" \
     -H "Content-Type: application/json" \
     -d @tests/sample_data/sample_en.json

# Health check
curl http://localhost:8000/health
```

## SEO Guidelines

### What the System Does

 **Includes key searchable phrases:**
- "apartment for sale in Lisbon" 
- "T3 apartment in Campo de Ourique"
- "real estate in Portugal"

 **Optimizes content structure:**
- Proper HTML tags for each section
- Character limits for SEO best practices
- Natural keyword integration

 **Multilingual SEO:**
- Language-specific keywords
- Local search optimization
- Cultural adaptation

### Monitoring

Use the health endpoint for monitoring:

```bash
curl http://your-domain.com/health
```

**Built with Google Gemini 1.5 Flash, FastAPI, and modern Python for the AI Engineer Technical Challenge.**

Enes Ozyaramis.