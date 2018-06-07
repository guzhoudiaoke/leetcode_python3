import queue

class Solution:
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = queue.PriorityQueue()
        for n in nums:
            pq.put(-n)

        ans = 0
        for i in range(k):
            ans = pq.get()
        return -ans


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        return heapq.nlargest(k, nums)[k-1]
        
sol = Solution()

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(sol.findKthLargest(nums, k))

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(sol.findKthLargest(nums, k))
