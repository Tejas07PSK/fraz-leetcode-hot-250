class Solution:
    def subarraysWithKDistinct (self, nums: List[int], k: int) -> int:
        start1, start2, ans, hm_win = 0, 0, 0, {}
        for end in range(len(nums)):
            if (nums[end] not in hm_win): hm_win[nums[end]] = 1
            else: hm_win[nums[end]] += 1
            if (len(hm_win) == k + 1):
                del hm_win[nums[start2]]
                start2 += 1
                start1 = start2
            if (len(hm_win) == k):
                while (hm_win[nums[start2]] > 1):
                    hm_win[nums[start2]] -= 1
                    start2 += 1
                ans += start2 - start1 + 1
        return ans
