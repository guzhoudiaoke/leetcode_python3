class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in nums:
            ans ^= n
        return ans
        
sol = Solution()

nums = [2, 2, 1]
print(sol.singleNumber(nums))

nums = [4, 1, 2, 1, 2]
print(sol.singleNumber(nums))
