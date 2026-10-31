# 198. House Robber

**Difficulty:** Medium · **Topics:** Array, Dynamic Programming · [Problem on LeetCode](https://leetcode.com/problems/house-robber/)

## Problem

`nums[i]` is the money in house `i` along a street. You can't rob two adjacent houses. Return the most money you can take.

## Approach

Let `best(i)` be the most money from houses `0` to `i`. At each house there are two choices:

- **Skip it:** keep `best(i − 1)`.
- **Rob it:** the previous house must be untouched, so `best(i − 2) + nums[i]`.

`best(i) = max(best(i − 1), best(i − 2) + nums[i])`. The loop only needs the last two answers:

```python
two_back, one_back = 0, 0
for num in nums:
    best = max(one_back, two_back + num)
    two_back, one_back = one_back, best
return one_back
```

## Complexity

- **Time:** O(n), one pass
- **Space:** O(1), two variables

## What I learned

- **Local choices don't work.** My first idea was to decide inside each triplet of houses. On `[2, 1, 1, 2]` that takes houses 0 and 2 (3), which then blocks house 3, but the best plan is houses 0 and 3 (4). A choice now can matter many houses later.
- **It took three attempts to change what the variables mean**, and that was the real lesson. My second attempt kept one running `total` and added house values to it; it couldn't remember which houses were already in it, so it added the same house twice and took neighbours together (it returned 5 for houses summing to 6). My third attempt stored house values in `two_back` and `one_back`, so each step only saw a few houses.
- **In DP, the variables hold the best answer so far, not the values in front of you.** Once `one_back` meant "the best total up to the previous house", each step carried every earlier decision with it. Adding `nums[i]` only to `two_back` enforces the no-neighbours rule without tracking which houses were taken.
- It's the Climbing Stairs loop again, combining the last two answers with `max` instead of `+`.
- Starting both variables at 0 handles an empty street and a single house with no special cases.
