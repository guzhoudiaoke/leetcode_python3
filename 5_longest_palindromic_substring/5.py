#class Solution:
#    def longestPalindrome(self, s):
#        """
#        :type s: str
#        :rtype: str
#        """
#        def expandPalindrome(left, right):
#            while left >= 0 and right < length and s[left] == s[right]:
#                left -= 1
#                right += 1
#            return left+1, right-1
#
#        start, end = 0, 0
#        length = len(s)
#        for i in range(0, length):
#            sp, ep = expandPalindrome(i, i)
#            if ep - sp > end - start:
#                start, end = sp, ep
#
#            sp, ep = expandPalindrome(i, i+1)
#            if ep - sp > end - start:
#                start, end = sp, ep
#
#        return s[start : end+1]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(ss):
            return ss == ss[::-1]

        end, max_len = 0, 1
        length = len(s)
        for i in range(1, length):
            if i - max_len >= 0 and isPalindrome(s[i-max_len : i+1]):
                max_len += 1
                end = i
            elif i - max_len >= 1 and isPalindrome(s[i-max_len-1 : i+1]):
                max_len += 2
                end = i

        return s[end-max_len+1 : end+1]
        
sol = Solution()
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('babab'))
print(sol.longestPalindrome('ababab'))
print(sol.longestPalindrome('abababc'))
print(sol.longestPalindrome('cbababc'))
print(sol.longestPalindrome(''))
print(sol.longestPalindrome('a'))
print(sol.longestPalindrome('aa'))
print(sol.longestPalindrome('aaa'))
print(sol.longestPalindrome('aaaa'))

