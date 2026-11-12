# 739. Daily Temperatures

**Difficulty:** Medium · **Topics:** Array, Stack, Monotonic Stack · [Problem on LeetCode](https://leetcode.com/problems/daily-temperatures/)

## Problem

For each day in `temperatures`, return how many days you have to wait for a warmer day, or 0 if no warmer day comes.

## Approach: monotonic stack

Keep a stack of the days still waiting for a warmer day. Store their **indexes**, not their temperatures: the answer is a number of days, and the temperature can always be looked up from the index.

When a new day arrives, it's the answer for every waiting day that's colder than it. Pop those days and record the gap. Then the new day starts waiting too.

```python
result = [0] * len(temperatures)
waiting_list = []                          # indexes of days still waiting
for i in range(len(temperatures)):
    while waiting_list and temperatures[i] > temperatures[waiting_list[-1]]:
        waiting_day = waiting_list.pop()
        result[waiting_day] = i - waiting_day
    waiting_list.append(i)
return result
```

The temperatures of the days in the stack never go up from bottom to top (that's what "monotonic" means). A day only stays in the stack while nothing warmer has come. Days still in the stack at the end keep their 0.

## Complexity

- **Time:** O(n). The `while` loop is inside a `for` loop, but each day is pushed once and popped at most once, so all the pops together are at most n.
- **Space:** O(n) for the stack, for example when the temperatures only go down.

## What I learned

- **The while condition needs `waiting_list`, not `not waiting_list`.** The stack has to be non-empty before `waiting_list[-1]` is read. With `not`, the check passed exactly when the stack was empty, so `waiting_list[-1]` was read on an empty list and crashed.
- **Record the answer for the day that was waiting, not for today.** I wrote `result[i]`, but `i` is the warmer day that ends the wait. The answer belongs to `waiting_day`, the index just popped.
- **Nested loops aren't always O(n²).** What matters is the total work: count how many times each item can be pushed and popped. This is amortised analysis.
- **`result = [0] * n` sets the default answer up front**, so days that never get a warmer day need no extra code.

## Pattern: monotonic stack

For "next greater" or "next smaller" questions, keep a stack of items still waiting for their answer. Each new item settles the waiting items it beats, then waits itself.
