#class Solution:
#    def findDisappearedNumbers(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: List[int]
#        """
#        for i in range(len(nums)):
#            if nums[i] != i+1:
#                x = nums[i]
#                while nums[x-1] != x:
#                    y = nums[x-1]
#                    nums[x-1] = x
#                    x = y
#
#        ans = []
#        for i in range(len(nums)):
#            if nums[i] != i+1:
#                ans.append(i+1)
#
#        return ans


#class Solution:
#    def findDisappearedNumbers(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: List[int]
#        """
#        length = len(nums)
#        for n in nums:
#            nums[(n-1) % length] += length
#
#        ans = []
#        for i, n in enumerate(nums):
#            if n <= length:
#                ans.append(i+1)
#
#        return ans
        

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        m = [0] * (length+1)

        for n in nums:
            m[n] = 1

        ans = []
        for i in range(1, length+1):
            if m[i] == 0:
                ans.append(i)

        return ans
        
        
sol = Solution()

nums = [4, 3, 2, 8, 8, 2, 3, 1]
print(sol.findDisappearedNumbers(nums))

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(sol.findDisappearedNumbers(nums))

nums = [4, 3, 2, 7, 8, 2, 5, 1]
print(sol.findDisappearedNumbers(nums))

nums = [4, 3, 6, 7, 8, 2, 5, 1]
print(sol.findDisappearedNumbers(nums))

nums = []
print(sol.findDisappearedNumbers(nums))

nums = [1]
print(sol.findDisappearedNumbers(nums))

nums = [2, 2]
print(sol.findDisappearedNumbers(nums))

nums = [2, 2, 3]
print(sol.findDisappearedNumbers(nums))
