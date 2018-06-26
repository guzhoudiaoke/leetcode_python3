class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_min = [0] * len(nums)
        dp_max = [0] * len(nums)

        ans = dp_min[0] = dp_max[0] = nums[0]
        for i in range(1, len(nums)):
            x, y = dp_max[i-1] * nums[i], dp_min[i-1] * nums[i]
            dp_max[i] = max(nums[i], x, y)
            dp_min[i] = min(nums[i], x, y)
            if ans < dp_max[i]:
                ans = dp_max[i]
        return ans

sol = Solution()
print(sol.maxProduct([2, 3, -2, -4]))
print(sol.maxProduct([2, 3, -2, 4]))
print(sol.maxProduct([-2, 0, -1]))

