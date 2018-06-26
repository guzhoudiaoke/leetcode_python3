class Solution:
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(start, target):
            l = start
            r = length-1
            while l < r:
                if nums[l] + nums[r] == target:
                    vl, vr = nums[l], nums[r]
                    ans.append([-target, vl, vr])
                    while l < r and nums[l] == vl:
                        l += 1
                    while l < r and nums[r] == vr:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1


        length = len(nums)
        nums.sort()
        ans = []
        i = 0
        while i < length - 2:
            twoSum(i+1, -nums[i])
            vi = nums[i]
            while i < length - 2 and nums[i] == vi:
                i += 1

        return ans


    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        ans = []
        i = 0
        for i in range(length-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = length-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l, r = l+1, r-1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return ans



    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        ans = []
        if 0 in d and d[0] > 2:
            ans.append([0, 0, 0])

        negative = sorted(x for x in d if x < 0)
        positive = sorted(x for x in d if x >= 0)

        for n in negative:
            for p in positive:
                s = -(n + p)
                if s in d:
                    if s in (n, p) and d[s] > 1:
                        ans.append([n, p, s])
                    elif s < n:
                        ans.append([n, p, s])
                    elif p < s:
                        ans.append([n, p, s])
        return ans



sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
