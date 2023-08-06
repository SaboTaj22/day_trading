def calculate_roi(price, percent_change):
    # Calculate ROI using the formula: (1 + percent_change / 100)
    return price * (1 + percent_change / 100)

def find_best_investment(stock1_price, stock1_percent_change, stock2_price, stock2_percent_change):
    # Calculate ROI for each stock
    stock1_roi = calculate_roi(stock1_price, stock1_percent_change)
    stock2_roi = calculate_roi(stock2_price, stock2_percent_change)

    # Determine the best investment
    if stock1_roi < stock2_roi:
        return "Stock 1 yields the highest ROI for the lowest price."
    elif stock2_roi < stock1_roi:
        return "Stock 2 yields the highest ROI for the lowest price."
    else:
        return "Both stocks have the same ROI."

if __name__ == "__main__":
    try:
        stock1_price = float(input("Enter the price of Stock 1: "))
        stock1_percent_change = float(input("Enter the weekly percent average change of Stock 1: "))

        stock2_price = float(input("Enter the price of Stock 2: "))
        stock2_percent_change = float(input("Enter the weekly percent average change of Stock 2: "))

        result = find_best_investment(stock1_price, stock1_percent_change, stock2_price, stock2_percent_change)
        print(result)

    except ValueError:
        print("Invalid input. Please enter numeric values for stock price and percentage change.")
