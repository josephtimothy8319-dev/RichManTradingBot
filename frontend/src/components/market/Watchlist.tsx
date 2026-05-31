import { Star, TrendingUp, TrendingDown } from 'lucide-react'
import Card from '../common/Card'

interface WatchlistItem {
  symbol: string
  price: number
  change24h: number
}

const watchlistItems: WatchlistItem[] = [
  { symbol: 'BTC', price: 43521, change24h: 2.35 },
  { symbol: 'ETH', price: 2256, change24h: -1.20 },
  { symbol: 'SOL', price: 178.50, change24h: 5.67 },
  { symbol: 'BNB', price: 612.35, change24h: 0.45 },
  { symbol: 'XRP', price: 0.523, change24h: -2.10 },
]

export default function Watchlist() {
  return (
    <Card>
      <h3 className="text-lg font-semibold text-text-primary mb-4">WATCHLIST</h3>
      
      <div className="space-y-3">
        {watchlistItems.map((item) => (
          <div key={item.symbol} className="flex items-center justify-between p-3 bg-bg-secondary/30 rounded-lg hover:bg-bg-hover/30 transition-colors cursor-pointer">
            <div className="flex-1">
              <p className="font-medium text-text-primary">{item.symbol}</p>
              <p className="text-sm text-text-muted">${item.price.toLocaleString()}</p>
            </div>
            <div className={`flex items-center gap-1 font-semibold ${item.change24h >= 0 ? 'text-accent-green' : 'text-accent-red'}`}>
              {item.change24h >= 0 ? <TrendingUp className="w-4 h-4" /> : <TrendingDown className="w-4 h-4" />}
              {item.change24h >= 0 ? '+' : ''}{item.change24h.toFixed(2)}%
            </div>
            <Star className="w-5 h-5 text-accent-gold ml-3" />
          </div>
        ))}
      </div>

      <button className="w-full mt-4 py-2 text-accent-cyan hover:bg-accent-cyan/10 rounded-lg transition-colors font-medium">
        + Add to watchlist
      </button>
    </Card>
  )
}
