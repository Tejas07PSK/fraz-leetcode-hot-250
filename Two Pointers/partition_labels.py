class Solution:
    def partitionLabels (self, s: str) -> List[int]:
        ch_last = [-1 for i in range(26)]
        for i in range(len(s)): ch_last[ord(s[i]) - ord('a')] = i
        j, ans, last_i = 0, [], 0
        for i in range(len(s)):
            j = max(j, ch_last[ord(s[i]) - ord('a')])
            if (j == i):
                ans.append(i - last_i + 1)
                last_i = i + 1
        return ans
