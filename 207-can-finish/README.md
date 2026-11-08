# 207. Course Schedule

**Difficulty:** Medium · **Topics:** Graph, Topological Sort, Breadth-First Search · [Problem on LeetCode](https://leetcode.com/problems/course-schedule/)

## Problem

There are `numCourses` courses, `0` to `numCourses - 1`. Each pair `[a, b]` in `prerequisites` means course `a` needs course `b` first. Return `True` if every course can be finished, which is the same as asking whether the prerequisite graph has no cycle.

## Approach: Kahn's algorithm (topological sort)

Think of a student planning a degree: a course can be taken once all its prerequisites are done.

Three structures, each with its own job:

| Name | What it holds |
|---|---|
| `graph` | an adjacency list: for each course, the courses waiting on it |
| `needs` | for each course, how many prerequisites are still unfinished (its in-degree) |
| `queue` | the courses ready to take right now |

```python
needs = [0] * numCourses
graph = [[] for _ in range(numCourses)]
for course, prereq in prerequisites:
    graph[prereq].append(course)
    needs[course] += 1

queue = deque([c for c in range(numCourses) if needs[c] == 0])
taken = 0
while queue:
    taken_course = queue.popleft()
    taken += 1
    for waiting in graph[taken_course]:
        needs[waiting] -= 1
        if needs[waiting] == 0:
            queue.append(waiting)
return taken == numCourses
```

Courses in a cycle each wait on another, so their counts never reach 0, they never enter the queue, and `taken` ends up less than `numCourses`.

## Complexity

- **Time:** O(V + E): each course is taken at most once, and each pair is used once to reduce a count
- **Space:** O(V + E) for `graph`, `needs` and the queue

## What I learned

- **The graph isn't given; you build it.** `numCourses` is the number of nodes and `prerequisites` the edges, and the two counts are independent. Courses that appear in no pair still exist and are free. `graph` is just a variable name for a list of lists; Python has no graph type.
- **The queue holds course numbers, not pairs.** The pairs are only read once, to build `graph` and `needs`.
- **Build the queue after counting.** My queue was created while `needs` was still all zeros, so every course went in, and the function answered `True` for any input.
- **My tests passed by coincidence.** With a stale variable in the inner loop (`course`, left over from the pairs loop) and a reused loop name, the three examples happened to give the right answers. A cycle plus another pair, `3, [[1,0],[0,1],[2,0]]`, exposed it: it returned `True`. Clear names fixed it: `taken_course` for the course just taken, `waiting` for each course waiting on it. Lesson: one passing set of tests doesn't prove the logic; add a case designed to break it.
- **`[[] for _ in range(n)]`** is a list comprehension: `[]` is created fresh on each pass, and `_` means "I don't use this value". `[c for c in range(n) if needs[c] == 0]` adds a filter.
- **`[]` and `[[]]` are different inputs.** `[[]]` is one empty pair, which can't be unpacked; "no prerequisites" is `[]`.
- `queue.popleft()` is the normal way to call the method; `deque.popleft(queue)` works but reads oddly.
- **This one needed seeing.** I built a line-by-line debugger with Claude showing the graph being built arrow by arrow, each course's `needs` count going down, the queue, and which courses are never freed. The diamond example made it clear why `needs` is a count and not just yes/no.
- **Plan:** solve it again from an empty file after a week, to check the pattern has stuck.

## Alternative

DFS with three states per course (not visited, visiting, done): reaching a course that's still "visiting" means the path has looped back on itself.
