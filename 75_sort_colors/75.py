class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1

        index = 0
        for i in range(3):
            c = count[i]
            for j in range(c):
                nums[index] = i
                index += 1
        

sol = Solution()

nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print(nums)
