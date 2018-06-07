import sys

class Solution:
    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        for i in range(amount+1):
            for c in coins:
                if i >= c and dp[i-c] >= 0 and dp[i-c] + 1 < dp[i]:
                    dp[i] = 1 + dp[i-c]

        return -1 if dp[amount] == sys.maxsize else dp[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def dfs(current, index, target):
            if target == 0:
                if current < self.ans:
                    self.ans = current

            if current >= self.ans:
                return

            for i in range(index, len(coins)):
                if coins[i] <= target and coins[i] * (self.ans-current) >= target:
                    dfs(current+1, i, target-coins[i])

        coins = sorted(coins, reverse=True)
        self.ans = sys.maxsize
        dfs(0, 0, amount)
        return -1 if self.ans == sys.maxsize else self.ans

        
sol = Solution()

coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount))

coins = [2, 5, 10, 1]
amount = 27
print(sol.coinChange(coins, amount))
