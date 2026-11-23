# 17. Letter Combinations of a Phone Number

**Difficulty:** Medium · **Topics:** Hash Table, String, Backtracking · [Problem on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Problem

Each digit from 2 to 9 maps to letters, as on an old phone keypad. Return every letter combination a string of digits could spell. `"23"` → `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`, and `""` → `[]`.

## Approach: one call per digit

Each call handles **one** digit, the one at `index`: it tries every letter for that digit and hands the next digit to a new call.

```python
if len(digits) == 0:
    return []
number_to_letter = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
}
result = []

def explore(index: int, path: str) -> None:
    if len(path) == len(digits):
        result.append(path)
        return
    for letter in number_to_letter[digits[index]]:
        explore(index + 1, path + letter)

explore(0, "")
return result
```

```
explore(0, "")            loop over "abc"
  explore(1, "a")         loop over "def"
    explore(2, "ad") → save
    explore(2, "ae") → save
    explore(2, "af") → save
  explore(1, "b")         ...
```

## Complexity

- **Time:** O(4ⁿ · n): up to 4 letters per digit gives at most 4ⁿ combinations, and building each string costs up to n
- **Space:** O(n) for the recursion, not counting the output

## What I learned

- **The recursion is the loop over the digits.** My first versions had loops over all the digits, outside `explore` and then inside it. Each call only needs the digit at `digits[index]`; `index + 1` hands the next one on. If I'm writing a loop over the whole input inside a recursive function, I should check whether the recursion is already doing that job.
- **While one call explores, its caller is paused** inside its own `for` loop, with its bookmark on the current letter. When the call returns, the loop moves on to the next letter.
- **`path + letter` builds a new string, so there's nothing to undo.** Strings can't be changed in place, so each call gets its own `path`. In 39 and 79 one shared list or set needed a `pop` or `remove`. With `path += letter` before the call, the loop kept adding to the same `path`: `"a"`, then `"ab"`, then `"abc"`.
- **Pass `index + 1`, not `index`.** With the same index, the next call picked from the same digit's letters again.
- **`digits[index]`, not `digit[index]`.** `digit` was one character, so `digit[1]` was out of range.
- **`range` needs a number.** `range("abc")` fails; to loop over the letters, loop over the string: `for letter in "abc"`.
- **A list keyed by position would work too**, with empty strings at 0 and 1 and `letters[int(digit)]`, but a dict can use the character directly as the key.
- **The empty input returns `[]`, not `[""]`.**
