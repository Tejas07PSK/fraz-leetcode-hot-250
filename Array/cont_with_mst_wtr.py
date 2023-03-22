class Solution:
    def maxArea (self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = 0
        while (i < j):
            diff = j - i
            if (height[i] <= height[j]):
                ans = max(ans, (height[i] * diff))
                i += 1
            else:
                ans = max(ans, (height[j] * diff))
                j -= 1
        return ans
