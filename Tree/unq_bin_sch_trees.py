class Solution:
    def __bino_coeff (self, n, k):
        if (k > (n - k)): k = n - k
        ans = 1
        for i in range(k):
            ans *= (n - i)
            ans /= (i + 1)
        return ans

    def numTrees (self, n: int) -> int:
        c = self.__bino_coeff((2 * n), n)
        c /= (n + 1)
        return int(c)
