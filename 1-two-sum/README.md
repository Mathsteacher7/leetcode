# 1. Two Sum

**Difficulty:** Easy · **Topics:** Array, Hash Table · [Problem on LeetCode](https://leetcode.com/problems/two-sum/)

## Problem

Given a list of integers `nums` and a `target`, return the indexes of the two numbers that add up to `target`. There is exactly one solution, and the same element can't be used twice.

## Approach

**One pass with a dict of value → index.** For each number, work out the number it needs to complete the pair. If that number has already been seen, the dict gives its index straight away. Otherwise, record the current number and move on.

```python
seen = {}
for i, num in enumerate(nums):
    needed = target - num
    if needed in seen:
        return [seen[needed], i]
    seen[num] = i
```

## Complexity

- **Time:** O(n), one pass with O(1) dict lookups
- **Space:** O(n) for the dict

## What I learned

- **I wrote the O(n²) version first** (every pair, with the inner loop starting at `i + 1`) to have a correct baseline before optimising.
- **Trading space for time:** an O(n) dict turns the inner loop into an O(1) lookup. The same trade as the set in 141.
- **Check before you record.** Looking up `needed` *before* adding the current number means an element can never pair with itself, so `[3, 2, 4]` with target 6 correctly skips `3 + 3`. It also handles a real duplicate: `[3, 3]` gives `[0, 1]`.
- **The dict's value is the index.** My first version returned `target - nums[i]`, the needed *value*. Then `nums[needed]` used that value as a list position. The answer is `seen[needed]`.
- **Don't carry over loop limits.** The `- 1` in `range(len(nums) - 1)` was right for the nested version, but in one pass each number looks *backwards*, so the last element is often where the pair is completed.
- `range(i + 1, range(len(nums)))` is a `TypeError`: the second argument has to be a number, not another `range`.
- Two loops one after the other are still O(n); only nesting multiplies the work.

## Alternative

Nested loops over every pair: O(n²) time, O(1) space.
