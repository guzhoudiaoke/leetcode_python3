class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        length = len(s)

        i = 0
        while i < length:
            j = i
            while j < length and s[j] == s[i]:
                j += 1
            ans += (j - i) * (j - i + 1) // 2

            l, r = i - 1, j
            while l >= 0 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
                ans += 1

            i = j

        return ans
"""
    def countSubstrings(self, s):
        ans = 0
        length = len(s)
        for i in range(length):
            j = 0
            while i - j >= 0 and i + j < length and s[i-j] == s[i+j]:
                j += 1
                ans += 1

            j = 0
            while i - j >= 0 and i + j + 1 < length and s[i-j] == s[i+j+1]:
                j += 1
                ans += 1

        return ans
"""

sol = Solution()

s = "abc"
ans = sol.countSubstrings(s)
print(ans)

s = "aaa"
ans = sol.countSubstrings(s)
print(ans)

s = "abcba"
ans = sol.countSubstrings(s)
print(ans)

s = "bcddcdbddbdccabdabaccdacadadabcabdbddcccabaaab"
ans = sol.countSubstrings(s)
print(ans)

