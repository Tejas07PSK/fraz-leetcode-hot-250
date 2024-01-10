class Solution:
    def __is_palin (self, start, end, string):
        while (start < end):
            if (string[start] != string[end]): return False
            start += 1 ; end -= 1
        return True

    def __helper (self, start, string, curr_path):
        if (start == len(string)):
            self.final_res.append(list(curr_path))
            return
        for end in range(start, len(string)):
            if (self.__is_palin(start, end, string)):
                curr_path.append(string[start:end+1])
                self.__helper(end + 1, string, curr_path)
                curr_path.pop()

    def partition (self, s: str) -> List[List[str]]:
        self.final_res = []
        self.__helper(0, s, deque())
        return self.final_res
