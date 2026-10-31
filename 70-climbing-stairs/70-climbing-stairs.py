def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    first_way = 1
    second_way = 2
    total_ways = 0
    for _ in range(2, n):
        total_ways = first_way + second_way
        first_way = total_ways - first_way
        second_way = total_ways
    return total_ways
