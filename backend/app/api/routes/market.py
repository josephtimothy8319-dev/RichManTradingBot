from fastapi import APIRouter
from app.services.market_service import market_service
from typing import Optional

router = APIRouter(prefix="/api/market", tags=["market"])

@router.get("/symbols")
async def get_symbols():
    """Get list of available trading symbols"""
    symbols = await market_service.get_available_symbols()
    return {"symbols": symbols}

@router.get("/price/{symbol}")
async def get_price(symbol: str):
    """Get current price for symbol"""
    price = await market_service.get_current_price(symbol)
    if not price:
        return {"error": "Symbol not found"}
    return price

@router.get("/ohlcv/{symbol}")
async def get_ohlcv(symbol: str, timeframe: str = "1h", limit: int = 500):
    """Get OHLCV data for symbol and timeframe"""
    data = await market_service.get_ohlcv(symbol, timeframe, limit)
    return {"symbol": symbol, "timeframe": timeframe, "data": data}

@router.get("/indicators/{symbol}")
async def get_indicators(symbol: str, timeframe: str = "1h"):
    """Get technical indicators for symbol"""
    indicators = await market_service.calculate_indicators(symbol, timeframe)
    return indicators
