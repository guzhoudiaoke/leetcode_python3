class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def solve(begin, current):
            ans.append(current)
            for i in range(begin, len(nums)):
                solve(i+1, current+[nums[i]])

        solve(0, [])
        return ans


sol = Solution()

nums = [1, 2, 3]
ans = sol.subsets(nums)
print(ans)


#nums = [1, 2, 3, 4]
#ans = sol.subsets(nums)
#print(ans)
