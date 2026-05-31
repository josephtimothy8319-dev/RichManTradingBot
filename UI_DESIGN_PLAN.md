# RichManTradingBot - UI/UX Design Plan

## 1. DESIGN PHILOSOPHY

**Target:** Professional traders, hedge fund managers, prop traders  
**Aesthetic:** Premium dark theme with glassmorphism accents  
**Inspiration:** TradingView, Bloomberg Terminal, Binance Pro  
**Tone:** Confidence, precision, professionalism  

---

## 2. COLOR PALETTE

### Primary Colors
```
Background (Dark):
  - #0A0E27    Primary background (very dark navy)
  - #0F1335    Secondary background
  - #151D3F    Tertiary background (card backgrounds)
  - #1A2250    Surface hover state

Accents:
  - #00D9FF    Primary accent (cyan/bright blue)
  - #00FF88    Success/Buy signal (neon green)
  - #FF0055    Danger/Sell signal (neon pink)
  - #FFB800    Warning/Neutral (gold)
  - #7C3AED    AI/Premium feature (purple)

Text:
  - #FFFFFF    Primary text
  - #E5E7EB    Secondary text
  - #9CA3AF    Tertiary text (muted)
  - #6B7280    Disabled/Placeholder text

Glassmorphism:
  - rgba(255, 255, 255, 0.05)   Glass background
  - rgba(0, 217, 255, 0.1)       Blue tint
  - Backdrop blur: 20px
  - Border: 1px rgba(255, 255, 255, 0.1)
```

### Status Colors
```
BUY Signal:      #00FF88 (Neon Green)
SELL Signal:     #FF0055 (Neon Pink)
WAIT Signal:     #FFB800 (Gold)
NEUTRAL:         #9CA3AF (Gray)
UP Trend:        #00FF88 (Green)
DOWN Trend:      #FF0055 (Red)
Flat Trend:      #FFB800 (Yellow)
```

---

## 3. TYPOGRAPHY

```
Font Family:
  - Primary: Inter, -apple-system, BlinkMacSystemFont, sans-serif
  - Monospace: JetBrains Mono, Fira Code, Courier New

Font Sizes:
  - Hero Title:        48px / 64px (bold, letter-spacing: -1px)
  - Page Title:        32px / 40px (bold)
  - Section Title:     24px (bold)
  - Card Title:        18px (semi-bold)
  - Body Large:        16px
  - Body Normal:       14px
  - Body Small:        12px
  - Label/Tag:         11px / 12px (uppercase, letter-spacing: 0.5px)
  - Code/Numbers:      13px (monospace)

Font Weights:
  - Bold:              700
  - Semi-bold:         600
  - Medium:            500
  - Regular:           400
  - Light:             300

Line Heights:
  - Headings:          1.2
  - Body:              1.6
  - Compact:           1.4
```

---

## 4. LAYOUT STRUCTURE

### Main Dashboard Layout

```
┌─────────────────────────────────────────────────────────────────┐
│                        HEADER (80px)                             │
│ Logo | Search | Market Stats | Notifications | Profile Menu    │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┬─────────────────────────────────────────────────┐
│              │                                                 │
│   SIDEBAR    │           MAIN CONTENT AREA                    │
│   (240px)    │                                                 │
│              │  ┌──────────────────────────────────────────┐  │
│ - Dashboard  │  │ CHART AREA (60% height)                  │  │
│ - Market     │  │ - TradingView Lightweight Charts         │  │
│ - Portfolio  │  │ - Indicators panel                       │  │
│ - Strategies │  │ - Timeframe selector                     │  │
│ - Signals    │  └──────────────────────────────────────────┘  │
│ - Backtest   │                                                 │
│ - AI Chat    │  ┌──────────┬────────┬──────────────────────┐  │
│ - Settings   │  │ Watchlist│ Market │ AI Recommendations │  │
│              │  │ (20%)    │ Facts  │ (40%)               │  │
│              │  │          │ (20%)  │                     │  │
│              │  └──────────┴────────┴──────────────────────┘  │
└──────────────┴─────────────────────────────────────────────────┘
```

### Responsive Breakpoints
```
Desktop:   ≥ 1400px (full layout)
Tablet:    768px - 1399px (sidebar collapses)
Mobile:    < 768px (stacked layout, bottom navigation)
```

---

## 5. COMPONENT DESIGNS

### Header
- Fixed positioning, height: 80px
- Logo on left with wordmark
- Centered search bar (searchable coins, strategies)
- Market stats in center (BTC price, total 24h volume)
- Right side: notifications bell, user profile dropdown
- Subtle gradient border at bottom

### Sidebar
- Width: 240px (collapsible to 80px on tablet)
- Dark background with accent highlights
- Navigation items with hover states (blue accent on left)
- Active state: background color + left border highlight
- Smooth collapse/expand animation
- Footer with settings and logout

### Price Card Component
```
┌─────────────────────────────────┐
│ BTC/USDT               ▼        │  
│ $43,521.50                      │  Title row
│ +2.35% ▲ (24h)                  │  Price + change
├─────────────────────────────────┤
│ High: $44,200  │  Vol: $28.5B   │  Stats
│ Low:  $42,100  │  Chg: +$1,240  │
└─────────────────────────────────┘

Style: Glassmorphism with accent border
Animation: Smooth price transitions
```

### Chart Component
- TradingView Lightweight Charts
- Full width, responsive height
- Timeframe buttons: 1M, 5M, 15M, 1H, 4H, 1D, 1W, 1M
- Candlestick + Volume bars
- Technical indicators dropdown
- Drawing tools (optional for Phase 1)
- Crosshair cursor with price tooltip

### Watchlist Component
```
┌────────────────────────────┐
│ WATCHLIST                  │
├────────────────────────────┤
│ BTC  $43,521  +2.35%  ✓   │  ← clickable
│ ETH  $2,256   -1.20%  ✓   │  ← shows checkmark when watching
│ SOL  $178.50  +5.67%  ✓   │
│ BNB  $612.35  +0.45%  ✓   │
│ XRP  $0.523   -2.10%  ✓   │
├────────────────────────────┤
│ + Add to watchlist         │
└────────────────────────────┘

Interactions:
- Click coin: navigate to detail view
- Hover: show mini details
- Star icon: toggle watching
- Right-click: context menu
```

### Portfolio Panel
```
┌──────────────────────────────┐
│ PORTFOLIO                    │
├──────────────────────────────┤
│ Total Value: $125,340.50     │  Header
│ 24h Change: +$2,340 (+1.9%)  │
├──────────────────────────────┤
│ Cash: $25,340.50             │  Breakdown
│ Positions: $100,000.00       │
├──────────────────────────────┤
│ BTC  50.5  $43,521  50%  ↑   │  Position row
│ ETH  200   $2,256   45%  ↓   │
│ SOL  500   $178.50  5%   ↑   │
└──────────────────────────────┘
```

### Signal Card
```
┌─────────────────────────────────────────┐
│ BUY  STRONG  Confidence: 87%           │
├─────────────────────────────────────────┤
│ Bitcoin showing bullish divergence      │
│ Technical: RSI oversold bounce          │
│ Sentiment: Positive news flow           │
│ Price target: $46,000                   │
│ Signal generated: 2 mins ago            │
├─────────────────────────────────────────┤
│ Strategy: "Growth Pattern"  |  Details ▶ │
└─────────────────────────────────────────┘

Color: Background changes based on signal type
BUY: green accent
SELL: red accent
WAIT: yellow accent
```

### AI Assistant Chat Panel
```
┌───────────────────────────────────────┐
│ AI ASSISTANT                      × ⚙ │
├───────────────────────────────────────┤
│                                       │
│ Bot: Market analysis shows BTC in     │  Message bubble
│      strong uptrend. Current RSI      │
│      is 62, indicating momentum.      │
│ [Chart] [Buy]  [Dismiss]             │
│                                       │
│ You: Should I buy now?                │  Message bubble
│                                       │
│ Bot: Based on:
│      • Technical: 75% bullish        │
│      • Sentiment: +82%               │
│      • News: 3 positive articles     │
│      Recommendation: BUY              │
│ [View Details] [Set Alert]            │
│                                       │
├───────────────────────────────────────┤
│ [Input field...] [Send] [🎤]          │
└───────────────────────────────────────┘
```

---

## 6. INTERACTIVE ELEMENTS

### Buttons
```
Primary Button:
  - Background: Linear gradient (cyan to blue)
  - Hover: Brightness increase
  - Active: Scale 0.98
  - Disabled: Opacity 0.5, cursor not-allowed
  - Padding: 12px 24px
  - Border-radius: 8px
  - Font-weight: 600

Secondary Button:
  - Background: Transparent with border
  - Border: 1px solid #00D9FF
  - Hover: Background rgba(0, 217, 255, 0.1)
  - Active: Background rgba(0, 217, 255, 0.2)

Danger Button:
  - Background: #FF0055
  - Hover: Brightness increase
  - Active: Scale 0.98

Success Button:
  - Background: #00FF88
  - Color: #000000
```

### Input Fields
```
Base Style:
  - Background: rgba(255, 255, 255, 0.05)
  - Border: 1px solid rgba(255, 255, 255, 0.1)
  - Border-radius: 8px
  - Padding: 12px 16px
  - Font-size: 14px
  - Color: #FFFFFF
  - Transition: all 0.2s ease

Focused:
  - Background: rgba(255, 255, 255, 0.08)
  - Border: 1px solid #00D9FF
  - Box-shadow: 0 0 20px rgba(0, 217, 255, 0.3)

Error:
  - Border: 1px solid #FF0055
  - Box-shadow: 0 0 20px rgba(255, 0, 85, 0.2)
```

### Tooltips & Popovers
- Background: Glassmorphism effect
- Animation: Fade in + slight scale
- Arrow pointer with smooth edges
- Font-size: 12px
- Max-width: 300px
- Delay: 300ms hover before show

---

## 7. ANIMATIONS & TRANSITIONS

### Page Transitions
- Duration: 300ms
- Easing: cubic-bezier(0.4, 0, 0.2, 1)
- Fade + subtle slide: translateY(-10px) fade-in

### Component Animations
```css
/* Smooth hover effects */
transition: all 0.2s ease;

/* Chart animations */
candle-render: 150ms ease-out;

/* Price changes */
price-update: 300ms ease-out (number animation)

/* Signal appearance */
signal-fade-in: 400ms ease-out

/* Button press */
button-active: scale(0.98) 150ms
```

### Real-time Updates
- Price changes: Green pulse (up) or Red pulse (down)
- Smooth number transitions (tweening)
- Portfolio updates: Slide in from right
- New signals: Pop-in with bounce effect

---

## 8. DARK MODE THEMES

### Default (Dark Blue)
- Primary: #0A0E27
- Accent: #00D9FF (Cyan)
- Used: Default theme

### Professional (Darker)
- Primary: #050812
- Accent: #00D9FF
- Used: Alternative dark theme

### Trading Green
- Primary: #0A0E27
- Accent: #00FF88 (Green)
- Used: Alternative theme

---

## 9. ACCESSIBILITY

- WCAG 2.1 AA compliance
- Minimum contrast ratio: 4.5:1
- Keyboard navigation support
- Screen reader support
- Focus indicators on all interactive elements
- Alt text on all images
- Semantic HTML structure
- ARIA labels where necessary

---

## 10. RESPONSIVE DESIGN

### Desktop (1400px+)
- Full sidebar (240px)
- 3-column layout for content
- All panels visible
- Full feature set

### Tablet (768px - 1399px)
- Collapsible sidebar (icon only)
- 2-column content layout
- Bottom sheets for modals
- Stack some panels vertically

### Mobile (<768px)
- Hidden sidebar (hamburger menu)
- Single column layout
- Bottom navigation bar
- Full-screen modals
- Touch-optimized buttons (min 48px)
- Swipe gestures for navigation

---

## 11. MICRO-INTERACTIONS

### Loading States
- Skeleton screens with pulse animation
- Animated spinners (rotating gradient circles)
- Loading text with animated dots

### Success States
- Checkmark animation (draw effect)
- Brief success message
- Color flash (green)

### Error States
- Shake animation
- Red highlight
- Error message with dismiss option

### Empty States
- Centered illustration
- Helpful message
- Call-to-action button

---

## 12. PAGE FLOWS

### Dashboard Page
1. Header with market stats
2. Large chart area (center)
3. Watchlist panel (bottom left)
4. Market facts panel (bottom center)
5. AI recommendations (bottom right)
6. Floating action button for quick actions

### Portfolio Page
1. Portfolio summary card (total value, daily change)
2. Performance chart
3. Positions table with sorting/filtering
4. Add position button
5. Portfolio history tab

### Strategies Page
1. Active strategies list
2. Strategy creation modal
3. Strategy detail panel
4. Strategy performance metrics
5. Strategy edit/delete options

### AI Assistant Page
1. Chat history panel (left)
2. Large chat area (center)
3. Input field at bottom
4. Context panel (right): current analysis
5. Quick action buttons

### Backtesting Page
1. Backtest configuration panel
2. "Run backtest" button
3. Results visualization
4. Detailed metrics
5. Equity curve chart
6. Trade history table

---

## 13. NOTIFICATION SYSTEM

### Toast Notifications
- Position: Top right
- Auto-dismiss: 5 seconds
- Duration: 300ms fade-in/out
- Stack: Multiple toasts stack vertically

Types:
```
Success:  Green accent, checkmark icon
Error:    Red accent, x icon
Warning:  Yellow accent, ! icon
Info:     Cyan accent, i icon
```

### In-App Alerts
- Persistent until dismissed
- Full-width banner style
- Position: Below header
- Types: Success, Error, Warning, Info

---

## 14. FORMS & MODALS

### Modal Style
- Overlay: Semi-transparent dark (rgba(0,0,0,0.7))
- Backdrop blur: 4px
- Card: Glassmorphism effect
- Border-radius: 16px
- Padding: 32px
- Animation: Fade + scale from center

### Form Fields
- Label above input
- Helper text below
- Inline error messages (red text)
- Focus indicators (cyan border + glow)
- Placeholder text (muted gray)

---

## 15. DESIGN SYSTEM TOKENS

```
Spacing Scale:
  xs:  4px
  sm:  8px
  md:  16px
  lg:  24px
  xl:  32px
  2xl: 48px

Border Radius:
  sm:  4px
  md:  8px
  lg:  12px
  xl:  16px
  full: 9999px

Shadows:
  sm:  0 1px 2px rgba(0,0,0,0.3)
  md:  0 4px 12px rgba(0,0,0,0.3)
  lg:  0 8px 24px rgba(0,0,0,0.3)
  xl:  0 12px 32px rgba(0,0,0,0.3)
  glow: 0 0 20px rgba(0,217,255,0.3)

Transitions:
  fast:   150ms
  normal: 300ms
  slow:   500ms
  easing: cubic-bezier(0.4, 0, 0.2, 1)
```

---

## 16. NEXT STEPS

1. Create Figma design file with all components
2. Build component library in React
3. Setup Tailwind CSS with custom configuration
4. Implement all interactive states
5. Setup responsive design breakpoints
6. Test on multiple devices
7. Get design approval
8. Proceed with backend integration
