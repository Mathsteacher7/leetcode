# 62. Unique Paths

**Difficulty:** Medium · **Topics:** Math, Dynamic Programming, Combinatorics · [Problem on LeetCode](https://leetcode.com/problems/unique-paths/)

## Problem

A robot starts in the top-left corner of an `m × n` grid and can only move right or down. How many different paths reach the bottom-right corner? `m = 3`, `n = 7` → 28.

## Approach 1: dynamic programming on a 2D table

The robot can only arrive at a square from above or from the left, so:

```
paths to (row, col) = paths to (row − 1, col) + paths to (row, col − 1)
```

The top row and the left column can only be reached in a straight line, so they're all 1: the base cases.

```
1   1   1   1
1   2   3   4
1   3   6  10
```

```python
grid = [[1] * n for _ in range(m)]
for row in range(1, m):
    for col in range(1, n):
        grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
return grid[-1][-1]
```

## Approach 2: combinations

Every path is `m − 1` downs and `n − 1` rights in some order, `m + n − 2` moves in all. Choosing which of those moves are the downs picks one path. That's [`62-unique-path-maths-solution.py`](62-unique-path-maths-solution.py):

```python
from math import comb

return comb(m + n - 2, m - 1)
```

The table in approach 1 is Pascal's triangle turned on its side.

## Complexity

- **Table:** O(m · n) time and space
- **Formula:** about O(min(m, n)) time for the arithmetic, O(1) space

## What I learned

- **This was the first 2D table.** In 70 the answer depended on the two previous numbers in a line, so two variables could carry them. I started from the Climbing Stairs code, and two variables weren't enough: each square needs the square above it, worked out a whole row earlier, so there are `n` "above" values to remember at once.
- **`(m and n) == 1` only checks `n`.** `m and n` evaluates to `n` whenever `m` isn't 0: the same trap as `(a or b) is None`. And a 1 × 1 grid has 1 path, not 2; the table handles it without an early return.
- **A list of lists is read with `grid[row][col]`**, square brackets, row first. `grid(...)` tries to call it as a function.
- **Look back, not forward:** above is `row - 1`, left is `col - 1`. Those cells are already filled.
- **`range` leaves its end out**, so `range(1, m)` reaches `m − 1`; `range(1, m - 1)` missed the last row and column.
- **`[[1] * n for _ in range(m)]`** sets up every base case at once, and each row is a separate list (not `[[1] * n] * m`, the trap from 207).
- **This one needed seeing.** I built a debugger with Claude showing the grid filling cell by cell, with the cell above and the cell on the left highlighted for each sum, and a final check against `math.comb`.
- **The formula needs `from math import comb`** in a standalone file; LeetCode imports it for you.

## Alternative

Each row only needs the row above it, so the table can be one list of length `n`, updated row by row: O(n) space.
