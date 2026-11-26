# 424. Longest Repeating Character Replacement

**Difficulty:** Medium · **Topics:** Hash Table, String, Sliding Window · [Problem on LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Problem

`s` is made of capital letters, and up to `k` of them can be changed into any other letter. Return the length of the longest substring that can be made of one repeated letter. `"AABABBA"`, `k = 1` → 4.

## Approach: sliding window with letter counts

For any window, the cheapest fix is to keep its most common letter and change everything else:

```
changes = window length − count of the most common letter
```

The window is valid while `changes <= k`. The right edge moves forward every step; the left edge moves only while the window needs more than `k` changes.

```python
letter_count = {}
left_pointer = 0
longest_string = 0
for right_pointer in range(len(s)):
    letter_count[s[right_pointer]] = letter_count.get(s[right_pointer], 0) + 1
    window = right_pointer - left_pointer + 1
    while window - max(letter_count.values()) > k:
        letter_count[s[left_pointer]] -= 1
        left_pointer += 1
        window = right_pointer - left_pointer + 1
    longest_string = max(longest_string, window)
return longest_string
```

## Complexity

- **Time:** O(n): each pointer moves forward at most n times, and `max` over the counts looks at no more than 26 keys
- **Space:** O(1): at most 26 keys, however long the string is

## What I learned

- **I warmed up with `k = 0` first**: the longest run of one letter, which is LeetCode 1446. There the left edge **jumps** to `right` when the letter changes. It took a few rounds:
  - `longest = ...` replaced the best instead of keeping the larger one; it needs `max`.
  - The length was off by one: `right - left + 1` is the length when `right` is the last letter inside the window.
  - Measuring only when a run broke missed the last run and runs of length 1 (`"ABBB"` gave 1, `"A"` gave 0). Measuring on every step fixes both.
  - `right_pointer += 1` inside a `for` loop over `right_pointer` isn't needed: the `for` already moves it.
- **For `k`, the `while` replaces the `if`.** Only the rule for moving the left edge changes; the counts dict does the job of comparing with the previous letter.
- **Keep the most common letter and change all the others**, not just the rarest one.
- **Lower a count, don't delete the key**, when a letter leaves the window: it may still appear elsewhere in it. A count of 0 never changes the `max`. (`del d[key]` or `d.pop(key)` would remove the key, like `delete` in JavaScript.)
- **The window length must be the same everywhere.** My `while` used `right - left` without the `+ 1`, so the window could hold one change too many, and `"AABABBA"` returned 5. Naming it `window`, and recomputing it inside the `while` because `left` changes there, keeps the two uses in step.
- **The string can hold any capital letter**, not just A and B, which is why a dict of counts beats tracking a fixed letter.

## Alternative

Many solutions keep a `max_count` that only ever goes up, even when the left edge removes letters. It looks wrong, but the answer only grows when a window beats the previous `max_count`, so a stale value never gives a wrong result, and it saves the `max(...)` call.
