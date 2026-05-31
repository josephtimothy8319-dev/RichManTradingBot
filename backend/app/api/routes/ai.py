from fastapi import APIRouter
from app.services.ai_service import ai_service
from pydantic import BaseModel

router = APIRouter(prefix="/api/ai", tags=["ai"])

class AnalysisRequest(BaseModel):
    symbol: str
    data: dict = {}

@router.post("/analyze-market")
async def analyze_market(request: AnalysisRequest):
    """Analyze market structure and trends"""
    analysis = await ai_service.analyze_market(request.symbol, request.data)
    return analysis

@router.post("/analyze-setup")
async def analyze_setup(request: AnalysisRequest):
    """Analyze trade setup"""
    analysis = await ai_service.analyze_setup(request.symbol, request.data)
    return analysis

@router.post("/analyze-strategy")
async def analyze_strategy(request: AnalysisRequest):
    """Analyze strategy performance"""
    analysis = await ai_service.analyze_strategy(request.data)
    return analysis

@router.post("/analyze-backtest")
async def analyze_backtest(request: AnalysisRequest):
    """Analyze backtest results"""
    analysis = await ai_service.analyze_backtest(request.data)
    return analysis
