import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    
    # API Settings
    API_TITLE = "RichManBot"
    API_VERSION = "1.0.0"
    API_DESCRIPTION = "Professional Crypto Trading Bot Dashboard"
    
    # Server
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = os.getenv("DEBUG", "True") == "True"
    
    # Binance API
    BINANCE_API_BASE = "https://api.binance.com"
    
    # Crypto symbols to track
    DEFAULT_SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "ADAUSDT"]
    
    # Update interval (seconds)
    PRICE_UPDATE_INTERVAL = 2
    
    # CORS
    ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]
