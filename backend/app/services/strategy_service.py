import logging
from typing import List, Dict
import json

logger = logging.getLogger(__name__)

class StrategyService:
    """Service for strategy management"""
    
    def __init__(self):
        # Mock strategies for demo
        self.strategies = {
            "ma_crossover": {
                "id": "ma_crossover",
                "name": "Moving Average Crossover",
                "description": "Simple MA 10/20 crossover strategy",
                "type": "moving_average",
                "parameters": {"fast_ma": 10, "slow_ma": 20}
            },
            "rsi_overbought": {
                "id": "rsi_overbought",
                "name": "RSI Overbought/Oversold",
                "description": "RSI divergence strategy",
                "type": "rsi",
                "parameters": {"period": 14, "overbought": 70, "oversold": 30}
            },
            "macd_divergence": {
                "id": "macd_divergence",
                "name": "MACD Divergence",
                "description": "MACD signal line crossover",
                "type": "macd",
                "parameters": {"fast": 12, "slow": 26, "signal": 9}
            }
        }
        
        # Mock backtest results
        self.backtest_results = {
            "ma_crossover": {
                "strategy_id": "ma_crossover",
                "win_rate": 61,
                "profit_factor": 1.85,
                "net_profit": 5340,
                "max_drawdown": 12.5,
                "sharpe_ratio": 1.45,
                "total_trades": 45,
                "score": 85.2
            },
            "rsi_overbought": {
                "strategy_id": "rsi_overbought",
                "win_rate": 58,
                "profit_factor": 1.72,
                "net_profit": 4120,
                "max_drawdown": 15.3,
                "sharpe_ratio": 1.20,
                "total_trades": 52,
                "score": 78.5
            },
            "macd_divergence": {
                "strategy_id": "macd_divergence",
                "win_rate": 55,
                "profit_factor": 1.68,
                "net_profit": 3850,
                "max_drawdown": 18.2,
                "sharpe_ratio": 0.98,
                "total_trades": 61,
                "score": 72.1
            }
        }
    
    async def get_all_strategies(self) -> List[Dict]:
        """Get all strategies"""
        return list(self.strategies.values())
    
    async def get_strategy(self, strategy_id: str) -> Dict:
        """Get specific strategy"""
        return self.strategies.get(strategy_id)
    
    async def get_top_strategies(self, top_n: int = 3) -> List[Dict]:
        """Get top performing strategies ranked by score"""
        results = list(self.backtest_results.values())
        results.sort(key=lambda x: x['score'], reverse=True)
        
        ranked = []
        for idx, result in enumerate(results[:top_n], 1):
            strategy = self.strategies.get(result['strategy_id'])
            ranked.append({
                'rank': idx,
                'strategy': strategy,
                'backtest_result': result
            })
        
        return ranked
    
    async def get_strategy_comparison(self, strategy_ids: List[str]) -> List[Dict]:
        """Compare multiple strategies"""
        comparison = []
        for sid in strategy_ids:
            strategy = self.strategies.get(sid)
            result = self.backtest_results.get(sid)
            if strategy and result:
                comparison.append({
                    'strategy': strategy,
                    'backtest_result': result
                })
        return comparison

strategy_service = StrategyService()
