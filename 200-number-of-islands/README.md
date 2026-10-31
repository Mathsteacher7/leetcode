# 200. Number of Islands

**Difficulty:** Medium · **Topics:** Array, Depth-First Search, Breadth-First Search, Matrix · [Problem on LeetCode](https://leetcode.com/problems/number-of-islands/)

## Problem

Given a grid of `"1"` (land) and `"0"` (water), count the islands. An island is land connected up, down, left or right; diagonals don't count.

## Approach

**Scan, count, explore.**

1. **Scan** every cell. Land that hasn't been visited yet is a new island, so count it.
2. **Explore** that island with DFS, marking every connected land cell as visited, so the scan never counts it again.

```python
visited = set()

def explore(row, col):
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        return
    if grid[row][col] != "1" or (row, col) in visited:
        return
    visited.add((row, col))
    explore(row - 1, col)
    explore(row + 1, col)
    explore(row, col - 1)
    explore(row, col + 1)
```

`explore` is defined inside `numIslands`, so it can use `grid` and `visited` directly.

## Complexity

- **Time:** O(rows × cols). Every cell is scanned once, and each land cell is explored at most once.
- **Space:** O(rows × cols) for `visited`, plus the call stack.

This is the best possible time: an unchecked cell could be a one-cell island, so every cell must be read.

## What I learned

- **Counting and exploring are separate jobs.** My first version called `numIslands` recursively on a small grid of neighbours, which lost the cells' positions, restarted the set and counted islands inside the mini grid. The recursive part needed its own function taking a position.
- **The recursion has to be inside `explore`.** In one version the four neighbour calls were in the scanning loop, so only cells one step away were marked and the example gave 5 islands instead of 3.
- **Only count unvisited land**, then explore from that cell itself.
- **Negative indexes don't crash in Python.** `grid[-1]` silently reads the last row, so the bounds check has to be explicit. `0 <= row < len(grid)` chains comparisons like maths; columns are checked against `len(grid[0])`.
- **`(row or col) >= 0` doesn't test both.** `or` returns one of its operands, the same trap as in 100 and 21.
- Cells are `"1"` strings, not the number 1. Positions go in a set as `(row, col)` tuples, which works because tuples are immutable, using `.add()` rather than `.append()`, with double brackets: `visited.add((r, c))`.
- **Early return (guard clauses):** stop-conditions first, each on its own line, then the main work unindented. Equivalent to wrapping everything in one `if`, but easier to read.

## Alternatives

- **Sink the land:** overwrite visited cells with `"0"` instead of keeping a set. Faster in practice and no extra space, but it changes the input.
- **BFS with a queue** (`collections.deque`): the same amount of work, without deep recursion. On a large all-land grid, recursion can go as deep as the number of cells, past Python's default limit of about 1,000 calls.
- **Union-Find:** useful when the grid changes over time, not faster here.
