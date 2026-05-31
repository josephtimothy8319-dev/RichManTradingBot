import { TrendingUp, TrendingDown } from 'lucide-react'
import Card from '../common/Card'

interface PriceCardProps {
  symbol: string
  price: number
  change24h: number
  high24h: number
  low24h: number
  volume24h: number
}

export default function PriceCard({ symbol, price, change24h, high24h, low24h, volume24h }: PriceCardProps) {
  const isPositive = change24h >= 0
  const changeColor = isPositive ? 'text-accent-green' : 'text-accent-red'
  const changeIcon = isPositive ? <TrendingUp className="w-4 h-4" /> : <TrendingDown className="w-4 h-4" />

  return (
    <Card className="hover:shadow-glow cursor-pointer">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-lg font-semibold text-text-primary">{symbol}/USDT</h3>
        </div>
        <div className="px-3 py-1 bg-accent-cyan/20 rounded-full text-xs font-medium text-accent-cyan">
          Watching
        </div>
      </div>

      {/* Price */}
      <div className="mb-4">
        <p className="text-3xl font-bold text-text-primary mb-1">${price.toLocaleString()}</p>
        <p className={`flex items-center gap-1 font-semibold ${changeColor}`}>
          {changeIcon}
          {isPositive ? '+' : ''}{change24h.toFixed(2)}% (24h)
        </p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 gap-4 pt-4 border-t border-white/10">
        <div>
          <p className="text-text-muted text-sm mb-1">High 24h</p>
          <p className="text-text-secondary font-medium">${high24h.toLocaleString()}</p>
        </div>
        <div>
          <p className="text-text-muted text-sm mb-1">Low 24h</p>
          <p className="text-text-secondary font-medium">${low24h.toLocaleString()}</p>
        </div>
        <div className="col-span-2">
          <p className="text-text-muted text-sm mb-1">Volume 24h</p>
          <p className="text-text-secondary font-medium">${(volume24h / 1e9).toFixed(2)}B</p>
        </div>
      </div>
    </Card>
  )
}
