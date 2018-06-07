import copy

#class Solution:
#    def minPathSum(self, grid):
#        """
#        :type grid: List[List[int]]
#        :rtype: int
#        """
#        rows = len(grid)
#        cols = len(grid[0])
#        if rows == 0 or cols == 0:
#            return 0
#
#        dp = copy.deepcopy(grid)
#        for i in range(rows):
#            for j in range(cols):
#                if i == 0 and j == 0:
#                    pass
#                elif i < 1:
#                    dp[i][j] += dp[i][j-1]
#                elif j < 1:
#                    dp[i][j] += dp[i-1][j]
#                else:
#                    if dp[i-1][j] < dp[i][j-1]:
#                        dp[i][j] += dp[i-1][j]
#                    else:
#                        dp[i][j] += dp[i][j-1]
#
#        return dp[rows - 1][cols - 1]

#class Solution:
#    def minPathSum(self, grid):
#        """
#        :type grid: List[List[int]]
#        :rtype: int
#        """
#        rows = len(grid)
#        cols = len(grid[0])
#        if rows == 0 or cols == 0:
#            return 0
#
#        for i in range(rows):
#            for j in range(cols):
#                if i == 0 and j == 0:
#                    pass
#                elif i < 1:
#                    grid[i][j] += grid[i][j-1]
#                elif j < 1:
#                    grid[i][j] += grid[i-1][j]
#                else:
#                    if grid[i-1][j] < grid[i][j-1]:
#                        grid[i][j] += grid[i-1][j]
#                    else:
#                        grid[i][j] += grid[i][j-1]
#
#        return grid[-1][-1]


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0 or cols == 0:
            return 0

        for i in range(1, rows):
            grid[i][0] += grid[i-1][0]
        for j in range(1, cols):
            grid[0][j] += grid[0][j-1]

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i-1][j] < grid[i][j-1]:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += grid[i][j-1]

        return grid[-1][-1]
        
sol = Solution()

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(sol.minPathSum(grid))
