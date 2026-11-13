# 15. 3Sum

**Difficulty:** Medium · **Topics:** Array, Two Pointers, Sorting · [Problem on LeetCode](https://leetcode.com/problems/3sum/)

## Problem

Return every distinct triple of numbers in `nums` that adds up to 0. The same triple must not appear twice, even if the numbers appear more than once in `nums`.

## Approach: sort, fix one number, two pointers for the other two

After sorting, fix `nums[i]`. The other two numbers must add up to `-nums[i]`, and in the sorted part to its right that's a two-pointer search: if the sum is too small, move `start` right; too big, move `end` left.

```python
nums.sort()
result = []
for i in range(len(nums) - 2):
    if nums[i] > 0:
        break                                   # everything to the right is positive too
    if i > 0 and nums[i] == nums[i - 1]:
        continue                                # same fixed number, same triples
    start, end = i + 1, len(nums) - 1
    while start < end:
        total = nums[i] + nums[start] + nums[end]
        if total < 0:
            start += 1
        elif total > 0:
            end -= 1
        else:
            result.append([nums[i], nums[start], nums[end]])
            start += 1
            end -= 1
            while start < end and nums[start] == nums[start - 1]:
                start += 1                      # skip repeats of the number just used
return result
```

## Complexity

- **Time:** O(n²): the sort is O(n log n), then n fixed numbers each with an O(n) two-pointer pass
- **Space:** O(1) extra besides the output (Python's sort uses up to O(n))

## What I learned

- **Sorting is what makes the pointers work.** With the numbers in order, a sum that's too small can only be fixed by moving `start` right, and one that's too big by moving `end` left.
- **Duplicates are skipped in two places:** the fixed number (`nums[i] == nums[i - 1]`), and the second number after a match. Without these, `[-1, -1, 0, 1]` gives `[-1, 0, 1]` twice.
- **`i > 0` comes first in the check.** At `i = 0`, `nums[i - 1]` would be `nums[-1]`, the last element, and the comparison would quietly skip a valid first number.
- **One fixed number can have several matches.** My first version had a `break` after the first match, which missed triples like `[-4, 0, 4]` and `[-4, 1, 3]` for the same `-4`. After a match, both pointers move and the search continues.
- **The early `break` when `nums[i] > 0`**: three positive numbers can't add up to 0.
- **This is 1 Two Sum turned into a loop**: fix one number, then solve a two-sum on what's left. Two Sum used a dict because its input isn't sorted; here, sorting allows two pointers instead.

## Alternative

For each fixed number, run the hashing version of Two Sum on the rest. It's still O(n²), but avoiding duplicate triples is harder without the sorted order.
