import collections

class Solution:
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        for n in nums:
            d[n] += 1

        counts = [[] for i in range(len(nums)+1)]
        for key in d:
            if d[key]:
                counts[d[key]].append(key)

        ans = []
        c = len(nums)
        while len(ans) < k:
            if counts[c]:
                ans += counts[c]
            c -= 1

        return ans[:k]


    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.Counter(nums)
        counts = collections.defaultdict(list)

        for key in d:
            counts[d[key]].append(key)

        ans = []
        c = len(nums)
        while len(ans) < k:
            if counts[c]:
                ans += counts[c]
            c -= 1

        return ans[: k]

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums).most_common()

        ans = []
        for c in counts:
            ans.append(c[0])
            if len(ans) == k:
                break;

        return ans

        
sol = Solution()

nums = [1, 1, 1, 4, 4, 4, 2, 2, 5, 5, 3, 7]
k = 4
print(sol.topKFrequent(nums, k))

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(sol.topKFrequent(nums, k))

nums = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 1, 2, 3, 5, 5, 5, 5, 5, 5, 9, 9]
k = 4
print(sol.topKFrequent(nums, k))

nums = [1, 1, 1, 1, 1, 1]
k = 1
print(sol.topKFrequent(nums, k))

nums = [1, 1, 1, 1, 1, 1, 2]
k = 2
print(sol.topKFrequent(nums, k))
