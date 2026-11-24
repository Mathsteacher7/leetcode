def exist(board: list[list[str]], word) -> bool:
    visited = set()

    def explore(row: int, col: int, index: int) -> bool:
        if index == len(word):
            return True
        if (
            0 <= row < len(board)
            and 0 <= col < len(board[0])
            and board[row][col] == word[index]
            and (row, col) not in visited
        ):
            visited.add((row, col))
            found = (
                explore(row - 1, col, index + 1)
                or explore(row + 1, col, index + 1)
                or explore(row, col - 1, index + 1)
                or explore(row, col + 1, index + 1)
            )
            visited.remove((row, col))
            return found

    for row in range(len(board)):
        for col in range(len(board[row])):
            if explore(row, col, 0):
                return True
    return False
