from bisect import bisect_left, bisect_right

class Solution:
    def searchRange (self, nums: List[int], target: int) -> List[int]:
        if (not nums): return [-1, -1]
        left_pos, right_pos = -1, -1
        tmp_left_pos = bisect_left(nums, target)
        if ((tmp_left_pos < len(nums)) and (nums[tmp_left_pos] == target)): left_pos = tmp_left_pos
        tmp_right_pos = bisect_right(nums, target)
        if ((tmp_right_pos > 0) and (nums[tmp_right_pos - 1] == target)): right_pos = tmp_right_pos - 1
        return [left_pos, right_pos]
