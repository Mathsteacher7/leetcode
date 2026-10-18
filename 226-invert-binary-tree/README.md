# 226. Invert Binary Tree

**Difficulty:** Easy · **Topics:** Tree, Depth-First Search, Recursion · [Problem on LeetCode](https://leetcode.com/problems/invert-binary-tree/)

## Problem

Given the root of a binary tree, mirror it: swap every node's left and right children, all the way down, and return the root.

## Approach

**Recursive depth-first search**, swapping links rather than values:

- **Base case:** an empty tree (`None`) inverted is still empty, so return `None`.
- **Recursive step:** invert both subtrees, attach them in swapped order, then return the node:
  `root.left, root.right = invertTree(root.right), invertTree(root.left)`.

## Complexity

- **Time:** O(n), every node is visited once
- **Space:** O(h) for the call stack

## What I learned

- **Swap the links, not the values.** I first thought I had to record every `val` and rebuild a new tree. But `left` and `right` point at whole subtrees, so one swap moves each subtree with everything below it. Each node only needs to know about itself and its two children.
- **Same shape as 104, different job.** In `maxDepth` each call returned a number for the parent to combine; here each call changes the tree and returns the node, so the parent can link it back in.
- **Two separate assignments lose data.** `root.left = invertTree(root.right)` followed by `root.right = invertTree(root.left)` reads the *new* left on the second line. The original left subtree disappears and the right one ends up on both sides.
- **Tuple assignment fixes it.** In `a, b = b, a`, Python evaluates the whole right-hand side first, then assigns. Both original subtrees are used before either link changes.
- You can't assign to a function call: the left side of `=` must be somewhere that can hold a value, like a variable or an attribute.
- The return type is the tree (`TreeNode | None`), not an `int`, so the base case returns `None`, not `0`.
- Locally, the `TreeNode` hint raises a `NameError` because the class doesn't exist. Defining the class at the top of the file keeps the hint and lets me build test trees.
