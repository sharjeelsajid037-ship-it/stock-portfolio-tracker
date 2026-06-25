# 📈 Stock Portfolio Tracker

A beginner-friendly Python program to track stock investments and calculate portfolio value.

## Features

- **Hardcoded Stock Prices** — Track popular stocks: AAPL, TSLA, GOOGL, AMZN, MSFT
- **Input Validation** — Validates stock symbols and quantities with helpful error messages
- **Portfolio Summary** — Displays a clean, formatted summary of your investments
- **Save to File** — Optionally save your portfolio summary to a text file

## How to Run

1. Make sure you have **Python 3** installed
2. Clone this repository:
   ```bash
   git clone https://github.com/sharjeelsajid037-ship-it/stock-portfolio-tracker.git
   cd stock-portfolio-tracker
   ```
3. Run the program:
   ```bash
   python portfolio_tracker.py
   ```

## Usage

```
==================================================
       STOCK PORTFOLIO TRACKER
==================================================

Available stocks and their current prices:

  AAPL   -> $180
  TSLA   -> $250
  GOOGL  -> $140
  AMZN   -> $130
  MSFT   -> $320

--------------------------------------------------

How many different stocks do you want to enter? 2

--- Stock #1 ---
Enter stock symbol (e.g., AAPL): AAPL
Enter quantity for AAPL: 10

--- Stock #2 ---
Enter stock symbol (e.g., AAPL): TSLA
Enter quantity for TSLA: 5

==================================================
         PORTFOLIO SUMMARY
==================================================

Stock        Qty     Price       Value
--------------------------------------
AAPL          10      $180      $1800
TSLA           5      $250      $1250
--------------------------------------
TOTAL                           $3050
==================================================
```

## Concepts Used

- **Dictionaries** — Storing stock data
- **Loops** — Iterating through stocks and user inputs
- **Input Validation** — Try/except blocks and conditional checks
- **String Formatting** — Clean, aligned output
- **File Handling** — Writing results to a text file

## Author

**Sharjeel Sajid** — [@sharjeelsajid037-ship-it](https://github.com/sharjeelsajid037-ship-it)
