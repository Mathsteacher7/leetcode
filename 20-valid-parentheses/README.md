# 20. Valid Parentheses

**Difficulty:** Easy · **Topics:** String, Stack · [Problem on LeetCode](https://leetcode.com/problems/valid-parentheses/)

## Problem

Given a string containing only `(`, `)`, `[`, `]`, `{` and `}`, return `True` if the brackets are valid: every opening bracket is closed by the same type, in the right order (the most recently opened closes first), and every closing bracket has an opening bracket before it.

## Approach

A **stack** of opening brackets, plus a dict that maps each opening bracket to its closing partner:

- For each character: if the stack isn't empty and the character is the closer that the top of the stack expects, `pop()` the top.
- Otherwise, if the character is an opening bracket, `append` it.
- Otherwise, it's a closing bracket that doesn't match (or nothing is open), so return `False`.
- At the end, return `not stack`: valid only if every opened bracket was closed.

In Python a stack is just a list used from one end: `append` to push, `pop()` to remove, `stack[-1]` to read the top, all O(1). "Last in, first out" is exactly the rule that the most recent bracket must close first.

## Complexity

- **Time:** O(n), one pass with O(1) stack and dict work per character
- **Space:** O(n), the stack holds every bracket in the worst case (all opening)

## What I learned

- Two jobs, two structures: the **stack** remembers the order brackets were opened in, and the **dict** only knows which brackets belong together.
- I considered `match` / `case`, but three near-identical cases for the closing brackets is a sign the difference is **data**, so it belongs in a dict and the logic is written once. `match` shines when the shapes of the data differ.
- Python's one-line conditional puts the true value first: `stack[-1] if stack else None`.
- An empty list is falsy, so `if stack` means "not empty" and `return not stack` means "is empty".
- Two cases that passing every comparison doesn't catch: `"(("` (nothing ever fails, but brackets are left open) and `")"` (a closer with an empty stack).
- `if stack and char == pairs[stack[-1]]`: `and` stops early on an empty stack, so the lookup never runs on `None`.
