class Solution:
    def longestArithSeqLength (self, nums: List[int]) -> int:
        dp, ans = {}, 0
        for i in range(len(nums) - 1, -1, -1):
            dp[(i, 0)] = 1
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if ((i, diff) not in dp): dp[(i, diff)] = 0
                dp[(i, diff)] = max(dp[(i, diff)], dp.get((j, diff), 1) + 1)
                ans = max(ans, dp[(i, diff)])
        return ans
