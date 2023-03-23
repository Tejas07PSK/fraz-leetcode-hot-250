class Solution:
    def rotate (self, matrix: List[List[int]]) -> None:
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        while ((row_start < row_end) and (col_start < col_end)):
            for i in range(row_start, row_end):
                matrix[row_start][i], matrix[i][col_end] = matrix[i][col_end], matrix[row_start][i]
            for i in range(col_end, col_start, -1):
                matrix[row_start][col_start + col_end - i], matrix[row_end][i] = matrix[row_end][i], matrix[row_start][col_start + col_end - i]
            for i in range(row_end, row_start, -1):
                matrix[row_start][col_start + row_end - i], matrix[i][col_start] = matrix[i][col_start], matrix[row_start][col_start + row_end - i]
            row_start += 1 ; row_end -= 1
            col_start += 1 ; col_end -= 1
