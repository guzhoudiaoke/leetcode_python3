class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss in dict:
                dict[ss].append(s)
            else:
                dict[ss] = [s]

        ans = []
        for key, l in dict.items():
            ans.append(l)

        return ans

sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = sol.groupAnagrams(strs)
print(ans)
