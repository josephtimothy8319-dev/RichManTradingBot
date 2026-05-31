import { MessageSquare, Send } from 'lucide-react'
import Card from '../common/Card'

export default function AIPanel() {
  return (
    <Card className="flex flex-col h-full">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-text-primary flex items-center gap-2">
          <MessageSquare className="w-5 h-5 text-accent-purple" />
          AI ASSISTANT
        </h3>
      </div>

      {/* Chat area */}
      <div className="flex-1 overflow-y-auto mb-4 space-y-4">
        {/* AI message */}
        <div className="flex gap-3">
          <div className="w-8 h-8 rounded-full bg-gradient-to-br from-accent-purple to-accent-cyan flex items-center justify-center flex-shrink-0 text-sm">🤖</div>
          <div className="flex-1 bg-bg-secondary/50 rounded-lg p-3">
            <p className="text-sm text-text-secondary">
              Market analysis shows BTC in strong uptrend. Current RSI is 62, indicating momentum building.
            </p>
            <div className="flex gap-2 mt-2">
              <button className="text-xs px-2 py-1 bg-accent-cyan/20 text-accent-cyan rounded hover:bg-accent-cyan/30 transition-colors">
                View Details
              </button>
              <button className="text-xs px-2 py-1 bg-accent-green/20 text-accent-green rounded hover:bg-accent-green/30 transition-colors">
                [BUY]
              </button>
            </div>
          </div>
        </div>

        {/* User message */}
        <div className="flex gap-3 justify-end">
          <div className="bg-accent-cyan/20 rounded-lg p-3 max-w-xs">
            <p className="text-sm text-accent-cyan">Should I buy now?</p>
          </div>
        </div>

        {/* AI response */}
        <div className="flex gap-3">
          <div className="w-8 h-8 rounded-full bg-gradient-to-br from-accent-purple to-accent-cyan flex items-center justify-center flex-shrink-0 text-sm">🤖</div>
          <div className="flex-1 bg-bg-secondary/50 rounded-lg p-3">
            <p className="text-sm text-text-secondary mb-2 font-semibold text-accent-green">RECOMMENDATION: BUY</p>
            <p className="text-xs text-text-muted mb-2">Based on:</p>
            <ul className="text-xs text-text-secondary space-y-1 mb-2">
              <li>• Technical: 75% bullish</li>
              <li>• Sentiment: +82%</li>
              <li>• News: 3 positive articles</li>
            </ul>
          </div>
        </div>
      </div>

      {/* Input */}
      <div className="flex gap-2 pt-4 border-t border-white/10">
        <input
          type="text"
          placeholder="Ask me anything..."
          className="flex-1 bg-bg-secondary/50 border border-white/10 rounded-lg px-3 py-2 text-sm text-text-primary placeholder-text-muted focus:outline-none focus:border-accent-cyan transition-colors"
        />
        <button className="p-2 bg-gradient-to-r from-accent-cyan to-accent-purple rounded-lg hover:shadow-glow transition-all">
          <Send className="w-4 h-4 text-white" />
        </button>
      </div>
    </Card>
  )
}
