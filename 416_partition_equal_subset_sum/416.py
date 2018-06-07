class Solution(object):
    def canPartition_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_all = sum(nums)
        if sum_all & 1 != 0:
            return False

        target = sum_all // 2
        dp = [False] * (target+1)
        dp[0] = True

        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] = dp[i] or dp[i-n]
                if dp[target]:
                    return True
        return dp[target]


    def canPartition_dfs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(current, index):
            if current == target:
                return True

            for i in range(index, length):
                if current+nums[index] <= target and dfs(current+nums[index], i+1):
                    return True

            return False

        sum_all = sum(nums)
        if sum_all & 1 != 0:
            return False

        target = sum_all // 2
        length = len(nums)

        return dfs(0, 0)


    def canPartition_dfs1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(current, index):
            if current == target:
                return True

            for i in range(index, length):
                if current+nums[index] <= target and dfs(current+nums[index], i+1):
                    return True

            return False

        sum_all = sum(nums)
        if sum_all & 1 != 0:
            return False

        target = sum_all >> 1
        length = len(nums)

        nums.sort(reverse = True)
        if nums[0] > target:
            return False

        return dfs(0, 0)


    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(current, index):
            for i in range(index, length):
                if current == nums[i]:
                    return True
                if current > nums[index] and dfs(current-nums[index], i+1):
                    return True

            return False

        sum_all = sum(nums)
        if sum_all & 1 != 0:
            return False

        target = sum_all >> 1
        length = len(nums)

        nums.sort(reverse = True)
        if nums[0] > target:
            return False

        return dfs(target, 0)

        
sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))
print(sol.canPartition([1, 2, 3, 5]))
print(sol.canPartition([1, 1, 1, 1]))
