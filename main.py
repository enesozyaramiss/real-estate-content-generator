from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from typing import Optional

from app.models import PropertyData, GeneratedContent, APIResponse
from app.services.content_generator import ContentGenerator
from app.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="AI-powered content generator for real estate property listings",
    version=settings.app_version,
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.debug else ["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Initialize content generator
content_generator = ContentGenerator()

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    try:
        await content_generator.initialize()
        logger.info("✅ Content generator initialized successfully")
    except Exception as e:
        logger.error(f"❌ Failed to initialize content generator: {e}")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "status": "healthy"
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "gemini_configured": bool(settings.gemini_api_key),
        "model": settings.gemini_model
    }

@app.post("/generate-content", response_model=APIResponse)
async def generate_content(property_data: PropertyData):
    """
    Generate SEO-optimized content for real estate property listing
    
    Args:
        property_data: Property information in JSON format
        
    Returns:
        Generated content with HTML tags for each section
    """
    try:
        logger.info(f"Generating content for property: {property_data.title}")
        
        # Generate content using AI service
        generated_content = await content_generator.generate_all_sections(property_data)
        
        return APIResponse(
            success=True,
            data=generated_content,
            message="Content generated successfully"
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid input data: {str(e)}"
        )
    
    except Exception as e:
        logger.error(f"Content generation failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate content. Please try again."
        )

@app.post("/generate-section")
async def generate_single_section(
    property_data: PropertyData, 
    section_name: str
):
    """
    Generate content for a specific section only
    
    Args:
        property_data: Property information
        section_name: Name of section to generate (title, meta_description, etc.)
    """
    try:
        valid_sections = [
            "title", "meta_description", "headline", 
            "description", "key_features", "neighborhood", "call_to_action"
        ]
        
        if section_name not in valid_sections:
            raise ValueError(f"Invalid section name. Must be one of: {valid_sections}")
        
        content = await content_generator.generate_section(property_data, section_name)
        
        return APIResponse(
            success=True,
            data={"section": section_name, "content": content},
            message=f"Section '{section_name}' generated successfully"
        )
        
    except Exception as e:
        logger.error(f"Section generation failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate section: {str(e)}"
        )

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal server error",
            "message": "Something went wrong. Please try again."
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level="info"
    )