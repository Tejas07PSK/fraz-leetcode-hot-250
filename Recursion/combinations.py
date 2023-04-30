class Solution:
    def __helper (self, i, n, k, temp_ans):
        while (i <= n):
            temp_ans.append(i)
            if ((k - 1) == 0): self.res.append(list(temp_ans))
            else: self.__helper(i + 1, n + 1, k - 1, temp_ans)
            temp_ans.pop()
            i += 1

    def combine (self, n: int, k: int) -> List[List[int]]:
        self.res = [] ; self.__helper(1, n - k + 1, k, [])
        return self.res
