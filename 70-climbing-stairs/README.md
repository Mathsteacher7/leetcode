# 70. Climbing Stairs

**Difficulty:** Easy · **Topics:** Math, Dynamic Programming · [Problem on LeetCode](https://leetcode.com/problems/climbing-stairs/)

## Problem

You're climbing a staircase with `n` steps, and each move climbs either 1 or 2 steps. Return the number of distinct ways to reach the top.

## Approach

**Sort the routes by their last move.** The last move onto step `n` is either a 1-step from `n − 1` or a 2-step from `n − 2`:

- The two groups don't overlap, and between them they cover every route.
- Removing the last move matches each group one-to-one with the routes to a smaller staircase.

So by the addition principle, `ways(n) = ways(n − 1) + ways(n − 2)`: the Fibonacci recurrence, shifted by one (`ways(n) = F(n + 1)`).

The loop only ever needs the last two answers:

```python
two_below, one_below = 1, 1   # ways(0), ways(1)
for _ in range(n - 1):
    two_below, one_below = one_below, one_below + two_below
return one_below
```

## Complexity

- **Time:** O(n)
- **Space:** O(1), two variables

## What I learned

- I spotted the Fibonacci pattern early by working out the first few cases by hand. The pattern isn't a proof, though: the "last move" argument is what justifies the recurrence, and it's what an interviewer wants to hear.
- **Watch the offset.** The staircase gives 1, 2, 3, 5…, while the textbook Fibonacci sequence starts 1, 1, 2, 3…, so the starting values have to match the staircase.
- **Name variables by what they hold.** My first version used `first_way`, `second_way` and `total_ways`, and shifted them with `first_way = total_ways - first_way`. It worked, but the reader has to stop and work it out. `two_below` and `one_below` make the recurrence readable straight from the code.
- **Tuple assignment slides both values along at once**, the same `a, b = b, a` idea as in 226: the right-hand side is evaluated first, so no temporary variable or subtraction is needed.
- **Choosing base cases removes special cases.** Starting from `ways(0) = 1` (one way to climb zero steps: don't move) lets the loop handle every `n ≥ 1` with no `if`s.

## Pattern: dynamic programming

A big question is answered from smaller versions of the same question, and those smaller answers are **reused** (`ways(3)` feeds both `ways(4)` and `ways(5)`). There are three ways to write it:

1. Plain recursion straight from the recurrence: correct, but exponential time, because the same subproblems are recomputed again and again.
2. Recursion with memoisation: each subproblem computed once, O(n) time and space.
3. A bottom-up loop keeping only what the recurrence needs: O(n) time, O(1) space. That's this solution.
