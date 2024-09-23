""" def max_profit(prices):
    # Initialize minimum price to a large number and max profit to 0
    min_price = float('inf')
    max_profit = 0

    # Iterate through the prices
    for price in prices:
        # Update the minimum price so far
        min_price = min(min_price, price)
        if price > min_price:
            print(prices.index)
        
        # Calculate the potential profit if sold today
        profit = price - min_price
        
        # Update the maximum profit
        max_profit = max(max_profit, profit)
    
    return max_profit """

""" def max_profit(prices):
    # Initialize minimum price to a large number and max profit to 0
    min_price = float('inf')
    max_profit = 0
    buy_day = 0  # Track the day to buy
    sell_day = 0  # Track the day to sell

    # Iterate through the prices
    for i in range(len(prices)):
        # If we find a new minimum price, update the buy day
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i  # Update buy day to current index (day)
        
        # Calculate the potential profit if sold today
        profit = prices[i] - min_price
        
        # If we find a better profit, update the sell day and max profit
        if profit > max_profit:
            max_profit = profit
            sell_day = i  # Update sell day to current index (day)
    
    # Print the results
    print(f"Buy on day {buy_day} at price {prices[buy_day]}")
    print(f"Sell on day {sell_day} at price {prices[sell_day]}")
    print(f"Maximum profit: {max_profit}")
    
    return max_profit """

def max_profit(prices):
    if not prices:
        return 0, -1, -1  # Return 0 profit and invalid days if prices list is empty

    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i  # Update buy day to current index (day)
        
        profit = prices[i] - min_price
        
        # If we find a better profit, update the sell day and max profit
        if profit > max_profit:
            max_profit = profit
            sell_day = i  # Update sell day to current index (day)
    
    # Return the results
    return max_profit, buy_day, sell_day

prices = [7, 1, 5, 3, 6, 4]
profit, buy_day, sell_day = max_profit(prices)

print(f"Buy on day {buy_day} at price {prices[buy_day]}")
print(f"Sell on day {sell_day} at price {prices[sell_day]}")
print(f"Maximum profit: {profit}")

