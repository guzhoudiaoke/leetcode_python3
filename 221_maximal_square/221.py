class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for i in range(cols+1)] for j in range(rows+1)]

        ans = 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    ans = max(ans, dp[i][j])
        return ans*ans
        
sol = Solution()
matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
]
print(sol.maximalSquare(matrix))

matrix = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
]
print(sol.maximalSquare(matrix))

matrix = [
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
]
print(sol.maximalSquare(matrix))
