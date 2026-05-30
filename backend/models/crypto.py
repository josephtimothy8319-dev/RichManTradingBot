from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CryptoPrice(BaseModel):
    """Crypto price data model"""
    symbol: str
    price: float
    change_percent: float
    volume: float
    timestamp: datetime
    
class CryptoPriceUpdate(BaseModel):
    """Real-time price update for WebSocket"""
    symbol: str
    price: float
    change_percent: float
    volume: float
    high_24h: float
    low_24h: float
    timestamp: str

class CryptoTicker(BaseModel):
    """Full ticker information"""
    symbol: str
    price: float
    change_percent: float
    volume: float
    high_24h: float
    low_24h: float
    bid: float
    ask: float

class WatchlistItem(BaseModel):
    """Watchlist item"""
    symbol: str
    name: str
    quantity: Optional[float] = None
