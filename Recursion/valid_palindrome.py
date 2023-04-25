class Solution:
    def __method2 (self, i, j, s):
        while (i < j):
            while ((i < j) and (not s[i].isalnum())): i += 1
            while ((j > i) and (not s[j].isalnum())): j -= 1
            if (i == j): break
            if (s[i].lower() != s[j].lower()): return False
            i += 1 ; j -= 1
        return True

    def __method1 (self, i, j, s):
        while ((i < j) and (not s[i].isalnum())): i += 1
        while ((j > i) and (not s[j].isalnum())): j -= 1
        if (i == j): return True
        if (s[i].lower() == s[j].lower()):
            i += 1 ; j -= 1
            if (i < j): return self.__method1(i, j, s)
            return True
        return False

    def isPalindrome (self, s: str) -> bool:
        return self.__method1(0, len(s) - 1, s)
        #return self.__method2(0, len(s) - 1, s)
