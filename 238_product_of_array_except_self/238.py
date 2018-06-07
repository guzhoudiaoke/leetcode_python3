class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)
        
        current = 1
        for i in range(len(nums)):
            ans[i] = current
            current *= nums[i]

        current = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= current
            current *= nums[i]

        return ans
        
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
print(sol.productExceptSelf([1, 2, 3, 4, 5]))
