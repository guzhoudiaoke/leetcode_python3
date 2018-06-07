# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#class Solution:
#    def buildTree(self, preorder, inorder):
#        """
#        :type preorder: List[int]
#        :type inorder: List[int]
#        :rtype: TreeNode
#        """
#        if len(preorder) == 0 or len(inorder) == 0:
#            return None
#
#        root = TreeNode(preorder[0])
#        index = inorder.index(preorder[0])
#        root.left = self.buildTree(preorder[1 : index+1], inorder[0 : index])
#        root.right = self.buildTree(preorder[index+1 : ], inorder[index+1 : ])
#
#        return root

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(start, end):
            if start >= end:
                return None

            root = TreeNode(preorder.pop(0))
            index = dict[root.val]
            root.left = build(start, index)
            root.right = build(index+1, end)

            return root
        
        dict = {}
        for index, value in enumerate(inorder):
            dict[value] = index
        return build(0, len(preorder))


#class Solution:
#    def buildTree(self, preorder, inorder):
#        """
#        :type preorder: List[int]
#        :type inorder: List[int]
#        :rtype: TreeNode
#        """
#        if len(preorder) == 0 or len(inorder) == 0:
#            return None
#
#        dict = {}
#        for index, value in enumerate(inorder):
#            dict[value] = index
#
#        root = TreeNode(preorder[0])
#        index = dict[root.val]
#        root.left = self.buildTree(preorder[1 : index+1], inorder[0 : index])
#        root.right = self.buildTree(preorder[index+1 : ], inorder[index+1 : ])
#
#        return root

sol = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol.buildTree(preorder, inorder)
