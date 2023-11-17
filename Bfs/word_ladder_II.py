from collections import deque

class Solution:
    def __dfs_helper (self, curr_word, target_word, path, adj_lst, res):
        for next_word in adj_lst[curr_word]:
            path.appendleft(next_word)
            if (next_word == target_word): res.append(list(path))
            else: self.__dfs_helper(next_word, target_word, path, adj_lst, res)
            path.popleft()

    def findLadders (self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        mx_lvl, adj_lst, wordList = 0, {}, set(wordList)
        if (endWord not in wordList): return []
        q, visited, found = deque([beginWord]), {beginWord : 0}, False
        while (q):
            curr_sz = len(q)
            while (curr_sz > 0):
                curr_word = q.popleft()
                curr_word_lst = list(curr_word)
                for i in range(len(curr_word_lst)):
                    orig_chr = curr_word_lst[i]
                    for ch in map(chr, range(ord('a'), ord('z') + 1)):
                        if (ch != orig_chr):
                            curr_word_lst[i] = ch
                            next_word = "".join(curr_word_lst)
                            if (next_word in wordList):
                                if (next_word not in visited):
                                    if (next_word == endWord): found = True
                                    q.append(next_word)
                                    visited[next_word] = mx_lvl + 1
                                    adj_lst[next_word] = [curr_word]
                                elif (visited[next_word] == mx_lvl + 1): adj_lst[next_word].append(curr_word)
                    curr_word_lst[i] = orig_chr
                curr_sz -= 1
            mx_lvl += 1
            if (found): break
        res = []
        if (not found): return res
        self.__dfs_helper(endWord, beginWord, deque([endWord]), adj_lst, res)
        return res
