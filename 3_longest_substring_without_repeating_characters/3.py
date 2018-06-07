class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        begin = -1
        ans = 0
        dict = {}

        for end, c in enumerate(s):
            if c in dict and dict[c] > begin:
                begin = dict[c]
            else:
                ans = max(ans, end-begin)
            dict[c] = end

        return ans
        

sol = Solution()

s = "abcabcbb"
ans = sol.lengthOfLongestSubstring(s)
print(ans)

s = "bbbbb"
ans = sol.lengthOfLongestSubstring(s)
print(ans)

s = "pwwkew"
ans = sol.lengthOfLongestSubstring(s)
print(ans)
