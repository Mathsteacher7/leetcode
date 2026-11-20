# 199. Binary Tree Right Side View

**Difficulty:** Medium · **Topics:** Tree, Breadth-First Search · [Problem on LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)

## Problem

Standing to the right of a binary tree, return the values you can see from top to bottom.

```
          1          ← see 1
         / \
        2   3        ← see 3
       /
      4              ← see 4
     /
    5                ← see 5
```

→ `[1, 3, 4, 5]`

## Approach: BFS, keeping the last node of each level

102 Level Order Traversal, keeping one value per level instead of the whole level:

```python
result = []
if not root:
    return result
queue = deque([root])
while queue:
    right_most = None
    for _ in range(len(queue)):
        node = queue.popleft()
        right_most = node.val           # overwritten until the last node of the level
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(right_most)
return result
```

## Complexity

- **Time:** O(n), every node goes through the queue once
- **Space:** O(n) for the queue on the widest level

## What I learned

- **"Right side view" means the rightmost node of each level, not the nodes on the right branch.** In the example, 4 and 5 hang off the left side, but nothing to their right on their level hides them, so they're seen.
- **Every node still has to go into the queue.** I first thought of `elif` to add only one child. That would have lost the left child's whole subtree, including the 4 and the 5 here. Any node might turn out to be the rightmost on its level.
- **Children go in left first, then right, so the last node taken from each level is the rightmost.** Adding them right first instead would make it the first.
- **Overwriting a variable in the loop** leaves it holding the last value once the loop ends, so there's no need to check the index.
- **The return type is `list[int]`**, one value per level, not `list[list[int]]` as in 102.
