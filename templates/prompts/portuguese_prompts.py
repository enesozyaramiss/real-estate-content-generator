PORTUGUESE_PROMPTS = {
    "title": """
Crie um título HTML otimizado para SEO para um anúncio imobiliário.
- Máximo 60 caracteres
- Inclua tipo de propriedade, localização e intenção do anúncio
- Formato: <title>conteúdo aqui</title>

Detalhes da Propriedade:
- Título: {title}
- Localização: {neighborhood}, {city}
- Quartos: {bedrooms}
- Área: {area_sqm} m²
- Tipo de anúncio: {listing_type}
- Preço: €{price}

Palavras-chave SEO para incluir: {seo_keywords}

Gere APENAS a tag HTML title, nada mais.
""",

    "meta_description": """
Crie uma meta descrição otimizada para SEO para um anúncio imobiliário.
- Máximo 155 caracteres
- Atrativa e descritiva
- Inclua características principais e localização
- Formato: <meta name="description" content="conteúdo aqui">

Detalhes da Propriedade:
- Título: {title}
- Localização: {neighborhood}, {city}
- Quartos: {bedrooms}, Casas de banho: {bathrooms}
- Área: {area_sqm} m²
- Características: {features_text}
- Tipo de anúncio: {listing_type}
- Preço: €{price}

Gere APENAS a tag HTML meta, nada mais.
""",

    "headline": """
Crie um título H1 envolvente para uma página de anúncio imobiliário.
- Descritivo e atrativo
- Inclua tipo de propriedade e melhores características
- Formato: <h1>conteúdo aqui</h1>

Detalhes da Propriedade:
- Título: {title}
- Localização: {neighborhood}, {city}
- Quartos: {bedrooms}
- Área: {area_sqm} m²
- Características Principais: {features_text}
- Tipo de anúncio: {listing_type}

Gere APENAS a tag HTML h1, nada mais.
""",

    "description": """
Crie uma descrição rica e envolvente para um anúncio imobiliário.
- Entre 500-700 caracteres
- Destaque características principais e benefícios da localização
- Tom profissional mas atrativo
- Inclua todos os detalhes importantes naturalmente
- Formato: <section id="description"><p>conteúdo aqui</p></section>

Detalhes da Propriedade:
- Título: {title}
- Localização: {neighborhood}, {city}
- Quartos: {bedrooms}, Casas de banho: {bathrooms}
- Área: {area_sqm} m²
- Características: {features_text}
- Tipo de anúncio: {listing_type}
- Preço: €{price}

Gere APENAS a secção HTML com parágrafo, nada mais.
""",

    "key_features": """
Crie uma lista de características principais para um anúncio imobiliário.
- 3-5 pontos
- Destaque as características mais importantes da propriedade
- Conciso e informativo
- Formato: <ul id="key-features"><li>característica</li></ul>

Detalhes da Propriedade:
- Quartos: {bedrooms}, Casas de banho: {bathrooms}
- Área: {area_sqm} m²
- Características: {features_text}
- Localização: {neighborhood}, {city}

Gere APENAS a lista HTML não ordenada, nada mais.
""",

    "neighborhood": """
Crie uma descrição do bairro para um anúncio imobiliário.
- Um parágrafo envolvente (150-300 caracteres)
- Destaque estilo de vida e benefícios da área
- Tom profissional e informativo
- Formato: <section id="neighborhood"><p>conteúdo aqui</p></section>

Localização: {neighborhood}, {city}

Crie uma descrição atrativa deste bairro, mencionando benefícios de estilo de vida, comodidades e por que é desejável viver lá.

Gere APENAS a secção HTML com parágrafo, nada mais.
""",

    "call_to_action": """
Crie um apelo à ação convincente para um anúncio imobiliário.
- Curto e envolvente (menos de 100 caracteres)
- Encoraje ação imediata
- Tom profissional
- Formato: <p class="call-to-action">conteúdo aqui</p>

Tipo de anúncio: {listing_type}
Localização: {city}

Gere APENAS o parágrafo HTML com classe call-to-action, nada mais.
"""
}