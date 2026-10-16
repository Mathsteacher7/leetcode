# LeetCode Practice

A daily habit: at least one LeetCode problem a day, solved in Python.

## Why

- **Python fluency.** My day-to-day work is React, Next.js and TypeScript. Solving problems in Python every day keeps the language in my hands rather than just in my head.
- **Problem-solving.** Breaking a problem down, spotting the pattern, and reasoning about edge cases before writing code.
- **Algorithms and Big O.** Keeping the core patterns fresh, and getting used to explaining *why* a solution has the complexity it does, not just stating it.

The aim is consistency over volume. One problem understood properly is worth more than five copied.

## How I use AI

I write every solution myself in VS Code, with AI assistants and code completion **turned off**.

I do use AI outside the editor, in two ways:

- **As a reference for syntax**: the way I used to use Stack Overflow. For example, how to remove the first key from a dict, or how Python writes a one-line conditional.
- **As a rubber duck**: talking through my approach before and while I code. It asks questions and points at the case that breaks my logic, but it doesn't hand me the solution.

The reasoning, the code and the bugs are mine. The "What I learned" section in each problem's README records the mistakes I made along the way.

The problem READMEs are drafted with AI from my working sessions, and I review them against what actually happened.

## Structure

Each problem has its own folder, named with the LeetCode number and the problem's title:

```
146-lru-cache/
  solution.py
  README.md
```

Every problem README follows the same outline:

- **Problem**: a short restatement in my own words
- **Approach**: the idea behind the solution
- **Complexity**: time and space, with the reasoning
- **What I learned**: the mistakes I actually made and the Python details I picked up
- **Alternative**: another approach and its trade-off, where there's one worth knowing

## Problems

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---|---|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](3-longest-substring-without-repeating-characters/) | Medium | Sliding window | O(n) | O(k) |
| 11 | [Container With Most Water](11-container-with-most-water/) | Medium | Two pointers | O(n) | O(1) |
| 20 | [Valid Parentheses](20-valid-parentheses/) | Easy | Stack | O(n) | O(n) |
| 49 | [Group Anagrams](49-group-anagrams/) | Medium | Hashing | O(n · k log k) | O(n · k) |
| 121 | [Best Time to Buy and Sell Stock](121-best-time-to-buy-and-sell-stock/) | Easy | Single pass | O(n) | O(1) |
| 146 | [LRU Cache](146-lru-cache/) | Medium | Design, hashing | O(1) per op | O(capacity) |
| 153 | [Find Minimum in Rotated Sorted Array](153-find-minimum-in-rotated-sorted-array/) | Medium | Binary search | O(log n) | O(1) |
| 242 | [Valid Anagram](242-valid-anagram/) | Easy | Hashing | O(n) | O(k) |
| 380 | [Insert Delete GetRandom O(1)](380-insert-delete-getrandom-o1/) | Medium | Design, hashing | O(1) per op | O(n) |
| 704 | [Binary Search](704-binary-search/) | Easy | Binary search | O(log n) | O(1) |

## Patterns covered so far

- **Hashing:** using a dict for O(1) lookup, and choosing what the key and value should be (49, 146, 242, 380)
- **Design:** classes whose state persists between calls, often combining two data structures so each covers the other's weakness (146, 380)
- **Single pass with a running summary:** scanning once and keeping only what the past tells you (121)
- **Sliding window:** two pointers moving in the same direction over a sequence (3)
- **Two pointers from opposite ends:** moving towards each other, with a reason for which one moves (11)
- **Stack:** last in, first out, for anything that must be closed or undone in reverse order (20)
- **Binary search:** halving a window that always contains the answer, for a target or for a boundary (153, 704)
