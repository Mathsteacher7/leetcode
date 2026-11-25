def generateParenthesis(n: int) -> list[str]:
    result = []

    def explore(path: str, opened: int, closed: int) -> None:
        if len(path) == n * 2:
            result.append(path)
            return
        if opened < n:
            explore(path + "(", opened + 1, closed)
        if closed < opened:
            explore(path + ")", opened, closed + 1)

    explore("", 0, 0)
    return result
