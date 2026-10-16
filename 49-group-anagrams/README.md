# 49. Group Anagrams

**Difficulty:** Medium · **Topics:** Array, Hash Table, String, Sorting · [Problem on LeetCode](https://leetcode.com/problems/group-anagrams/)

## Problem

Given a list of strings, group the anagrams together (words made of the same letters, the same number of times). Groups can be returned in any order.

## Approach

Give every word a **signature** that is identical for all its anagrams, and use that signature as a **dict key**:

- Signature: the word's letters in alphabetical order, `"".join(sorted(word))`. For example, `"eat"`, `"tea"` and `"ate"` all become `"aet"`.
- The dict maps signature → list of words with that signature.
- For each word: if the signature is already a key, append the word to its list; otherwise start a new list.
- Return `list(groups.values())`.

## Complexity

- **Time:** O(n · k log k), sorting each of the n words of length up to k
- **Space:** O(n · k), every word is stored once

## What I learned

- The hard part was choosing the **key**. A dict key must be immutable: a string or tuple works, a list or dict doesn't. That's why the `join` is needed here (`sorted()` returns a list).
- `list.append()` changes the list in place and returns `None`. Writing `groups[key] = groups[key].append(word)` overwrites the group with `None`.
- `dict.values()` returns a view, not a list, so wrap it with `list(...)`.
- `collections.defaultdict(list)` would remove the `if/else`, because it creates the empty list automatically.

## Alternative

Use letter **counts** as the signature: a tuple of 26 numbers, one per letter `a` to `z`. A tuple can be a dict key, and building it avoids sorting, so the time drops to O(n · k). On LeetCode's short words, it isn't necessarily faster in practice.
