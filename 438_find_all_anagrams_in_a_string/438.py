#class Solution:
#    def findAnagrams(self, s, p):
#        """
#        :type s: str
#        :type p: str
#        :rtype: List[int]
#        """
#        if len(s) < len(p):
#            return []
#
#        ms = [0] * 26
#        mp = [0] * 26
#
#        for i in range(len(p)):
#            mp[ord(p[i]) - ord('a')] += 1
#            ms[ord(s[i]) - ord('a')] += 1
#
#        ans = []
#        if ms == mp:
#            ans.append(0)
#
#        j = 0
#        for i in range(len(p), len(s)):
#            ms[ord(s[i]) - ord('a')] += 1
#            ms[ord(s[j]) - ord('a')] -= 1
#
#            j += 1
#            if ms == mp:
#                ans.append(j)
#
#        return ans


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        ds = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
        dp = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)

        for i in range(len(p)):
            dp[p[i]] += 1
            ds[s[i]] += 1

        ans = []
        j = 0
        if ds == dp:
            ans.append(j)

        for i in range(len(p), len(s)):
            ds[s[i]] += 1
            ds[s[j]] -= 1

            j += 1
            if ds == dp:
                ans.append(j)

        return ans


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
print(sol.findAnagrams("abab", "ab"))
print(sol.findAnagrams("abab", "abccc"))
print(sol.findAnagrams("abab", "abc"))
