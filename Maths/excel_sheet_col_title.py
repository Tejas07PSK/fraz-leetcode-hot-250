from collections import deque

class Solution:
    def convertToTitle (self, columnNumber: int) -> str:
        res = deque()
        while (columnNumber > 0):
            columnNumber -= 1
            res.appendleft(chr(ord('A') + (columnNumber % 26)))
            columnNumber //= 26
        return "".join(res)
