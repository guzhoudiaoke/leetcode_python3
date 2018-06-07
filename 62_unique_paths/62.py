#class Solution:
#    def uniquePaths(self, m, n):
#        """
#        :type m: int
#        :type n: int
#        :rtype: int
#        """
#        dp = [1] * n
#        for i in range(1, m):
#            for j in range(1, n):
#                dp[j] += dp[j-1]
#
#        return dp[n-1]

#class Solution:
#    def uniquePaths(self, m, n):
#        """
#        :type m: int
#        :type n: int
#        :rtype: int
#        """
#        def factorial(x):
#            ret = 1
#            for i in range(1, x+1):
#                ret *= i
#            return ret
#
#        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
        
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x, y = 1, 1
        for i in range(m, m+n-1):
            x *= i
        for i in range(1, n):
            y *= i

        return x // y
        
sol = Solution()
print(sol.uniquePaths(3, 2))
print(sol.uniquePaths(7, 3))
print(sol.uniquePaths(5, 4))
print(sol.uniquePaths(8, 9))
