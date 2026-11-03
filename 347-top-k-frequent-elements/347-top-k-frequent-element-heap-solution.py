import heapq


def topKFrequent(nums: list[int], k: int) -> list[int]:
    result = []
    buckets = []
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    for num, count in freq_dict.items():
        heapq.heappush(buckets, (count, num))
        if len(buckets) > k:
            heapq.heappop(buckets)
    for couple in buckets:
        result.append(couple[1])
    return result
