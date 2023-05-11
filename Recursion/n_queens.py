bitmask_filters = [(1 << i) for i in range(17)]
queen_present_90deg, queen_present_45deg, queen_present_135deg = 0, 0, 0 

class Solution:
    def __queen_placer (self, row, n):
        global queen_present_90deg, queen_present_45deg, queen_present_135deg, bitmask_filters
        if (row == n):
            self.res.append([("".join(self.board_state[i])) for i in range(n)])
            return
        for col in range(n):
            mask_45deg = bitmask_filters[row + col]
            mask_135deg = bitmask_filters[col - row + n - 1]
            mask_90deg = bitmask_filters[col]
            cond = (
                ((queen_present_90deg & mask_90deg) == 0) and
                ((queen_present_45deg & mask_45deg) == 0) and
                ((queen_present_135deg & mask_135deg) == 0)
            )
            if (cond):
                self.board_state[row][col] = 'Q'
                queen_present_90deg |= mask_90deg
                queen_present_45deg |= mask_45deg
                queen_present_135deg |= mask_135deg
                self.__queen_placer(row + 1, n)
                queen_present_90deg ^= mask_90deg
                queen_present_45deg ^= mask_45deg
                queen_present_135deg ^= mask_135deg
                self.board_state[row][col] = '.'

    def solveNQueens (self, n: int) -> List[List[str]]:
        self.board_state, self.res = [['.' for j in range(n)] for i in range(n)], []
        self.__queen_placer(0, n) ; return self.res
