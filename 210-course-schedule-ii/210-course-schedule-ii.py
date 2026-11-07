from collections import deque


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    result = []
    needs = [0] * numCourses
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        needs[course] += 1
    queue = deque([course for course in range(numCourses) if needs[course] == 0])
    while queue:
        taken_course = queue.popleft()
        result.append(taken_course)
        for waiting in graph[taken_course]:
            needs[waiting] -= 1
            if needs[waiting] == 0:
                queue.append(waiting)
    return result if len(result) == numCourses else []
