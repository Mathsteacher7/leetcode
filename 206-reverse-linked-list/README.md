# 206. Reverse Linked List

**Difficulty:** Easy · **Topics:** Linked List · [Problem on LeetCode](https://leetcode.com/problems/reverse-linked-list/)

## Problem

Given the head of a linked list, reverse it and return the new head: `1 → 2 → 3 → None` becomes `3 → 2 → 1 → None`.

## Approach

Walk the list once, flipping each `next` pointer to point backwards. Three labels:

- `previous`: the node behind, which starts as `None`
- `current`: the node being flipped, which starts at `head`
- `next_node`: the rest of the list, saved fresh at the start of each pass

While `current` exists:

1. **Save** the rest: `next_node = current.next`
2. **Flip** the link: `current.next = previous`
3. **Move** `previous` onto `current`
4. **Move** `current` onto `next_node`

When the loop ends, `current` is `None` and `previous` is on the new head, so return `previous`.

## Complexity

- **Time:** O(n), one pass
- **Space:** O(1), three labels

## What I learned

- **Start with `previous = None`.** The old head becomes the last node, so its `next` must become `None`. Starting with `previous = head` and `current = head.next` left the old head pointing forward, which created a cycle: `1 → 2 → 1 → 2 …`.
- **Save `next_node` inside the loop, at the start of each pass.** Saving it once before the loop and stepping it forward at the end crashed on the last pass, when it was already `None`. Reading `current.next` inside the loop is always safe, because the `while` guarantees `current` exists.
- **Save before you overwrite.** Flipping `current.next` destroys the only link to the rest of the list, so it has to be saved first.
- **Order of the moves:** move `previous` before `current`, or the node `previous` should move onto is lost.
- **Return `previous`, not `head`.** After reversing, `head` points at the last node.
- With these starting values, an empty list needs no special case: the loop never runs and `previous` is `None`.
- `previous_node.next = previous_node` makes a node point at itself, which is an easy bug when a label is reassigned on the line before.
