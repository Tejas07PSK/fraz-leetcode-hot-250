from collections import deque

class Solution:
    def minimumJumps (self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q, visited = deque([((0, -1), 0)]), set([(0, -1)])
        direcs, forbidden = [a, -b], set(forbidden)
        while (q):
            curr_node, curr_jump = q.popleft()
            if (curr_node[0] == x): return curr_jump
            for offset in direcs:
                next_node = (curr_node[0] + offset, -1 if (offset < 0) else 1)
                next_jump = curr_jump + 1
                if ((next_node not in visited) and (not ((curr_node[1] < 0) and (next_node[1] < 0))) and (next_node[0] not in forbidden) and (0 <= next_node[0] <= 6000)):
                    q.append((next_node, next_jump))
                    visited.add(next_node)
        return -1
