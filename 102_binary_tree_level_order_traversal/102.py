# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        q = [root]
        ans= [[root.val]]

        while q:
            next_level = []
            values = []
            for n in q:
                if n.left:
                    next_level.append(n.left)
                    values.append(n.left.val)
                if n.right:
                    next_level.append(n.right)
                    values.append(n.right.val)

            q = next_level
            if values:
                ans.append(values)

        return ans

sol = Solution()

root = TreeNode(3)
l = TreeNode(9)
r = TreeNode(20)
r.left = TreeNode(15)
r.right = TreeNode(7)
root.left = l
root.right = r

ans = sol.levelOrder(root)
print(ans)
