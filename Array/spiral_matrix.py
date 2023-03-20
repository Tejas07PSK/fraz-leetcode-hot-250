class Solution:
    def spiralOrder (self, matrix: List[List[int]]) -> List[int]:
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        ans, cntr = [None for i in range(len(matrix) * len(matrix[0]))], 0
        while ((row_start <= row_end) and (col_start <= col_end)):
            i = col_start
            while (i <= col_end):
                ans[cntr] = matrix[row_start][i]
                i += 1 ; cntr += 1
            if (cntr == len(ans)): break
            row_start += 1 ; i = row_start
            while (i <= row_end):
                ans[cntr] = matrix[i][col_end]
                i += 1 ; cntr += 1
            if (cntr == len(ans)): break
            col_end -= 1 ; i = col_end
            while (i >= col_start):
                ans[cntr] = matrix[row_end][i]
                i -= 1 ; cntr += 1
            if (cntr == len(ans)): break
            row_end -= 1 ; i = row_end
            while (i >= row_start):
                ans[cntr] = matrix[i][col_start]
                i -= 1 ; cntr += 1
            if (cntr == len(ans)): break
            col_start += 1
        return ans
