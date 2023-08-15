from collections import deque

class Solution:
    def findOrder (self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_ord_arr, res, q = [0 for i in range(numCourses)], [], deque()
        graph = [[] for i in range(numCourses)]
        for end, start in prerequisites:
            graph[start].append(end)
            in_ord_arr[end] += 1
        for i in range(numCourses):
            if (in_ord_arr[i] == 0): q.append(i)
        while (q):
            curr_node = q.popleft()
            res.append(curr_node)
            for next_node in graph[curr_node]:
                in_ord_arr[next_node] -= 1
                if (in_ord_arr[next_node] == 0): q.append(next_node)
        return res if (len(res) == numCourses) else []
