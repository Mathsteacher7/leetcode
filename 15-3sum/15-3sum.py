def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        start = i + 1
        end = len(nums) - 1
        while start < end:
            if nums[i] + nums[start] + nums[end] > 0:
                end -= 1
                continue
            if nums[i] + nums[start] + nums[end] < 0:
                start += 1
                continue
            if nums[i] + nums[start] + nums[end] == 0:
                result.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                continue
    return result
