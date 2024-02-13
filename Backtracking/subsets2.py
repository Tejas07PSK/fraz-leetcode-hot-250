class Solution:
    def __helper(self, start, end, nums, curr_path):
        if (start == end):
            self.res.append(list(curr_path))
            return
        curr_path.append(nums[start])
        self.__helper(start + 1, end, nums, curr_path)
        curr_path.pop()
        while (((start + 1) < end) and (nums[start] == nums[start + 1])): start += 1
        self.__helper(start + 1, end, nums, curr_path)

    def subsetsWithDup (self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.__helper(0, len(nums), nums, [])
        return self.res
