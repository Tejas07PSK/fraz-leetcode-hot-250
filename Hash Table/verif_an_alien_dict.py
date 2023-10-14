class Solution:
    def isAlienSorted (self, words: List[str], order: str) -> bool:
        ch_map = [0 for i in range(26)]
        for i in range(1, 27): ch_map[ord(order[i - 1]) - ord('a')] = i
        for i in range(len(words) - 1):
            j, end = 0, min(len(words[i]), len(words[i + 1]))
            while (j < end):
                val1 = ch_map[ord(words[i][j]) - ord('a')]
                val2 = ch_map[ord(words[i + 1][j]) - ord('a')]
                if (val1 > val2): return False
                elif (val1 < val2):
                    j = len(words[i])
                    break
                j += 1
            if (j < len(words[i])): return False
        return True
