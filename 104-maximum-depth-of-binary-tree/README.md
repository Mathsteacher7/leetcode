# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy · **Topics:** Tree, Depth-First Search, Recursion · [Problem on LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Problem

Given the root of a binary tree, return its depth: the number of **nodes** on the longest path from the root down to a leaf (a node with no children). An empty tree has depth 0.

## Approach

**Recursive depth-first search.** Each call answers one question for its own subtree: "how deep is the tree from this node down?"

- **Base case:** an empty node (`None`) has depth 0.
- **Recursive step:** ask the left subtree, ask the right subtree, and return `max(left, right) + 1`. Only the longer path counts, and the current node adds 1.

## Complexity

- **Time:** O(n), every node is visited once
- **Space:** O(h), where h is the height of the tree, for the call stack: O(log n) for a balanced tree, O(n) for a tree shaped like a chain

## What I learned

- **Nobody counts the calls.** I got stuck trying to keep one counter travelling down the tree. In recursion, the answer is built **on the way back up**: each call returns a number, and the parent combines its children's numbers into its own.
- **It's proof by induction.** The base case is right (`None` → 0), and if the children's answers are right, `max(...) + 1` is right for the parent, so it's right for the whole tree.
- A call waits for its first recursive call to finish **completely** before moving to the next line. That's why the left side of the tree is fully explored before the right.
- Debugging recursion: printing `root.val` alongside each value shows which node is talking. Without it, the prints all look the same.
- `TreeNode | None` means "a node or `None`", like `TreeNode | null` in TypeScript. LeetCode provides the `TreeNode` class, so to run locally I have to define it myself.
- Depth-first search (DFS) goes down one path to the bottom before trying the next. Breadth-first search (BFS) goes level by level, and would also work here, by counting levels with a queue.
