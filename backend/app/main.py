from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.api.routes import market, strategies, backtest, ai

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    logger.info("🚀 Starting RichManTradingBot API...")
    yield
    logger.info("🛑 Shutting down...")

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(market.router)
app.include_router(strategies.router)
app.include_router(backtest.router)
app.include_router(ai.router)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "version": settings.API_VERSION}

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "RichManTradingBot API", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)
