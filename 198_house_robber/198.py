#class Solution:
#    def rob(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        length = len(nums)
#        if length == 0:
#            return 0
#        if length == 1:
#            return nums[0]
#        if length == 2:
#            return nums[0] if nums[0] > nums[1] else nums[1]
#
#        dp = [0] * len(nums)
#        dp[0] = nums[0]
#        dp[1] = nums[1] if nums[1] > nums[0] else nums[0]
#        for i in range(2, len(nums)):
#            dp[i] = dp[i-1]
#            if dp[i-2] + nums[i] > dp[i]:
#                dp[i] = dp[i-2] + nums[i]
#
#        return dp[length - 1]


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1]), 0]
        sum = 0
        for i in range(2, len(nums)):
            sum = dp[0] + nums[i]
            dp[2] = sum if sum > dp[1] else dp[1]
            dp[0] = dp[1]
            dp[1] = dp[2]

        return dp[1]
        
sol = Solution()
print(sol.rob([1, 2, 3, 1]))
print(sol.rob([2, 7, 9, 3, 1]))
print(sol.rob([]))
print(sol.rob([1]))
print(sol.rob([1, 2]))
print(sol.rob([2, 1]))
print(sol.rob([1, 3, 1]))
print(sol.rob([1, 2, 1, 1]))
