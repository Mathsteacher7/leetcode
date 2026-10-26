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


"""
1 , 1 , 2, 3, 5, 8 , 13, 21 , 34...
"""
print(climbStairs(2))
"""
1
2
"""
print(climbStairs(3))
"""
1 + 1 + 1
1 + 2
2 + 1
"""
print(climbStairs(4))
"""
1 + 1 + 1 + 1
1 + 1 + 2
1 + 2 + 1
2 + 1 + 1
2 + 2
"""
print(climbStairs(5))
"""
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 1 + 2 + 1 
1 + 2 + 1 + 1
1 + 2 + 2
2 + 1 + 1 + 1
2 + 1 + 2
2 + 2 + 1
"""

print(climbStairs(6))
"""
1 + 1 + 1 + 1 + 1 + 1 
1 + 1 + 1 + 1 + 2
1 + 1 + 2 + 2
1 + 1 + 1 + 2 + 1
1 + 1 + 2 + 1 + 1
1 + 2 + 1 + 1 + 1
1 + 2 + 1 + 2
1 + 2 + 2 + 1
2 + 1 + 1 + 1 + 1
2 + 1 + 1 + 2
2 + 1 + 2 + 1
2 + 2 + 1 + 1
2 + 2 + 2 + 2
"""
