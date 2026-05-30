from fastapi import APIRouter, HTTPException
from backend.services.binance_service import BinanceService
from backend.config import Config

router = APIRouter(prefix="/api/crypto", tags=["crypto"])
binance_service = BinanceService()

@router.get("/prices")
async def get_all_prices():
    """Get current prices for all default symbols"""
    prices = await binance_service.get_multiple_prices(Config.DEFAULT_SYMBOLS)
    if not prices:
        raise HTTPException(status_code=500, detail="Failed to fetch prices")
    return {"data": prices}

@router.get("/price/{symbol}")
async def get_price(symbol: str):
    """Get price for a specific symbol"""
    price = await binance_service.get_24h_ticker(symbol)
    if not price:
        raise HTTPException(status_code=404, detail=f"Symbol {symbol} not found")
    return {"data": price}

@router.get("/klines/{symbol}")
async def get_klines(symbol: str, interval: str = "1h", limit: int = 100):
    """Get candlestick data"""
    if interval not in ["1m", "5m", "15m", "1h", "4h", "1d"]:
        raise HTTPException(status_code=400, detail="Invalid interval")
    
    klines = await binance_service.get_klines(symbol, interval, limit)
    if not klines:
        raise HTTPException(status_code=500, detail="Failed to fetch klines")
    
    # Format klines
    formatted = []
    for kline in klines:
        formatted.append({
            "time": int(kline[0]) // 1000,
            "open": float(kline[1]),
            "high": float(kline[2]),
            "low": float(kline[3]),
            "close": float(kline[4]),
            "volume": float(kline[7])
        })
    
    return {"data": formatted}

@router.get("/symbols")
async def get_default_symbols():
    """Get default symbols"""
    return {"symbols": Config.DEFAULT_SYMBOLS}
