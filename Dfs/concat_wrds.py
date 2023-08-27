from collections import deque

class Solution:
    def __dfs_check (self, word, words):
        q, visited = deque([0]), [False for i in range(len(word) + 1)]
        visited[0] = True
        while (q):
            start = q.popleft()
            for end in range(start + 1, len(word) + 1):
                if (word[start:end] in words):
                    if (end == len(word)): return True
                    if (not visited[end]):
                        q.append(end)
                        visited[end] = True
        return False

    def __bfs_check (self, word, words):
        q, visited = deque([0]), [False for i in range(len(word) + 1)]
        visited[0] = True
        while (q):
            start = q.popleft()
            for end in range(start + 1, len(word) + 1):
                if (word[start:end] in words):
                    if (end == len(word)): return True
                    if (not visited[end]):
                        q.append(end)
                        visited[end] = True
        return False

    def findAllConcatenatedWordsInADict (self, words: List[str]) -> List[str]:
        words, res = set(words), []
        for word in words:
            words.remove(word)
            if (self.__bfs_check(word, words)): res.append(word)
            words.add(word)
        return res
