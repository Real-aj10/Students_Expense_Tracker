# 🎓 CampusSpend - Student Expense Tracker

A modern, student-focused financial ledger and habit analytics application built for Hacktoberfest and everyday campus life. Features offline-first local storage, interactive SVG charts, campus habit savings simulators, and Python's legendary **Antigravity** Easter egg.

---

## 🚀 Key Features

### 1. 📅 Daily Spending & Monthly Budget
- **Student Spending Ledger**: Record daily expenses with description, amount, category, date, payment method (*Campus ID Card, Debit, Venmo/UPI, Cash*), notes, and tags (`#cafeteria`, `#books`, `#dorm`, `#study`).
- **1-Click Student Presets**: Instant one-tap logging for recurring campus purchases:
  - 🍱 Campus Cafeteria Lunch ($12.50)
  - 📚 Textbook Rental ($35.00)
  - 🚇 Subway / Metro Pass ($2.75)
  - 🛒 Dorm Groceries ($48.20)
  - ☕ Iced Coffee & Study Fuel ($5.25)
  - 🍕 Late Night Pizza Slice ($4.50)
- **Monthly Budget & Cushion Gauge**:
  - Configure overall monthly budget ceiling and per-category allocations (*Food & Groceries, Tuition & Books, Rent & Housing, Entertainment, Tech & Subscriptions, Transit, Health*).
  - Live **Safe Daily Burn Rate** calculator based on calendar days remaining.
  - **Financial Health Score (0–100)** evaluating spending pace against month progression.
- **Offline-First Persistence & Export**:
  - Automatically persists to browser `localStorage`.
  - 1-click **Export to CSV** and **Export to JSON**.
  - **Import JSON / CSV** file reader to restore or migrate data.

---

### 2. 📊 Spending Charts & Habit Analysis
- **Category Donut Chart**:
  - Interactive SVG proportional breakdown.
  - Hover over slices or legend entries to inspect dollar amounts and percentage shares.
- **14-Day Spending Trajectory**:
  - Chronological daily bar chart tracking the last 14 days of campus spending.
  - Reference dashed line for **Safe Daily Burn Rate** with color indicators for days over budget.
  - Hover tooltips displaying exact daily expenditure and date.
- **Budget vs. Actual Variance**:
  - Side-by-side category progress bars displaying remaining cushion margins (`+$45.00 left`) or overage alerts (`-$12.50 over`).
- **Student Habit Insights**:
  - **Weekend vs. Weekday Ratio**: Compares Saturday–Sunday spending vs. Monday–Friday spending with daily averages.
  - **Largest Single Expense Detection**: Identifies your peak purchase and its % impact on your monthly budget.

---

### 3. 💡 Student Savings Hacks & Calculator
- **Habit Savings Simulator**:
  - Toggle realistic student adjustments to calculate projected monthly and semester savings in real-time:
    - 🥪 *Batch-prep 2 lunches/week* (+$120/mo)
    - 📚 *Rent digital / library course reserves* (+$30/mo)
    - 💻 *Activate .edu developer & student perks* (+$45/mo)
    - ☕ *Home-brew dorm coffee* (+$100/mo)
    - 🚲 *Campus shuttle & biking over rideshares* (+$80/mo)
    - 🤝 *Roommate bulk pantry buys* (+$60/mo)
  - Projects total semester savings and computes equivalent campus perks (e.g. "Equivalent to 24 campus dining meals!").
- **Spending Heuristics & AI Financial Advisor**:
  - Real-time recommendations dynamically evaluated against your logged transactions (food concentration alerts, micro-transaction leakage, Venmo cashflow).
- **Curated Campus Hacks Directory**:
  - Actionable guides on university library course reserves, subsidized transit stickers, campus emergency food pantries, and department free printing allocations.

---

### 4. 🛸 The "Antigravity" Easter Egg (xkcd #353 Tribute)
- **Zero-Gravity Mode 🚀**:
  - Toggle button in the header activates floating CSS keyframe physics across all application cards.
  - Cards gently bob in zero gravity with hovering rebound physics and floating space dust particles.
- **Python Terminal Simulator 🐍**:
  - Interactive retro terminal supporting commands:
    - `import antigravity` (Triggers zero-gravity mode and displays Randall Munroe's famous xkcd #353 comic tribute: *"You're flying! How? Python!"*)
    - `expenses()` (Outputs formatted student ledger in terminal)
    - `burn_rate()` (Calculates daily safe spending allowance)
    - `budget()` (Displays budget ceiling & category caps)
    - `help()` (Lists all available commands)

---

## ⚡ Quick Start

### Option 1: Open Directly in Any Browser (Zero Setup Required)
You can double-click `index.html` in Windows Explorer or open it directly in Google Chrome, Microsoft Edge, or Firefox. Everything works offline immediately!

### Option 2: Run with Python
If you have Python installed, simply run:
```bash
python app.py
```
- If **Flask** is installed, it runs a full Flask web server.
- If Flask is not installed, it automatically falls back to Python's built-in `http.server`, requiring **zero `pip install` steps**.
- Open `http://localhost:5000` in your browser.

---

## 📂 Project Structure

```
StudentExpenseTracker/
├── index.html              # Standalone, responsive web app (Tailwind CSS, SVG charts, offline-first)
├── app.py                  # Python server (Flask with built-in http.server fallback)
├── templates/
│   └── index.html          # Flask template copy
└── README.md               # Documentation & Hacktoberfest guide
```
