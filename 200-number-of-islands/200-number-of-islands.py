def numIslands(grid: list[list[str]]) -> int:
    visited = set()

    def explore(row: int, col: int) -> None:
        if (
            0 <= row < len(grid)
            and 0 <= col < len(grid[0])
            and grid[row][col] == "1"
            and (row, col) not in visited
        ):
            visited.add((row, col))
            explore(row - 1, col)
            explore(row + 1, col)
            explore(row, col - 1)
            explore(row, col + 1)

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) not in visited and grid[row][col] == "1":
                count += 1
                explore(row, col)
    return count
