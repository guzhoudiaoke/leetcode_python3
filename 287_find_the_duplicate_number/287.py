class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast, t = slow, slow
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        while t != slow:
            t = nums[t]
            slow = nums[slow]

        return t

sol = Solution()

nums = [1, 3, 4, 2, 2]
print(sol.findDuplicate(nums))

nums = [3, 1, 3, 4, 2]
print(sol.findDuplicate(nums))
