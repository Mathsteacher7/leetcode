# 213. House Robber II

**Difficulty:** Medium · **Topics:** Array, Dynamic Programming · [Problem on LeetCode](https://leetcode.com/problems/house-robber-ii/)

## Problem

The same as 198, but the houses are in a **circle**, so the first and last houses are neighbours.

## Approach

The first and last houses can't both be robbed, so every valid plan leaves out the first house, the last house, or both. Each case is a straight street, which 198 already solves:

```python
def rob(self, nums):
    if len(nums) == 1:
        return nums[0]
    return max(self.rob_line(nums[1:]), self.rob_line(nums[:-1]))
```

`rob_line` is the 198 solution unchanged.

## Complexity

- **Time:** O(n), two passes, and 2n is still O(n)
- **Space:** O(n), because each slice makes a copy. Passing start and end indexes to `rob_line` instead would make it O(1).

## What I learned

- **I found the key fact myself:** the first and last houses can't be robbed together.
- **Don't try to decide in advance.** My next instinct was a condition for which end to drop, then checking the houses next to each end. That's the same trap as the triplets in 198: the right choice can depend on the whole street.
- **Solve every case and take the best.** When you can't tell which option is right, split into cases that together cover every possibility, solve each, and take the `max`. It's the same `max` as inside the loop, one level up. Running the function twice felt wasteful, but it doesn't change the complexity.
- **Reuse instead of rewriting:** yesterday's solution became a helper.
- **Edge case:** a single house has no neighbour to clash with, but both slices of `[5]` are empty, so without the check the answer would be 0 instead of 5.
- `nums[:1]` is just the first element; `nums[:-1]` is everything except the last. An easy typo.
- Name helpers so they can't be confused: `rob_1` and `rob_i` look almost identical.
