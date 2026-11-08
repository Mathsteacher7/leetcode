# 210. Course Schedule II

**Difficulty:** Medium · **Topics:** Graph, Topological Sort, Breadth-First Search · [Problem on LeetCode](https://leetcode.com/problems/course-schedule-ii/)

## Problem

The same setup as 207, but return an order in which every course can be taken, or an empty list if it's impossible. Any valid order is accepted.

## Approach

Kahn's algorithm from 207, recording each course at the moment it's taken:

```python
while queue:
    taken_course = queue.popleft()
    result.append(taken_course)          # taken now: record it, once
    for waiting in graph[taken_course]:
        needs[waiting] -= 1
        if needs[waiting] == 0:
            queue.append(waiting)
return result if len(result) == numCourses else []
```

`len(result)` replaces the `taken` counter.

## Complexity

- **Time:** O(V + E)
- **Space:** O(V + E)

## What I learned

- **I rebuilt the solution without copying from 207**, to check the pattern from the previous day.
- **A course is known to be takeable when it comes out of the queue.** My first version appended inside the `if needs[waiting] == 0` branch, which recorded the course that *freed* another. Courses that free nothing, like the end of a chain, were never recorded, and a course that freed two others was recorded twice.
- **A cycle means `[]`, not a partial order**, hence the length check at the end.
- **No early return is needed.** Mine had two bugs: `prerequisites[0]` crashes on an empty list, and with no prerequisites the answer is every course in any order, not `[]`. The main code already handles that case: every count is 0, so every course goes through the queue.
- **A `for` loop over an empty list runs zero times**, so `prerequisites = []` can't break the unpacking loop. My error came from testing with `[[]]` by mistake.
- **Spaced repetition beats volume.** More problems on the same topic straight away won't fix the pattern in memory as well as coming back to it after a gap.
