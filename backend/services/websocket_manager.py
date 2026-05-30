import asyncio
from typing import Set
from fastapi import WebSocket
from backend.services.binance_service import BinanceService
from backend.config import Config
import json

class WebSocketManager:
    """Manage WebSocket connections and price broadcasting"""
    
    def __init__(self):
        self.active_connections: Set[WebSocket] = set()
        self.binance_service = BinanceService()
        self.broadcaster_task = None
    
    async def connect(self, websocket: WebSocket):
        """Accept a WebSocket connection"""
        await websocket.accept()
        self.active_connections.add(websocket)
        print(f"Client connected. Total connections: {len(self.active_connections)}")
    
    async def disconnect(self, websocket: WebSocket):
        """Remove a WebSocket connection"""
        self.active_connections.discard(websocket)
        print(f"Client disconnected. Total connections: {len(self.active_connections)}")
    
    async def broadcast_prices(self):
        """Broadcast prices to all connected clients"""
        while True:
            try:
                # Fetch prices for all symbols
                prices = await self.binance_service.get_multiple_prices(Config.DEFAULT_SYMBOLS)
                
                if prices:
                    message = json.dumps({
                        "type": "price_update",
                        "data": prices,
                        "timestamp": prices.get(list(prices.keys())[0], {}).get("timestamp")
                    })
                    
                    # Broadcast to all connected clients
                    disconnected = set()
                    for connection in self.active_connections:
                        try:
                            await connection.send_text(message)
                        except Exception as e:
                            print(f"Error sending message: {e}")
                            disconnected.add(connection)
                    
                    # Clean up disconnected clients
                    for connection in disconnected:
                        await self.disconnect(connection)
                
                await asyncio.sleep(Config.PRICE_UPDATE_INTERVAL)
            
            except Exception as e:
                print(f"Error in broadcast_prices: {e}")
                await asyncio.sleep(Config.PRICE_UPDATE_INTERVAL)
    
    async def start_broadcaster(self):
        """Start the background price broadcaster"""
        self.broadcaster_task = asyncio.create_task(self.broadcast_prices())
    
    async def stop_broadcaster(self):
        """Stop the background price broadcaster"""
        if self.broadcaster_task:
            self.broadcaster_task.cancel()
