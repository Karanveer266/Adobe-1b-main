"""
Configuration settings for Part 1B: Persona-Driven Document Intelligence
Updated for all-mpnet-base-v2 model
"""

from pathlib import Path

class Config1B:
    EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  
    EMBEDDING_DIMENSION = 384  

    MAX_MODEL_SIZE_MB = 1024  # 1GB limit
    
    # Text processing limits
    MAX_TEXT_LENGTH_FOR_EMBEDDING = 512  # model's token limit
    MAX_CONTENT_LENGTH = 5000  # Max content to extract per section
    MAX_CONTENT_FOR_EMBEDDING = 500  # Max content for embedding
    
    # Section analysis limits 
    MAX_SECTIONS_TO_ANALYZE = 12 
    MAX_SECTIONS_FOR_SUBSECTION_ANALYSIS = 5  # Top sections for detailed analysis
    MAX_SUBSECTIONS_TO_RETURN = 8  # Controlled output
    MAX_SUBSECTIONS_PER_SECTION = 3  # Limited per section
    
    # Subsection processing
    MIN_CONTENT_LENGTH_FOR_SUBSECTION = 100
    MIN_SUBSECTION_LENGTH = 50
    MAX_SUBSECTION_LENGTH = 800
    MAX_REFINED_TEXT_LENGTH = 500
    MIN_SUBSECTION_RELEVANCE_SCORE = 0.30  
    MAX_KEY_CONCEPTS_PER_SUBSECTION = 5
    
    # Scoring weights (must sum to 1.0)
    SEMANTIC_SIMILARITY_WEIGHT = 0.40  
    DOMAIN_RELEVANCE_WEIGHT = 0.20
    KEYWORD_MATCH_WEIGHT = 0.20  
    SECTION_TYPE_WEIGHT = 0.10
    CONTENT_QUALITY_WEIGHT = 0.10
    
    # Performance settings
    MAX_PROCESSING_TIME_SECONDS = 55  # Leave buffer from 60s limit
    BATCH_SIZE_FOR_EMBEDDING = 3  
    
    # Cache settings
    ENABLE_EMBEDDING_CACHE = True
    MAX_CACHE_SIZE = 1000
    
    # Output formatting 
    MAX_SECTIONS_IN_OUTPUT = 5 
    MAX_SUBSECTIONS_IN_OUTPUT = 5
    INCLUDE_DEBUG_INFO = False
    
    # Filtering thresholds 
    MIN_SECTION_RELEVANCE_SCORE = 0.25  
    MIN_CONTENT_QUALITY_SCORE = 0.2
    MIN_TITLE_WORDS = 1
    MAX_TITLE_WORDS = 15
