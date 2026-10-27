def rob(nums: list[int]) -> int:
    two_back = 0
    one_back = 0
    for num in nums:
        best = max(one_back, two_back + num)
        two_back, one_back = one_back, best
    return one_back
