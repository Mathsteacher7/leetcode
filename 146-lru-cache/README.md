# 146. LRU Cache

**Difficulty:** Medium · **Topics:** Hash Table, Design · [Problem on LeetCode](https://leetcode.com/problems/lru-cache/)

## Problem

Design a key-value cache with a fixed capacity. `get(key)` returns the value, or `-1` if the key is missing. `put(key, value)` inserts or updates a key. When the cache is full, the **least recently used** key is evicted. Both a successful `get` and any `put` count as using a key. Both operations must run in **O(1)** average time.

## Approach

A single Python `dict`, relying on the fact that dicts keep insertion order (guaranteed since Python 3.7):

- **Oldest key** is always the first key: `next(iter(cache))`.
- **Mark a key as most recently used** by deleting it and re-inserting it, which moves it to the end.
- **`get`**: return `-1` if the key is missing; otherwise move it to the end and return its value.
- **`put`**: if the key exists, delete it first; if the cache is still full, evict the first key; then insert the key at the end.

## Complexity

- **Time:** O(1) average for both `get` and `put`
- **Space:** O(capacity)

## What I learned

- Remove an existing key **before** checking capacity. Otherwise, updating a key in a full cache evicts another key for no reason.
- `dict.popitem()` removes the **newest** item, not the oldest.
- Reading a key changes the eviction order, so `get` must move the key too.

## Alternative

The classic language-agnostic solution pairs a hash map with a **doubly linked list**. The map finds a node in O(1); the list keeps usage order and lets you move or remove any node in O(1). It's worth knowing for interviews, where relying on dict ordering may not be accepted.
