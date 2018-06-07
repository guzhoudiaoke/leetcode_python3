#class Solution:
#    def moveZeroes(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: void Do not return anything, modify nums in-place instead.
#        """
#        length = len(nums)
#        if length <= 1:
#            return nums
#
#        left, right = 0, 0
#        while left < length and right < length:
#            while left < length and nums[left] != 0:
#                left += 1
#
#            if right < left:
#                right = left
#            while right < length and nums[right] == 0:
#                right += 1
#
#            if left < right and right < length:
#                nums[left] = nums[right]
#                nums[right] = 0
#
#        return nums
        
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

sol = Solution()

nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)

nums = [0, 0, 0, 3, 12, 0, 0, 44, 122]
sol.moveZeroes(nums)
print(nums)

nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
sol.moveZeroes(nums)
print(nums)

nums = []
sol.moveZeroes(nums)
print(nums)

nums = [0]
sol.moveZeroes(nums)
print(nums)

nums = [1]
sol.moveZeroes(nums)
print(nums)

nums = [1, 0]
sol.moveZeroes(nums)
print(nums)

nums = [0, 1]
sol.moveZeroes(nums)
print(nums)
