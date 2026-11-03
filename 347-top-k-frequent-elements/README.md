# 347. Top K Frequent Elements

**Difficulty:** Medium · **Topics:** Array, Hash Table, Sorting, Heap, Bucket Sort · [Problem on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem

Given a list of integers and `k`, return the `k` most frequent elements, in any order. The solution must be better than O(n log n).

Both solutions start by counting with a dict: `freq[num] = freq.get(num, 0) + 1`.

## Approach 1: Bucket sort, O(n)

Make a list where the **index is a frequency**, and put each number into the bucket for its count. Then read the buckets from the highest frequency down until there are `k` numbers:

```python
buckets = [[] for _ in range(len(nums) + 1)]
for num, count in freq.items():
    buckets[count].append(num)
for bucket in reversed(buckets):
    for num in bucket:
        result.append(num)
        if len(result) == k:
            return result
```

## Approach 2: Min-heap of size k, O(n + m log k)

Keep a heap of at most `k` `(count, num)` tuples. The smallest count is always at the front, so it's the one to throw out when the heap grows past `k`:

```python
heap = []
for num, count in freq.items():
    heapq.heappush(heap, (count, num))
    if len(heap) > k:
        heapq.heappop(heap)
return [num for count, num in heap]
```

## Complexity

| | Time | Space |
|---|---|---|
| Buckets | O(n) | O(n) |
| Heap | O(n + m log k), m = distinct numbers | O(m + k) |

## Big O isn't the same as speed

On LeetCode the bucket version ran in 11 ms and beat only about 25% of submissions; the heap version was faster. `heapq` is written in C, the heap never holds more than `k + 1` items, and log k is tiny in practice. The buckets version creates one list for every possible frequency (up to 100,001), most of them empty, and runs three loops in plain Python. Big O describes how the cost *grows*, not which solution is faster at a given size. `Counter(nums).most_common(k)` is the fastest of all here, for the same reason.

## What I learned

- **Bucket sort:** the position in the list carries the meaning (the frequency), so nothing is ever compared or sorted. It clicked once I saw `buckets[count].append(num)`: `append` adds to the list *at* that index, so one slot holds several numbers. Assigning `buckets[count] = num` overwrote numbers with the same count.
- **`[[]] * n` is a trap.** Every slot is the same list. `[[] for _ in range(n)]` creates separate ones. `* n` is fine for numbers, because a number is replaced, never changed in place.
- **A `for` loop over an empty list runs zero times**, so empty buckets need no special check. A `while len(result) < k` loop got stuck forever on an empty bucket.
- **`return` leaves both loops at once**; `break` would only leave the inner one.
- **`.items()` gives key and value together**, like `Object.entries()` in JavaScript. `reversed()` loops backwards without copying.
- **Count first, then pick the top `k`.** Keeping a top-`k` list while still counting is wrong, because a later number can still overtake. My first plan, a hand-made top-`k` list scanned for every item, was O(m · k): the heap is the same idea with an O(log k) "find the smallest".
- **A heap only stays a heap through `heapq`.** `heap.pop()` removes the last list item, not the smallest; it has to be `heapq.heappop(heap)`. The heap list isn't sorted either, so slicing its end doesn't give the biggest items. Only `heap[0]` is guaranteed.
- **Tuples compare element by element**, so `(count, num)` puts the heap in order of frequency.
- `result[k:]` means "from index `k`"; the last `k` items are `result[-k:]`.
