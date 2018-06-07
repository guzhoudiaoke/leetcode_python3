class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if total < S or (total + S) % 2 != 0:
            return 0

        target = (total + S) >> 1
        dp = [0] * (target+1)
        dp[0] = 1

        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] += dp[i-n]

        return dp[target]

sol = Solution()
print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(sol.findTargetSumWays([1, 1, 1, 1, 1, 2, 3, 4], 7))
print(sol.findTargetSumWays([1, 1, 1, 1, 2, 3, 4], 7))
