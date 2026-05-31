import { useLocation, Link } from 'react-router-dom'
import { BarChart3, TrendingUp, Wallet, Zap, Activity, Brain, Settings, LogOut } from 'lucide-react'

const navigation = [
  { name: 'Dashboard', path: '/', icon: BarChart3 },
  { name: 'Market', path: '/market', icon: TrendingUp },
  { name: 'Portfolio', path: '/portfolio', icon: Wallet },
  { name: 'Signals', path: '/signals', icon: Zap },
  { name: 'Strategies', path: '/strategies', icon: Activity },
  { name: 'AI Assistant', path: '/ai', icon: Brain },
]

export default function Sidebar() {
  const location = useLocation()

  return (
    <aside className="w-64 bg-bg-secondary/30 backdrop-blur-glass border-r border-white/10 flex flex-col">
      {/* Navigation */}
      <nav className="flex-1 px-4 py-8 space-y-2">
        {navigation.map((item) => {
          const Icon = item.icon
          const isActive = location.pathname === item.path
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-all group ${
                isActive
                  ? 'bg-gradient-to-r from-accent-cyan/20 to-accent-cyan/10 border-l-2 border-accent-cyan text-accent-cyan'
                  : 'text-text-secondary hover:bg-bg-hover/50'
              }`}
            >
              <Icon className="w-5 h-5" />
              <span className="font-medium">{item.name}</span>
            </Link>
          )
        })}
      </nav>

      {/* Footer */}
      <div className="border-t border-white/10 p-4 space-y-2">
        <button className="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-text-secondary hover:bg-bg-hover/50 transition-colors">
          <Settings className="w-5 h-5" />
          <span className="font-medium">Settings</span>
        </button>
        <button className="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-text-secondary hover:text-accent-red transition-colors">
          <LogOut className="w-5 h-5" />
          <span className="font-medium">Logout</span>
        </button>
      </div>
    </aside>
  )
}
