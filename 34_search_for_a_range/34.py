class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower = self.lowerBound(nums, target)
        ans = [-1, -1]
        if lower >= 0 and lower < len(nums) and nums[lower] == target:
            upper = self.upperBound(nums, target)
            ans = [lower, upper-1]
        return ans

    def lowerBound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l

    def upperBound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        return l

sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))
