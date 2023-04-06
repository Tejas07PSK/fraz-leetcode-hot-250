class Solution:
    def maxArea (self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_height, prev_hor_cut = 0, 0
        for cur_hor_cut in horizontalCuts:
            max_height = max(max_height, (cur_hor_cut - prev_hor_cut))
            prev_hor_cut = cur_hor_cut
        max_height = max(max_height, (h - prev_hor_cut))
        max_length, prev_vert_cut = 0, 0
        for cur_vert_cut in verticalCuts:
            max_length = max(max_length, (cur_vert_cut - prev_vert_cut))
            prev_vert_cut = cur_vert_cut
        max_length = max(max_length, (w - prev_vert_cut))
        return (max_height * max_length) % 1000000007
