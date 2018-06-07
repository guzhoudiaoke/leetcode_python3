# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node):
            if node == None:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        ans = []
        dfs(root)
        return ans
        
sol = Solution()

root= TreeNode(1)
r = TreeNode(2)
r.left = TreeNode(3)
root.right = r
print(sol.inorderTraversal(root))
