class Solution:
    def __method1 (self, i, j, nums1, nums2):
        if ((i == len(nums1)) or (j == len(nums2))): return 0
        if (self.dp[i][j] != None): return self.dp[i][j]
        self.__method1(i + 1, j, nums1, nums2)
        self.__method1(i, j + 1, nums1, nums2)
        self.dp[i][j] = 0
        if (nums1[i] == nums2[j]): self.dp[i][j] = 1 + self.__method1(i + 1, j + 1, nums1, nums2)
        self.ans = max(self.ans, self.dp[i][j])
        return self.dp[i][j]

    def __method1_handler (self, nums1, nums2):
        self.dp = [[None for j in range(len(nums2))] for i in range(len(nums1))]
        self.ans = 0
        self.__method1(0, 0, nums1, nums2)
        return self.ans

    def __method2 (self, nums1, nums2):
        self.dp = [[0 for j in range(len(nums2) + 1)] for i in range(len(nums1) + 1)]
        self.ans = 0
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if (nums1[i] == nums2[j]):
                    self.dp[i][j] = 1 + self.dp[i + 1][j + 1]
                self.ans = max(self.ans, self.dp[i][j])
        return self.ans

    def __method3 (self, nums1, nums2):
        self.dp = [[0 for j in range(len(nums2) + 1)] for i in range(2)]
        self.ans = 0
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                self.dp[0][j] = 0
                if (nums1[i] == nums2[j]):
                    self.dp[0][j] = 1 + self.dp[1][j + 1]
                self.ans = max(self.ans, self.dp[0][j])
            self.dp[0], self.dp[1] = self.dp[1], self.dp[0]
        return self.ans

    def __check (self, mid, nums1, nums2):
        base, mod, pwr = 101, 1000000007, 1
        roll_hash1, roll_hash2 = 0, 0
        for i in range(mid - 1, -1, -1):
            roll_hash1 = (roll_hash1 + ((nums1[i] * pwr) % mod)) % mod
            roll_hash2 = (roll_hash2 + ((nums2[i] * pwr) % mod)) % mod
            if (i != 0): pwr = (pwr * base) % mod
        if (roll_hash2 == roll_hash1): return True
        hash_set_1 = set() ; hash_set_1.add(roll_hash1)
        i = 0
        for j in range(mid, len(nums1)):
            roll_hash1 = ((((roll_hash1 - ((nums1[i] * pwr) % mod)) * base) % mod) + nums1[j]) % mod
            hash_set_1.add(roll_hash1) ; i += 1
        if (roll_hash2 in hash_set_1): return True
        i = 0
        for j in range(mid, len(nums2)):
            roll_hash2 = ((((roll_hash2 - ((nums2[i] * pwr) % mod)) * base) % mod) + nums2[j]) % mod
            if (roll_hash2 in hash_set_1): return True
            i += 1
        return False

    def __method4 (self, nums1, nums2):
        if (len(nums2) < len(nums1)): nums1, nums2 = nums2, nums1
        low, high = 1, len(nums1)
        ans = 0
        while (low <= high):
            mid = low + ((high - low) // 2)
            check = self.__check(mid, nums1, nums2)
            if (check):
                ans = max(ans, mid)
                low = mid + 1
            else: high = mid - 1
        return ans

    def findLength (self, nums1: List[int], nums2: List[int]) -> int:
        #return self.__method1_handler(nums1, nums2)
        #return self.__method2(nums1, nums2)
        #return self.__method3(nums1, nums2)
        return self.__method4(nums1, nums2)
