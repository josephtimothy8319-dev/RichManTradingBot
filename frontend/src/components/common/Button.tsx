import { ReactNode } from 'react'
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '../../utils/cn'

const buttonVariants = cva(
  'inline-flex items-center justify-center gap-2 font-medium rounded-lg transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed focus:outline-none focus:ring-2 focus:ring-offset-2',
  {
    variants: {
      variant: {
        primary: 'bg-gradient-to-r from-accent-cyan to-accent-cyan/80 text-bg-primary hover:shadow-glow active:scale-95',
        secondary: 'bg-transparent border border-accent-cyan text-accent-cyan hover:bg-accent-cyan/10',
        danger: 'bg-accent-red text-white hover:bg-accent-red/90 active:scale-95',
        success: 'bg-accent-green text-bg-primary hover:bg-accent-green/90 active:scale-95',
        ghost: 'text-text-secondary hover:bg-bg-hover/50',
      },
      size: {
        sm: 'px-3 py-1.5 text-sm',
        md: 'px-4 py-2 text-base',
        lg: 'px-6 py-3 text-lg',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

interface ButtonProps extends VariantProps<typeof buttonVariants> {
  children: ReactNode
  className?: string
  [key: string]: any
}

export default function Button({ variant, size, className, ...props }: ButtonProps) {
  return (
    <button className={cn(buttonVariants({ variant, size }), className)} {...props} />
  )
}
