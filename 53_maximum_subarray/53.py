class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        cur, ans = nums[0], nums[0] 
        for n in nums[1: ]:
            cur += n
            if cur < n:
                cur = n
            if cur > ans:
                ans = cur

        return ans
        
sol = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = sol.maxSubArray(nums)
print(ans)

nums = [-2]
ans = sol.maxSubArray(nums)
print(ans)
