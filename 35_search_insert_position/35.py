import bisect

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l

    def searchInsert1(self, nums, target):     
        return bisect.bisect_left(nums,target)

sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 5))
print(sol.searchInsert([1, 3, 5, 6], 2))
print(sol.searchInsert([1, 3, 5, 6], 7))
print(sol.searchInsert([1, 3, 5, 6], 0))


print(sol.searchInsert1([1, 3, 5, 6], 5))
print(sol.searchInsert1([1, 3, 5, 6], 2))
print(sol.searchInsert1([1, 3, 5, 6], 7))
print(sol.searchInsert1([1, 3, 5, 6], 0))
