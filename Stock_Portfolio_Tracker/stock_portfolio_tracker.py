# Attractive Stock Portfolio Tracker

print("📊 ====================================")
print("📈      STOCK PORTFOLIO TRACKER")
print("📊 ====================================")

# User name
name = input("👤 Enter your name: ")

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "AMZN": 150
}

total_investment = 0
portfolio = {}

print(f"\n👋 Welcome {name}!")
print("\n📌 Available Stocks:")

# Display stock prices nicely
for stock, price in stock_prices.items():
    print(f"   🔹 {stock} : ₹{price}")

# Taking user input
while True:

    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:

        quantity = int(input(f"Enter quantity of {stock_name}: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        # Save portfolio details
        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

        print(f"✅ Added {stock_name} worth ₹{investment}")

    else:
        print("❌ Stock not available.")

# Final Portfolio Summary
print("\n📋 ===== YOUR PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    print(f"🔸 {stock} × {quantity} shares")

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# Save result to file
with open("portfolio.txt", "w", encoding="utf-8") as file:

    file.write("===== STOCK PORTFOLIO SUMMARY =====\n")

    for stock, quantity in portfolio.items():
        file.write(f"{stock} × {quantity} shares\n")

    file.write(f"\nTotal Investment Value: ₹{total_investment}")

highest_stock = max(stock_prices, key=stock_prices.get)

print(f"\n📌 Highest priced stock today: {highest_stock}")

print("\n📁 Portfolio saved successfully in portfolio.txt")
print(f"🙏 Thank you for using the tracker, {name}!")