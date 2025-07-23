import google.generativeai as genai
import logging
from typing import Dict, List, Optional
import json
import re

from app.models import PropertyData, GeneratedContent, ContentSection
from app.config import settings, CONTENT_LIMITS, SEO_KEYWORDS
from templates.prompts.english_prompts import ENGLISH_PROMPTS
from templates.prompts.portuguese_prompts import PORTUGUESE_PROMPTS

logger = logging.getLogger(__name__)

class ContentGenerator:
    def __init__(self):
        self.model = None
        self.prompts = {
            "en": ENGLISH_PROMPTS,
            "pt": PORTUGUESE_PROMPTS
        }
    
    async def initialize(self):
        """Initialize Gemini Flash API (FREE)"""
        try:
            genai.configure(api_key=settings.gemini_api_key)
            
            # Gemini Flash configuration for better performance
            generation_config = genai.types.GenerationConfig(
                temperature=settings.gemini_temperature,
                max_output_tokens=settings.gemini_max_output_tokens,
                top_p=0.95,
                top_k=40,
                candidate_count=1,
            )
            
            # Safety settings for content generation
            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
            ]
            
            self.model = genai.GenerativeModel(
                model_name=settings.gemini_model,  # gemini-1.5-flash
                generation_config=generation_config,
                safety_settings=safety_settings
            )
            logger.info(f"Gemini Flash API initialized successfully with model: {settings.gemini_model}")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini Flash API: {e}")
            raise
    
    def _build_property_context(self, property_data: PropertyData) -> Dict:
        """Build context dictionary from property data"""
        context = {
            "title": property_data.title,
            "city": property_data.location.city,
            "neighborhood": property_data.location.neighborhood,
            "bedrooms": property_data.features.bedrooms,
            "bathrooms": property_data.features.bathrooms,
            "area_sqm": property_data.features.area_sqm,
            "price": property_data.price,
            "listing_type": property_data.listing_type.value,
            "language": property_data.language.value,
            "currency": "€",
        }
        
        # Add optional features
        features_list = []
        if property_data.features.balcony:
            features_list.append("balcony" if context["language"] == "en" else "varanda")
        if property_data.features.parking:
            features_list.append("parking" if context["language"] == "en" else "estacionamento")
        if property_data.features.elevator:
            features_list.append("elevator" if context["language"] == "en" else "elevador")
        if property_data.features.floor is not None:
            floor_text = f"floor {property_data.features.floor}" if context["language"] == "en" else f"andar {property_data.features.floor}"
            features_list.append(floor_text)
        if property_data.features.year_built is not None:
            year_text = f"built in {property_data.features.year_built}" if context["language"] == "en" else f"construído em {property_data.features.year_built}"
            features_list.append(year_text)
        
        context["features_list"] = features_list
        context["features_text"] = ", ".join(features_list)
        
        return context
    
    def _get_seo_keywords(self, property_data: PropertyData) -> List[str]:
        """Generate SEO keywords based on property data"""
        lang = property_data.language.value
        keywords = SEO_KEYWORDS[lang]["base_terms"].copy()
        
        # Add location-based keywords
        city_keywords = [
            f"{property_data.location.city.lower()}",
            f"{property_data.location.neighborhood.lower()}",
        ]
        keywords.extend(city_keywords)
        
        # Add property type keywords
        property_type = "apartment" if lang == "en" else "apartamento"
        keywords.append(f"T{property_data.features.bedrooms} {property_type}")
        
        return keywords
    
    async def _generate_with_gemini(self, prompt: str) -> str:
        """Generate content using Gemini Flash API (FREE)"""
        try:
            # Add system instructions for better results
            enhanced_prompt = f"""You are a professional real estate content writer. Generate high-quality, SEO-optimized content that is engaging and informative.

{prompt}

IMPORTANT: Generate ONLY the requested HTML tag with content, no additional text or explanations."""

            response = await self.model.generate_content_async(enhanced_prompt)
            
            if not response.text:
                raise ValueError("Empty response from Gemini Flash API")
                
            # Clean up response (remove markdown formatting if present)
            content = response.text.strip()
            content = content.replace('```html', '').replace('```', '').strip()
            
            return content
            
        except Exception as e:
            logger.error(f"Gemini Flash API error: {e}")
            raise ValueError(f"Failed to generate content: {e}")
    
    async def generate_section(self, property_data: PropertyData, section_name: str) -> str:
        """Generate content for a specific section"""
        if not self.model:
            await self.initialize()
        
        lang = property_data.language.value
        if section_name not in self.prompts[lang]:
            raise ValueError(f"Unknown section: {section_name}")
        
        context = self._build_property_context(property_data)
        keywords = self._get_seo_keywords(property_data)
        context["seo_keywords"] = ", ".join(keywords[:5])  # Limit keywords
        
        # Build prompt
        prompt_template = self.prompts[lang][section_name]
        prompt = prompt_template.format(**context)
        
        logger.info(f"Generating {section_name} for {property_data.title}")
        
        # Generate content
        content = await self._generate_with_gemini(prompt)
        
        return content
    
    async def generate_all_sections(self, property_data: PropertyData) -> GeneratedContent:
        """Generate all content sections for a property"""
        if not self.model:
            await self.initialize()
        
        sections = []
        section_names = [
            "title", "meta_description", "headline", 
            "description", "key_features", "neighborhood", "call_to_action"
        ]
        
        for section_name in section_names:
            try:
                content = await self.generate_section(property_data, section_name)
                sections.append(ContentSection(
                    tag=section_name,
                    content=content
                ))
                logger.info(f"✅ Generated {section_name}")
            except Exception as e:
                logger.error(f"❌ Failed to generate {section_name}: {e}")
                # Add fallback content
                sections.append(ContentSection(
                    tag=section_name,
                    content=f"<!-- Error generating {section_name}: {str(e)} -->"
                ))
        
        return GeneratedContent(
            language=property_data.language,
            sections=sections
        )