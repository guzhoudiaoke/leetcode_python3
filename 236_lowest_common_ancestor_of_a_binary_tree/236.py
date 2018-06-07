# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        if p == root or q == root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left

        return root


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def isParent(p, c):
            if p is None:
                return False
            if p == c:
                return True
            return isParent(p.left, c) or isParent(p.right, c)

        if root is None or p == root or q == root:
            return root

        if isParent(p, q):
            return p
        if isParent(q, p):
            return q

        while root:
            if isParent(root.left, p) and isParent(root.left, q):
                root = root.left
            elif isParent(root.right, p) and isParent(root.right, q):
                root = root.right
            else:
                return root

        return root

