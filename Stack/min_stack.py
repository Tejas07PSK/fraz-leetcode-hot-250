class MinStack:
    def __init__ (self): self.stk1, self.stk2 = [], []

    def push (self, val: int) -> None:
        self.stk1.append(val)
        self.stk2.append(val if ((not self.stk2) or (val < self.stk2[-1])) else self.stk2[-1])

    def pop (self) -> None:
        self.stk1.pop()
        self.stk2.pop()

    def top (self) -> int: return self.stk1[-1]

    def getMin (self) -> int: return self.stk2[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
