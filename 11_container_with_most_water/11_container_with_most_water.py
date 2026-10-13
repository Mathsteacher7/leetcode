def maxArea(height: list[int]) -> int:
    right_index = len(height) - 1
    left_index = 0
    max_area = 0
    while right_index > left_index:
        new_area = min(height[left_index], height[right_index]) * (
            right_index - left_index
        )
        max_area = max(max_area, new_area)
        if height[left_index] > height[right_index]:
            right_index -= 1
        else:
            left_index += 1
    return max_area
