class Solution:
    def __combinationSum3Helper (self, i, k, n, temp_sol):
        while (i <= (9 - k + 1)):
            if ((n - i) == 0):
                if ((k - 1) == 0): self.res.append(temp_sol + [i])
                break
            elif ((n - i) < 0): break
            else:
                if ((k - 1) > 0):
                    temp_sol.append(i)
                    self.__combinationSum3Helper(i + 1, k - 1, n - i, temp_sol)
                    temp_sol.pop()
            i += 1

    def combinationSum3 (self, k: int, n: int) -> List[List[int]]:
        self.res = [] ; self.__combinationSum3Helper(1, k, n, []) ; return self.res
