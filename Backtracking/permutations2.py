class Solution:
    def __helper (self, n, curr_per):
        if (n == 0):
            self.res.append(list(curr_per))
            return
        for num in self.hm:
            if (self.hm[num] > 0):
                self.hm[num] -= 1
                curr_per.append(num)
                self.__helper(n - 1, curr_per)
                curr_per.pop()
                self.hm[num] += 1

    def permuteUnique (self, nums: List[int]) -> List[List[int]]:
        self.res, self.hm = [], {}
        for num in nums: self.hm[num] = self.hm.get(num, 0) + 1
        self.__helper(len(nums), [])
        return self.res
