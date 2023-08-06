def calculate_expected_value(price, returns, probabilities):
    expected_value = sum(price * return_ * prob for return_, prob in zip(returns, probabilities))
    return expected_value

def find_stock_with_greater_expectancy(stock1_price, stock1_returns, stock1_probabilities,
                                       stock2_price, stock2_returns, stock2_probabilities):
    stock1_expected_value = calculate_expected_value(stock1_price, stock1_returns, stock1_probabilities)
    stock2_expected_value = calculate_expected_value(stock2_price, stock2_returns, stock2_probabilities)

    if stock1_expected_value > stock2_expected_value:
        percent_gain = (stock1_expected_value - stock1_price) / stock1_price * 100
        return "Buy Stock 1. It has a greater expectancy of gaining by {:.2f}%.".format(percent_gain)
    elif stock2_expected_value > stock1_expected_value:
        percent_gain = (stock2_expected_value - stock2_price) / stock2_price * 100
        return "Buy Stock 2. It has a greater expectancy of gaining by {:.2f}%.".format(percent_gain)
    else:
        return "Both stocks have the same expectancy of gaining."

if __name__ == "__main__":
    try:
        # Input data for Stock ABC
        stock1_price = 20
        stock1_returns = [3, -7]  # Represents potential gains of 3$ (from 20$ to 23$) and potential losses of -7$ (from 20$ to 13$)
        stock1_probabilities = [0.6, 0.4]  # Represents the probability of each return occurring (60% and 40% respectively)

        # Input data for Stock XYZ
        stock2_price = 10
        stock2_returns = [6, -2]  # Represents potential gains of 6$ (from 10$ to 16$) and potential losses of -2$ (from 10$ to 8$)
        stock2_probabilities = [0.4, 0.6]  # Represents the probability of each return occurring (40% and 60% respectively)

        result = find_stock_with_greater_expectancy(stock1_price, stock1_returns, stock1_probabilities,
                                                    stock2_price, stock2_returns, stock2_probabilities)
        print(result)

    except ValueError:
        print("Invalid input. Please enter numeric values for stock price, returns, and probabilities.")
