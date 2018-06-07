#class Solution:
#    def hammingDistance(self, x, y):
#        """
#        :type x: int
#        :type y: int
#        :rtype: int
#        """
#        t = x ^ y
#        b = 1
#        ans = 0
#        for i in range(32):
#            if t & b:
#                ans += 1
#            b <<= 1
#
#        return ans
#


#class Solution:
#    def hammingDistance(self, x, y):
#        """
#        :type x: int
#        :type y: int
#        :rtype: int
#        """
#        t = x ^ y
#        ans = 0
#        while t:
#            ans += 1
#            t &= t-1
#
#        return ans

#class Solution:
#    def hammingDistance(self, x, y):
#        """
#        :type x: int
#        :type y: int
#        :rtype: int
#        """
#        return bin(x ^ y).count('1')

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^ y 
        y = 0
        while x > 0:
            y += x & 1
            x >>= 1
        return y

sol = Solution()
print(sol.hammingDistance(1, 4))
print(sol.hammingDistance(2, 5))
print(sol.hammingDistance(23, 8))
print(sol.hammingDistance(1234, 4323))
