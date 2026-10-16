# 704. Binary Search

**Difficulty:** Easy · **Topics:** Array, Binary Search · [Problem on LeetCode](https://leetcode.com/problems/binary-search/)

## Problem

Given a sorted list of distinct integers and a `target`, return the index of `target`, or `-1` if it isn't there. The solution must run in O(log n).

## Approach

Keep a **window** of indices that might still hold the target, from `left` to `right` **inclusive**, and halve it each step:

- Start with `left = 0` and `right = len(nums) - 1` (the last real index).
- While `left <= right`: take `mid = (left + right) // 2`.
  - `nums[mid] == target` → return `mid`.
  - `nums[mid] < target` → the target can only be to the right: `left = mid + 1`.
  - `nums[mid] > target` → the target can only be to the left: `right = mid - 1`.
- If the window empties (the pointers cross), return `-1`.

## Complexity

- **Time:** O(log n), the window halves every step (about 20 steps for a million elements)
- **Space:** O(1)

## What I learned

All three boundary choices come from one definition: **the window is every index that might still hold the target, inclusive.** My bugs were each a break from that definition:

- **Stopping too early.** My first version used `right = len(nums)` and looped while the window had more than one element, so the last remaining index was never checked. It failed on `[5]` with target 5, and on any target at index 0, such as `[-1, 0, 3, 5, 9, 12]` with target -1.
- **`==` instead of `<=`.** `while right == left` runs *only* when they're equal. The loop must run whenever the window is non-empty.
- **Infinite loop.** With `left = mid` or `right = mid`, a two-element or one-element window can stop shrinking (`[1, 3]` with target 3, `[5]` with target 3). `mid` has already been checked, so it must be skipped: `mid + 1` and `mid - 1`.
- Passing the given examples isn't enough. The edge cases (one element, target at either end, target missing) are where binary search breaks.
- LeetCode showed 0 ms ("beats 100%"), but most submissions land in that bar: O(log n) on these input sizes is too fast to time.
