class Solution:
    def __helper (self, i, digits, temp_res):
        if (i == len(digits)):
            self.result.append("".join(temp_res))
            return
        for ch in self.keypad[digits[i]]:
            temp_res.append(ch)
            self.__helper(i + 1, digits, temp_res)
            temp_res.pop()

    def letterCombinations (self, digits: str) -> List[str]:
        if (digits == ""): return []
        self.keypad, self.result = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz" 
        }, []
        self.__helper(0, digits, [])
        return self.result
