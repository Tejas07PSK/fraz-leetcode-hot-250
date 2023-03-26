class Solution:
    def numPairsDivisibleBy60 (self, time: List[int]) -> int:
        seen_before, ans = {}, 0
        for i in range(len(time)):
            rem = time[i] % 60
            if (rem != 0): rem = 60 - rem
            if (rem in seen_before): ans += seen_before[rem]
            rem = time[i] % 60
            if (rem not in seen_before): seen_before[rem] = 0
            seen_before[rem] += 1
        return ans
