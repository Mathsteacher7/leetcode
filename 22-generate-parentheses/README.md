# 22. Generate Parentheses

**Difficulty:** Medium · **Topics:** String, Dynamic Programming, Backtracking · [Problem on LeetCode](https://leetcode.com/problems/generate-parentheses/)

## Problem

Return every correctly balanced string of `n` pairs of brackets. `n = 3` → `["((()))", "(()())", "(())()", "()(())", "()()()"]`.

## Approach: build the string, with a rule for each character

The same shape as 17: build a string one character at a time and pass `path + char` down. Each call has two possible characters, and each has a rule:

- `(` is allowed while `opened < n`: no more than `n` opening brackets.
- `)` is allowed while `closed < opened`: there has to be an unclosed `(` waiting. Reading left to right with +1 for `(` and −1 for `)`, the running count never goes below 0.

Often both are allowed, so both branches are tried.

```python
result = []

def explore(path: str, opened: int, closed: int) -> None:
    if len(path) == n * 2:
        result.append(path)
        return
    if opened < n:
        explore(path + "(", opened + 1, closed)
    if closed < opened:
        explore(path + ")", opened, closed + 1)

explore("", 0, 0)
return result
```

## Complexity

- **Time:** about O(4ⁿ / √n). The number of answers is the n-th Catalan number (1, 2, 5, 14, 42, …), which grows like 4ⁿ / n^1.5, and each costs O(n) to build. The rules mean every branch the search starts ends as a valid string.
- **Space:** O(n) for the recursion, not counting the output

## What I learned

- **Looking at the answers for n = 4 and n = 5 first** (14 and 42 strings) showed the stopping rule: every string has length `2 * n`.
- **My first rules were wrong.** I thought `(` was only allowed when the close count was 0, and `)` when the open count was 0. `(()())` breaks that. The real rules come from two facts about every valid string: the number of `(` never goes above `n`, and the running count never goes below 0.
- **Don't change the prefix in place when two branches start from it.** With `path += "("` before the first call, the second branch added `)` on top of the extra `(`. Building the new string inside the call, `path + "("`, leaves `path` the same for both branches. The same lesson as 17.
- **`opened < n`, not `<=`.** At `opened == n` all the opening brackets are used.
- **`open` is a Python built-in**, the function that opens files. Naming a variable `open` hides it; the literals `"("` and `")"` are clearer anyway.
- **1, 2, 5, 14, 42 are the Catalan numbers.**
