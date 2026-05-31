import { TrendingUp } from 'lucide-react'
import Card from '../common/Card'

export default function PortfolioStats() {
  return (
    <Card gradient>
      <h3 className="text-lg font-semibold text-text-primary mb-4">PORTFOLIO</h3>
      
      <div className="mb-6">
        <p className="text-text-muted text-sm mb-1">Total Value</p>
        <p className="text-4xl font-bold text-text-primary mb-2">$125,340.50</p>
        <div className="flex items-center gap-2 text-accent-green font-semibold">
          <TrendingUp className="w-4 h-4" />
          +$2,340 (+1.9%) Today
        </div>
      </div>

      <div className="grid grid-cols-2 gap-4 pt-4 border-t border-white/10">
        <div>
          <p className="text-text-muted text-sm mb-1">Cash Balance</p>
          <p className="text-xl font-bold text-text-secondary">$25,340.50</p>
        </div>
        <div>
          <p className="text-text-muted text-sm mb-1">In Positions</p>
          <p className="text-xl font-bold text-text-secondary">$100,000.00</p>
        </div>
      </div>

      {/* Allocation */}
      <div className="mt-6 pt-4 border-t border-white/10">
        <p className="text-text-muted text-sm mb-3">Allocation</p>
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-text-secondary text-sm">BTC (50%)</span>
            <div className="flex-1 mx-3 h-2 bg-bg-secondary rounded-full overflow-hidden">
              <div className="h-full bg-gradient-to-r from-accent-green to-accent-cyan" style={{ width: '50%' }}></div>
            </div>
            <span className="text-text-secondary text-sm font-medium">$62,670</span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-text-secondary text-sm">ETH (45%)</span>
            <div className="flex-1 mx-3 h-2 bg-bg-secondary rounded-full overflow-hidden">
              <div className="h-full bg-gradient-to-r from-accent-cyan to-accent-purple" style={{ width: '45%' }}></div>
            </div>
            <span className="text-text-secondary text-sm font-medium">$56,403</span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-text-secondary text-sm">SOL (5%)</span>
            <div className="flex-1 mx-3 h-2 bg-bg-secondary rounded-full overflow-hidden">
              <div className="h-full bg-gradient-to-r from-accent-purple to-accent-red" style={{ width: '5%' }}></div>
            </div>
            <span className="text-text-secondary text-sm font-medium">$6,267</span>
          </div>
        </div>
      </div>
    </Card>
  )
}
