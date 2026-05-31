from typing import List
from binance.client import Client
from binance.exceptions import BinanceAPIException
from app.config import settings
import numpy as np
import logging

logger = logging.getLogger(__name__)

class MarketService:
    """Service for market data operations"""
    
    def __init__(self):
        self.client = Client(
            api_key=settings.BINANCE_API_KEY or "",
            api_secret=settings.BINANCE_SECRET_KEY or "",
            testnet=settings.BINANCE_TESTNET
        )
        self.symbols = [
            'BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 
            'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT',
            'LINKUSDT', 'UNIUSDT', 'ARBUSDT', 'OPUSDT'
        ]
    
    async def get_available_symbols(self) -> List[str]:
        """Get list of available trading symbols"""
        return [s.replace('USDT', '') for s in self.symbols]
    
    async def get_current_price(self, symbol: str) -> dict:
        """Get current price for symbol"""
        try:
            ticker = self.client.get_symbol_ticker(symbol=f"{symbol}USDT")
            return {
                'symbol': symbol,
                'price': float(ticker['price']),
                'timestamp': ticker['time']
            }
        except Exception as e:
            logger.error(f"Error fetching price for {symbol}: {e}")
            return None
    
    async def get_ohlcv(self, symbol: str, timeframe: str, limit: int = 500) -> List[dict]:
        """Get OHLCV data for symbol and timeframe"""
        try:
            # Map timeframe names to Binance format
            timeframe_map = {
                '1m': Client.KLINE_INTERVAL_1MINUTE,
                '5m': Client.KLINE_INTERVAL_5MINUTE,
                '15m': Client.KLINE_INTERVAL_15MINUTE,
                '1h': Client.KLINE_INTERVAL_1HOUR,
                '4h': Client.KLINE_INTERVAL_4HOUR,
                '1D': Client.KLINE_INTERVAL_1DAY,
                '1W': Client.KLINE_INTERVAL_1WEEK,
            }
            
            binance_interval = timeframe_map.get(timeframe)
            if not binance_interval:
                return []
            
            klines = self.client.get_klines(
                symbol=f"{symbol}USDT",
                interval=binance_interval,
                limit=limit
            )
            
            data = []
            for kline in klines:
                data.append({
                    'time': int(kline[0]) / 1000,
                    'open': float(kline[1]),
                    'high': float(kline[2]),
                    'low': float(kline[3]),
                    'close': float(kline[4]),
                    'volume': float(kline[7])
                })
            return data
        except Exception as e:
            logger.error(f"Error fetching OHLCV for {symbol}: {e}")
            return []
    
    async def calculate_indicators(self, symbol: str, timeframe: str = '1h') -> dict:
        """Calculate technical indicators"""
        ohlcv = await self.get_ohlcv(symbol, timeframe, limit=100)
        if not ohlcv:
            return None
        
        closes = np.array([k['close'] for k in ohlcv])
        
        # Calculate indicators
        rsi = self._calculate_rsi(closes)
        macd, signal, histogram = self._calculate_macd(closes)
        bb_upper, bb_middle, bb_lower = self._calculate_bollinger_bands(closes)
        
        return {
            'symbol': symbol,
            'timeframe': timeframe,
            'rsi': float(rsi[-1]) if len(rsi) > 0 else None,
            'macd': float(macd[-1]) if len(macd) > 0 else None,
            'macd_signal': float(signal[-1]) if len(signal) > 0 else None,
            'macd_histogram': float(histogram[-1]) if len(histogram) > 0 else None,
            'bb_upper': float(bb_upper[-1]) if len(bb_upper) > 0 else None,
            'bb_middle': float(bb_middle[-1]) if len(bb_middle) > 0 else None,
            'bb_lower': float(bb_lower[-1]) if len(bb_lower) > 0 else None,
        }
    
    def _calculate_rsi(self, closes: np.ndarray, period: int = 14) -> np.ndarray:
        """Calculate RSI indicator"""
        deltas = np.diff(closes)
        gains = np.where(deltas > 0, deltas, 0)
        losses = np.where(deltas < 0, -deltas, 0)
        
        avg_gain = np.mean(gains[:period])
        avg_loss = np.mean(losses[:period])
        
        rsi = np.zeros_like(closes, dtype=float)
        for i in range(period, len(closes)):
            avg_gain = (avg_gain * (period - 1) + gains[i]) / period
            avg_loss = (avg_loss * (period - 1) + losses[i]) / period
            
            if avg_loss == 0:
                rsi[i] = 100
            else:
                rs = avg_gain / avg_loss
                rsi[i] = 100 - (100 / (1 + rs))
        
        return rsi
    
    def _calculate_macd(self, closes: np.ndarray) -> tuple:
        """Calculate MACD indicator"""
        ema_12 = self._ema(closes, 12)
        ema_26 = self._ema(closes, 26)
        
        macd = ema_12 - ema_26
        signal = self._ema(macd, 9)
        histogram = macd - signal
        
        return macd, signal, histogram
    
    def _calculate_bollinger_bands(self, closes: np.ndarray, period: int = 20, std_dev: float = 2.0) -> tuple:
        """Calculate Bollinger Bands"""
        sma = np.convolve(closes, np.ones(period)/period, mode='valid')
        std = np.std(closes[-period:])
        
        upper = sma + (std_dev * std)
        lower = sma - (std_dev * std)
        
        return upper, sma, lower
    
    def _ema(self, data: np.ndarray, period: int) -> np.ndarray:
        """Calculate EMA"""
        alpha = 2 / (period + 1)
        ema = np.zeros_like(data, dtype=float)
        ema[0] = data[0]
        
        for i in range(1, len(data)):
            ema[i] = alpha * data[i] + (1 - alpha) * ema[i-1]
        
        return ema

market_service = MarketService()
