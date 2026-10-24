# 100. Same Tree

**Difficulty:** Easy · **Topics:** Tree, Depth-First Search, Recursion · [Problem on LeetCode](https://leetcode.com/problems/same-tree/)

## Problem

Given the roots of two binary trees, `p` and `q`, return `True` if they are identical: the same shape, with the same `val` in every matching position.

## Approach

**Recursive DFS over both trees at once.** Each call compares one node from `p` with the matching node from `q`:

1. **Both `None`:** two empty trees are the same → `True`.
2. **Exactly one `None`, or the values differ:** → `False`.
3. **Both real, same value:** the trees are the same only if the left subtrees are the same **and** the right subtrees are the same:
   `return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)`.

## Complexity

- **Time:** O(n), where n is the size of the smaller tree; every pair is compared at most once
- **Space:** O(h) for the call stack

## What I learned

- **Each call only compares `p` with `q`.** My first version checked the children (`p.left`, `p.right`) inside the base cases. That crashed on leaves and when only one node was `None`. The children are the *next* call's job.
- **`len()` doesn't work on a `TreeNode`.** A node only knows its own `val`, `left` and `right`, not the size of the tree below it. A size mismatch is caught naturally when one tree has a node where the other has `None`.
- **`(p or q) is None` doesn't mean "either is `None`".** `or` returns one of its operands, so that's only `True` when both are `None`. The test has to be written out: `p is None or q is None`.
- **Order matters in a condition.** `p.val != q.val or p is None` crashes on `None`, because Python evaluates left to right. Putting the `None` checks first lets short-circuiting stop before `.val` is read.
- **`==` on two nodes compares identity, not contents.** `TreeNode` doesn't define `__eq__`, so comparing subtrees with `==` is always `False` for two separate trees. Comparing trees is the job of the recursive function itself.
- `and` short-circuits here too: if the left subtrees differ, the right ones are never explored.

## Pattern

Same shape as 104 and 226, with a different combining rule:

| Problem | Base case | What each node returns |
|---|---|---|
| 104 | `None` → 0 | `max(left, right) + 1` |
| 226 | `None` → `None` | the node, with its children swapped |
| 100 | `None`/`None` → `True`, mismatch → `False` | `left and right` |
