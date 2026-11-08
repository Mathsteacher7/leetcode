# 238. Product of Array Except Self

**Difficulty:** Medium · **Topics:** Array, Prefix Sum · [Problem on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

## Problem

Return a list where position `i` holds the product of every element except `nums[i]`. No division, and O(n) time. Follow-up: O(1) extra space, not counting the output.

## Approach

Everything except `nums[i]` splits into two parts:

```
answer[i] = (product of everything LEFT of i) × (product of everything RIGHT of i)
```

One pass left to right stores each left product in `result`; one pass right to left multiplies each right product into it:

```python
result = []
left_side = 1
for i in range(len(nums)):
    result.append(left_side)     # product of everything before i
    left_side *= nums[i]         # then include nums[i] for the next index

right_side = 1
for i in reversed(range(len(nums))):
    result[i] *= right_side      # left × right
    right_side *= nums[i]
return result
```

For `[1, 2, 3, 4]`: the left pass gives `[1, 1, 2, 6]`, and the right pass turns it into `[24, 12, 8, 6]`.

## Complexity

- **Time:** O(n), two passes
- **Space:** O(1) extra: just `left_side` and `right_side` besides the output

## What I learned

- **I started with an O(n²) baseline**: for each index, `math.prod(nums[:i]) * math.prod(nums[i + 1:])`. Correct, but at 100,000 numbers it's billions of multiplications.
- **The waste was recalculating.** At `i = 3`, the prefix 1 × 2 × 3 re-multiplies 1 × 2, which was already worked out at `i = 2`. Keeping a running product means one multiplication per step, like a running total on a till, or `ways(n − 1)` in 70.
- **Record first, then multiply in `nums[i]`.** That order is what keeps each element out of its own product: the "except self".
- **`nums[i - 1]` at `i = 0` is `nums[-1]`**, the last element. It doesn't crash; it silently gives the wrong number. Recording before multiplying removed the need for `i - 1` altogether.
- **Start the running product at 1, not `nums[0]`**: 1 is the empty product (`math.prod([])` is 1), and starting at `nums[0]` would include the first element in its own answer.
- **No second list for the right side:** multiplying into `result[i]` reuses the output, which is how the O(1) follow-up is met.
- **Loop over reversed indexes, not reversed values**: `reversed(range(len(nums)))`, because the position is needed to update `result[i]`.
- **Zeros work without a special case**, which is why division was ruled out anyway: `[0, 1, 2]` gives `[2, 0, 0]`.
- **Read the Constraints section.** It says `2 <= len(nums)`, so empty and single-element lists can't happen. The prefix approach handles them anyway.

## Pattern: prefix and suffix products

When each answer depends on everything to its left and everything to its right, build each side with a running value in one pass per direction, instead of recomputing it for every position.
