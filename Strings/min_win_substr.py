from collections import defaultdict

class Solution:
    def minWindow (self, s: str, t: str) -> str:
        table, current_win = defaultdict(int), defaultdict(int)
        for ch in t: table[ch] += 1
        all_present, table_size, current_win_size, n = 0, len(table), 0, len(t)
        i, j, min_i, min_j, min_win_sz = 0, 0, 0, 0, len(s) + 1
        while (j < len(s)):
            if (s[j] in table):
                current_win[s[j]] += 1
                if (current_win[s[j]] == table[s[j]]): all_present += 1
                current_win_size += 1
            while ((all_present == table_size) and (current_win_size >= len(t))):
                if ((j - i + 1) < min_win_sz): min_i, min_j, min_win_sz = i, j, (j - i + 1)
                if (s[i] in table):
                    if (current_win[s[i]] == table[s[i]]): all_present -= 1
                    current_win[s[i]] -= 1
                    current_win_size -= 1
                i += 1
            j += 1
        return s[min_i:min_j + 1] if (min_win_sz != (len(s) + 1)) else ""
