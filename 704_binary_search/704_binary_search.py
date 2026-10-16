def search(nums: list[int], target: int) -> int:
    left_pointer = 0
    right_pointer = len(nums) - 1
    while right_pointer >= left_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        if nums[mid_pointer] < target:
            left_pointer = mid_pointer + 1
        elif nums[mid_pointer] > target:
            right_pointer = mid_pointer - 1
        else:
            return mid_pointer
    return -1
