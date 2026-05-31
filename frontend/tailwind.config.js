/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Background
        'bg-primary': '#0A0E27',
        'bg-secondary': '#0F1335',
        'bg-tertiary': '#151D3F',
        'bg-hover': '#1A2250',
        
        // Accents
        'accent-cyan': '#00D9FF',
        'accent-green': '#00FF88',
        'accent-red': '#FF0055',
        'accent-gold': '#FFB800',
        'accent-purple': '#7C3AED',
        
        // Text
        'text-primary': '#FFFFFF',
        'text-secondary': '#E5E7EB',
        'text-tertiary': '#9CA3AF',
        'text-muted': '#6B7280',
      },
      backdropBlur: {
        'glass': '20px',
      },
      boxShadow: {
        'glow': '0 0 20px rgba(0, 217, 255, 0.3)',
        'glow-red': '0 0 20px rgba(255, 0, 85, 0.2)',
      },
      animation: {
        'pulse-cyan': 'pulse-cyan 1s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        'pulse-cyan': {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.5' },
        },
      },
    },
  },
  plugins: [],
}
