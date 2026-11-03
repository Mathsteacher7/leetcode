# 46. Permutations

**Difficulty:** Medium · **Topics:** Array, Backtracking · [Problem on LeetCode](https://leetcode.com/problems/permutations/)

## Problem

Given a list of distinct integers, return every possible ordering of them.

## Approach

**Backtracking, one position per call.** There are n choices for the first position, n − 1 for the second, and so on, so n! permutations ("n factorial"). Each call fills one position, and its `for` loop tries every number not used yet:

```python
result = []

def backtrack(path):
    if len(path) == len(nums):     # every position filled
        result.append(path[:])
        return
    for num in nums:
        if num in path:
            continue               # already used: try the next number
        path.append(num)           # choose
        backtrack(path)            # explore
        path.pop()                 # undo

backtrack([])
return result
```

## Complexity

- **Time:** O(n · n!): n! permutations, each copied in n steps
- **Space:** O(n) for the recursion and `path`, not counting the output

## What I learned

- **How it differs from Subsets:** in 78 every node had two branches (include or skip). Here a node has one branch per unused number (3, then 2, then 1), so the `for` loop belongs *inside* the function. The base case and the append, recurse, pop rhythm are the same.
- **Rotations aren't permutations.** My first idea, `nums[i:] + nums[:i]`, only gives n of the n! orderings, because the numbers keep their circular order. One number has to be placed per level.
- **Adding several elements at once:** `path.extend(...)`, `path += ...`, or Python's spread, `[*a, *b]`. `append` always adds one item.
- **All of choose, explore and undo must sit inside the "unused" check.** In one version only the `append` was inside the `if`, so used numbers still recursed with an unchanged path, forever.
- **There's no skip branch here.** The second `backtrack(path)` left over from Subsets would explore extra branches and record duplicates; the loop already provides the branches.
- **`continue` skips to the next pass of the nearest loop; `break` leaves the loop.** Neither is affected by the surrounding `if`.
- **`num in path` is O(n)** per check; a `used` set would make it O(1). With at most 6 numbers it makes no practical difference.
- **Runtime:** most submissions are within a few milliseconds because 6! = 720. Slower versions build new lists at every node, join returned lists, or generate nⁿ candidates and filter. `itertools.permutations` (written in C) is faster still, but skips the part an interviewer wants to see.
- I built a second line-by-line debugger with Claude for this solution, which shows each paused call remembering its own `num`, and the `continue` steps that skip used numbers.
