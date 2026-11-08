# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium · **Topics:** Tree, Breadth-First Search · [Problem on LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Problem

Given the root of a binary tree, return its values level by level, from left to right: `[[3], [9, 20], [15, 7]]`.

## Approach

**Breadth-first search with a queue.** DFS dives down one branch first, so it can't easily go level by level. A queue (first in, first out) visits nodes in the order they were discovered, which is level order.

```python
if not root:
    return []
result = []
queue = deque([root])
while queue:
    level = []
    for _ in range(len(queue)):        # exactly the nodes of this level
        node = queue.popleft()
        level.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(level)
return result
```

## Complexity

- **Time:** O(n), each node enters and leaves the queue once
- **Space:** O(n), the widest level can hold about half the nodes

## What I learned

- **`len(queue)` at the start of a level *is* the level's size.** The queue holds nodes from two levels at once while it runs, but `range(len(queue))` is worked out once, before the loop starts, so the children added during it wait for the next level. The same trick as `range(len(subsets_list))` in 78.
- **Levels aren't 1, 2, 4, 8.** That's only true for a perfect tree; any child can be missing, which is exactly why the queue length is used instead of a formula.
- **Only real nodes go in the queue.** My first run broke because I added children without checking they existed; a `None` in the queue crashes on `.val` at the next level.
- **Append the value, not the node.** `level.append(node)` filled the result with `TreeNode` objects instead of numbers.
- **An empty tree needs an early return.** `deque([None])` would put `None` in the queue.
- **`collections.deque`** is Python's queue, pronounced "deck": `append` adds at the back and `popleft()` takes from the front, both O(1). A list's `pop(0)` is O(n), because everything shifts. `popleft` needs its brackets to actually be called.
- `append` takes one item, so two children need two calls.
