def characterReplacement(s: str, k: int) -> int:
    letter_count = {}
    left_pointer = 0
    longest_string = 0
    for right_pointer in range(len(s)):
        letter_count[s[right_pointer]] = letter_count.get(s[right_pointer], 0) + 1
        window = right_pointer - left_pointer + 1
        while window - max(letter_count.values()) > k:
            letter_count[s[left_pointer]] -= 1
            left_pointer += 1
            window = right_pointer - left_pointer + 1
        longest_string = max(longest_string, window)
    return longest_string
