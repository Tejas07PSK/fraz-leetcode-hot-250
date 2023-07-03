from collections import deque

class Solution:
    def __reverse (self, i, j, ch_arr):
        while (i < j):
            ch_arr[i], ch_arr[j] = ch_arr[j], ch_arr[i]
            i += 1 ; j -= 1

    def __method1 (self, s):
        i, res = 0, deque()
        while (i < len(s)):
            if (s[i] == ' '):
                while (((i + 1) < len(s)) and (s[i + 1] == s[i])): i += 1
            else:
                temp_ch_arr = [s[i]]
                while (((i + 1) < len(s)) and (s[i + 1] != ' ')):
                    temp_ch_arr.append(s[i + 1])
                    i += 1
                res.appendleft(''.join(temp_ch_arr))
            i += 1
        return ' '.join(res)

    def __method2 (self, s):
        res = list(reversed(s))
        i, space_start, word_end = 0, 0, 0
        while (i < len(res)):
            while ((i < len(res)) and (res[i] == ' ')): i += 1
            if (i == len(res)): break
            word_start, word_end = space_start, space_start
            while ((i < len(res)) and (res[i] != ' ')):
                if (i == word_end):
                    i += 1 ; word_end += 1
                    continue
                res[word_end] = res[i]
                res[i] = ' '
                i += 1 ; word_end += 1
            self.__reverse(word_start, word_end - 1, res)
            space_start = word_end + 1
            i = space_start
        return "".join(res[:word_end])

    def reverseWords (self, s: str) -> str:
        #return self.__method1(s)
        return self.__method2(s)
