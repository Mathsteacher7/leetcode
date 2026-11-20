# 98. Validate Binary Search Tree

**Difficulty:** Medium · **Topics:** Tree, Depth-First Search, Binary Search Tree · [Problem on LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)

## Problem

Return `True` if a binary tree is a valid binary search tree: for every node, every value in its left subtree is smaller and every value in its right subtree is bigger. No equal values.

## Approach: pass the limits down the recursion

Checking each node only against its own children isn't enough:

```
      5
     / \
    1   6
       / \
      3   7
```

Every parent is happy with its children (1 < 5 < 6, 3 < 6 < 7), but 3 is in the right subtree of 5, so it must be bigger than 5.

Each call carries the two limits its node must sit between. Going left, the node's value becomes the new upper limit; going right, it becomes the new lower limit.

```python
def check(current: TreeNode | None, low: float, high: float) -> bool:
    if current is None:
        return True
    if low < current.val < high:
        return check(current.left, low, current.val) and check(current.right, current.val, high)
    return False

return check(root, float("-inf"), float("inf"))
```

For the 3 above: `check(5, -inf, inf)` → right: `check(6, 5, inf)` → left: `check(3, 5, 6)`, and 3 isn't between 5 and 6.

## Complexity

- **Time:** O(n), each node checked once
- **Space:** O(h) for the recursion, where h is the height of the tree

## What I learned

- **Each node needs two limits, a minimum and a maximum**, and they travel as arguments, not stored on the node.
- **`inf` on its own isn't Python.** It's `float("inf")` and `float("-inf")`, as in 322, or `math.inf`. At the root, `-inf` to `inf` means "anything goes".
- **Pass the node, not its value.** I called `check(root.val, ...)`, which passes a number, so `current.val` crashed.
- **One `None` check at the top is enough.** I asked whether I needed separate checks for the left and right children. No: each child gets its own call, and that call does its own `None` check. The base case is about the node the call was given, as in 104 and 226.
- **Use what the recursive calls return.** My first version made both calls and threw the answers away, so the function returned `None`. A node is valid only if both subtrees are: `and`, which also stops early when the left side fails.
- **Return the result of the first call.** I ended with `return True`, which ignored everything the check found.
- **`<`, not `<=`**, because equal values aren't allowed: `[2, 2, 2]` is `False`.
- **The `else:` after a `return` isn't needed**: if the `if` returns, the code below it never runs.
