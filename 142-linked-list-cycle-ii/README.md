# 142. Linked List Cycle II

**Difficulty:** Medium · **Topics:** Hash Table, Linked List, Two Pointers · [Problem on LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)

## Problem

Given the head of a linked list, return the node where the cycle begins, or `None` if there is no cycle.

## Approach 1: Set of visited nodes

The same walk as in 141, recording each node in a set. The first node seen a second time is the cycle start, so the only change is returning that **node** instead of `True`, and `None` instead of `False`.

- **Time:** O(n) · **Space:** O(n)

## Approach 2: Floyd's tortoise and hare

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:              # phase 1: they met inside the cycle
        slow = head               # phase 2: restart one pointer at the head
        while slow is not fast:
            slow = slow.next
            fast = fast.next      # both now move one node per step
        return slow
return None
```

- **Time:** O(n) · **Space:** O(1)

## Why phase 2 lands on the cycle start

Let **a** be the distance from the head to the cycle start, **b** the distance from the cycle start to the meeting point, and **c** the cycle length. When the pointers meet, slow has walked a + b nodes. Fast has walked twice as far, which is slow's path plus some whole number k of extra laps:

```
2(a + b) = a + b + k·c
    a + b = k·c
        a = k·c − b
```

The meeting point is b nodes into the cycle. Walking a more nodes from there brings it to b + (k·c − b) = k·c nodes into the cycle: a whole number of laps, so exactly back at the cycle start. The pointer from the head also reaches the cycle start after a nodes, so they arrive together, without either pointer ever knowing a, b or c.

## What I learned

- **The set version took seconds**, because it was 141 with two return values changed. The Floyd version was the real learning.
- **The meeting point is usually *not* the cycle start.** I first assumed phase 1 would give the answer directly, but it only proves a cycle exists. The start has to be recovered in phase 2.
- **Move first, then compare.** My first phase 1 checked `slow == fast` before moving. Both start at the head, so it returned the head immediately for every list.
- `is` says "the same node object" directly. `==` happens to behave the same for `ListNode`, but only because the class doesn't define `__eq__`.
- I tried phase 2 on my own first and it didn't fully work. Once the mechanism was explained (restart one pointer at the head, then move both one node per step), the code followed quickly.
- **Seeing it made the proof click.** I worked through the algebra, then built two interactive animations with Claude to watch it happen: one that steps through the two phases with the equation filled in live, and a lab where I choose the number of nodes and the node the tail points back to, LeetCode's `pos`. Trying a long tail with a small cycle (where fast laps several times, so k > 1), a self-loop, and a list with no cycle showed that `a = k·c − b` holds every time, not just in the textbook example.

## Pattern: fast and slow pointers

Two pointers moving at different speeds along a linked list. Used here and in 141 to detect a cycle, and in 876 to find the middle. Also known as Floyd's cycle-finding algorithm.
