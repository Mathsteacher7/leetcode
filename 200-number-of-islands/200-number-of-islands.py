# def numIslands(grid: list[list[str]]) -> int:
#     number_of_islands = 0
#     previous_lands = set()
#     for row in range(len(grid)):
#         for col in row:
#             if grid[row][col] == "1":
#                 if (row, col) in previous_lands:
#                     previous_lands.append((row, col))

#                 else:
#                     number_of_islands += 1
#                 numIslands(
#                     ["0", grid[row - 1][col], "0"],
#                     [
#                         grid[row][col - 1],
#                         "0",
#                         grid[row][col + 1],
#                         [0, grid[row + 1][col]],
#                         "0",
#                     ],
#                 )
#     return number_of_islands


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
