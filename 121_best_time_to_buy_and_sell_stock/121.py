#class Solution:
#    def maxProfit(self, prices):
#        """
#        :type prices: List[int]
#        :rtype: int
#        """
#        if len(prices) == 0:
#            return 0
#
#        small = prices[0]
#        ans = 0
#        for n in prices[1 : ]:
#            ans = max(n - small, ans)
#            small = min(n, small)
#
#        return ans
#        


#class Solution:
#    def maxProfit(self, prices):
#        """
#        :type prices: List[int]
#        :rtype: int
#        """
#        if len(prices) < 2:
#            return 0
#
#        small = prices[0]
#        ans = 0
#        for n in prices[1 : ]:
#            if ans < n - small:
#                ans = n - small
#            if small > n:
#                small = n
#
#        return ans
        
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        small = prices[0]
        ans = 0
        for n in prices[1 : ]:
            if small > n:
                small = n
            elif ans < n - small:
                ans = n - small

        return ans

sol = Solution()

prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))
