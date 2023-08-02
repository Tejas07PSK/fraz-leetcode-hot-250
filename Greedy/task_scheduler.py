class Solution:
    def leastInterval (self, tasks: List[str], n: int) -> int:
        chr_map = [0 for i in range(26)]
        mx_freq, mx_freq_cnt = 0, 0
        for ch in tasks:
            chr_map[ord(ch) - ord('A')] += 1
            if (mx_freq == chr_map[ord(ch) - ord('A')]): mx_freq_cnt += 1
            elif (mx_freq < chr_map[ord(ch) - ord('A')]):
                mx_freq = chr_map[ord(ch) - ord('A')]
                mx_freq_cnt = 1
        gaps = mx_freq - 1
        gaps_len = n - (mx_freq_cnt - 1)
        slots_left = gaps * gaps_len
        tasks_left = len(tasks) - (mx_freq * mx_freq_cnt)
        idles = max(0, slots_left - tasks_left)
        return len(tasks) + idles
