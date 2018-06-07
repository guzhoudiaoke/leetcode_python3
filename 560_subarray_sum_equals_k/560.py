import collections

class Solution:
    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        d[0] = 1

        sum = 0
        ans = 0
        for n in nums:
            sum += n
            if sum-k in d:
                ans += d[sum-k]

            d[sum] += 1

        return ans


    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0 : 1}

        sum, ans = 0, 0
        for n in nums:
            sum += n
            if sum-k in d:
                ans += d[sum-k]

            if sum in d:
                d[sum] += 1
            else:
                d[sum] = 1

        return ans

sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))
print(sol.subarraySum([1, 1, 1, 1, 3, 4, 2, 1, 5, 2], 7))
print(sol.subarraySum([1, 1, 1, 3, 2, 4, 5, 6, 9, 10, 14], 17))
