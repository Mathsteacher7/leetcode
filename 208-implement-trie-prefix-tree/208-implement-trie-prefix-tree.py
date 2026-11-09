class TrieNode:
    def __init__(self):
        self.word_dict = {}
        self.is_end = False


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
        node = self._find(prefix)
        return bool(node)

    def _find(self, letters: str) -> TrieNode | None:
        node = self.root
        for letter in letters:
            if letter not in node.word_dict:
                return None
            node = node.word_dict[letter]
        return node
