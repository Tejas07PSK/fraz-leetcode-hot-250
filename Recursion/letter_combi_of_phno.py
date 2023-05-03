class Solution:
    def __letterCombinationsHelper (self, i, digits, temp_res):
        for ch in self.keypad[digits[i]]:
            temp_res.append(ch)
            if (i == (len(digits) - 1)): self.res.append("".join(temp_res))
            else: self.__letterCombinationsHelper(i + 1, digits, temp_res)
            temp_res.pop()

    def letterCombinations (self, digits: str) -> List[str]:
        if (digits == ""): return []
        self.keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.res = []
        self.__letterCombinationsHelper(0, digits, [])
        return self.res
