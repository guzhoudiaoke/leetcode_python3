class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {n : 1 for n in nums}
        ans = 0
        for n in nums:
            if d[n] == 0:
                continue

            d[n] = 0

            l = n - 1
            while l in d:
                d[l] = 0
                l -= 1

            r = n + 1
            while r in d:
                d[r] = 0
                r += 1

            if r - l - 1 > ans:
                ans = r - l - 1

        return ans


sol = Solution()        
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
