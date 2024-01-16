class Solution:
    def __helper (self, i, candidates, target, curr_path):
        if (i == len(candidates)):
            if (target == 0): self.res.append(list(curr_path))
            return
        if (target == 0):
          self.res.append(list(curr_path))
          return
        if ((target - candidates[i]) >= 0):
            curr_path.append(candidates[i])
            self.__helper(i + 1, candidates, target - candidates[i], curr_path)
            curr_path.pop()
        while (((i + 1) < len(candidates)) and (candidates[i] == candidates[i + 1])): i += 1
        self.__helper(i + 1, candidates, target, curr_path)

    def combinationSum2 (self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = [] ; candidates.sort()
        self.__helper(0, candidates, target, deque())
        return self.res

