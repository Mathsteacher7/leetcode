# 215. Kth Largest Element in an Array

**Difficulty:** Medium · **Topics:** Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect · [Problem on LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Problem

Return the k-th largest value in `nums`, by position in sorted order, so duplicates count separately. `[3, 2, 1, 5, 6, 4]`, `k = 2` → 5. Without sorting the whole list.

## Approach: a min-heap of the k largest so far

Keep a heap holding only the `k` largest numbers seen so far. Its smallest item, `heap[0]`, is the smallest of the top `k`, which is exactly the k-th largest.

```python
k_largest = []
for num in nums:
    heapq.heappush(k_largest, num)
    if len(k_largest) > k:
        heapq.heappop(k_largest)      # remove the smallest
return k_largest[0]
```

For 1 to 10 with `k = 3`, the heap ends holding 8, 9 and 10, and `heap[0]` is 8.

## Complexity

- **Time:** O(n log k): each push and pop costs O(log k)
- **Space:** O(k)

## What I learned

- **A heap in Python is an ordinary list.** `heapq` is a set of functions that keep the list in a special order. The "top" of a heap is **index 0**, the root when it's drawn as a tree, not the end of the list like the top of a stack.
- **Only `heap[0]` is guaranteed.** `[1, 3, 2, 5, 9, 8]` is a valid heap: the smallest is first, the rest isn't sorted.
- **`heapq.heappop(h)`, not `h.pop()`.** The list's own `pop` removes the last item, which isn't the smallest, and breaks the heap order.
- **Push then pop needs no comparison.** The heap briefly holds k + 1 items and popping removes the smallest; if the new number was the smallest, it's the one that leaves. Pop then push works too, but needs a `> heap[0]` check first. `heapq.heappushpop` and `heapq.heapreplace` do each order in one call.
- **It felt easy because I knew the pattern** from 347. Medium mostly assumes you don't know which structure to reach for.

## Alternative: Quickselect

The partition step from Quicksort: pick a pivot, put smaller numbers on its left and bigger on its right, and the pivot lands where it would be in sorted order. Then continue only into the side that contains the wanted position. It averages O(n) time and O(1) extra space, but it's O(n²) with unlucky pivots; a random pivot makes that unlikely.
