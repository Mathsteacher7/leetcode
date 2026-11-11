# 208. Implement Trie (Prefix Tree)

**Difficulty:** Medium · **Topics:** Hash Table, String, Design, Trie · [Problem on LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)

## Problem

Build a `Trie` class with three methods: `insert(word)`, `search(word)`, which is `True` only if that exact word was inserted, and `startsWith(prefix)`, which is `True` if any inserted word begins with `prefix`.

## Approach

A trie is a tree of letters. Each node maps a letter to the next node, and a flag marks where a whole word ends. Words that share a beginning share the same path, so `"app"` and `"apple"` use the same first three nodes.

```python
class TrieNode:
    def __init__(self):
        self.word_dict = {}      # letter -> next TrieNode
        self.is_end = False      # does a word end here?


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.word_dict:
                node.word_dict[letter] = TrieNode()
            node = node.word_dict[letter]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return bool(self._find(prefix))

    def _find(self, letters: str) -> TrieNode | None:
        node = self.root
        for letter in letters:
            if letter not in node.word_dict:
                return None
            node = node.word_dict[letter]
        return node
```

`search` and `startsWith` walk the same path, so the walk lives in one helper, `_find`. The only difference between them is whether the last node has to be the end of a word.

## Complexity

- **Time:** O(L) per call, where L is the length of the word or prefix. The cost doesn't depend on how many words are stored.
- **Space:** O(total letters inserted) in the worst case, less when words share prefixes.

## What I learned

- **The node is its own class.** The `Trie` holds only the root; every node underneath is a `TrieNode` with its own dict and flag.
- **An attribute name has to match everywhere.** I named it one thing in `TrieNode.__init__` and used a different name in the methods, which gave an `AttributeError`.
- **Don't reassign `self.root` while walking.** My first `insert` moved `self.root` down the tree, so after one word the trie had lost its top. The walk needs a local variable, `node`, that starts at the root.
- **`_find` returns `None` for "not there", and the public methods return a `bool`.** `None` and `False` are both falsy, but the problem asks for `True`/`False`, so `search` and `startsWith` turn the result into a real boolean. `bool(node)` works because `None` is falsy and any object, including a `TrieNode`, is truthy by default.
- **The leading underscore** marks `_find` as a helper for the class itself, not part of its public interface. Python doesn't enforce it; it's a convention.
- **`TrieNode | None`** is a type hint saying the function returns a node or `None`.
- **`__slots__`** (`__slots__ = ("word_dict", "is_end")`) fixes a class's attributes in advance, which saves memory when there are many small objects, like trie nodes.

## Alternative

Nested dicts with no node class: each node is a dict, and a special key such as `"$"` marks the end of a word. It's shorter, but the class version says what each part means.
