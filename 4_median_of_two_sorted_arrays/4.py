class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        count = (m + n) // 2



sol = Solution()

nums1 = [1, 2]
nums2 = [3, 4]
ans = sol.findMedianSortedArrays(nums1, nums2)
print(ans)

nums1 = [1, 3]
nums2 = [2]
ans = sol.findMedianSortedArrays(nums1, nums2)
print(ans)

nums1 = [1, 3, 4, 5, 8, 11, 14, 17]
nums2 = [2, 4, 5, 7, 9, 12, 13, 15]
ans = sol.findMedianSortedArrays(nums1, nums2)
print(ans)
