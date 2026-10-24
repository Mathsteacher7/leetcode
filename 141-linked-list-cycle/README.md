# 141. Linked List Cycle

**Difficulty:** Easy · **Topics:** Hash Table, Linked List, Two Pointers · [Problem on LeetCode](https://leetcode.com/problems/linked-list-cycle/)

## Problem

Given the head of a linked list, return `True` if it contains a cycle (some node's `next` points back to an earlier node, so the list never reaches `None`), otherwise `False`. LeetCode's `pos` value is only used to build the test list; it isn't passed to the function.

## Approach

Walk the list, remembering every node visited in a set. Each pass:

1. **Check:** if this node is already in `seen`, there's a cycle → return `True`.
2. **Record:** add it to `seen`.
3. **Move:** go to `node.next`.

If the walk reaches `None`, the list has an end → return `False`.

## Complexity

- **Time:** O(n), each node is visited once and set lookups are O(1)
- **Space:** O(n), `seen` can hold every node

## What I learned

- **Store the node, not its `val`.** Values can repeat (`1 → 1 → 1`), but each node is a separate object. A set of nodes compares them by identity, because `ListNode` doesn't define `==`. `id(node)` shows the object's memory address.
- **Check before you record.** My first version added each node before the loop asked `node in seen`, so the check was always `True` and the loop ran until it crashed on `None`.
- **Give each outcome its own `return`.** Returning `not node` after the loop was always `True`, because the loop only ends when `node` is `None`. That reported a cycle for every list that ended; `[1]` was the test case that exposed it. The loop ending *means* no cycle, so the answer there is simply `False`.
- The return type is `bool`, not `ListNode | None`.

## Alternative: Floyd's tortoise and hare (O(1) space)

Two pointers move along the list: `slow` one node per step, `fast` two. If the list ends, `fast` reaches `None` first. If there's a cycle, `fast` laps `slow` and they land on the same node, like two runners on a circular track. Same O(n) time, but O(1) space. Named after Robert W. Floyd; the general technique is called **fast and slow pointers**, and it also finds the middle of a list (876) and the start of a cycle (142).
