# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#class Solution:
#    def pathSum(self, root, sum):
#        """
#        :type root: TreeNode
#        :type sum: int
#        :rtype: int
#        """
#        if root is None:
#            return 0
#
#        return self.sum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
#
#    def sum(self, root, s):
#        if root is None:
#            return 0
#
#        ans = 1 if root.val == else 0
#        return ans + self.sum(root.left, s-root.val) + self.sum(root.right, s-root.val)

from collections import defaultdict
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        dict = defaultdict(int)
        dict[0] = 1
        return self.solve(root, sum, 0, dict)


    def solve(self, root, target, cur, dict):
        cur += root.val
        ans = dict[cur - target]

        dict[cur] += 1
        if root.left:
            ans += self.solve(root.left, target, cur, dict)
        if root.right:
            ans += self.solve(root.right, target, cur, dict)
        dict[cur] -= 1

        return ans


sol = Solution()
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)
r.right.right = TreeNode(7)

ans = sol.pathSum(r, 6)
print(ans)
