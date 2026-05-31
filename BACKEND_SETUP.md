# Backend Setup - Phase 2

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                   ← FastAPI app
│   ├── config.py                 ← Configuration
│   ├── dependencies.py           ← Dependency injection
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── market.py        ← Market data endpoints
│   │   │   ├── strategies.py    ← Strategy endpoints
│   │   │   ├── backtest.py      ← Backtest endpoints
│   │   │   └── ai.py            ← AI analysis endpoints
│   │   └── websocket/
│   │       ├── __init__.py
│   │       ├── manager.py       ← WebSocket manager
│   │       └── handlers.py      ← Event handlers
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── market_service.py    ← Binance integration
│   │   ├── strategy_service.py  ← Strategy management
│   │   ├── backtest_service.py  ← Backtesting engine
│   │   ├── ai_service.py        ← AI analysis
│   │   └── data_cache.py        ← Caching layer
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── strategy.py
│   │   ├── backtest.py
│   │   ├── market.py
│   │   └── schemas.py           ← Pydantic schemas
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py          ← DB connection
│   │   ├── base.py              ← Base models
│   │   └── migrations/          ← Alembic migrations
│   │
│   ├── external/
│   │   ├── __init__.py
│   │   ├── binance_client.py    ← Binance API wrapper
│   │   └── ai_provider.py       ← AI service wrapper
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── market_tasks.py      ← Celery tasks
│   │   ├── backtest_tasks.py
│   │   └── analysis_tasks.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── indicators.py        ← Technical indicators
│   │   ├── calculations.py      ← Metric calculations
│   │   ├── validators.py
│   │   ├── helpers.py
│   │   └── logger.py
│   │
│   └── middleware/
│       ├── __init__.py
│       ├── error_handler.py
│       └── cors.py
│
├── tests/
│   ├── __init__.py
│   ├── test_market.py
│   ├── test_strategies.py
│   ├── test_backtest.py
│   └── test_ai.py
│
├── requirements.txt
├── .env.example
├── Dockerfile
└── docker-compose.yml
```

## Requirements

```bash
# requirements.txt

# Core
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-dotenv==1.0.0
pydantic==2.6.0
pydantic-settings==2.1.0

# Database
sqlalchemy==2.0.23
alembic==1.13.1
psycopg2-binary==2.9.9

# Data Processing
numpy==1.24.3
pandas==2.0.3

# Market Data
python-binance==1.0.17
websocket-client==1.6.4

# Async
httpx==0.25.2
aiohttp==3.9.1

# Caching
redis==5.0.1

# Task Queue
celery==5.3.4

# Timezone
pytz==2023.3

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1

# Monitoring
python-json-logger==2.0.7
```

## Configuration

```python
# config.py
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API
    API_TITLE: str = "RichManTradingBot API"
    API_VERSION: str = "0.2.0"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost/richmantradingbot"
    SQLALCHEMY_ECHO: bool = False
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    CACHE_TTL: int = 300  # 5 minutes
    
    # Binance
    BINANCE_API_KEY: Optional[str] = None
    BINANCE_SECRET_KEY: Optional[str] = None
    BINANCE_TESTNET: bool = True
    
    # CORS
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"]
    
    # AI Provider
    AI_PROVIDER: str = "openai"  # or "huggingface"
    OPENAI_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
```

## Database Models

```python
# models/strategy.py
from sqlalchemy import Column, String, DateTime, Integer, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class Strategy(Base):
    __tablename__ = "strategies"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(1000))
    
    # Strategy configuration
    strategy_type = Column(String(50))  # moving_average, rsi, macd, etc.
    parameters = Column(JSON, default={})
    
    # Metadata
    status = Column(String(50), default="active")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relations
    backtest_results = relationship("BacktestResult", back_populates="strategy")

class BacktestResult(Base):
    __tablename__ = "backtest_results"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    strategy_id = Column(UUID(as_uuid=True), ForeignKey("strategies.id"))
    
    # Test parameters
    symbol = Column(String(20), nullable=False)
    timeframe = Column(String(10), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    
    # Performance metrics
    total_trades = Column(Integer)
    win_rate = Column(Float)
    profit_factor = Column(Float)
    net_profit = Column(Float)
    max_drawdown = Column(Float)
    sharpe_ratio = Column(Float)
    
    # Full results
    results = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relations
    strategy = relationship("Strategy", back_populates="backtest_results")
```

## API Routes Example

```python
# api/routes/market.py
from fastapi import APIRouter, HTTPException
from app.services.market_service import MarketService
from typing import List

router = APIRouter(prefix="/api/market", tags=["market"])
market_service = MarketService()

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
        raise HTTPException(status_code=404, detail="Symbol not found")
    return price

@router.get("/ohlcv/{symbol}/{timeframe}")
async def get_ohlcv(symbol: str, timeframe: str, limit: int = 500):
    """Get OHLCV data for symbol and timeframe"""
    data = await market_service.get_ohlcv(symbol, timeframe, limit)
    return {"data": data}

@router.get("/indicators/{symbol}")
async def get_indicators(symbol: str):
    """Get technical indicators for symbol"""
    indicators = await market_service.calculate_indicators(symbol)
    return indicators
```

```python
# api/routes/strategies.py
from fastapi import APIRouter, HTTPException
from app.services.strategy_service import StrategyService
from app.models.schemas import StrategyCreate, StrategyUpdate
from typing import List

router = APIRouter(prefix="/api/strategies", tags=["strategies"])
strategy_service = StrategyService()

@router.get("/")
async def list_strategies(user_id: str):
    """Get all strategies for user"""
    strategies = await strategy_service.get_user_strategies(user_id)
    return {"strategies": strategies}

@router.post("/")
async def create_strategy(user_id: str, strategy: StrategyCreate):
    """Create new strategy"""
    new_strategy = await strategy_service.create_strategy(user_id, strategy)
    return {"strategy": new_strategy}

@router.get("/compare")
async def compare_strategies(user_id: str, strategy_ids: List[str]):
    """Compare multiple strategies by their backtest results"""
    comparison = await strategy_service.compare_strategies(user_id, strategy_ids)
    return comparison

@router.get("/rankings")
async def get_strategy_rankings(user_id: str):
    """Get top 3 performing strategies"""
    rankings = await strategy_service.get_top_strategies(user_id, top_n=3)
    return {"rankings": rankings}
```

```python
# api/routes/backtest.py
from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.services.backtest_service import BacktestService
from app.models.schemas import BacktestConfig

router = APIRouter(prefix="/api/backtest", tags=["backtest"])
backtest_service = BacktestService()

@router.post("/run")
async def run_backtest(config: BacktestConfig, background_tasks: BackgroundTasks):
    """Start a backtest job"""
    backtest_id = await backtest_service.create_backtest_job(config)
    # Run in background
    background_tasks.add_task(backtest_service.run_backtest, backtest_id)
    return {"backtest_id": backtest_id, "status": "running"}

@router.get("/{backtest_id}")
async def get_backtest_status(backtest_id: str):
    """Get backtest status"""
    status = await backtest_service.get_backtest_status(backtest_id)
    return status

@router.get("/{backtest_id}/results")
async def get_backtest_results(backtest_id: str):
    """Get completed backtest results"""
    results = await backtest_service.get_backtest_results(backtest_id)
    if not results:
        raise HTTPException(status_code=404, detail="Backtest not found")
    return results
```

## Services Example

```python
# services/market_service.py
import asyncio
from typing import List, Dict, Optional
from binance.client import Client
from binance.exceptions import BinanceAPIException
from app.config import settings
import numpy as np

class MarketService:
    def __init__(self):
        self.client = Client(
            api_key=settings.BINANCE_API_KEY,
            api_secret=settings.BINANCE_SECRET_KEY,
            testnet=settings.BINANCE_TESTNET
        )
        self.symbols = [
            'BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 
            'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT'
        ]
    
    async def get_available_symbols(self) -> List[str]:
        """Get list of available trading symbols"""
        return [s.replace('USDT', '') for s in self.symbols]
    
    async def get_current_price(self, symbol: str) -> Optional[Dict]:
        """Get current price for symbol"""
        try:
            ticker = self.client.get_symbol_ticker(symbol=f"{symbol}USDT")
            return {
                'symbol': symbol,
                'price': float(ticker['price']),
                'timestamp': ticker['time']
            }
        except BinanceAPIException:
            return None
    
    async def get_ohlcv(self, symbol: str, timeframe: str, limit: int = 500) -> List[Dict]:
        """Get OHLCV data"""
        try:
            klines = self.client.get_klines(
                symbol=f"{symbol}USDT",
                interval=timeframe,
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
        except BinanceAPIException:
            return []
    
    async def calculate_indicators(self, symbol: str) -> Dict:
        """Calculate technical indicators"""
        ohlcv = await self.get_ohlcv(symbol, '1h', limit=100)
        closes = np.array([k['close'] for k in ohlcv])
        
        # Calculate RSI
        rsi = self._calculate_rsi(closes)
        
        # Calculate MACD
        macd, signal, histogram = self._calculate_macd(closes)
        
        return {
            'symbol': symbol,
            'rsi': float(rsi[-1]) if len(rsi) > 0 else None,
            'macd': float(macd[-1]) if len(macd) > 0 else None,
            'macd_signal': float(signal[-1]) if len(signal) > 0 else None,
            'macd_histogram': float(histogram[-1]) if len(histogram) > 0 else None
        }
    
    def _calculate_rsi(self, closes: np.ndarray, period: int = 14) -> np.ndarray:
        """Calculate RSI indicator"""
        deltas = np.diff(closes)
        gains = np.where(deltas > 0, deltas, 0)
        losses = np.where(deltas < 0, -deltas, 0)
        
        avg_gain = np.mean(gains[:period])
        avg_loss = np.mean(losses[:period])
        
        rsi = np.zeros_like(closes)
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
    
    def _ema(self, data: np.ndarray, period: int) -> np.ndarray:
        """Calculate EMA"""
        alpha = 2 / (period + 1)
        ema = np.zeros_like(data)
        ema[0] = data[0]
        
        for i in range(1, len(data)):
            ema[i] = alpha * data[i] + (1 - alpha) * ema[i-1]
        
        return ema
```

## WebSocket Handler

```python
# api/websocket/manager.py
from fastapi import WebSocket
from typing import List, Dict
import json
import asyncio

class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.subscriptions: Dict[str, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def subscribe(self, websocket: WebSocket, channel: str):
        if channel not in self.subscriptions:
            self.subscriptions[channel] = []
        self.subscriptions[channel].append(websocket)
    
    async def unsubscribe(self, websocket: WebSocket, channel: str):
        if channel in self.subscriptions:
            self.subscriptions[channel].remove(websocket)
    
    async def broadcast(self, channel: str, data: Dict):
        if channel in self.subscriptions:
            for connection in self.subscriptions[channel]:
                try:
                    await connection.send_json(data)
                except Exception:
                    pass

manager = WebSocketManager()
```

## Main FastAPI App

```python
# main.py
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.api.routes import market, strategies, backtest, ai
from app.api.websocket.manager import manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting RichManTradingBot API...")
    yield
    # Shutdown
    print("Shutting down...")

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(market.router)
app.include_router(strategies.router)
app.include_router(backtest.router)
app.include_router(ai.router)

# WebSocket
@app.websocket("/ws/market/{symbol}")
async def websocket_endpoint(websocket: WebSocket, symbol: str):
    await manager.connect(websocket)
    await manager.subscribe(websocket, f"market:{symbol}")
    try:
        while True:
            data = await websocket.receive_text()
            # Handle incoming messages
    except Exception:
        manager.disconnect(websocket)

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Environment Variables

```bash
# .env.example

# Database
DATABASE_URL=postgresql://user:password@localhost/richmantradingbot
REDIS_URL=redis://localhost:6379

# Binance
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
BINANCE_TESTNET=true

# API
API_HOST=0.0.0.0
API_PORT=8000

# CORS
CORS_ORIGINS=["http://localhost:3000","http://localhost:5173"]

# AI Provider
AI_PROVIDER=openai
OPENAI_API_KEY=your_openai_key
```

## Running the Backend

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
alembic upgrade head

# Run development server
uvicorn app.main:app --reload

# Server runs at: http://localhost:8000
# API docs: http://localhost:8000/docs
```

## Docker Setup

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml snippet
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://user:password@postgres:5432/richmantradingbot
      REDIS_URL: redis://redis:6379
    depends_on:
      - postgres
      - redis
  
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: richmantradingbot
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

---

**This is the complete backend structure for Phase 2. Ready to implement!**
