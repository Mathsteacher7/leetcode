# 268. Missing Number

**Difficulty:** Easy · **Topics:** Array, Math, Bit Manipulation · [Problem on LeetCode](https://leetcode.com/problems/missing-number/)

## Problem

`nums` holds `n` different numbers taken from `0` to `n`, so exactly one number in that range is missing. Return it. Follow-up: O(1) extra space and O(n) time.

## Approach 1: the sum formula

The numbers `0` to `n` add up to `n(n + 1) / 2`. Subtract what's actually there, and what's left is the missing number.

```python
n = len(nums)
return n * (n + 1) // 2 - sum(nums)
```

For `[3, 0, 1]`: n = 3, the full sum is 6, the actual sum is 4, so 2 is missing.

## Approach 2: XOR

The same cancelling trick as 136. XOR every index `0` to `n` with every value. Each number that's present appears twice (once as an index, once as a value) and cancels to 0. The missing number appears only once, as an index, so it's what's left.

```python
result = len(nums)               # the index n, which the loop never reaches
for i, num in enumerate(nums):
    result ^= i ^ num
return result
```

## Complexity

- **Time:** O(n) for both
- **Space:** O(1) for both

## What I learned

- **The sum formula is the one from teaching:** Gauss adding 1 to 100. The answer is the difference between what should be there and what is there.
- **`//` keeps the answer an integer.** `n * (n + 1)` is always even, so nothing is lost, but `/` would return a float like `6.0`.
- **The XOR version must start at `len(nums)`, not 0.** `enumerate` only gives the indexes `0` to `n − 1`, so `n` would never go in. My first version started at 0, which fails whenever the missing number is `n`: `[0, 1]` should give 2.
- **XOR doesn't care about order.** The pairs don't need to sit next to each other; `a ^ b ^ a` is still `b`.
- **Overflow:** in Python integers never overflow, so the sum is safe. In a language with fixed-size integers, XOR is the safer choice.

## Alternative

Put the numbers in a set and check `0` to `n` until one is missing. It's O(n) time but O(n) extra space, so it misses the follow-up.
