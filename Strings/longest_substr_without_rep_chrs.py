class Solution:
    def lengthOfLongestSubstring (self, s: str) -> int:
        i, j, ans = 0, 0, 0
        seen_before = [-1 for i in range(129)]
        while (j < len(s)):
            ch_int = ord(s[j])
            if (seen_before[ch_int] >= i): i = seen_before[ch_int] + 1
            seen_before[ch_int] = j
            ans = max(ans, (j - i + 1))
            j += 1
        return ans
