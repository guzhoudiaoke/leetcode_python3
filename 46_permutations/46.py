class Solution(object):
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(current):
            if len(current) == length:
                ans.append(current)
            else:
                for i in range(length):
                    if not visited[i]:
                        visited[i] = True
                        dfs(current+[nums[i]])
                        visited[i] = False

        ans = []
        length = len(nums)
        if length == 0:
            return ans

        visited = [False] * length
        dfs([])
        return ans

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums, len(nums)))
        
sol = Solution()

nums = [1, 2, 3]
print(sol.permute(nums))
