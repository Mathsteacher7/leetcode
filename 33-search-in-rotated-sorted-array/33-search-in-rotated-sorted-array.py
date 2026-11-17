def search(nums: list[int], target: int) -> int:
    left_pointer = 0
    right_pointer = len(nums) - 1
    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        if nums[mid_pointer] == target:
            return mid_pointer
        if nums[left_pointer] <= nums[mid_pointer]:
            if nums[left_pointer] <= target < nums[mid_pointer]:
                right_pointer = mid_pointer - 1
            else:
                left_pointer = mid_pointer + 1
        else:
            if nums[mid_pointer] < target <= nums[right_pointer]:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer - 1
    return -1
