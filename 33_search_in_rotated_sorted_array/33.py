class Solution:
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


sol = Solution()

nums = [4, 5, 6, 7, 0, 1, 2]
print(sol.search(nums, 4))
print(sol.search(nums, 5))
print(sol.search(nums, 6))
print(sol.search(nums, 7))
print(sol.search(nums, 8))
print(sol.search(nums, 9))
print(sol.search(nums, 3))
print(sol.search(nums, 2))
print(sol.search(nums, 1))
print(sol.search(nums, 0))
print(sol.search(nums, -1))
print(sol.search(nums, -2))
