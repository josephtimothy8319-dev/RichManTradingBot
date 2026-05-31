import { ReactNode } from 'react'
import { cn } from '../../utils/cn'

interface CardProps {
  children: ReactNode
  className?: string
  gradient?: boolean
  [key: string]: any
}

export default function Card({ children, className, gradient = false, ...props }: CardProps) {
  return (
    <div
      className={cn(
        'bg-gradient-to-br from-bg-tertiary/50 to-bg-tertiary/30 backdrop-blur-glass border border-white/10 rounded-xl p-6 transition-all hover:border-white/20',
        gradient && 'bg-gradient-to-br from-accent-cyan/10 to-accent-purple/10',
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
}
