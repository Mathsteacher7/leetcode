def isValid(s: str) -> bool:
    closing_dict = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for char in s:
        if stack and char == closing_dict[stack[-1]]:
            stack.pop()
        elif char in closing_dict:
            stack.append(char)
        else:
            return False
    return not stack
