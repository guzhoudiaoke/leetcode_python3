# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def solve(r):
            if r == None:
                return 0

            hl = solve(r.left)
            hr = solve(r.right)

            if hl + hr > ans[0]:
                ans[0] = hl + hr

            if hl > hr:
                return hl + 1
            return hr + 1

        ans = [0]
        solve(root)
        return ans[0]
        
sol = Solution()

l = TreeNode(2)
r = TreeNode(3)
l.left = TreeNode(4)
l.right = TreeNode(5)
root = TreeNode(1)
root.left = l
root.right = r
print(sol.diameterOfBinaryTree(root))
