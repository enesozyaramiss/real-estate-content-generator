ENGLISH_PROMPTS = {
    "title": """
Create an SEO-optimized HTML title tag for a real estate listing. 
- Maximum 60 characters
- Include property type, location, and listing intent
- Format: <title>content here</title>

Property Details:
- Title: {title}
- Location: {neighborhood}, {city}
- Bedrooms: {bedrooms}
- Area: {area_sqm} sqm
- Listing type: {listing_type}
- Price: €{price}

SEO Keywords to include: {seo_keywords}

Generate ONLY the HTML title tag, nothing else.
""",

    "meta_description": """
Create an SEO-optimized meta description for a real estate listing.
- Maximum 155 characters
- Compelling and descriptive
- Include key features and location
- Format: <meta name="description" content="content here">

Property Details:
- Title: {title}
- Location: {neighborhood}, {city}
- Bedrooms: {bedrooms}, Bathrooms: {bathrooms}
- Area: {area_sqm} sqm
- Features: {features_text}
- Listing type: {listing_type}
- Price: €{price}

Generate ONLY the HTML meta tag, nothing else.
""",

    "headline": """
Create an engaging H1 headline for a real estate listing page.
- Descriptive and appealing
- Include property type and best features
- Format: <h1>content here</h1>

Property Details:
- Title: {title}
- Location: {neighborhood}, {city}
- Bedrooms: {bedrooms}
- Area: {area_sqm} sqm
- Key Features: {features_text}
- Listing type: {listing_type}

Generate ONLY the HTML h1 tag, nothing else.
""",

    "description": """
Create a rich, engaging property description for a real estate listing.
- Between 500-700 characters
- Highlight key features and location benefits
- Professional yet appealing tone
- Include all important details naturally
- Format: <section id="description"><p>content here</p></section>

Property Details:
- Title: {title}
- Location: {neighborhood}, {city}
- Bedrooms: {bedrooms}, Bathrooms: {bathrooms}
- Area: {area_sqm} sqm
- Features: {features_text}
- Listing type: {listing_type}
- Price: €{price}

Generate ONLY the HTML section with paragraph, nothing else.
""",

    "key_features": """
Create a key features list for a real estate listing.
- 3-5 bullet points
- Highlight most important property features
- Concise and informative
- Format: <ul id="key-features"><li>feature</li></ul>

Property Details:
- Bedrooms: {bedrooms}, Bathrooms: {bathrooms}
- Area: {area_sqm} sqm
- Features: {features_text}
- Location: {neighborhood}, {city}

Generate ONLY the HTML unordered list, nothing else.
""",

    "neighborhood": """
Create a neighborhood description for a real estate listing.
- One engaging paragraph (150-300 characters)
- Highlight lifestyle and area benefits
- Professional and informative tone
- Format: <section id="neighborhood"><p>content here</p></section>

Location: {neighborhood}, {city}

Create a compelling description of this neighborhood, mentioning lifestyle benefits, amenities, and why it's desirable to live there.

Generate ONLY the HTML section with paragraph, nothing else.
""",

    "call_to_action": """
Create a compelling call-to-action for a real estate listing.
- Short and engaging (under 100 characters)
- Encourage immediate action
- Professional tone
- Format: <p class="call-to-action">content here</p>

Listing type: {listing_type}
Location: {city}

Generate ONLY the HTML paragraph with call-to-action class, nothing else.
"""
}