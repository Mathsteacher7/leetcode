def max_profit(prices: list[int]) -> int:
    best_profit = 0
    lowest_price = prices[0]
    for price in prices:
        lowest_price = min(lowest_price, price)
        best_profit = max(best_profit, price - lowest_price)
    return best_profit
