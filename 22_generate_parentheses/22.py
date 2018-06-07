class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []

        def generate(current, left, right):
            if left == 0 and right == 0:
                results.append(current)
                return

            if left > 0:
                generate(current + "(", left - 1, right)
            if right > left:
                generate(current + ")", left, right - 1)

        generate('', n, n)
        return results
        
sol = Solution()

n = 3
ans = sol.generateParenthesis(n)
print(ans)

n = 4
ans = sol.generateParenthesis(n)
print(ans)
