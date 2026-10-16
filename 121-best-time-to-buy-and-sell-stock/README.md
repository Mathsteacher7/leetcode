# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy · **Topics:** Array, Dynamic Programming · [Problem on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem

Given daily stock prices, choose one day to buy and a **later** day to sell. Return the maximum profit, or 0 if no profit is possible.

## Approach

A single pass that keeps a summary of the past, the **lowest price so far**:

- Start with `lowest_price = prices[0]` and `best_profit = 0`.
- For each price: update `lowest_price = min(lowest_price, price)`, then `best_profit = max(best_profit, price - lowest_price)`.

At each day, the best possible trade that sells today buys at the lowest price seen up to now, so no pair needs to be compared directly.

## Complexity

- **Time:** O(n), one pass
- **Space:** O(1), two variables

## What I learned

- Finding the global minimum first and then looking to its right fails: the best buy may come before it, or the minimum may be the last day.
- My first code was a nested loop, O(n²), and had two bugs: it allowed selling **before** buying (the inner loop must start at `i + 1`), and it flipped the sign when storing the profit. The single-pass idea was already in my written reasoning; the code just needed to follow it.
- Updating the minimum before calculating the profit is fine: on a new low the profit is 0, which never beats the record. It also means the profit is never negative, so no extra `if` is needed.
- Python's conditional expression is `a if condition else b`, but `min()` / `max()` are often cleaner.
- `float("inf")` is the general starting value for a running minimum when the list might be empty.
