# 380. Insert Delete GetRandom O(1)

**Difficulty:** Medium · **Topics:** Array, Hash Table, Math, Design, Randomized · [Problem on LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## Problem

Design a set that supports `insert(val)` and `remove(val)` (each returns whether the set changed) and `getRandom()`, which returns an element with equal probability. All three must run in **O(1)** average time.

## Approach

A **dict and a list** working together:

- `values` (list) holds the elements, so `random.choice(values)` picks one in O(1).
- `index_of` (dict) maps each value → its position in the list, so any value can be found in O(1).
- **`insert`**: if the value is new, record its index (`len(values)`) and append it.
- **`remove`**: copy the **last** element into the slot of the value being removed, update the last element's index in the dict, `pop()` the end of the list, then delete the removed value from the dict.

## Complexity

- **Time:** O(1) average for all three operations
- **Space:** O(n)

## What I learned

- Each structure covers the other's weakness: a list can't find a value quickly, and a dict can't pick a random element.
- A dict's value doesn't have to be the data. Here it stores a **position**.
- `pop(i)` from the middle of a list is O(n), and shifting the items also makes every stored index after `i` wrong. Only `pop()` from the end is O(1).
- The order of the list doesn't matter for a set, which is what makes the **swap-with-last** trick allowed.
- Update the moved element's index **before** deleting the removed value. That order also handles the case where the removed value is already the last one.
- `values[-1]` is the last element; `len(-1)` is a `TypeError`.
- Python's `set` is mutable but can't be indexed, so it can't support `random.choice` in O(1).
