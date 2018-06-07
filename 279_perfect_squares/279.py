import sys

class Solution(object):
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0

        for i in range(0, n+1):
            j = 1
            while i + j*j <= n:
                if dp[i + j*j] > 1 + dp[i]:
                    dp[i + j*j] = 1 + dp[i]
                j += 1

        return dp[n]


    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n+1)
        dp[0] = 0

        for j in range(1, 1+int(n**0.5)):
            for i in range(0, n+1-j*j):
                dp[i + j*j] = min(dp[i + j*j], dp[i] + 1)

        return dp[n]
    # 33.10% python


    def numSquares3(self, n):
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


    def numSquares4(self, n):
        """
        :type n: int
        :rtype: int
        """
        import collections

        q = collections.deque()
        q.append((n, 0))
        while q:
            target, level = q.popleft()
            sqrt = int(target ** 0.5)
            while sqrt >= 1:
                left = target - sqrt*sqrt
                if left == 0:
                    return level+1
                if left > 0:
                    q.append((left, level+1))
                sqrt -= 1
    # 68.13% python


    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isSquare(x):
            sqrt = int(x ** 0.5)
            return sqrt*sqrt == x

        if isSquare(n):
            return 1

        # while n % 4 == 0: n /= 4
        while n & 3 == 0:
            n >>= 2

        if n & 7 == 7:
            return 4

        sqrt = int(n ** 0.5)
        for i in range(1, sqrt+1):
            if isSquare(n - i*i):
                return 2

        return 3
    # 100.0% python

        
sol = Solution()
print(sol.numSquares(11))
print(sol.numSquares(12))
print(sol.numSquares(13))
print(sol.numSquares(17))

