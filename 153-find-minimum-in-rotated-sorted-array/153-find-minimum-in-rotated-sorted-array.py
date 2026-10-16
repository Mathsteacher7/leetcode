def findMin(nums: list[int]) -> int:
    left_pointer = 0
    right_pointer = len(nums) - 1
    while left_pointer < right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        if nums[mid_pointer] < nums[right_pointer]:
            right_pointer = mid_pointer
        else:
            left_pointer = mid_pointer + 1
    return nums[left_pointer]
