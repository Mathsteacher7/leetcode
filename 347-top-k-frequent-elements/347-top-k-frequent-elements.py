def topKFrequent(nums: list[int], k: int) -> list[int]:
    result = []
    buckets = [[] for _ in range(len(nums) + 1)]
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    for num, count in freq_dict.items():
        buckets[count].append(num)
    for bucket in reversed(buckets):
        for num in bucket:
            result.append(num)
            if len(result) == k:
                return result
