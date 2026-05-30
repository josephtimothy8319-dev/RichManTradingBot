class DashboardApp {
    constructor() {
        this.prices = {};
        this.selectedSymbol = 'BTCUSDT';
        this.init();
    }

    init() {
        this.setupWebSocket();
        this.setupEventListeners();
        this.loadInitialData();
    }

    setupWebSocket() {
        wsClient.on('price_update', (data) => {
            this.updatePrices(data);
            this.updateLastUpdate();
        });

        wsClient.on('connected', () => {
            console.log('Dashboard connected to WebSocket');
        });

        wsClient.connect();
    }

    setupEventListeners() {
        // Price card clicks
        document.querySelectorAll('.price-card').forEach(card => {
            card.addEventListener('click', () => {
                const symbol = card.dataset.symbol;
                this.selectSymbol(symbol);
            });
        });
    }

    async loadInitialData() {
        try {
            const response = await fetch('/api/crypto/prices');
            const result = await response.json();
            this.updatePrices(result.data);
        } catch (error) {
            console.error('Error loading initial data:', error);
        }
    }

    updatePrices(priceData) {
        Object.entries(priceData).forEach(([symbol, data]) => {
            this.prices[symbol] = data;
            this.updatePriceCard(symbol, data);
            this.updateWatchlistItem(symbol, data);
            this.updateMarketTable(symbol, data);
        });
    }

    updatePriceCard(symbol, data) {
        const card = document.querySelector(`[data-symbol="${symbol}"]`);
        if (!card) return;

        const change = parseFloat(data.change_percent);
        const changeClass = change >= 0 ? 'positive' : 'negative';
        const changeSign = change >= 0 ? '+' : '';

        card.querySelector('.current-price').textContent = `$${parseFloat(data.price).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        card.querySelector('.price-change').textContent = `${changeSign}${change.toFixed(2)}%`;
        card.querySelector('.price-change').className = `price-change ${changeClass}`;
        card.querySelector('.high').textContent = `$${parseFloat(data.high_24h).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        card.querySelector('.low').textContent = `$${parseFloat(data.low_24h).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;

        if (symbol === this.selectedSymbol && chartManager) {
            chartManager.switchSymbol(symbol);
        }
    }

    updateWatchlistItem(symbol, data) {
        let item = document.querySelector(`[data-watchlist-symbol="${symbol}"]`);
        
        if (!item) {
            item = this.createWatchlistItem(symbol, data);
        }

        const change = parseFloat(data.change_percent);
        const changeClass = change >= 0 ? 'positive' : 'negative';
        const changeSign = change >= 0 ? '+' : '';

        item.querySelector('.watchlist-item-price').textContent = `$${parseFloat(data.price).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        item.querySelector('.watchlist-item-change').textContent = `${changeSign}${change.toFixed(2)}%`;
        item.querySelector('.watchlist-item-change').className = `watchlist-item-change ${changeClass}`;
    }

    createWatchlistItem(symbol, data) {
        const change = parseFloat(data.change_percent);
        const changeClass = change >= 0 ? 'positive' : 'negative';
        const changeSign = change >= 0 ? '+' : '';

        const item = document.createElement('div');
        item.className = 'watchlist-item';
        item.dataset.watchlistSymbol = symbol;
        item.innerHTML = `
            <div class="watchlist-item-header">
                <span class="watchlist-item-symbol">${symbol.replace('USDT', '')}</span>
                <span class="watchlist-item-price">$${parseFloat(data.price).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</span>
            </div>
            <span class="watchlist-item-change ${changeClass}">${changeSign}${change.toFixed(2)}%</span>
        `;

        item.addEventListener('click', () => this.selectSymbol(symbol));
        document.getElementById('watchlist').appendChild(item);

        return item;
    }

    updateMarketTable(symbol, data) {
        let row = document.querySelector(`[data-market-symbol="${symbol}"]`);
        
        if (!row) {
            row = this.createMarketTableRow(symbol, data);
        }

        const change = parseFloat(data.change_percent);
        const changeClass = change >= 0 ? 'positive' : 'negative';
        const changeSign = change >= 0 ? '+' : '';

        row.querySelector('[data-col="price"]').textContent = `$${parseFloat(data.price).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 8 })}`;
        row.querySelector('[data-col="change"]').textContent = `${changeSign}${change.toFixed(2)}%`;
        row.querySelector('[data-col="change"]').className = `${changeClass}`;
        row.querySelector('[data-col="high"]').textContent = `$${parseFloat(data.high_24h).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        row.querySelector('[data-col="low"]').textContent = `$${parseFloat(data.low_24h).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        row.querySelector('[data-col="volume"]').textContent = `$${(parseFloat(data.volume) / 1e6).toFixed(2)}M`;
    }

    createMarketTableRow(symbol, data) {
        const change = parseFloat(data.change_percent);
        const changeClass = change >= 0 ? 'positive' : 'negative';
        const changeSign = change >= 0 ? '+' : '';

        const row = document.createElement('tr');
        row.dataset.marketSymbol = symbol;
        row.innerHTML = `
            <td><strong>${symbol}</strong></td>
            <td data-col="price">$${parseFloat(data.price).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 8 })}</td>
            <td data-col="change" class="${changeClass}">${changeSign}${change.toFixed(2)}%</td>
            <td data-col="high">$${parseFloat(data.high_24h).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
            <td data-col="low">$${parseFloat(data.low_24h).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
            <td data-col="volume">$${(parseFloat(data.volume) / 1e6).toFixed(2)}M</td>
        `;

        document.getElementById('marketTableBody').appendChild(row);
        return row;
    }

    selectSymbol(symbol) {
        this.selectedSymbol = symbol;
        document.querySelectorAll('.price-card').forEach(card => {
            card.classList.remove('active');
        });
        document.querySelector(`[data-symbol="${symbol}"]`).classList.add('active');

        document.querySelectorAll('.watchlist-item').forEach(item => {
            item.classList.remove('active');
        });
        document.querySelector(`[data-watchlist-symbol="${symbol}"]`).classList.add('active');

        if (chartManager) {
            chartManager.switchSymbol(symbol);
        }
    }

    updateLastUpdate() {
        const now = new Date();
        document.getElementById('lastUpdate').textContent = `Last update: ${now.toLocaleTimeString()}`;
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const app = new DashboardApp();
    
    // Update last update time every second
    setInterval(() => {
        app.updateLastUpdate();
    }, 1000);
});
