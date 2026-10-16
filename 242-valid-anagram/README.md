# 242. Valid Anagram

**Difficulty:** Easy · **Topics:** Hash Table, String, Sorting · [Problem on LeetCode](https://leetcode.com/problems/valid-anagram/)

## Problem

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s` (the same letters, the same number of times, in any order), otherwise `False`.

## Approach

Count each letter in both strings and compare the counts:

- A helper builds a dict of letter → count with one pass: `counts[letter] = counts.get(letter, 0) + 1`.
- Return `count_letters(s) == count_letters(t)`.

## Complexity

- **Time:** O(n), one pass over each string
- **Space:** O(k), where k is the number of distinct letters

## What I learned

- In Python, `==` on dicts compares **contents** (same keys, same values, order ignored). In TypeScript, `===` on objects compares references, so this needs a manual loop or a library.
- Calling another method inside a class needs `self.`: `self.count_letters(s)`.
- Dict type hints use a comma: `dict[str, int]`, not `dict[str: int]`.
- `.get(key, 0)` replaces an `if key in dict / else` block when counting.
- An early `if len(s) != len(t): return False` skips the work when lengths differ.
- `collections.Counter(s) == collections.Counter(t)` does the same in one line.

## Alternative

Compare the sorted strings: `sorted(s) == sorted(t)`. It's shorter, but sorting makes it **O(n log n)**. Two lists can be compared directly, so no `join` is needed.
