# 56. Merge Intervals

**Difficulty:** Medium · **Topics:** Array, Sorting · [Problem on LeetCode](https://leetcode.com/problems/merge-intervals/)

## Problem

Given a list of intervals `[start, end]`, merge every pair that overlaps (touching counts) and return the result.

## Approach

**Sort by start, then one pass.** Once the starts only go up, each interval only needs comparing with the last interval in the result. If it doesn't overlap that one, no later interval can either, so nothing earlier ever needs rechecking:

```python
intervals.sort()
result = [intervals[0][:]]
for start, end in intervals[1:]:
    if start <= result[-1][1]:
        result[-1][1] = max(result[-1][1], end)   # overlap: extend
    else:
        result.append([start, end])               # gap: start a new interval
return result
```

## Complexity

- **Time:** O(n log n), dominated by the sort; the pass itself is O(n)
- **Space:** O(n) for the result

## What I learned

- **Sorting removes the nested loop.** I expected to compare every pair, O(n²). After sorting, `result[-1]` is a running summary of everything so far, like the lowest price in 121.
- **The new end is the larger of the two.** `[[1, 10], [2, 3]]` must stay `[1, 10]`, so the end is `max(...)`, not the new interval's end.
- **`list.sort()` sorts in place and returns `None`.** `sorted_intervals = intervals.sort()` gave `None`; `sorted(intervals)` returns a new list. Rule of thumb: methods that change a list (`sort`, `append`, `reverse`) return `None`; functions that build something (`sorted`, `len`) return the result.
- **`key` is a function applied to each item**, for example `intervals.sort(key=lambda interval: interval[0])`, the same as `(interval) => interval[0]` in JavaScript. Python passes one item, not two as in a JavaScript comparator. Plain `sort()` also works here, because lists compare element by element.
- **`result[0]` is the same object as `intervals[0]`.** Changing `result[-1][1]` in place would change the caller's input, so the tidy version copies the first interval (`[:]`). My first version built a new list on every merge, which avoided the problem too.
- Unpacking `for start, end in intervals[1:]` reads better than indexing, and `max` replaces an inner `if`.
