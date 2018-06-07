#class Solution:
#    def mergeTrees(self, t1, t2):
#        """
#        :type t1: TreeNode
#        :type t2: TreeNode
#        :rtype: TreeNode
#        """
#        def dfs(r1, r2):
#            r = None
#            if r1 and not r2:
#                r = TreeNode(r1.val)
#                r.left = dfs(r1.left, None)
#                r.right = dfs(r1.right, None)
#            elif r2 and not r1:
#                r = TreeNode(r2.val)
#                r.left = dfs(None, r2.left)
#                r.right = dfs(None, r2.right)
#            elif r1 and r2:
#                r = TreeNode(r1.val + r2.val)
#                r.left = dfs(r1.left, r2.left)
#                r.right = dfs(r1.right, r2.right)
#            return r
#
#        return dfs(t1, t2)
        
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t2:
            return t1
        if not t1:
            return t2

        t2.val += t1.val
        t2.left = mergeTrees(t1.left, t2.left)
        t2.right = mergeTrees(t1.right, t2.right)
        return t2
