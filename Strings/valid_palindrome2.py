class Solution:
    def __isPalindrome (self, i, j, s):
        while (i < j):
            if (s[i] != s[j]): return False
            i += 1 ; j -= 1
        return True

    def validPalindrome (self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while (i < j):
            if (s[i] == s[j]):
                i += 1 ; j -= 1
            else: return self.__isPalindrome(i + 1, j, s) or self.__isPalindrome(i, j - 1, s)
        return True
