def uniquePaths(m: int, n: int) -> int:
    if m == 1 and n == 1:
        return 1
    grid = [[1] * n for _ in range(m)]
    for row in range(1, m):
        for col in range(1, n):
            grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

    return grid[-1][-1]
