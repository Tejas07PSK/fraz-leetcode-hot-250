class Solution:
    def __combinationSumHelper (self, i, candidates, target, temp_sol):
        if (i == (len(candidates) - 1)):
            if ((target % candidates[i]) == 0):
                self.res.append(temp_sol + [candidates[i] for j in range(target // candidates[i])])
            return
        next_target = target - candidates[i]
        temp_sol.append(candidates[i])
        if (next_target > 0): self.__combinationSumHelper(i, candidates, next_target, temp_sol)
        elif (next_target == 0): self.res.append(list(temp_sol))
        temp_sol.pop()
        self.__combinationSumHelper(i + 1, candidates, target, temp_sol) 

    def combinationSum (self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.__combinationSumHelper(0, candidates, target, [])
        return self.res
