from collections import deque

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        deq = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                deq.append(c)
            else:
                if len(deq) == 0:
                    return False

                top = deq[-1]
                if c == ')' and top != '(':
                    return False
                elif c == ']' and top != '[':
                    return False
                elif c == '}' and top != '{':
                    return False

                deq.pop()

        return len(deq) == 0

"""
        if len(s) % 2 != 0:
            return False

        l = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                l.append(c)
            else:
                if len(l) == 0:
                    return False

                top = l[-1]
                if c == ')' and top != '(':
                    return False
                elif c == ']' and top != '[':
                    return False
                elif c == '}' and top != '{':
                    return False

                l.pop()

        return len(l) == 0
"""

sol = Solution()

s = "((()))"
print(sol.isValid(s))

s = "("
print(sol.isValid(s))

s = "(()))"
print(sol.isValid(s))


s = "{([])}"
print(sol.isValid(s))

s = "(]"
print(sol.isValid(s))

s = "(("
print(sol.isValid(s))
