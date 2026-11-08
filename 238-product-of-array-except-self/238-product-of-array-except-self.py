def productExceptSelf(nums: list[int]) -> list[int]:
    result = []
    left_side = 1
    right_side = 1
    for i in range(len(nums)):
        result.append(left_side)
        left_side *= nums[i]
    for i in reversed(range(len(nums))):
        result[i] *= right_side
        right_side *= nums[i]
    return result
