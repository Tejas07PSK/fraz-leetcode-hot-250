class Solution:
    def shortestSubarray (self, nums: List[int], k: int) -> int:
        res, curr = len(nums) + 1, 0
        dq = deque([(0, 0)])
        for i in range(len(nums)):
            curr += nums[i]
            while (dq and ((curr - dq[0][1]) >= k)): res = min(res, (i - dq.popleft()[0] + 1))
            while (dq and (curr <= dq[-1][1])): dq.pop()
            dq.append((i + 1, curr))
        return res if (res <= len(nums)) else -1
