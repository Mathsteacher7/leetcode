def subsets(nums: list[int]) -> list[list[int]]:
    subsets_list = [[]]
    for num in nums:
        for i in range(len(subsets_list)):
            subsets_list.append(subsets_list[i] + [num])
    return subsets_list
