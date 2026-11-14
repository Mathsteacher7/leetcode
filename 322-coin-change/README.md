# 322. Coin Change

**Difficulty:** Medium · **Topics:** Array, Dynamic Programming, Breadth-First Search · [Problem on LeetCode](https://leetcode.com/problems/coin-change/)

## Problem

Given coin values `coins` (with as many of each as you like) and a target `amount`, return the fewest coins that add up to exactly `amount`, or `-1` if it can't be done.

## Why greedy doesn't work

Taking the biggest coin that fits each time seems natural, but with coins `[1, 3, 4]` and amount 6 it takes 4 + 1 + 1 = 3 coins, while 3 + 3 = 2 coins. Every combination has to be considered, without trying them all one by one.

## Approach: dynamic programming, "what was the last coin?"

`best[x]` is the fewest coins that make the amount `x`. If the last coin used was `c`, the coins before it made `x − c`, and the table already has the cheapest way to make that. So try each coin as the last one and keep the smallest:

```
best[x] = min over every coin c ≤ x of  best[x − c] + 1
```

```python
best = [float("inf")] * (amount + 1)
best[0] = 0                                   # 0 needs no coins
for x in range(1, amount + 1):
    for c in coins:
        if c <= x:
            best[x] = min(best[x], best[x - c] + 1)
return best[amount] if best[amount] != float("inf") else -1
```

For `[1, 2, 5]` and 11, the table ends `[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]`, so the answer is 3 (5 + 5 + 1).

## Complexity

- **Time:** O(amount × len(coins)), one cell per amount, and each cell tries every coin
- **Space:** O(amount) for the table

## What I learned

- **The table is a list, not a dict.** The keys are the amounts `0` to `amount` with no gaps, so a list index is the key.
- **Infinity means "can't be made yet".** `float("inf")` is bigger than every number, so `min` never picks it, and `inf + 1` is still `inf`. Amounts that can't be made need no special case. My first version used the string `"inf"`, which isn't a number: comparing it with an int raises a `TypeError`.
- **Don't change the loop variable inside the loop.** I wrote `x = x - c`, which changed the amount being filled. `x - c` is only an index to look up: `best[x - c]`.
- **The outer loop is over amounts, the inner loop over coins.** Every smaller amount has to be finished before a bigger one reads it.
- **It's the same shape as 70 Climbing Stairs.** There, the last step was a 1 or a 2, and the ways were added: `ways[n] = ways[n - 1] + ways[n - 2]`. Here, the last move is any coin and the counts are compared with `min`.
- **This one needed seeing.** I built a line-by-line debugger with Claude, showing the `best` table filling one amount at a time, the cell being looked up, and `x`, `c` and `x − c` at every step. Watching each cell reuse earlier cells is what made the "last coin" idea click.

## Alternative

Breadth-first search: start at 0 and each level adds one coin. The first level that reaches `amount` is the fewest coins. It's the same idea as the table, ordered by number of coins instead of by amount.
