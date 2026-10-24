# 21. Merge Two Sorted Lists

**Difficulty:** Easy · **Topics:** Linked List, Recursion · [Problem on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem

Given the heads of two sorted linked lists, merge them into one sorted list by re-linking the existing nodes, and return its head.

## Approach 1: Recursion

- **Base cases:** if one list is empty, the merge is simply the other list.
- **Recursive step:** the smaller front node comes first. Everything after it is the merge of the rest of its list with the whole other list:
  `list1.next = mergeTwoLists(list1.next, list2)`, then `return list1` (and the mirror image for `list2`).

The head of the whole result is whatever the very first call returns.

## Approach 2: Loop with a placeholder node

- `dummy = ListNode()` is a placeholder, and `tail = dummy` puts a second label on it.
- While **both** lists have nodes: attach the smaller front node with `tail.next = ...`, move `tail` onto it, then move that list's label forward.
- When one list runs out, the other's leftovers are already sorted: `tail.next = list1 or list2` attaches them with one link.
- Return `dummy.next`. `dummy` never moved, so its `next` is the first real node.

## Complexity

| | Recursion | Loop |
|---|---|---|
| Time | O(n + m) | O(n + m) |
| Extra space | O(n + m), one waiting call per node | **O(1)**, a placeholder and two labels |

The loop is O(n + m), not O(n · m): each pass attaches exactly one node and moves one label forward, and neither label ever goes back. Because both lists are sorted, only the two front nodes ever need comparing.

## What I learned

- **A parameter like `list1` is the head node itself.** There's no `.head`; the first node *is* the list from that point on. Returning the head returns the whole list, since every node can be reached through `next`.
- **A variable is a label on a node, not the node.** `list1 = list1.next` moves the label; the node is unchanged. Before moving a label away from a node, that node must already be attached to the result, or it's lost.
- **`node.next = other` overwrites the old link.** Doing this inside a list loses the rest of it: save what you're about to overwrite, or move labels in the right order.
- **Each recursive call must make the problem smaller.** Calling `mergeTwoLists(list1, list2)` again with the same nodes, or just swapping them, recurses forever. The calls are guaranteed to finish because each one removes one node.
- **The loop condition needs `and`.** `while list1 or list2` (or `(list1 or list2) is not None`) keeps going after one list runs out and crashes on `.val`.
- The list that runs out first isn't necessarily the shorter one: it's the one whose values finish first.
- **A dict is not an object.** In Python, `{"val": 0}` is read with `d["val"]`, not `d.val`, and dicts can't be dict keys. Nodes are created by calling the class: `ListNode()`.
- **Re-linking costs no extra space.** Only new nodes would count; `tail.next = ...` changes a pointer inside a node that already exists.
- Python limits recursion depth (about 1,000 calls by default), so the recursive version would fail on very long lists.
