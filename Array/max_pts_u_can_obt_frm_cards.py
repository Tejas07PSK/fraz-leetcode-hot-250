class Solution:
    def maxScore (self, cardPoints: List[int], k: int) -> int:
        ans, curr_sum = 0, 0
        for i in range(k): curr_sum += cardPoints[i]
        if (k == len(cardPoints)): return curr_sum
        ans = curr_sum
        end = len(cardPoints) - 1
        while (k > 0):
            k -= 1
            curr_sum -= cardPoints[k]
            curr_sum += cardPoints[end]
            ans = max(ans, curr_sum)
            end -= 1
        return ans
