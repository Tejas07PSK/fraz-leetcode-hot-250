class Solution:
    def subsets (self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2 ** len(nums)):
            tmp_res, tmp_i, idx =[], i, 0
            while (tmp_i != 0):
                if ((tmp_i & 1) > 0): tmp_res.append(nums[idx])
                idx += 1 ; tmp_i >>= 1
            ans.append(tmp_res)
        return ans
