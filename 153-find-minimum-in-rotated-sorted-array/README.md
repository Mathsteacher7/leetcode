# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium · **Topics:** Array, Binary Search · [Problem on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Problem

A sorted list of distinct integers has been rotated: cut at some point, with the two parts swapped, like `[4, 5, 6, 7, 0, 1, 2]`. It may also not be rotated at all. Return the minimum element in O(log n).

## Approach

Binary search for a **boundary** (the drop where the order restarts) instead of a target. The window `left` to `right` always contains the minimum, and shrinks until one candidate is left:

- While `left < right`: take `mid = (left + right) // 2` and compare `nums[mid]` with `nums[right]`.
  - `nums[mid] < nums[right]` → `mid` to `right` is in order, so the minimum is at `mid` or to its left: `right = mid`.
  - Otherwise, `nums[mid]` is bigger than something to its right, so the drop is after `mid`: `left = mid + 1`.
- Return `nums[left]`.

## Complexity

- **Time:** O(log n)
- **Space:** O(1)

## What I learned

- **The two pointers move differently, unlike in 704.** `right = mid` keeps `mid`, because a smaller `nums[mid]` means it might be the minimum. `left = mid + 1` skips it, because a bigger `nums[mid]` means it can't be. The rule behind both problems is the same: keep `mid` in the window only if it could still be the answer.
- **The loop condition is `<`, not `<=`.** Here the answer always exists, so the search runs until exactly one candidate is left, instead of until the window is empty.
- **My first version stopped at two candidates and guessed between them.** It passed every rotated case but failed on lists that aren't rotated, like `[-1, 5]` or `[0, 1, 2]`. Testing all rotations of small lists, including the zero rotation, found it.
- **Comparing with `right` matters.** `nums[mid] < nums[right]` gives a clear answer about which side holds the drop, including for an unrotated list.
- Calculate `mid` once at the top of the loop, rather than repeating the line in every branch.

## Alternative

Stop when two candidates are left (`while left < mid < right`) and return `min(nums[left], nums[right])`. It's correct and still O(log n), but narrowing down to one candidate avoids the final comparison and is the cleaner pattern.
