# 136. Single Number

**Difficulty:** Easy · **Topics:** Array, Bit Manipulation · [Problem on LeetCode](https://leetcode.com/problems/single-number/)

## Problem

Every number in the list appears exactly twice, except one, which appears once. Find it in O(n) time and O(1) extra space.

## Approach

**XOR everything together.** Start from 0 and XOR (`^`) each number into the result:

```python
result = 0
for num in nums:
    result ^= num
return result
```

## Why it works

Three properties of XOR:

- `x ^ x = 0`: a number cancels itself out
- `x ^ 0 = x`: 0 is the identity, so the result can start at 0
- XOR is commutative and associative, so the order doesn't matter

So the list can be reordered in pairs:

```
4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1 ^ 1) ^ (2 ^ 2) = 4 ^ 0 ^ 0 = 4
```

At the bit level, XOR gives 1 where exactly one input has a 1. Anything that appears an even number of times leaves no bits behind.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## What I learned

- Spotting the algebraic properties made this a few lines; it's the kind of problem where maths does the work.
- `result ^= num` is the shorthand for `result = result ^ num`, like `+=`.

## Alternative

A set or dict of counts finds the single number in O(n) time too, but uses O(n) space, which the problem rules out.
