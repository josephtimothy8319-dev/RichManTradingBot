from fastapi import APIRouter
from app.services.strategy_service import strategy_service
from typing import List

router = APIRouter(prefix="/api/strategies", tags=["strategies"])

@router.get("/")
async def list_strategies():
    """Get all strategies"""
    strategies = await strategy_service.get_all_strategies()
    return {"strategies": strategies}

@router.get("/top")
async def get_top_strategies(limit: int = 3):
    """Get top performing strategies"""
    rankings = await strategy_service.get_top_strategies(limit)
    return {"rankings": rankings}

@router.get("/compare")
async def compare_strategies(strategy_ids: List[str]):
    """Compare multiple strategies"""
    comparison = await strategy_service.get_strategy_comparison(strategy_ids)
    return {"comparison": comparison}

@router.get("/{strategy_id}")
async def get_strategy(strategy_id: str):
    """Get specific strategy"""
    strategy = await strategy_service.get_strategy(strategy_id)
    if not strategy:
        return {"error": "Strategy not found"}
    return strategy
