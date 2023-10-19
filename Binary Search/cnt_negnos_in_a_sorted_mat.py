class Solution:
    def countNegatives (self, grid: List[List[int]]) -> int:
        tot_negs = 0
        for lst in grid:
            if (lst[0] < 0):
                tot_negs += len(lst)
                continue
            if (lst[-1] >= 0): continue
            left, right = 0, len(lst) - 1
            while (left < right):
                mid = left + ((right - left) // 2)
                if (lst[mid] >= 0): left = mid + 1
                else: right = mid
            tot_negs += len(lst) - right
        return tot_negs
