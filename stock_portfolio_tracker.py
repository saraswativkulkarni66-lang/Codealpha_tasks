# TASK 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190,
    "META": 500,
    "NFLX": 650
}

portfolio = {}
total_investment = 0

print("=" * 50)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter the stocks you want to add.")
print("Type 'done' when you have finished.\n")

while True:
    stock = input("Enter stock symbol: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"✅ {quantity} shares of {stock} added.\n")

    except ValueError:
        print("❌ Please enter a valid number.")

# Display portfolio
print("\n" + "=" * 50)
print("           YOUR PORTFOLIO")
print("=" * 50)

print(f"{'Stock':<10}{'Quantity':<10}{'Price':<12}{'Value':<12}")
print("-" * 50)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(f"{stock:<10}{quantity:<10}${price:<11}${value:<11}")

print("-" * 50)
print(f"Total Investment: ${total_investment}")
print("=" * 50)

# Save result to a text file
save = input("\nDo you want to save the portfolio? (yes/no): ").lower()

if save == "yes":
    with open("stock_portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=" * 40 + "\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock} - Quantity: {quantity}, "
                f"Price: ${price}, Value: ${value}\n"
            )

        file.write("=" * 40 + "\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("✅ Portfolio saved successfully as stock_portfolio.txt")

else:
    print("Portfolio was not saved.")

print("\nThank you for using Stock Portfolio Tracker! 📈")