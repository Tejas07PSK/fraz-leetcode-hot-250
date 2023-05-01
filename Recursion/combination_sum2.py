class Solution:
    def __combinationSum2Helper (self, i, candidates, target, temp_sol):
        if (target == 0):
            self.res.append(list(temp_sol))
            return
        if (i == (len(candidates) - 1)):
            if ((target - candidates[i]) == 0): self.res.append(temp_sol + [candidates[i]])
            return
        temp_sol.append(candidates[i])
        if ((target - candidates[i]) >= 0):
            self.__combinationSum2Helper(i + 1, candidates, target - candidates[i], temp_sol)
        temp_sol.pop()
        while (((i + 1) < len(candidates)) and (candidates[i] == candidates[i + 1])): i += 1
        if ((i + 1) < len(candidates)): self.__combinationSum2Helper(i + 1, candidates, target, temp_sol)

    def combinationSum2 (self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() ; self.res = [] ; self.__combinationSum2Helper(0, candidates, target, [])
        return self.res
