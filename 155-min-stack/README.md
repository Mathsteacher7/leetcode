# 155. Min Stack

**Difficulty:** Medium · **Topics:** Stack, Design · [Problem on LeetCode](https://leetcode.com/problems/min-stack/)

## Problem

Build a stack with `push`, `pop`, `top` and `getMin`, all in O(1) time. `getMin` returns the smallest value currently in the stack.

## Approach: a second stack of minimums

Keep a second list the same length as the stack. Each position holds the minimum of everything from the bottom up to that position, so the current minimum is always its last item.

```
push(5)   stack: [5]          mins: [5]
push(3)   stack: [5, 3]       mins: [5, 3]
push(7)   stack: [5, 3, 7]    mins: [5, 3, 3]
pop()     stack: [5, 3]       mins: [5, 3]
pop()     stack: [5]          mins: [5]       ← 5 comes back by itself
```

```python
class MinStack:
    def __init__(self):
        self.stack_object = []
        self.min_list = []

    def push(self, value: int) -> None:
        self.stack_object.append(value)
        min_value = value if not self.min_list else min(value, self.min_list[-1])
        self.min_list.append(min_value)

    def pop(self) -> None:
        self.stack_object.pop()
        self.min_list.pop()

    def top(self) -> int:
        return self.stack_object[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
```

## Complexity

- **Time:** O(1) for every method
- **Space:** O(n): the second list doubles the storage

## What I learned

- **The same missing `self.` as in 146.** `stack_object = []` in `__init__` makes a local variable that disappears when `__init__` ends; it has to be `self.stack_object`.
- **`min(self.stack_object)` is O(n)**, because it checks every item, so it breaks the O(1) requirement.
- **One `min_value` variable isn't enough.** It can't tell you the previous minimum once the smallest value is popped.
- **Push a minimum on every push**, even when it doesn't change (the second 3 above). That keeps the two lists the same length, so `pop` can always remove one from each.
- **The first push needs its own case.** My first version read `self.min_list[-1]` on an empty list. An empty list is falsy, so `not self.min_list` is the check.
- **One `min` is enough.** I took the minimum twice; the second didn't change anything.
- **A starting value of `-inf` would be wrong.** Nothing is smaller than `-inf`, so the minimum would stay `-inf` forever. It would have to be `inf`, and the empty-list check is cleaner anyway.
- **`[-1]` reads the top without removing it.** Here the negative index is exactly what's wanted, unlike the wraparound bug in 238.
- **Runtime percentages on design problems are noise.** This beat 97.5% on memory and 5% on runtime; the timing is mostly LeetCode's own harness calling the methods.

## Alternative

One list of pairs, `(value, current_min)`: `top` reads `[-1][0]` and `getMin` reads `[-1][1]`. The two values can never get out of step.
