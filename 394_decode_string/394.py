class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("2[abc]3[cd]ef"))
