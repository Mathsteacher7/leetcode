def twoSum(nums: list[int], target: int) -> list[int]:
    nums_dict = {}
    for i in range(len(nums)):
        if (target - nums[i]) in nums_dict:
            return [nums_dict[target - nums[i]], i]
        nums_dict[nums[i]] = i
