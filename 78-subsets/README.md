# 78. Subsets

**Difficulty:** Medium · **Topics:** Array, Backtracking, Bit Manipulation · [Problem on LeetCode](https://leetcode.com/problems/subsets/)

## Problem

Given a list of distinct integers, return every possible subset (the power set), in any order.

## Why there are 2ⁿ subsets

Building a subset is one independent yes/no decision per element: is it in or not? By the multiplication principle that's 2 × 2 × … × 2 = 2ⁿ subsets, and each subset comes from exactly one combination of answers. Each element ends up in exactly half of them, 2ⁿ⁻¹.

## Approach 1: Doubling

Start with `[[]]`. For each element, copy every subset built so far and add the element to the copy:

```python
subsets_list = [[]]
for num in nums:
    for i in range(len(subsets_list)):
        subsets_list.append(subsets_list[i] + [num])
return subsets_list
```

When the element at index `i` arrives there are already 2ⁱ subsets, and the list doubles.

## Approach 2: Backtracking (the decision tree)

Walk the tree of yes/no choices. Each call decides one element; the leaves are the subsets:

```python
result = []

def backtrack(i, path):
    if i == len(nums):            # every element decided
        result.append(path[:])    # record a copy
        return
    path.append(nums[i])          # include
    backtrack(i + 1, path)
    path.pop()                    # undo
    backtrack(i + 1, path)        # skip

backtrack(0, [])
return result
```

## Complexity

- **Time:** O(n · 2ⁿ) for both: 2ⁿ subsets, each up to n long. No solution can do better, because the output itself is that big.
- **Space:** O(n) for the recursion and `path` in the backtracking version, not counting the output.

## What I learned

- **The counting came first.** I worked out 2ⁿ, and noticed that the element at index `i` meets 2ⁱ existing subsets. That observation *is* the doubling algorithm. The algorithm was mine; what tripped me up was Python's list operations.
- **`.append()` returns `None` and changes the list in place.** `subsets_list.append(subsets_list[i].append(num))` added `None`, and also changed the original subset. `subsets_list[i] + [num]` builds a new list and leaves the original alone.
- **With `+`, both sides must be lists.** Wrapping the subset too, `[subsets_list[i]] + [num]`, gives `[[1], 2]` instead of `[1, 2]`. Only wrap a single item.
- **`range(len(...))` is worked out once,** when the loop starts. So even though the list grows inside the loop, it only goes over the subsets that existed before this element, which is exactly the doubling.
- **In backtracking, the recursion replaces the loop.** My first attempt mixed the two versions with an outer `for` loop. `i` moves forward through `backtrack(i + 1, ...)`, and each call moves forward twice (include and skip), which is what makes the tree branch.
- **`path` is one subset, shared by every call.** It grows on `append` and shrinks on `pop`, so the base case must record a copy (`path[:]`), or every entry would be the same list, empty by the end.
- `backtrack[i + 1, path]` is indexing, not a call. Function calls need round brackets.
- **Seeing the pauses made it click.** The hardest part to understand wasn't the code: it was that each call pauses on its recursive line and carries on from the next line when that call returns. I built a line-by-line debugger with Claude that shows the line that just ran, which calls are paused and where, and the decision tree lighting up. That's what made backtracking clear.
