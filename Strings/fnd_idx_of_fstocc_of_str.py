class Solution:
    def __constructLPSArr (self, pattern):
        lps = [0 for ch in pattern]
        i, j, n = 0, 1, len(pattern)
        while (j < n):
            if (pattern[i] == pattern[j]):
                i += 1
                lps[j] = i
                j += 1
            else:
                if (i == 0): j += 1
                else: i = lps[i - 1]
        return lps

    def __kmp (self, text, pattern):
        m, n = len(text), len(pattern)
        i, j, lps = 0, 0, self.__constructLPSArr(pattern)
        while (i < m):
            if (text[i] == pattern[j]):
                i += 1 ; j += 1
            else:
                if (j == 0): i += 1
                else: j = lps[j - 1]
            if (j == n):
                return (i - j)
                # j = lps[j - 1]
        return -1

    def __rabin_karp (self, text, pattern):
        m, n = len(text), len(pattern)
        if (m < n): return -1
        mod, base, pwr = 101, 26, 1
        text_hash, pattern_hash = 0, 0
        for i in range(n - 1): pwr = (pwr * base) % mod
        for i in range(n):
            pattern_hash = ((base * pattern_hash) + ord(pattern[i])) % mod
            text_hash = ((base * text_hash) + ord(text[i])) % mod
        text_win_start, text_win_end = 0, n - 1
        while (text_win_end < m):
            if (text_hash == pattern_hash):
                i = 0
                while ((i < n) and (text[text_win_start + i] == pattern[i])): i += 1
                if (i == n): return text_win_start
            text_win_end += 1
            if (text_win_end < m):
                text_hash = (((text_hash - (ord(text[text_win_start]) * pwr)) * base) + ord(text[text_win_end])) % mod
            text_win_start += 1
        return -1

    def strStr (self, haystack: str, needle: str) -> int:
        #return self.__kmp(haystack, needle)
        return self.__rabin_karp(haystack, needle)
