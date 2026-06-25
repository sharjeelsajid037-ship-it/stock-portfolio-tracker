# ============================================
# Stock Portfolio Tracker
# A beginner-friendly Python program to track
# stock investments and calculate portfolio value.
# ============================================

import sys
# Fix output buffering so print() appears immediately in VS Code terminal
sys.stdout.reconfigure(line_buffering=True)

# --- Section 1: Hardcoded Stock Prices Dictionary ---
# This dictionary stores stock symbols as keys and their current prices as values.
stock_prices = {
    "AAPL": 180,    # Apple
    "TSLA": 250,    # Tesla
    "GOOGL": 140,   # Google (Alphabet)
    "AMZN": 130,    # Amazon
    "MSFT": 320     # Microsoft
}

# --- Section 2: Display Available Stocks ---
# Show the user which stocks are available for tracking.
print("=" * 50)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 50)
print("\nAvailable stocks and their current prices:\n")

for symbol, price in stock_prices.items():
    print(f"  {symbol:6s} -> ${price}")

print("\n" + "-" * 50)

# --- Section 3: Get User Input ---
# Ask the user how many different stocks they want to add to their portfolio.

# This list will store each stock entry as a dictionary with symbol, quantity, and value.
portfolio = []

# Keep asking until the user provides a valid positive number for stock count.
while True:
    try:
        num_stocks = int(input("\nHow many different stocks do you want to enter? "))
        if num_stocks <= 0:
            print("Error: Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")

# --- Section 4: Collect Stock Symbols and Quantities ---
# For each stock, ask the user for the symbol and quantity.
# Validate that the symbol exists in the dictionary and the quantity is positive.

for i in range(1, num_stocks + 1):
    print(f"\n--- Stock #{i} ---")

    # Validate stock symbol
    while True:
        symbol = input("Enter stock symbol (e.g., AAPL): ").upper().strip()
        if symbol in stock_prices:
            break
        else:
            print(f"Error: '{symbol}' is not a valid stock symbol.")
            print(f"Available symbols: {', '.join(stock_prices.keys())}")

    # Validate quantity (must be a positive number)
    while True:
        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Error: Quantity must be a positive number.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

    # Calculate the investment value for this stock (price x quantity)
    price = stock_prices[symbol]
    investment_value = price * quantity

    # Store the stock entry in the portfolio list
    portfolio.append({
        "symbol": symbol,
        "quantity": quantity,
        "price": price,
        "value": investment_value
    })

# --- Section 5: Calculate and Display Results ---
# Show a summary of each stock and the total portfolio value.

print("\n" + "=" * 50)
print("         PORTFOLIO SUMMARY")
print("=" * 50)
print(f"\n{'Stock':<10}{'Qty':>6}{'Price':>10}{'Value':>12}")
print("-" * 38)

# Variable to accumulate the total investment value
total_investment = 0

for entry in portfolio:
    print(f"{entry['symbol']:<10}{entry['quantity']:>6}{('$' + str(entry['price'])):>10}{('$' + str(entry['value'])):>12}")
    total_investment += entry["value"]

print("-" * 38)
print(f"{'TOTAL':<10}{'':>6}{'':>10}{'$' + str(total_investment):>12}")
print("=" * 50)

# --- Display Total Investment Value Prominently ---
print("\n" + "*" * 50)
print(f"*{'':>4}TOTAL INVESTMENT VALUE: ${total_investment:,}{'':>4}*")
print("*" * 50)

# --- Section 6: Save Results to File (Optional) ---
# Ask the user if they want to save the portfolio summary to a text file.

while True:
    save_choice = input("\nWould you like to save this summary to a file? (yes/no): ").lower().strip()
    if save_choice in ("yes", "no", "y", "n"):
        break
    else:
        print("Error: Please enter 'yes' or 'no'.")

if save_choice in ("yes", "y"):
    # Use a 'with' statement for proper file handling (auto-closes the file)
    with open("portfolio_summary.txt", "w") as file:
        file.write("=" * 50 + "\n")
        file.write("         PORTFOLIO SUMMARY\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"{'Stock':<10}{'Qty':>6}{'Price':>10}{'Value':>12}\n")
        file.write("-" * 38 + "\n")

        for entry in portfolio:
            file.write(f"{entry['symbol']:<10}{entry['quantity']:>6}{('$' + str(entry['price'])):>10}{('$' + str(entry['value'])):>12}\n")

        file.write("-" * 38 + "\n")
        file.write(f"{'TOTAL':<10}{'':>6}{'':>10}{'$' + str(total_investment):>12}\n")
        file.write("=" * 50 + "\n")

    print("\nPortfolio summary saved to 'portfolio_summary.txt' successfully!")
else:
    print("\nSummary not saved. Thank you for using the Stock Portfolio Tracker!")

print("\nGoodbye!")
