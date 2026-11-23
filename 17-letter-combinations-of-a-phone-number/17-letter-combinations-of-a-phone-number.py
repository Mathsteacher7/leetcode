def letterCombinations(digits: str) -> list[str]:
    if len(digits) == 0:
        return []
    number_to_letter = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []

    def explore(index: int, path: str) -> None:
        if len(path) == len(digits):
            result.append(path)
            return
        for letter in number_to_letter[digits[index]]:
            explore(index + 1, path + letter)

    explore(0, "")
    return result
