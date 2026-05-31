from fastapi import APIRouter, BackgroundTasks
from app.services.backtest_service import backtest_service
from pydantic import BaseModel

router = APIRouter(prefix="/api/backtest", tags=["backtest"])

class BacktestConfig(BaseModel):
    strategy_id: str
    symbol: str
    timeframe: str
    start_date: str
    end_date: str

@router.post("/run")
async def run_backtest(config: BacktestConfig, background_tasks: BackgroundTasks):
    """Start a backtest job"""
    backtest_id = await backtest_service.create_backtest_job(config.dict())
    background_tasks.add_task(backtest_service.run_backtest, backtest_id)
    return {"backtest_id": backtest_id, "status": "running"}

@router.get("/{backtest_id}")
async def get_backtest_status(backtest_id: str):
    """Get backtest status"""
    status = await backtest_service.get_backtest_status(backtest_id)
    if not status:
        return {"error": "Backtest not found"}
    return status

@router.get("/{backtest_id}/results")
async def get_backtest_results(backtest_id: str):
    """Get completed backtest results"""
    results = await backtest_service.get_backtest_results(backtest_id)
    if not results:
        return {"error": "Backtest not found or still running"}
    return results
