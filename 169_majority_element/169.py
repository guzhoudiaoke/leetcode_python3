#class Solution:
#    def majorityElement(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        cnt, cur = 0, None
#        for n in nums:
#            if cnt == 0:
#                cur = n
#            if n == cur:
#                cnt += 1
#            else:
#                cnt -= 1
#
#        return cur
#        


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]

sol = Solution()
print(sol.majorityElement([3, 2, 3]))
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(sol.majorityElement([8, 8, 7, 7, 7]))
