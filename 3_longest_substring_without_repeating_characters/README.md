# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium · **Topics:** Hash Table, String, Sliding Window · [Problem on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem

Given a string `s`, return the length of the longest **substring** (contiguous characters) that contains no repeated character. For `"pwwkew"` the answer is 3 (`"wke"`); `"pwke"` doesn't count because it isn't contiguous.

## Approach

A **sliding window** with a dict that stores each character's **last seen index**:

- The right edge is the loop index; it moves forward on every character.
- If the current character was seen before, move the left edge to **one past its previous position**, but only forward: `left = max(left, last_seen[char] + 1)`.
- Record the character's new index, then update the best length with `index - left + 1`.

## Complexity

- **Time:** O(n), one pass with O(1) dict work per character
- **Space:** O(k), where k is the number of distinct characters (bounded by the alphabet)

## What I learned

- **Don't delete from the dict.** Old entries can stay; the `left` pointer decides what's inside the window. Deleting would need an inner loop and bring back O(n²).
- **The left edge must never move backwards.** A repeated character may have last appeared *before* the window started (a stale entry). `max(left, ...)` ignores it. Test cases that catch this: `"abba"` → 2, `"tmmzuxt"` → 5.
- Measure the window on **every** character, not only when there's no repeat.
- Window length is `index - left + 1`. Watch the brackets: `index - (left + 1)` is off by two.
