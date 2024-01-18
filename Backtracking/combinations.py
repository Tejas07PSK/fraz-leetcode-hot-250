class Solution:
    def __helper (self, idx, n, k, curr_path):
        while (idx <= n):
            curr_path.append(idx)
            if ((k - 1) == 0): self.res.append(list(curr_path))
            else: self.__helper(idx + 1, n + 1, k - 1, curr_path)
            curr_path.pop()
            idx += 1

    def combine (self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.__helper(1, n - k + 1, k, deque())
        return self.res
