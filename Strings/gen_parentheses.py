class Solution:
    def __method1 (self, n):
        res = [['']]
        for i in range(1, n + 1):
            tmp_lst = []
            for k in range(i):
                first_lst = res[k]
                second_lst = res[i - k - 1]
                for par_string1 in first_lst:
                    for par_string2 in second_lst:
                        tmp_lst.append("({}){}".format(par_string1, par_string2))
            res.append(tmp_lst)
        return res[-1]

    def __method2 (self, string, left, right):
        if (left == right == 0):
            self.res.append(string)
            return
        if (left > 0): self.__method2(string + '(', left - 1, right)
        if (right > left): self.__method2(string + ')', left, right - 1)

    def generateParenthesis (self, n: int) -> List[str]:
        #return self.__method1(n)
        self.res = []
        self.__method2("", n, n)
        return self.res
