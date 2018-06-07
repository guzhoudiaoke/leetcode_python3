# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.current = 0

        def dfs(node):
            if node is None:
                return

            dfs(node.right)
            node.val += self.current
            self.current = node.val
            dfs(node.left)

        dfs(root)
        return root
        
sol = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

sol.convertBST(root)
print(root.val)
print(root.left.val)
print(root.right.val)
