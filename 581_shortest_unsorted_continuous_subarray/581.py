import sys

#class Solution:
#    def findUnsortedSubarray(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        flag = False
#        min_num, max_num = sys.maxsize, -sys.maxsize
#        for i in range(1, len(nums)):
#            if nums[i] < nums[i-1]:
#                flag = True
#            if flag:
#                min_num = min(min_num, nums[i])
#
#        flag = False
#        for i in range(len(nums) - 2, -1, -1):
#            if nums[i] > nums[i+1]:
#                flag = True
#            if flag:
#                max_num = max(max_num, nums[i])
#
#        l, r = 0, len(nums) - 1
#        while l < len(nums) and min_num >= nums[l]:
#            l += 1
#        while r >= 0 and max_num <= nums[r]:
#            r -= 1
#
#        print(r, l)
#        return r - l + 1 if r > l else 0


#class Solution:
#    def findUnsortedSubarray(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        length = len(nums)
#
#        l = 0
#        while l < length-1 and nums[l] <= nums[l+1]:
#            l += 1
#        if l == length-1:
#            return 0
#
#        r = length-1
#        while r > 0 and nums[r] >= nums[r-1]:
#            r -= 1
#        if r == 0:
#            return 0
#
#        min_num, max_num = sys.maxsize, -sys.maxsize
#        for i in range(l, r+1):
#            min_num = min(min_num, nums[i])
#            max_num = max(max_num, nums[i])
#
#        i, j = 0, length-1
#        while i < l and nums[i] <= min_num:
#            i += 1
#        while j > r and nums[j] >= max_num:
#            j -= 1
#
#        return j - i + 1


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        l = 0
        while l < length-1 and nums[l] <= nums[l+1]:
            l += 1
        if l == length-1:
            return 0

        r = length-1
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1

        min_num, max_num = sys.maxsize, -sys.maxsize
        for i in range(l, r+1):
            if nums[i] < min_num:
                min_num = nums[i]
            if nums[i] > max_num:
                max_num = nums[i]

        i, j = 0, length-1
        while i < l and nums[i] <= min_num:
            i += 1
        while j > r and nums[j] >= max_num:
            j -= 1

        return j - i + 1



sol = Solution()
ans = sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
print(ans)

ans = sol.findUnsortedSubarray([9, 15])
print(ans)

ans = sol.findUnsortedSubarray([15])
print(ans)

ans = sol.findUnsortedSubarray([])
print(ans)

ans = sol.findUnsortedSubarray([2, 1])
print(ans)
