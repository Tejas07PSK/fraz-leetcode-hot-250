from collections import deque

class Solution:
    def ladderLength (self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wrd_lst = set(wordList) ; wrd_lst.add(beginWord)
        if (endWord not in wrd_lst): return 0
        q, visited = deque([(list(endWord), 1)]), set([endWord])
        while (q):
            curr_word_lst, curr_jumps = q.popleft()
            if ("".join(curr_word_lst) == beginWord): return curr_jumps
            for i in range(len(curr_word_lst)):
                old_chr = curr_word_lst[i]
                for ch in map(chr, range(ord('a'), ord('z') + 1)):
                    curr_word_lst[i] = ch
                    next_word, next_jumps = "".join(curr_word_lst), curr_jumps + 1
                    if ((next_word not in visited) and (next_word in wrd_lst)):
                        q.append((list(next_word), next_jumps))
                        visited.add(next_word)
                curr_word_lst[i] = old_chr
        return 0
