def coinChange(coins: list[int], amount: int) -> int:
    best = [float("inf")] * (amount + 1)
    best[0] = 0
    for x in range(1, amount + 1):
        for c in coins:
            if c <= x:
                best[x] = min(best[x], best[x - c] + 1)
    return best[amount] if best[amount] != float("inf") else -1
