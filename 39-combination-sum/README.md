# 39. Combination Sum

**Difficulty:** Medium · **Topics:** Array, Backtracking · [Problem on LeetCode](https://leetcode.com/problems/combination-sum/)

## Problem

Return every unique combination of `candidates` (distinct positive numbers) that adds up to `target`. Each number can be used as many times as you like, and `[2, 2, 3]` and `[3, 2, 2]` count as the same combination.

`[2, 3, 6, 7]`, target 7 → `[[2, 2, 3], [7]]`

## Approach: backtracking with a start index

The same choose, explore, undo shape as 78 Subsets, with one loop of choices per call:

```python
candidates.sort()
result = []
path = []

def explore(start: int, remaining: int) -> None:
    if remaining == 0:
        result.append(path[:])
        return
    for i in range(start, len(candidates)):
        if candidates[i] > remaining:
            break                                   # sorted: every later one is too big too
        path.append(candidates[i])                  # choose
        explore(i, remaining - candidates[i])       # explore, starting at i again
        path.pop()                                  # undo

explore(0, target)
return result
```

## Complexity

- **Time:** exponential, with no neat formula: it depends on how many combinations exist. A common rough bound is O(n^(T/m)), where T is the target and m the smallest candidate, since a path is at most T/m numbers deep.
- **Space:** O(T/m) for the recursion and `path`, not counting the output

## What I learned

- **Compared with 78, three things change:**
  - the next call starts at `i`, not `i + 1`, so the same number can be picked again;
  - a combination is saved only when `remaining == 0`, not at every leaf;
  - the `break` cuts off branches that can't work.
- **The repeats come from the recursion, not a `while` loop.** My instinct was a `while` loop that kept adding 2 while it fitted. But each call has its own `for` loop, and passing `i` as the next `start` lets the next call pick the same number again. Three nested calls each choosing 2 is how `[2, 2, 2]` happens.
- **The start index is what prevents duplicates.** Once a call moves on from 2 to 3, nothing below it can go back to 2, so `[3, 2, 2]` is never built. Sorting doesn't prevent duplicates; it's what makes the `break` safe.
- **`start` is a position, not a value.** My first version did `remaining - start`, mixing an index with an amount, and appended `remaining` to `path` instead of a candidate.
- **Check `remaining == 0` first, before the loop.** I had it inside the loop, after the `break`. When `remaining` is 0, every candidate is bigger, so the `break` fired first and nothing was ever saved.
- **Use `candidates[i]`, not `candidates[start]`**: the loop variable is the candidate being tried.
- **`path.pop()` undoes the choice** once everything starting with it has been explored, so the loop can try the next candidate in its place.
- **`path[:]` saves a copy**, because `path` keeps changing after it's saved.
- **This one needed seeing.** I built a line-by-line debugger with Claude showing the tree of choices, the same number being picked again, and the branches cut by the `break`, and played it next to the 78 Subsets debugger to compare the two.
