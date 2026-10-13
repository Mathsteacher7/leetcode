# 11. Container With Most Water

**Difficulty:** Medium · **Topics:** Array, Two Pointers, Greedy · [Problem on LeetCode](https://leetcode.com/problems/container-with-most-water/)

## Problem

Given an array `height` of vertical lines, choose two lines that, together with the x-axis, hold the most water. Return that maximum area, where the area is the **shorter** height × the distance between the lines.

## Approach

**Two pointers from opposite ends**, moving towards each other:

- Start with `left = 0` and `right = len(height) - 1`.
- While `left < right`: calculate the area, update the maximum, then move the pointer at the **shorter** line inwards.

## Why moving the shorter line is safe

The area is capped by the shorter line. Every container that keeps that line and pairs it with something further in is narrower and still capped at the same height, so none of them can beat the area just measured. Discarding the shorter line never loses the best answer, so the scan checks only n pairs instead of all n²/2.

## Complexity

- **Time:** O(n), each step moves one pointer inwards
- **Space:** O(1)

## What I learned

- A `for` loop advances its index on every iteration. When two pointers move independently, use a `while` loop and move them yourself.
- Keep the two jobs separate and run both on every step: (1) record the best area, (2) move a pointer. Moving a pointer only when the record improves skips valid pairs. Test case: `[10, 2, 9, 1]` → 18.
- Use a real index for the right end (`len - 1`), not `-1`, because the index is used in the width calculation.
- If both heights are equal, it doesn't matter which pointer moves.
