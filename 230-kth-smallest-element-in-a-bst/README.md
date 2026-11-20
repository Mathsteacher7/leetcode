# 230. Kth Smallest Element in a BST

**Difficulty:** Medium · **Topics:** Tree, Depth-First Search, Binary Search Tree · [Problem on LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Problem

Given the root of a binary search tree and `k` (starting at 1), return the `k`-th smallest value.

```
        20
       /  \
     12    31
    /  \     \
   7    15    40
       /
     13
```

In order: 7, 12, 13, 15, 20, 31, 40. So `k = 3` → 13.

## Approach: in-order traversal (left, node, right)

A BST is already sorted if you read it in the right order: everything in the left subtree, then the node, then everything in the right subtree. Done recursively at every node, the values come out smallest first, with no sorting.

**Version 1: build the sorted list**

```python
num_list = []

def add_to_list(node: TreeNode | None) -> None:
    if node is None:
        return
    add_to_list(node.left)
    num_list.append(node.val)       # between the two calls
    add_to_list(node.right)

add_to_list(root)
return num_list[k - 1]
```

**Version 2: count, and stop at the `k`-th node**

```python
answer = None
count = 0

def visit(node: TreeNode | None) -> None:
    nonlocal count, answer
    if node is None or answer is not None:
        return
    visit(node.left)
    if answer is not None:          # the left side found it: skip the rest
        return
    count += 1
    if count == k:
        answer = node.val
        return
    visit(node.right)

visit(root)
return answer
```

## Complexity

- **Version 1:** O(n) time, every node visited; O(n) space for the list, plus O(h) for the recursion
- **Version 2:** O(h + k) time, because it stops early; O(h) space, no list

## What I learned

- **`k` is a position, not a value.** In the first example I looked at, the values were 1 to 5, so `k` and the answer were the same number, which hid what `k` means. A tree with other values made it clear.
- **In-order means left first**, because the left side holds the smaller values. I first described it the other way round, going right first.
- **Don't `return` the recursive calls.** I wrote `return add_to_list(node.left)`, which leaves the call as soon as the left side is done, so the node itself was never appended. On the example it found 7 and then every waiting call returned without appending anything. A call returns by itself when it reaches its last line, and that's what wakes up the node waiting above it.
- **Append the node's value, not `node.right`.** I had an extra line appending a node object, or `None`.
- **The `None` check only stops the call.** I briefly put the two recursive calls inside `if node is None:`, which crashes on `None.left`. The check holds only `return`; the three steps go after it.
- **`nonlocal`** is needed to change a number from the outer function. `num_list.append(...)` worked without it, because it changes the list in place, but `count += 1` assigns. Without `nonlocal`, Python made a new local `count`, the editor warned that the outer `count` was "not accessed", and running it would raise `UnboundLocalError`.
- **Stopping early:** once `answer` is set, every later call returns at once. The check after the left call has to sit right there to be useful; I first put it at the end of the function, where it does nothing.
- **The return type is `int`**, not `bool`, which my first version had.
