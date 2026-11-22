# 103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium · **Topics:** Tree, Breadth-First Search · [Problem on LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

## Problem

Return the values level by level, as in 102, but alternate the direction: the first level left to right, the next right to left, and so on.

```
      3
     / \
    9   20
       /  \
      15   7
```

→ `[[3], [20, 9], [15, 7]]`

## Approach: 102, reversing every other level when it's written

The queue works exactly as in 102. Only the way each finished level is added to the result changes.

```python
result = []
if not root:
    return result
queue = deque([root])
left_to_right = True                    # carries over between levels
while queue:
    level = []                          # fresh for each level
    for _ in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(level if left_to_right else level[::-1])
    left_to_right = not left_to_right   # use it, then flip it
return result
```

## Complexity

- **Time:** O(n). Reversing a level costs its length, so all the reversals together add up to O(n).
- **Space:** O(n)

## What I learned

- **The zigzag changes how each level is written, never what goes into the queue.** My first version tied the direction to adding the children, and flipped it per node. On the example, 20's left child, 15, was never added.
- **Where a variable lives decides how long it lasts.** `left_to_right` has to carry over from one level to the next, so it goes before the `while`. I had it inside the `while`, then inside the `for`, and each time it was reset to `True` and nothing ever reversed. `level` is the opposite: fresh for every level, so it goes inside.
- **Use the direction first, then flip it.** Flipping before the append reversed the first level.
- **Methods that change a list in place return `None`**: `append`, `reverse`, `sort`. `level[::-1].reverse()` reversed the list twice and appended `None`. Inside an expression, use the version that builds a new list: `level[::-1]`.
- **A conditional expression picks a value**, so it goes inside the call: `result.append(level if left_to_right else level[::-1])`, not two `append`s with `if`/`else` around them.
- **A boolean reads better than strings** for a two-way choice: `left_to_right = not left_to_right` instead of `"L"` and `"R"`.
- **Rename copied functions.** I started from 199 and kept its name, `rightSideView`, so my test wasn't running the code I was editing.
