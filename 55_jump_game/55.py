#class Solution:
#    def canJump(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: bool
#        """
#        length = len(nums)
#        if length == 0:
#            return True
#
#        dp = [False] * length
#        dp[0] = True
#
#        for i in range(length):
#            if dp[i]:
#                for j in range(1, nums[i]+1):
#                    if i + j < length:
#                        dp[i+j] = True
#                    else:
#                        break
#
#        return dp[length-1]


#class Solution:
#    def canJump(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: bool
#        """
#        length = len(nums)
#        if length <= 1:
#            return True
#
#        mmax, next = 0, 0
#        for i in range(length):
#            next = i + nums[i]
#            if next > mmax:
#                mmax = next
#                if mmax >= length-1:
#                    return True
#            elif mmax < i+1:
#                return False
#
#
#        return True

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length <= 1:
            return True

        last = length
        for i in range(length - 1, -1, -1):
            if i + nums[i] >= last:
                last = i

        return last == 0


sol = Solution()

nums = [2, 3, 1, 1, 4]
print(sol.canJump(nums))

nums = [3, 2, 1, 0, 4]
print(sol.canJump(nums))
