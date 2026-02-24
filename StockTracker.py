def stock_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 130,
        "MSFT": 300
    }

    total_investment = 0
    portfolio = []

    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' to finish.\n")

    while True:
        stock_name = input("Enter stock name: ").upper()

        if stock_name == "DONE":
            break

        if stock_name in stock_prices:
            quantity = int(input("Enter quantity: "))
            price = stock_prices[stock_name]
            investment = price * quantity
            total_investment += investment

            portfolio.append((stock_name, quantity, investment))

            print(f"Added {quantity} shares of {stock_name}")
        else:
            print("❌ Stock not available!")

    print("\n📊 Portfolio Summary:")
    for stock in portfolio:
        print(f"{stock[0]} - {stock[1]} shares - ${stock[2]}")

    print(f"\n💰 Total Investment Value: ${total_investment}")

    # Optional: Save to file
    save = input("\nDo you want to save to file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            for stock in portfolio:
                file.write(f"{stock[0]} - {stock[1]} shares - ${stock[2]}\n")
            file.write(f"\nTotal Investment: ${total_investment}")
        print("✅ Portfolio saved to portfolio.txt")


if __name__ == "__main__":
    stock_tracker()