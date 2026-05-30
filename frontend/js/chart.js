class ChartManager {
    constructor() {
        this.container = document.getElementById('chart');
        this.chart = null;
        this.currentSymbol = 'BTCUSDT';
        this.currentInterval = '1h';
        this.klineData = {};
        this.initChart();
        this.setupIntervalButtons();
    }

    initChart() {
        // Create a simple canvas chart using Chart.js
        const canvas = document.createElement('canvas');
        this.container.appendChild(canvas);
        
        this.ctx = canvas.getContext('2d');
        this.chart = new Chart(this.ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Price',
                    data: [],
                    borderColor: 'rgb(0, 212, 255)',
                    backgroundColor: 'rgba(0, 212, 255, 0.1)',
                    tension: 0.3,
                    fill: true,
                    pointRadius: 0,
                    pointHoverRadius: 6,
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)',
                            font: {
                                size: 12
                            }
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.05)'
                        }
                    },
                    x: {
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)',
                            font: {
                                size: 12
                            }
                        },
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
    }

    setupIntervalButtons() {
        const buttons = document.querySelectorAll('.btn-interval');
        buttons.forEach(button => {
            button.addEventListener('click', (e) => {
                buttons.forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                this.currentInterval = e.target.dataset.interval;
                this.loadChartData(this.currentSymbol);
            });
        });
    }

    async loadChartData(symbol) {
        try {
            const response = await fetch(`/api/crypto/klines/${symbol}?interval=${this.currentInterval}&limit=100`);
            const result = await response.json();
            
            if (result.data) {
                this.updateChart(result.data);
            }
        } catch (error) {
            console.error('Error loading chart data:', error);
        }
    }

    updateChart(klineData) {
        const labels = [];
        const prices = [];

        klineData.forEach(kline => {
            const date = new Date(kline.time * 1000);
            labels.push(date.toLocaleTimeString());
            prices.push(parseFloat(kline.close));
        });

        this.chart.data.labels = labels;
        this.chart.data.datasets[0].data = prices;
        this.chart.update('none');
    }

    switchSymbol(symbol) {
        this.currentSymbol = symbol;
        this.loadChartData(symbol);
    }
}

// Initialize chart when DOM is loaded
let chartManager;
document.addEventListener('DOMContentLoaded', () => {
    chartManager = new ChartManager();
});
