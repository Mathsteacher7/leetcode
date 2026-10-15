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


test_data_one = [1, 3, 5, 6, 7, 8, 9]
print(search(test_data_one, 8))

test_data_array_with_one = [5]
print(search(test_data_array_with_one, 5))
print(search(test_data_array_with_one, 3))

test_data_for_smaller = [-1, 0, 3, 5, 9, 12]
print(search(test_data_for_smaller, -1))

test_data_for_two = [1, 3]
print(search(test_data_for_two, 3))
