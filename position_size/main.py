#Explanation
# In this program, we first calculate the stop loss by multiplying the stock price with (1 - risk_percent / 100).
# This will give the price at which the investor should sell the stock to limit their loss to the specified risk percentage.

# Next, we calculate the position size by dividing the total amount the investor wants to invest by the difference between the stop loss price and 1% below the stop loss price.
# This helps ensure that even with a small buffer for transaction costs, the maximum loss per share remains within the desired risk percentage.

def calculate_stop_loss(stock_price, risk_percent):
    stop_loss = stock_price * (1 - risk_percent / 100)
    return stop_loss

def calculate_position_size(total_amount_to_invest, stop_loss):
    position_size = total_amount_to_invest / (stop_loss - stop_loss * 0.01)  # Consider a 1% buffer to account for transaction costs
    return position_size

if __name__ == "__main__":
    try:
        risk_percent = float(input("Enter the amount of risk (as a percentage): "))
        stock_price = float(input("Enter the stock price: "))
        total_amount_to_invest = float(input("Enter the total amount you would like to invest: "))

        stop_loss = calculate_stop_loss(stock_price, risk_percent)
        position_size = calculate_position_size(total_amount_to_invest, stop_loss)

        print("Stop Loss: {:.2f}".format(stop_loss))
        print("Position Size: {:.2f} shares".format(position_size))

    except ValueError:
        print("Invalid input. Please enter numeric values for risk, stock price, and total investment.")
