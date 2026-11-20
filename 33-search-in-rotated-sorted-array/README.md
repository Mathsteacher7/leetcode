# 33. Search in Rotated Sorted Array

**Difficulty:** Medium · **Topics:** Array, Binary Search · [Problem on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem

A sorted list of distinct numbers has been rotated at an unknown point, for example `[0, 1, 2, 4, 5, 6, 7]` → `[4, 5, 6, 7, 0, 1, 2]`. Return the index of `target`, or `-1`, in O(log n).

## Approach: binary search, checking which half is sorted

Split the window at `mid`. The rotation break can only be in one half, so **at least one half is always in normal sorted order**. Find that half, check whether the target is inside its range, and keep the half that must contain it.

```python
left_pointer = 0
right_pointer = len(nums) - 1
while left_pointer <= right_pointer:
    mid_pointer = (left_pointer + right_pointer) // 2
    if nums[mid_pointer] == target:
        return mid_pointer
    if nums[left_pointer] <= nums[mid_pointer]:                  # left half sorted
        if nums[left_pointer] <= target < nums[mid_pointer]:
            right_pointer = mid_pointer - 1
        else:
            left_pointer = mid_pointer + 1
    else:                                                        # right half sorted
        if nums[mid_pointer] < target <= nums[right_pointer]:
            left_pointer = mid_pointer + 1
        else:
            right_pointer = mid_pointer - 1
return -1
```

## Complexity

- **Time:** O(log n), the window halves on every pass
- **Space:** O(1)

## What I learned

- **One comparison tells you which half is sorted**: `nums[left] <= nums[mid]`. Both ends are only needed afterwards, for the range check. `<=` matters: when `left == mid`, that one-number "half" counts as sorted.
- **No recursion needed for the unsorted side.** Moving `left` or `right` and going round the loop again works, because any window, even one with the break inside it, splits into two halves where at least one is sorted.
- **`mid` has to be worked out inside the loop**, from the current window: `(left + right) // 2`. My first version calculated `len(nums) // 2` once, before the loop, so every pass looked at the same index.
- **In the right-half branch I moved the wrong pointer.** I'd copied the moves from the left-half branch. If the target is in the sorted right half, the window moves right: `left = mid + 1`.
- **The range ends matter.** `mid` has already been checked, so it's the end left out; the other end is a real candidate. With `< nums[right]`, a target at the very right end was never found: `[5, 1, 3]` with target 3 returned -1. The two ranges mirror each other:
  - left half: `nums[left] <= target < nums[mid]`
  - right half: `nums[mid] < target <= nums[right]`
- **Python chains comparisons** like maths: `a <= x < b`.
- **`while left <= right`**, as in 704, because this is a search for a value, not narrowing down to a boundary as in 153.
