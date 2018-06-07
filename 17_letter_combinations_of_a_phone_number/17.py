class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #dict = { 
        #        '2' : ['a', 'b', 'c'],
        #        '3' : ['d', 'e', 'f'],
        #        '4' : ['g', 'h', 'i'], 
        #        '5' : ['j', 'k', 'l'], 
        #        '6' : ['m', 'n', 'o'],
        #        '7' : ['p', 'q', 'r', 's'], 
        #        '8' : ['t', 'u', 'v'], 
        #        '9' : ['w', 'x', 'y', 'z']
        #}

        dict = { 
                '2' : "abc",
                '3' : "def",
                '4' : "ghi", 
                '5' : "jkl", 
                '6' : "mno",
                '7' : "pqrs", 
                '8' : "tuv", 
                '9' : "wxyz" 
        }

        def dfs(current, start):
            if start == length:
                ans.append(current)
                return

            for c in dict[digits[start]]:
                dfs(current+c, start+1)

        length = len(digits)
        if length == 0:
            return []

        ans = []
        dfs('', 0)
        return ans
        
sol = Solution()
print(sol.letterCombinations('23'))
print(sol.letterCombinations('223'))
print(sol.letterCombinations('3223'))
