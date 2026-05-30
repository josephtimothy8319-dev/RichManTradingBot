# RichManBot 📊

A professional cryptocurrency trading bot with a TradingView-style dashboard. Built with FastAPI, real-time WebSocket updates, and a responsive web interface.

## Features

### Phase 1 - Core Dashboard ✅
- **Dark-themed dashboard** similar to TradingView
- **Real-time price updates** via WebSocket
- **Live crypto prices** from Binance
- **Multiple coin support** (BTC, ETH, SOL, BNB, ADA)
- **Mobile-friendly design**
- **PC-friendly design**
- **Interactive watchlist panel**
- **Market overview table**
- **Candlestick charts** with multiple timeframes

### Upcoming Phases
- Phase 2: Market Data Integration
- Phase 3: AI Assistant
- Phase 4: Trading Strategies
- Phase 5: Backtesting Engine
- Phase 6: Telegram Integration
- Phase 7: Auto Trading

## Tech Stack

- **Backend**: Python, FastAPI, WebSocket
- **Frontend**: HTML, CSS, JavaScript
- **Market Data**: Binance API
- **Charts**: Chart.js
- **Real-time**: WebSocket

## Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/richmantradingbot.git
   cd richmantradingbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python backend/main.py
   ```

5. **Open the dashboard**
   - Navigate to: `http://localhost:8000/static/index.html`
   - Or access the API: `http://localhost:8000/docs`

## Project Structure

```
richmantradingbot/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── config.py              # Configuration settings
│   ├── services/
│   │   ├── binance_service.py # Binance API integration
│   │   └── websocket_manager.py # WebSocket management
│   ├── models/
│   │   └── crypto.py          # Data models
│   └── routes/
│       └── crypto.py          # API routes
├── frontend/
│   ├── index.html             # Main dashboard page
│   ├── css/
│   │   └── style.css          # Styling
│   └── js/
│       ├── app.js             # Main application logic
│       ├── chart.js           # Chart management
│       └── websocket.js       # WebSocket client
└── requirements.txt           # Python dependencies
```

## API Endpoints

### REST API

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/crypto/prices` - Get all current prices
- `GET /api/crypto/price/{symbol}` - Get price for specific symbol
- `GET /api/crypto/klines/{symbol}` - Get candlestick data
- `GET /api/crypto/symbols` - Get default symbols

### WebSocket

- `WS /ws` - Real-time price updates

## Usage

### Dashboard Features

1. **Price Cards**: Quick view of crypto prices with 24h change
2. **Watchlist**: Add/remove cryptocurrencies to watch
3. **Chart**: Interactive candlestick chart with multiple timeframes (1H, 4H, 1D)
4. **Market Overview**: Table with detailed market data
5. **Real-time Updates**: Automatic price updates via WebSocket

### Configuration

Edit `backend/config.py` to customize:
- API settings
- Default symbols to track
- Price update interval
- CORS origins

## Development

### Adding New Symbols

1. Update `Config.DEFAULT_SYMBOLS` in `backend/config.py`
2. Symbol format: `{COIN}USDT` (e.g., `XRPUSDT`)

### Modifying Update Interval

Change `PRICE_UPDATE_INTERVAL` in `backend/config.py` (in seconds)

## Roadmap

- ✅ Phase 1: Core Dashboard
- ⏳ Phase 2: Market Data Integration
- ⏳ Phase 3: AI Assistant
- ⏳ Phase 4: Trading Strategies
- ⏳ Phase 5: Backtesting
- ⏳ Phase 6: Telegram Integration
- ⏳ Phase 7: Auto Trading

## Performance

- **Real-time Updates**: 2-second interval (configurable)
- **WebSocket**: Efficient binary protocol
- **Chart**: 100-candle history
- **Mobile**: Responsive design for all devices

## Security Notes

- This is Phase 1 - no real trading functionality
- Do not expose API keys in code
- Use environment variables for sensitive data
- Implement proper authentication before Phase 7

## Troubleshooting

### WebSocket Connection Failed
- Ensure the FastAPI server is running
- Check that port 8000 is not blocked
- Verify CORS settings in `config.py`

### No Price Updates
- Check browser console for errors
- Verify Binance API is accessible
- Check network connectivity

### Chart Not Loading
- Ensure Chart.js library is loaded
- Check browser console for errors
- Verify klines endpoint is working

## License

MIT License

## Support

For issues and questions, please open an issue on GitHub.
