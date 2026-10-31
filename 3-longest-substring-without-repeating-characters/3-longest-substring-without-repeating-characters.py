def lengthOfLongestSubstring(s: str) -> int:
    longest_substring = 0
    left_edge = 0
    dict_of_letters = {}
    for index, letter in enumerate(s):
        if letter in dict_of_letters:
            left_edge = max(left_edge, dict_of_letters[letter] + 1)
        dict_of_letters[letter] = index
        longest_substring = max(index - left_edge + 1, longest_substring)

    return longest_substring
