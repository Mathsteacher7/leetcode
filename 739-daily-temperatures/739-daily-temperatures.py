def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    waiting_list = []
    for i in range(len(temperatures)):
        while waiting_list and temperatures[i] > temperatures[waiting_list[-1]]:
            waiting_day = waiting_list.pop()
            result[waiting_day] = i - waiting_day
        waiting_list.append(i)
    return result
