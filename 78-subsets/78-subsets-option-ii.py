def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(i: int, path: list[int]) -> None:
        if i == len(nums):
            result.append(path[:])
            return
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
        backtrack(i + 1, path)

    backtrack(0, [])
    return result
