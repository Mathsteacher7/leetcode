# 79. Word Search

**Difficulty:** Medium · **Topics:** Array, String, Backtracking, Depth-First Search, Matrix · [Problem on LeetCode](https://leetcode.com/problems/word-search/)

## Problem

Can `word` be spelled on a grid of letters by moving up, down, left or right from cell to cell, without using the same cell twice?

```
A B C E
S F C S
A D E E
```

`"ABCCED"` → `True`, `"SEE"` → `True`, `"ABCB"` → `False` (the B would be needed twice).

## Approach: backtracking from every cell

Two layers, like 200 Number of Islands: a double loop that tries every cell as a start, and a recursive helper that moves in four directions. The difference is that the helper follows **one path, letter by letter**, and frees each cell again when the path backs out.

`explore(row, col, index)` answers: starting at this cell, can I spell `word[index:]`?

```python
visited = set()

def explore(row: int, col: int, index: int) -> bool:
    if index == len(word):
        return True
    if (
        0 <= row < len(board)
        and 0 <= col < len(board[0])
        and board[row][col] == word[index]
        and (row, col) not in visited
    ):
        visited.add((row, col))                       # choose
        found = (
            explore(row - 1, col, index + 1)          # explore
            or explore(row + 1, col, index + 1)
            or explore(row, col - 1, index + 1)
            or explore(row, col + 1, index + 1)
        )
        visited.remove((row, col))                    # undo
        return found
    return False

for row in range(len(board)):
    for col in range(len(board[row])):
        if explore(row, col, 0):
            return True
return False
```

## Complexity

- **Time:** O(m · n · 3^L), where L is the length of the word: m · n starting cells, and after the first step at most 3 new directions, since one is the cell you came from
- **Space:** O(L) for the recursion and `visited`

## What I learned

- **How it differs from 200.** There, visited cells stay marked for good, because an island is counted once. Here a cell is "used" only while it's on the current path. Add it on the way in, remove it on the way back out: choose, explore, undo, as in 39, but on a grid.
- **No shared counter in the outer loop.** My first loop kept one `count` across all the starts. Every start is a fresh attempt at the whole word, so each begins at index 0; the index belongs to the recursion, which passes `index + 1` to the neighbours.
- **Use what the calls return**, in both places. My helper returned `True` as soon as its own letter matched, whatever the neighbours found, so `"AX"` would have been found on any board with an A. And my outer loop called `explore` and threw the answer away.
- **The outer `return False` goes after both loops.** Mine was inside, so only `(0, 0)` was ever tried.
- **Check "word complete" first.** When `index == len(word)`, `word[index]` is past the end and raises an `IndexError`.
- **`or` stops at the first direction that works.** I asked whether to write four `if`s that each return `True`. `or` does the same in one expression, and putting the result in `found` keeps the undo step in one place, before the single `return`.
- **Return `False` explicitly.** Falling off the end returns `None`, which is falsy, but the function promises a `bool`.
- **`return True` leaves only the innermost call.** In the debugger I saw the `True` come back and then every paused call still run its `visited.remove` and `return found`. Each paused call wakes up where it stopped, finishes its own lines, and hands the answer down. Nothing is re-checked: every call is already past its `if`.
- **This one needed seeing.** I built a line-by-line debugger with Claude showing the path growing and backing off across the board, the failed neighbour checks, and the call stack, and a second page, *Recursion Pause*, with a recursive countdown, just to watch calls pause and finish one by one.

## Alternative

Instead of a `visited` set, temporarily overwrite the cell with a character that matches no letter, such as `"#"`, and put the letter back afterwards. It saves the set, but it changes the input while the search runs.
