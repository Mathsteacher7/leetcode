from collections import deque


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    if numCourses == 0 or len(prerequisites) == 0:
        return True
    needs = [0] * numCourses
    graph = [[] for _ in range(numCourses)]
    taken = 0
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        needs[course] += 1
    queue = deque([course for course in range(numCourses) if needs[course] == 0])
    while queue:
        taken_course = queue.popleft()
        taken += 1
        for waiting in graph[taken_course]:
            needs[waiting] -= 1
            if needs[waiting] == 0:
                queue.append(waiting)
    return taken == numCourses
