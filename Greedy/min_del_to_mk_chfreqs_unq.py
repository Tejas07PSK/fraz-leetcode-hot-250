class Solution:
    def minDeletions (self, s: str) -> int:
        chrs = [0 for i in range(26)]
        for ch in s: chrs[ord(ch) - ord('a')] += 1
        seen, dels = set(), 0
        for i in range(26):
            while ((chrs[i] > 0) and (chrs[i] in seen)):
                chrs[i] -= 1
                dels += 1
            if (chrs[i] > 0): seen.add(chrs[i])
        return dels 
