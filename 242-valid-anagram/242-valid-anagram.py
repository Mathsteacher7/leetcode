class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_letter_count = self.create_dict(s)
        second_letter_count = self.create_dict(t)
        return first_letter_count == second_letter_count

    def create_dict(self, word: str) -> dict[str, int]:
        letters_in_dict = {}
        for letter in word:
            letters_in_dict[letter] = letters_in_dict.get(letter, 0) + 1
        return letters_in_dict
