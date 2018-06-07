class Solution:
    def countBits1(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0] * (num + 1)
        for i in range(1, num+1):
            ans[i] = ans[i & (i-1)] + 1
        return ans


    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        while len(ans) < num+1:
            ans += [1 + n for n in ans]
        return ans[: num+1]
        
sol = Solution()
print(sol.countBits(5))
print(sol.countBits(15))
