from collections import deque

class Solution:
    def __largestRectangleAreaInHistogramHelper (self, heights):
        stk, ans = deque(), 0
        for height in heights:
            curr_combo_height_width = [0, 0]
            while ((stk) and (height <= stk[-1][0])):
                temp_combo_height_width = stk.pop()
                curr_combo_height_width[0] = temp_combo_height_width[0]
                curr_combo_height_width[1] += temp_combo_height_width[1]
                ans = max(ans, (curr_combo_height_width[0] * curr_combo_height_width[1]))
            curr_combo_height_width[0] = height
            curr_combo_height_width[1] += 1
            ans = max(ans, (curr_combo_height_width[0] * curr_combo_height_width[1]))
            stk.append(curr_combo_height_width)
        curr_combo_height_width = stk.pop()
        while (stk):
            temp_combo_height_width = stk.pop()
            curr_combo_height_width[0] = temp_combo_height_width[0]
            curr_combo_height_width[1] += temp_combo_height_width[1]
            ans = max(ans, (curr_combo_height_width[0] * curr_combo_height_width[1]))
        return ans

    def maximalRectangle (self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix[0])): matrix[0][i] = int(matrix[0][i])
        ans = max(0, self.__largestRectangleAreaInHistogramHelper(matrix[0]))
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] != '0'): matrix[i][j] = int(matrix[i][j]) + matrix[i - 1][j]
                else: matrix[i][j] = int(matrix[i][j])
            ans = max(ans, self.__largestRectangleAreaInHistogramHelper(matrix[i]))
        return ans
