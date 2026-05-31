import logging
from typing import Dict, List
import json

logger = logging.getLogger(__name__)

class BacktestService:
    """Service for backtesting operations"""
    
    def __init__(self):
        self.backtests = {}  # In-memory storage
    
    async def create_backtest_job(self, config: Dict) -> str:
        """Create a new backtest job"""
        backtest_id = f"bt_{len(self.backtests) + 1}"
        self.backtests[backtest_id] = {
            'id': backtest_id,
            'config': config,
            'status': 'running',
            'progress': 0
        }
        return backtest_id
    
    async def run_backtest(self, backtest_id: str) -> Dict:
        """Run backtest simulation"""
        backtest = self.backtests.get(backtest_id)
        if not backtest:
            return None
        
        # Simulate backtest calculation
        results = {
            'id': backtest_id,
            'status': 'completed',
            'config': backtest['config'],
            'results': {
                'total_trades': 45,
                'winning_trades': 27,
                'losing_trades': 18,
                'win_rate': 60.0,
                'gross_profit': 8500,
                'gross_loss': 3160,
                'net_profit': 5340,
                'profit_factor': 1.85,
                'max_drawdown': 12.5,
                'sharpe_ratio': 1.45,
                'avg_trade': 118.67,
                'best_trade': 520,
                'worst_trade': -180,
                'avg_win': 314.81,
                'avg_loss': 175.56,
                'consecutive_wins': 7,
                'consecutive_losses': 4,
            },
            'equity_curve': self._generate_equity_curve(),
            'drawdown_curve': self._generate_drawdown_curve()
        }
        
        self.backtests[backtest_id].update(results)
        return results
    
    async def get_backtest_status(self, backtest_id: str) -> Dict:
        """Get backtest status"""
        backtest = self.backtests.get(backtest_id)
        if not backtest:
            return None
        
        return {
            'id': backtest_id,
            'status': backtest.get('status', 'running'),
            'progress': backtest.get('progress', 0)
        }
    
    async def get_backtest_results(self, backtest_id: str) -> Dict:
        """Get completed backtest results"""
        backtest = self.backtests.get(backtest_id)
        if not backtest or backtest.get('status') != 'completed':
            return None
        
        return backtest
    
    def _generate_equity_curve(self, points: int = 100) -> List[float]:
        """Generate simulated equity curve"""
        import random
        curve = [10000]
        for _ in range(points - 1):
            change = random.uniform(-0.5, 0.8)  # -0.5% to +0.8%
            curve.append(curve[-1] * (1 + change/100))
        return curve
    
    def _generate_drawdown_curve(self, points: int = 100) -> List[float]:
        """Generate simulated drawdown curve"""
        curve = [0]
        peak = 10000
        current = 10000
        for _ in range(points - 1):
            change = random.uniform(-0.3, 0.5)
            current = current * (1 + change/100)
            peak = max(peak, current)
            drawdown = ((current - peak) / peak) * 100
            curve.append(drawdown)
        return curve

import random
backtest_service = BacktestService()
