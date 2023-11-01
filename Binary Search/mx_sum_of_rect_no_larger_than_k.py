from bisect import bisect_left, insort
from math import inf

class Solution:
    def maxSumSubmatrix (self, matrix: List[List[int]], k: int) -> int:
        ans, row, col = -inf, len(matrix), len(matrix[0])
        for col_start in range(col):
            temp_arr = [0 for i in range(row)]
            for col_end in range(col_start, col):
                curr_sum, srtd_prefix_sums_lst = 0, [0]
                for row_idx in range(row):
                    temp_arr[row_idx] += matrix[row_idx][col_end]
                    curr_sum += temp_arr[row_idx]
                    idx = bisect_left(srtd_prefix_sums_lst, curr_sum - k)
                    if (idx != len(srtd_prefix_sums_lst)): ans = max(ans, curr_sum - srtd_prefix_sums_lst[idx])
                    insort(srtd_prefix_sums_lst, curr_sum)
        return ans
