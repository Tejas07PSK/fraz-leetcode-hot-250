class Solution:
    def __method1 (self, matrix, target):
        row_left, row_right = 0, len(matrix) - 1
        while (row_left <= row_right):
            row_mid = row_left + ((row_right - row_left) // 2)
            if (target < matrix[row_mid][0]): row_right = row_mid - 1
            elif (target > matrix[row_mid][-1]): row_left = row_mid + 1
            else:
                col_left, col_right = 0, len(matrix[0]) - 1
                while (col_left <= col_right):
                    col_mid = col_left + ((col_right - col_left) // 2)
                    if (target == matrix[row_mid][col_mid]): return True
                    elif (target > matrix[row_mid][col_mid]): col_left = col_mid + 1
                    else: col_right = col_mid - 1
                return False
        return False

    def __method2 (self, matrix, target):
        left, right = 0, (len(matrix) * len(matrix[0])) - 1
        while (left <= right):
            mid = left + ((right - left) // 2)
            if (target < matrix[mid // len(matrix[0])][mid % len(matrix[0])]): right = mid - 1
            elif (target > matrix[mid // len(matrix[0])][mid % len(matrix[0])]): left = mid + 1
            else: return True
        return False

    def searchMatrix (self, matrix: List[List[int]], target: int) -> bool:
        #return self.__method1(matrix, target)
        return self.__method2(matrix, target)
