from collections import deque

class Solution:
    def __method_1 (self, i, target, arr, dq):
        if (target == 0):
            self.ans.append(list(dq))
            return
        if (i == (len(arr) - 1)):
            if ((target % arr[i]) == 0):
                tmp_lst = list(dq) ; tmp_lst.extend([arr[i] for j in range(target // arr[i])])
                self.ans.append(tmp_lst)
            return
        dq.append(arr[i])
        if (arr[i] <= target): self.__method_1(i, target - arr[i], arr, dq)
        dq.pop()
        self.__method_1(i + 1, target, arr, dq)

    def combinationSum (self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.__method_1(0, target, candidates, deque())
        return self.ans

