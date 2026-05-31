import { Bell, Settings, User, Search } from 'lucide-react'

export default function Header() {
  return (
    <header className="h-20 bg-bg-secondary/50 backdrop-blur-glass border-b border-white/10 flex items-center justify-between px-6 sticky top-0 z-50">
      {/* Logo */}
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 bg-gradient-to-br from-accent-cyan to-accent-purple rounded-lg flex items-center justify-center">
          <span className="text-lg font-bold">🤖</span>
        </div>
        <span className="text-xl font-bold bg-gradient-to-r from-accent-cyan to-accent-purple bg-clip-text text-transparent">
          RichMan
        </span>
      </div>

      {/* Search */}
      <div className="flex-1 mx-8">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-text-muted" />
          <input
            type="text"
            placeholder="Search coins, strategies..."
            className="w-full pl-10 pr-4 py-2 bg-bg-tertiary/50 border border-white/10 rounded-lg text-text-primary placeholder-text-muted focus:outline-none focus:border-accent-cyan focus:shadow-glow transition-all"
          />
        </div>
      </div>

      {/* Right section */}
      <div className="flex items-center gap-6">
        {/* Market stats */}
        <div className="hidden lg:flex items-center gap-4 text-sm">
          <div>
            <p className="text-text-muted">BTC</p>
            <p className="text-accent-cyan font-semibold">$43,521</p>
          </div>
          <div>
            <p className="text-text-muted">ETH</p>
            <p className="text-accent-green font-semibold">$2,256</p>
          </div>
        </div>

        {/* Icons */}
        <button className="p-2 hover:bg-bg-hover rounded-lg transition-colors relative">
          <Bell className="w-5 h-5 text-text-secondary hover:text-accent-cyan" />
          <span className="absolute top-1 right-1 w-2 h-2 bg-accent-red rounded-full"></span>
        </button>

        <button className="p-2 hover:bg-bg-hover rounded-lg transition-colors">
          <Settings className="w-5 h-5 text-text-secondary hover:text-accent-cyan" />
        </button>

        <button className="p-2 hover:bg-bg-hover rounded-lg transition-colors">
          <User className="w-5 h-5 text-text-secondary hover:text-accent-cyan" />
        </button>
      </div>
    </header>
  )
}
