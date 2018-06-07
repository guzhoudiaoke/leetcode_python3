# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(r, mmin, mmax):
            if r == None:
                return True

            if r.val <= mmin or r.val >= mmax:
                return False

            return valid(r.left, mmin, r.val) and valid(r.right, r.val, mmax)
        
        return valid(root, -sys.minsize, sys.maxsize)
        
