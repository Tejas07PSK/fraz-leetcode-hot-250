class Solution:
    def __helper (self, idx, digits, temp_res):
        if (idx == len(digits)):
            self.res.append("".join(temp_res))
            return
        for ch in self.keypad[int(digits[idx])]:
            temp_res.append(ch)
            self.__helper(idx + 1, digits, temp_res)
            temp_res.pop()

    def letterCombinations (self, digits: str) -> List[str]:
        if (len(digits) == 0): return ""
        self.keypad = [
            [' '],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]
        self.res = []
        self.__helper(0, digits, [])
        return self.res
