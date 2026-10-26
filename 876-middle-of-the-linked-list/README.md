# 876. Middle of the Linked List

**Difficulty:** Easy · **Topics:** Linked List, Two Pointers · [Problem on LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/)

## Problem

Given the head of a linked list, return its middle node. With an even number of nodes, return the second of the two middle nodes.

## Approach

**Fast and slow pointers.** Both start at the head. Each step, `slow` moves one node and `fast` moves two. Because fast covers twice the distance, when it reaches the end slow is exactly halfway:

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

## Complexity

- **Time:** O(n), one pass
- **Space:** O(1), two labels

## What I learned

- **The loop condition took two failures to get right**, and each half of it prevents one crash:
  - `while fast:` alone crashed on the **odd** list. `fast` lands on the last node, which isn't `None`, so the loop runs again and `fast.next.next` reads `.next` of `None`.
  - `while fast.next:` alone crashed on the **even** list. `fast` steps past the end and becomes `None`, and then the condition itself reads `None.next`.
  - `fast and fast.next` covers both, and `fast` is checked first, so short-circuiting never reads `.next` on `None`. Working it out from the failures is what made it stick.
- **`slow` and `fast` are labels on nodes, not counters.** No index or step count is needed: when the loop stops, the node `slow` is on *is* the answer.
- **Returning a node returns the rest of the list.** LeetCode prints `[3, 4, 5]` for the middle of `[1, 2, 3, 4, 5]` because it follows `next` from the returned node to the end. Nothing is cut or copied.
- **Testing linked lists locally** needs two small helpers: one to build a list from a Python list (the placeholder-and-`tail` pattern from 21), and one to turn a list back into a Python list for printing.

## Alternative

Two passes: count the nodes, then walk `count // 2` steps from the head. Same O(n) time and O(1) space, but it reads the list twice.
