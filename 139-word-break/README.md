# 139. Word Break

**Difficulty:** Medium · **Topics:** Array, Hash Table, String, Dynamic Programming · [Problem on LeetCode](https://leetcode.com/problems/word-break/)

## Problem

Can the string `s` be cut into pieces where every piece is a word in `wordDict`? Words can be reused. `"leetcode"` with `["leet", "code"]` can; `"catsandog"` with `["cats", "dog", "sand", "and", "cat"]` can't.

## Approach: dynamic programming, "what was the last word?"

The same idea as 322 Coin Change, with words instead of coins.

`ok[i]` answers a yes/no question: can the first `i` characters, `s[:i]`, be cut into dictionary words? For `ok[i]` to be `True`, there has to be some earlier position `j` where:

1. `ok[j]` is `True`: everything before `j` already splits into words, and
2. `s[j:i]`, the last piece, is a word.

```python
ok = [False] * (len(s) + 1)
ok[0] = True                          # the empty string needs no words
word_set = set(wordDict)
for i in range(1, len(s) + 1):
    for j in range(i):
        if ok[j] and s[j:i] in word_set:
            ok[i] = True
            break
return ok[-1]
```

For `"leetcode"` the table ends `[True, False, False, False, True, False, False, False, True]`: cell 4 is `"leet"`, and cell 8 is `"leet"` + `"code"`.

## Complexity

- **Time:** O(n³) in the worst case: O(n²) pairs of `i` and `j`, and building and hashing each slice costs up to O(n)
- **Space:** O(n) for the table, plus the set of words

## What I learned

- **The index is a length, and the value is a yes/no.** In 322 each cell held a count, because the question was "how many?". Here the question is "is it possible?", so each cell holds a boolean.
- **The table needs `len(s) + 1` cells**, one for every length from 0 to `len(s)`, and `ok[0] = True` is the starting point, like `best[0] = 0` in 322.
- **My first slice was backwards.** `j` is where the last word starts and `i` is where it ends, so the piece is `s[j:i]`. With `j < i`, `s[i:j]` is always an empty string.
- **`j` only goes up to `i - 1`**: `range(i)`, not `range(len(s))`.
- **A word on its own isn't enough.** My second version set `ok[i]` whenever `s[j:i]` was a word, without checking what came before it. `"xcat"` with `["cat"]` returned `True`. The fix is `ok[j]`.
- **`ok[j]`, not `ok[:j]`.** I first wrote `ok[:j] == True`. That's a slice, a whole list, and a list is never equal to `True`. What's needed is the one cell right where the last word starts.
- **The `True`s carry the history.** `ok[j]` being `True` means `s[:j]` has already been checked, so only the last word ever needs checking. That's the core of dynamic programming.
- **Any earlier `True` can be the right one, not only the most recent.** `"aab"` with `["a", "ab"]`: the most recent `True` is cell 2, but the piece after it, `"b"`, isn't a word; cell 1 with `"ab"` is.
- **`set(wordDict)`** turns the list into a set, so `in` is O(1) instead of checking every word.
- **Python uses snake_case** for variable names. `wordBreak` and `wordDict` are camelCase only because LeetCode's template uses the same names in every language.

## Alternative

`j` only needs to go back as far as the longest word in the dictionary, since no piece can be longer. That cuts the inner loop when the words are short.
