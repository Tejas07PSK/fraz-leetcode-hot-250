class Solution:
    def trap (self, height: List[int]) -> int:
        left, left_max = 0, 0
        right, right_max = len(height) - 1, 0
        tot_wat = 0
        while (left < right):
            if (height[left] <= height[right]):
                if (height[left] >= left_max): left_max = height[left]
                else: tot_wat += (left_max - height[left])
                left += 1
            else:
                if (height[right] >= right_max): right_max = height[right]
                else: tot_wat += (right_max - height[right])
                right -= 1
        return tot_wat
