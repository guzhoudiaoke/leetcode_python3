#class Solution:
#    def isSubtree(self, s, t):
#        """
#        :type s: TreeNode
#        :type t: TreeNode
#        :rtype: bool
#        """
#        if s is None:
#            return t is None
#
#        if self.isSameTree(s, t):
#            return True
#
#        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
#
#    def isSameTree(self, s, t):
#        if s is None:
#            return t is None
#        if t is None:
#            return s is None
#
#        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return '$'
            return '(' + str(node.val) + ')' + dfs(node.left) + dfs(node.right)

        return dfs(t) in dfs(s)
