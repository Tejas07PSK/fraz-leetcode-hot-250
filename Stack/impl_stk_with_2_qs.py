from collections import deque

class MyStack:
    def __init__ (self): self.q1, self.q2 = deque(), deque()

    def push (self, x: int) -> None:
        if (self.q1): self.q2.append(self.q1.popleft())
        self.q1.append(x)

    def pop (self) -> int:
        if (self.empty()): return -1
        while (len(self.q2) > 1): self.q1.append(self.q2.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.popleft()

    def top (self) -> int:
        if (self.empty()): return -1
        return self.q1[0]

    def empty (self) -> bool: return not self.q1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
