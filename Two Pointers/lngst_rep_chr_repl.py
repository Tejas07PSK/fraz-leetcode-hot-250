class Solution:
    def characterReplacement (self, s: str, k: int) -> int:
        ch_map = [0 for i in range(26)]
        i, max_freq, ans = 0, 0, 0
        for j in range(len(s)):
            ch_idx = ord(s[j]) - ord('A')
            ch_map[ch_idx] += 1
            max_freq = max(max_freq, ch_map[ch_idx])
            while (j - i + 1 - max_freq > k):
                ch_map[ord(s[i]) - ord('A')] -= 1
                max_freq = max(ch_map)
                i += 1
            ans = max(ans, j - i + 1)
        return ans
