class Solution:
    def __digitSqSum (self, num):
        s = 0
        while (num > 0):
            s += ((num % 10) ** 2)
            num //= 10
        return s

    def isHappy (self, n: int) -> bool:
        slow, fast = n, n
        while (True):
            slow = self.__digitSqSum(slow)
            fast = self.__digitSqSum(self.__digitSqSum(fast))
            if (slow == fast): break
        return slow == 1
