def isPalindrome(s: str) -> bool:
    lower_and_clean = "".join(ch for ch in s if ch.isalnum()).lower()
    for i in range(len(lower_and_clean) // 2):
        if lower_and_clean[i] != lower_and_clean[-1 - i]:
            return False
    return True
