def permute(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(path: list[int]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num in path:
                continue
            path.append(num)
            backtrack(path)
            path.pop()

    backtrack([])
    return result
