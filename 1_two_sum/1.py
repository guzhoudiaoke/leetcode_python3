class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        length = len(nums)
        for i in range(length):
            if target - nums[i] in d:
                j = d.get(target - nums[i])
                if j != i:
                    return [i, j]
            d[nums[i]] = i


solution = Solution()
nums = [3, 2, 4]
target = 6
ans = solution.twoSum(nums, target)
print(ans)
