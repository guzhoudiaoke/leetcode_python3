#class Solution:
#    def climbStairs(self, n):
#        """
#        :type n: int
#        :rtype: int
#        """
#        if n <= 2:
#            return n
#
#        dp = [ 0 for i in range(n+1) ]
#        dp[0] = dp[1] = 1
#
#        for i in range(2, n+1):
#            dp[i] = dp[i-1] + dp[i-2]
#
#        return dp[n]

#class Solution:
#    def __init__(self):
#        self.dict = {}
#
#    def climbStairs(self, n):
#        """
#        :type n: int
#        :rtype: int
#        """
#        def solve(n):
#            if n <= 1:
#                return 1
#
#            if n in self.dict:
#                return self.dict[n]
#            else:
#                ret = solve(n-1) + solve(n-2)
#                self.dict[n] = ret
#                return ret
#
#        return solve(n)


#class Solution:
#    def __init__(self):
#        self.dict = {}
#
#    def climbStairs(self, n):
#        """
#        :type n: int
#        :rtype: int
#        """
#        if n <= 1:
#            return 1
#
#        if n in self.dict:
#            return self.dict[n]
#        else:
#            ret = self.climbStairs(n-1) + self.climbStairs(n-2)
#            self.dict[n] = ret
#            return ret



class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        n1, n2 = 1, 2
        for i in range(3, n+1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3

        return n2


sol = Solution()

# 2
ans = sol.climbStairs(2)
print(ans)

# 3
ans = sol.climbStairs(3)
print(ans)

# 5
ans = sol.climbStairs(4)
print(ans)

# 9227465
ans = sol.climbStairs(34)
print(ans)

