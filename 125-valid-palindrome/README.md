# 125. Valid Palindrome

**Difficulty:** Easy · **Topics:** Two Pointers, String · [Problem on LeetCode](https://leetcode.com/problems/valid-palindrome/)

## Problem

Ignoring case and every character that isn't a letter or a digit, does the string read the same forwards and backwards? `"A man, a plan, a canal: Panama"` does.

## Approach: two pointers from opposite ends

One pointer at the start, one at the end. Skip anything that isn't a letter or digit, compare the two characters in lower case, and move both inward.

```python
start, end = 0, len(s) - 1
while start < end:
    if not s[start].isalnum():
        start += 1
        continue
    if not s[end].isalnum():
        end -= 1
        continue
    if s[start].lower() != s[end].lower():
        return False
    start += 1
    end -= 1
return True
```

## Complexity

- **Time:** O(n), each character is visited at most once
- **Space:** O(1), no cleaned-up copy of the string

## What I learned

- **`continue` skips to the next pass of the loop**, which re-checks `start < end` before reading anything. `break` would leave the loop altogether.
- **Clean copy vs two pointers.** The quick version builds a cleaned string, `"".join(ch.lower() for ch in s if ch.isalnum())`, and compares it with its reverse. It's clear, but it costs O(n) extra space.
- **My clean-copy version crashed with an `IndexError` on an empty string.** Strings with no letters or digits, like `" "`, clean down to `""`, and reading index 0 of an empty string fails. An empty string is a palindrome, so the answer should be `True`.
- **`str.isalnum()`** is `True` for letters and digits; `str.lower()` returns a new lower-case string.
- **Skip one character at a time, then go back to the loop condition.** That way the pointers can't cross while skipping.

## Pattern

Two pointers from opposite ends, as in 11. Here both pointers always move together after a comparison, and each one moves on its own when skipping.
