class Solution:
    def __method1 (self, i, bits_arr):
        if (self.dp[i] != None): return self.dp[i]
        self.dp[i] = [bits_arr[i][0], bits_arr[i][1]]
        curr_bitmask, curr_str_len = bits_arr[i][0], bits_arr[i][1]
        for j in range(i + 1, len(bits_arr)):
            if ((curr_bitmask & bits_arr[j][0]) == 0):
                if ((curr_str_len + bits_arr[j][1]) > self.dp[i][1]):
                    self.dp[i][0] = (curr_bitmask | bits_arr[j][0])
                    self.dp[i][1] = curr_str_len + bits_arr[j][1]
                curr_bitmask |= bits_arr[j][0]
                curr_str_len += bits_arr[j][1]
            next_bitmask, next_str_len = self.__method1(j, bits_arr)
            if (next_str_len > self.dp[i][1]):
                self.dp[i][0] = next_bitmask
                self.dp[i][1] = next_str_len
            if ((bits_arr[i][0] & next_bitmask) == 0):
                if ((next_str_len + bits_arr[i][1]) > self.dp[i][1]):
                    self.dp[i][0] = (bits_arr[i][0] | next_bitmask)
                    self.dp[i][1] = next_str_len + bits_arr[i][1]
        return self.dp[i]

    def __method2 (self, bits_arr):
        for i in range(len(bits_arr) - 1, -1, -1):
            self.dp[i] = [bits_arr[i][0], bits_arr[i][1]]
            curr_bitmask, curr_str_len = bits_arr[i][0], bits_arr[i][1]
            for j in range(i + 1, len(bits_arr)):
                if ((curr_bitmask & bits_arr[j][0]) == 0):
                    if ((curr_str_len + bits_arr[j][1]) > self.dp[i][1]):
                        self.dp[i][0] = (curr_bitmask | bits_arr[j][0])
                        self.dp[i][1] = curr_str_len + bits_arr[j][1]
                    curr_bitmask |= bits_arr[j][0]
                    curr_str_len += bits_arr[j][1]
                next_bitmask, next_str_len = self.dp[j]
                if (next_str_len > self.dp[i][1]):
                    self.dp[i][0] = next_bitmask
                    self.dp[i][1] = next_str_len
                if ((bits_arr[i][0] & next_bitmask) == 0):
                    if ((next_str_len + bits_arr[i][1]) > self.dp[i][1]):
                        self.dp[i][0] = (bits_arr[i][0] | next_bitmask)
                        self.dp[i][1] = next_str_len + bits_arr[i][1]
        return self.dp[0][1]

    def maxLength (self, arr: List[str]) -> int:
        new_arr = []
        for i in range(len(arr)):
            mask, flag = 0, True
            for ch in arr[i]:
                fltr = 1 << (ord(ch) - 97)
                if ((mask & fltr) > 0):
                    flag = False
                    break
                mask |= fltr
            if (flag): new_arr.append([mask, len(arr[i])])
        if (len(new_arr) == 0): return 0
        self.res, self.dp = 0, [None for i in range(len(new_arr))]
        return self.__method1(0, new_arr)[1]
        #return self.__method2(new_arr)
