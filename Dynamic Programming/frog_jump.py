class Solution:
    def __helper (self, start, end, jump, stones):
        if (start == end): return True
        if ((start, jump) in self.dp): return self.dp[(start, jump)]
        ans = False
        for offset in self.dirs:
            next_jump = jump + offset
            if (next_jump > 0):
                next_start = start + next_jump
                if (next_start in stones): ans = ans or self.__helper(next_start, end, next_jump, stones)
            if (ans): break
        self.dp[(start, jump)] = ans
        return self.dp[(start, jump)]

    def canCross (self, stones: List[int]) -> bool:
        start, end, jump = stones[0], stones[-1], 0
        self.dp, stones = {}, set(stones)
        self.dirs = [-1, 0, 1]
        return self.__helper(start, end, jump, stones)
