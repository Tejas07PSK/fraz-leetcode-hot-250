from collections import defaultdict

class Solution:
    def findSubstring (self, s: str, words: List[str]) -> List[int]:
        words_map, fixed_len, ans = defaultdict(int), len(words[0]), []
        fixed_win_start, fixed_win_end = 0, (len(words) * fixed_len) - 1
        for word in words: words_map[word] += 1
        while (fixed_win_end < len(s)):
            curr_map = defaultdict(int)
            i = fixed_win_start
            while ((i + fixed_len - 1) <= fixed_win_end):
                curr_word = s[i:i + fixed_len]
                if (curr_word in words_map):
                    if ((curr_map[curr_word] + 1) > words_map[curr_word]): break
                    curr_map[curr_word] += 1
                else: break
                i += fixed_len
            if ((i - 1) == fixed_win_end): ans.append(fixed_win_start)
            fixed_win_end += 1
            fixed_win_start += 1
            del curr_map
        return ans
