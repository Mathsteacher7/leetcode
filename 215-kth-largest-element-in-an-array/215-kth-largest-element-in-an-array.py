import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    k_largest = []
    for num in nums:
        heapq.heappush(k_largest, num)
        if len(k_largest) > k:
            heapq.heappop(k_largest)
    return k_largest[0]
