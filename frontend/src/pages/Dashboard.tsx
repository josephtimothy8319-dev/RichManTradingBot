import { BarChart3, TrendingUp, Volume2 } from 'lucide-react'
import Card from '../components/common/Card'
import PriceCard from '../components/market/PriceCard'
import Watchlist from '../components/market/Watchlist'
import PortfolioStats from '../components/portfolio/PortfolioStats'
import AIPanel from '../components/ai/AIPanel'

export default function Dashboard() {
  return (
    <div className="p-6 space-y-6">
      {/* Market Stats Bar */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-text-muted text-sm mb-1">Market Cap</p>
              <p className="text-2xl font-bold text-text-primary">$1.2T</p>
            </div>
            <BarChart3 className="w-8 h-8 text-accent-cyan opacity-50" />
          </div>
        </Card>

        <Card>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-text-muted text-sm mb-1">24h Volume</p>
              <p className="text-2xl font-bold text-text-primary">$85.3B</p>
            </div>
            <Volume2 className="w-8 h-8 text-accent-green opacity-50" />
          </div>
        </Card>

        <Card>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-text-muted text-sm mb-1">BTC Dominance</p>
              <p className="text-2xl font-bold text-text-primary">52.4%</p>
            </div>
            <TrendingUp className="w-8 h-8 text-accent-gold opacity-50" />
          </div>
        </Card>
      </div>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Chart Area */}
        <div className="lg:col-span-2 space-y-6">
          {/* Chart Placeholder */}
          <Card className="h-96 bg-gradient-to-br from-bg-tertiary/50 to-bg-tertiary/30 flex items-center justify-center">
            <div className="text-center">
              <BarChart3 className="w-16 h-16 text-accent-cyan/30 mx-auto mb-4" />
              <p className="text-text-muted mb-2">TradingView Chart Coming Soon</p>
              <p className="text-text-muted text-sm">Real-time candlestick charts with technical indicators</p>
            </div>
          </Card>

          {/* Top Movers */}
          <Card>
            <h3 className="text-lg font-semibold text-text-primary mb-4">TOP GAINERS</h3>
            <div className="space-y-3">
              {[
                { symbol: 'SOL', change: 5.67, price: 178.50 },
                { symbol: 'AVAX', change: 4.23, price: 35.20 },
                { symbol: 'NEAR', change: 3.45, price: 6.89 },
              ].map((item) => (
                <div key={item.symbol} className="flex items-center justify-between p-2 hover:bg-bg-hover/30 rounded transition-colors cursor-pointer">
                  <span className="font-medium text-text-primary">{item.symbol}</span>
                  <div className="flex items-center gap-3">
                    <span className="text-text-secondary">${item.price}</span>
                    <span className="text-accent-green font-semibold">+{item.change}%</span>
                  </div>
                </div>
              ))}
            </div>
          </Card>
        </div>

        {/* Right Sidebar */}
        <div className="lg:col-span-2 space-y-6">
          {/* Watchlist */}
          <Watchlist />

          {/* Market Facts */}
          <Card>
            <h3 className="text-lg font-semibold text-text-primary mb-4">MARKET FACTS</h3>
            <div className="space-y-3 text-sm">
              <div className="flex justify-between items-center py-2 border-b border-white/10">
                <span className="text-text-muted">Fear & Greed Index</span>
                <span className="text-accent-gold font-semibold">72 (Greed)</span>
              </div>
              <div className="flex justify-between items-center py-2 border-b border-white/10">
                <span className="text-text-muted">Global Market Cap</span>
                <span className="text-text-secondary font-semibold">↑ 2.3%</span>
              </div>
              <div className="flex justify-between items-center py-2">
                <span className="text-text-muted">Active Coins</span>
                <span className="text-accent-cyan font-semibold">15,234</span>
              </div>
            </div>
          </Card>
        </div>
      </div>

      {/* Bottom Section - Portfolio & AI */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Portfolio Stats */}
        <PortfolioStats />

        {/* AI Assistant */}
        <div className="lg:col-span-2">
          <AIPanel />
        </div>
      </div>
    </div>
  )
}
