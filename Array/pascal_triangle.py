class Solution:
    def __method1 (self, numRows):
        ans = [None for i in range(numRows)]
        ans[0] = [1]
        for i in range(1, numRows):
            temp = [1 for k in range(i + 1)]
            for j in range(1, i):
                temp[j] = ans[i - 1][j] + ans[i - 1][j - 1]
            ans[i] = temp
        return ans

    def __method2 (self, numRows):
        ans = [None for i in range(numRows)]
        for i in range(0, numRows):
            temp = [1 for k in range(i + 1)]
            for j in range(1, i + 1):
                temp[j] = temp[j - 1] * (i - j + 1) // j
            ans[i] = temp
        return ans

    def generate (self, numRows: int) -> List[List[int]]:
        return self.__method1(numRows)
        # return self.__method2(numRows)
