import httpx
import asyncio
from typing import Dict, List, Optional
from datetime import datetime
from backend.config import Config
from backend.models.crypto import CryptoPriceUpdate, CryptoTicker

class BinanceService:
    """Service for fetching Binance market data"""
    
    def __init__(self):
        self.base_url = Config.BINANCE_API_BASE
        self.timeout = httpx.Timeout(10.0)
    
    async def get_price(self, symbol: str) -> Optional[Dict]:
        """Get current price for a symbol"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                url = f"{self.base_url}/api/v3/ticker/price"
                response = await client.get(url, params={"symbol": symbol})
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None
    
    async def get_24h_ticker(self, symbol: str) -> Optional[Dict]:
        """Get 24h ticker data"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                url = f"{self.base_url}/api/v3/ticker/24hr"
                response = await client.get(url, params={"symbol": symbol})
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching 24h ticker for {symbol}: {e}")
            return None
    
    async def get_multiple_prices(self, symbols: List[str]) -> Dict[str, Dict]:
        """Get prices for multiple symbols concurrently"""
        tasks = [self.get_24h_ticker(symbol) for symbol in symbols]
        results = await asyncio.gather(*tasks)
        
        prices = {}
        for symbol, data in zip(symbols, results):
            if data:
                prices[symbol] = {
                    "symbol": symbol,
                    "price": float(data["lastPrice"]),
                    "change_percent": float(data["priceChangePercent"]),
                    "volume": float(data["quoteAssetVolume"]),
                    "high_24h": float(data["highPrice"]),
                    "low_24h": float(data["lowPrice"]),
                    "bid": float(data["bidPrice"]),
                    "ask": float(data["askPrice"]),
                    "timestamp": datetime.now().isoformat()
                }
        
        return prices
    
    async def get_klines(self, symbol: str, interval: str = "1h", limit: int = 100) -> Optional[List]:
        """Get candlestick data (klines)"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                url = f"{self.base_url}/api/v3/klines"
                response = await client.get(
                    url,
                    params={"symbol": symbol, "interval": interval, "limit": limit}
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching klines for {symbol}: {e}")
            return None
    
    async def format_price_update(self, symbol: str) -> Optional[CryptoPriceUpdate]:
        """Format ticker data into price update"""
        ticker = await self.get_24h_ticker(symbol)
        if not ticker:
            return None
        
        return CryptoPriceUpdate(
            symbol=symbol,
            price=float(ticker["lastPrice"]),
            change_percent=float(ticker["priceChangePercent"]),
            volume=float(ticker["quoteAssetVolume"]),
            high_24h=float(ticker["highPrice"]),
            low_24h=float(ticker["lowPrice"]),
            timestamp=datetime.now().isoformat()
        )
