from math import inf
from collections import deque

class Solution:
    def __method1 (self, i, amount, coins):
        if (amount == 0): return 0
        if (self.dp[i][amount] != None): return self.dp[i][amount]
        self.dp[i][amount] = inf
        if (i == (len(coins) - 1)):
            if ((amount % coins[i]) == 0): self.dp[i][amount] = (amount // coins[i])
            return self.dp[i][amount]
        if ((amount - coins[i]) >= 0):
            self.dp[i][amount] = min(self.dp[i][amount], 1 + self.__method1(i, amount - coins[i], coins))
        self.dp[i][amount] = min(self.dp[i][amount], self.__method1(i + 1, amount, coins))
        return self.dp[i][amount]

    def __method1_handler (self, coins, amount):
        self.dp = [[None for j in range(amount + 1)] for i in range(len(coins))]
        res = self.__method1(0, amount, coins)
        return res if (res != inf) else -1

    def __method2 (self, coins, amount):
        dp = [[inf for j in range(amount + 1)] for i in range(len(coins))]
        for i in range(len(coins) - 1, -1, -1):
            dp[i][0] = 0
            for j in range(1, amount + 1):
                dp[i][j] = inf
                if (i == (len(coins) - 1)):
                    if ((j % coins[i]) == 0): dp[i][j] = (j // coins[i])
                    continue
                if ((j - coins[i]) >= 0):
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - coins[i]])
                dp[i][j] = min(dp[i][j], dp[i + 1][j])
        return dp[0][amount] if (dp[0][amount] != inf) else -1

    def __method3 (self, coins, amount):
        dp = [[inf for j in range(amount + 1)] for i in range(2)]
        for i in range(len(coins) - 1, -1, -1):
            dp[0][0] = 0
            for j in range(1, amount + 1):
                dp[0][j] = inf
                if (i == (len(coins) - 1)):
                    if ((j % coins[i]) == 0): dp[0][j] = (j // coins[i])
                    continue
                if ((j - coins[i]) >= 0):
                    dp[0][j] = min(dp[0][j], 1 + dp[0][j - coins[i]])
                dp[0][j] = min(dp[0][j], dp[1][j])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[1][amount] if (dp[1][amount] != inf) else -1

    def __method4 (self, coins, amount):
        q, visited = deque(), set()
        q.append((amount, 0)) ; visited.add(amount)
        while (q):
            curr_amt, curr_nof_coins = q.popleft()
            if (curr_amt == 0): return curr_nof_coins
            for coin in coins:
                next_amt, next_nof_coins = curr_amt - coin, curr_nof_coins + 1
                if ((next_amt >= 0) and (next_amt not in visited)):
                    q.append((next_amt, next_nof_coins)) ; visited.add(next_amt)
        return -1

    def coinChange (self, coins: List[int], amount: int) -> int:
        #return self.__method1_hndler(coins, amount)
        #return self.__method2(coins, amount)
        #return self.__method3(coins, amount)
        return self.__method4(coins, amount)
