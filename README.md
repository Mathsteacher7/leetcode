# LeetCode Practice

A daily habit: at least one LeetCode problem a day, solved in Python.

## Why

- **Python fluency.** My day-to-day work is React, Next.js and TypeScript. Solving problems in Python every day keeps the language in my hands rather than just in my head.
- **Problem-solving.** Breaking a problem down, spotting the pattern, and reasoning about edge cases before writing code.
- **Algorithms and Big O.** Keeping the core patterns fresh, and getting used to explaining *why* a solution has the complexity it does, not just stating it.

The aim is consistency over volume. One problem understood properly is worth more than five copied.

## How I use AI

I write every solution myself in VS Code, with AI assistants and code completion **turned off**.

I do use AI outside the editor, in two ways:

- **As a reference for syntax**: the way I used to use Stack Overflow. For example, how to remove the first key from a dict, or how Python writes a one-line conditional.
- **As a rubber duck**: talking through my approach before and while I code. It asks questions and points at the case that breaks my logic, but it doesn't hand me the solution.

The reasoning, the code and the bugs are mine. The "What I learned" section in each problem's README records the mistakes I made along the way.

The problem READMEs are drafted with AI from my working sessions, and I review them against what actually happened.

## Structure

Each problem has its own folder, named with the LeetCode number and the problem's title:

```
146-lru-cache/
  solution.py
  README.md
```

Every problem README follows the same outline:

- **Problem**: a short restatement in my own words
- **Approach**: the idea behind the solution
- **Complexity**: time and space, with the reasoning
- **What I learned**: the mistakes I actually made and the Python details I picked up
- **Alternative**: another approach and its trade-off, where there's one worth knowing

## Problems

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---|---|---|---|---|
| 1 | [Two Sum](1-two-sum/) | Easy | Hashing | O(n) | O(n) |
| 3 | [Longest Substring Without Repeating Characters](3-longest-substring-without-repeating-characters/) | Medium | Sliding window | O(n) | O(k) |
| 11 | [Container With Most Water](11-container-with-most-water/) | Medium | Two pointers | O(n) | O(1) |
| 15 | [3Sum](15-3sum/) | Medium | Sorting, two pointers | O(n²) | O(1) |
| 17 | [Letter Combinations of a Phone Number](17-letter-combinations-of-a-phone-number/) | Medium | Backtracking | O(4ⁿ · n) | O(n) |
| 20 | [Valid Parentheses](20-valid-parentheses/) | Easy | Stack | O(n) | O(n) |
| 21 | [Merge Two Sorted Lists](21-merge-two-sorted-lists/) | Easy | Linked list (recursion and loop) | O(n + m) | O(1) loop, O(n + m) recursion |
| 22 | [Generate Parentheses](22-generate-parentheses/) | Medium | Backtracking | O(4ⁿ / √n) | O(n) |
| 33 | [Search in Rotated Sorted Array](33-search-in-rotated-sorted-array/) | Medium | Binary search | O(log n) | O(1) |
| 39 | [Combination Sum](39-combination-sum/) | Medium | Backtracking | exponential (see README) | O(target / min) |
| 46 | [Permutations](46-permutations/) | Medium | Backtracking | O(n · n!) | O(n) |
| 49 | [Group Anagrams](49-group-anagrams/) | Medium | Hashing | O(n · k log k) | O(n · k) |
| 56 | [Merge Intervals](56-merge-intervals/) | Medium | Intervals, sorting | O(n log n) | O(n) |
| 62 | [Unique Paths](62-unique-paths/) | Medium | Dynamic programming (2D), maths | O(m · n) table, O(m + n) formula | O(m · n) table, O(1) formula |
| 70 | [Climbing Stairs](70-climbing-stairs/) | Easy | Dynamic programming | O(n) | O(1) |
| 78 | [Subsets](78-subsets/) | Medium | Backtracking | O(n · 2ⁿ) | O(n) |
| 79 | [Word Search](79-word-search/) | Medium | Backtracking on a grid | O(m · n · 3^L) | O(L) |
| 98 | [Validate Binary Search Tree](98-validate-binary-search-tree/) | Medium | BST, recursion (DFS) | O(n) | O(h) |
| 100 | [Same Tree](100-same-tree/) | Easy | Tree, recursion (DFS) | O(n) | O(h) |
| 102 | [Binary Tree Level Order Traversal](102-binary-tree-level-order-traversal/) | Medium | Tree, BFS | O(n) | O(n) |
| 103 | [Binary Tree Zigzag Level Order Traversal](103-binary-tree-zigzag-level-order-traversal/) | Medium | Tree, BFS | O(n) | O(n) |
| 104 | [Maximum Depth of Binary Tree](104-maximum-depth-of-binary-tree/) | Easy | Tree, recursion (DFS) | O(n) | O(h) |
| 121 | [Best Time to Buy and Sell Stock](121-best-time-to-buy-and-sell-stock/) | Easy | Single pass | O(n) | O(1) |
| 125 | [Valid Palindrome](125-valid-palindrome/) | Easy | Two pointers | O(n) | O(1) |
| 128 | [Longest Consecutive Sequence](128-longest-consecutive-sequence/) | Medium | Hashing | O(n) | O(n) |
| 136 | [Single Number](136-single-number/) | Easy | Bit manipulation | O(n) | O(1) |
| 139 | [Word Break](139-word-break/) | Medium | Dynamic programming, hashing | O(n³) | O(n + dictionary) |
| 141 | [Linked List Cycle](141-linked-list-cycle/) | Easy | Linked list, hashing | O(n) | O(n) |
| 142 | [Linked List Cycle II](142-linked-list-cycle-ii/) | Medium | Fast and slow pointers | O(n) | O(1) |
| 146 | [LRU Cache](146-lru-cache/) | Medium | Design, hashing | O(1) per op | O(capacity) |
| 153 | [Find Minimum in Rotated Sorted Array](153-find-minimum-in-rotated-sorted-array/) | Medium | Binary search | O(log n) | O(1) |
| 155 | [Min Stack](155-min-stack/) | Medium | Stack, design | O(1) per op | O(n) |
| 198 | [House Robber](198-house-robber/) | Medium | Dynamic programming | O(n) | O(1) |
| 199 | [Binary Tree Right Side View](199-binary-tree-right-side-view/) | Medium | Tree, BFS | O(n) | O(n) |
| 200 | [Number of Islands](200-number-of-islands/) | Medium | Graph, DFS | O(rows × cols) | O(rows × cols) |
| 206 | [Reverse Linked List](206-reverse-linked-list/) | Easy | Linked list | O(n) | O(1) |
| 207 | [Course Schedule](207-can-finish/) | Medium | Graph, topological sort (BFS) | O(V + E) | O(V + E) |
| 208 | [Implement Trie (Prefix Tree)](208-implement-trie-prefix-tree/) | Medium | Trie, design | O(L) per op | O(total letters) |
| 210 | [Course Schedule II](210-course-schedule-ii/) | Medium | Graph, topological sort (BFS) | O(V + E) | O(V + E) |
| 213 | [House Robber II](213-house-robber-ii/) | Medium | Dynamic programming | O(n) | O(n) |
| 215 | [Kth Largest Element in an Array](215-kth-largest-element-in-an-array/) | Medium | Heap | O(n log k) | O(k) |
| 226 | [Invert Binary Tree](226-invert-binary-tree/) | Easy | Tree, recursion (DFS) | O(n) | O(h) |
| 230 | [Kth Smallest Element in a BST](230-kth-smallest-element-in-a-bst/) | Medium | BST, in-order traversal | O(n) list, O(h + k) early stop | O(n) list, O(h) early stop |
| 238 | [Product of Array Except Self](238-product-of-array-except-self/) | Medium | Prefix and suffix products | O(n) | O(1) |
| 242 | [Valid Anagram](242-valid-anagram/) | Easy | Hashing | O(n) | O(k) |
| 268 | [Missing Number](268-missing-number/) | Easy | Maths, bit manipulation | O(n) | O(1) |
| 300 | [Longest Increasing Subsequence](300-longest-increasing-subsequence/) | Medium | Dynamic programming | O(n²) | O(n) |
| 322 | [Coin Change](322-coin-change/) | Medium | Dynamic programming | O(amount × coins) | O(amount) |
| 347 | [Top K Frequent Elements](347-top-k-frequent-elements/) | Medium | Hashing, bucket sort, heap | O(n) buckets, O(n + m log k) heap | O(n) |
| 380 | [Insert Delete GetRandom O(1)](380-insert-delete-getrandom-o1/) | Medium | Design, hashing | O(1) per op | O(n) |
| 424 | [Longest Repeating Character Replacement](424-longest-repeating-character-replacement/) | Medium | Sliding window, hashing | O(n) | O(1) |
| 704 | [Binary Search](704-binary-search/) | Easy | Binary search | O(log n) | O(1) |
| 739 | [Daily Temperatures](739-daily-temperatures/) | Medium | Monotonic stack | O(n) | O(n) |
| 876 | [Middle of the Linked List](876-middle-of-the-linked-list/) | Easy | Fast and slow pointers | O(n) | O(1) |

## Patterns covered so far

- **Hashing:** using a dict or set for O(1) lookup, and choosing what the key and value should be (1, 49, 128, 139, 141, 146, 242, 347, 380, 424)
- **Design:** classes whose state persists between calls, often combining two data structures so each covers the other's weakness (146, 155, 208, 380)
- **Single pass with a running summary:** scanning once and keeping only what the past tells you (121)
- **Sliding window:** two pointers moving in the same direction over a sequence; the right edge moves every step, the left edge only when the window breaks a rule (3, 424)
- **Two pointers from opposite ends:** moving towards each other, with a reason for which one moves (11, 15, 125)
- **Stack:** last in, first out, for anything that must be closed or undone in reverse order (20, 155)
- **Monotonic stack:** a stack of items still waiting for their answer; each new item settles the waiting ones it beats, then waits itself (739)
- **Binary search:** halving a window that always contains the answer, for a target or for a boundary (33, 153, 704)
- **Trees and recursion (DFS):** a base case for `None`, then each call handles its own subtree and the parent combines its children's results (98, 100, 104, 226, 230)
- **Linked lists:** re-linking existing nodes by moving labels and changing `next` pointers, always saving a link before overwriting it (21, 141, 142, 206, 876)
- **Fast and slow pointers:** two pointers moving at different speeds, to find the middle of a list or detect a cycle and where it starts (142, 876)
- **Dynamic programming:** answering a big question from smaller versions of itself, computing each smaller answer once and keeping only what's needed (62, 70, 139, 198, 213, 300, 322)
- **Graphs (grid DFS):** scanning a grid and exploring each connected region once, tracking visited cells (200)
- **Breadth-first search:** a queue (`collections.deque`) visits nodes in the order they were found, level by level (102, 103, 199, 207, 210)
- **Topological sort (Kahn's algorithm):** building an adjacency list and in-degree counts, then taking nodes whose count reaches 0; a cycle is whatever never gets taken (207, 210)
- **Bit manipulation:** using XOR's algebra to cancel out pairs without extra space (136, 268)
- **Backtracking:** walking a tree of choices. With one shared list or set: choose, explore, undo (39, 46, 78, 79); or pass a new string down each call, so nothing needs undoing (17, 22)
- **Heaps:** a priority queue that keeps the smallest item at the front, to track the top `k` without sorting everything (215, 347)
- **Bucket sort:** using a list position to carry meaning, such as a frequency, instead of comparing items (347)
- **Intervals:** sort by start, then one pass comparing each interval with the last one built (56)
- **Prefix and suffix products:** a running value in each direction, so each position combines "everything to the left" and "everything to the right" without recomputing (238)
- **Binary search trees:** smaller values on the left, bigger on the right; limits passed down the recursion to validate one, and an in-order traversal (left, node, right) to read it in sorted order (98, 230)
- **Tries:** a tree of letters where words with the same beginning share a path, for fast prefix lookups (208)
- **Maths shortcuts:** a formula instead of a loop, such as the sum of 0 to n, or counting paths with combinations (62, 268)
- **Sorting first:** putting the input in order so that pointers can move with a reason, duplicates sit next to each other, or a loop can stop early (15, 39, 56)
