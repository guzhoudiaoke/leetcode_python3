import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#class Solution:
#    def maxDepth(self, root):
#        """
#        :type root: TreeNode
#        :rtype: int
#        """
#        if root == None:
#            return 0
#
#        ans = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right));
#        return ans

#class Solution:
#    def maxDepth(self, root):
#        """
#        :type root: TreeNode
#        :rtype: int
#        """
#        if root == None:
#            return 0
#
#        q = collections.deque()
#        ans = 0
#        q.append((root, 1))
#
#        while q:
#            c = q.popleft()
#            if c[0].left != None:
#                q.append((c[0].left, c[1]+1))
#            if c[0].right != None:
#                q.append((c[0].right, c[1]+1))
#            ans = max(ans, c[1])
#
#        return ans

#class Solution:
#    def maxDepth(self, root):
#        """
#        :type root: TreeNode
#        :rtype: int
#        """
#        if root == None:
#            return 0
#
#        q = collections.deque()
#        ans = 0
#        q.append(root)
#
#        while q:
#            ans += 1
#            children = collections.deque()
#            for n in q:
#                if n.left:
#                    children.append(n.left)
#                if n.right:
#                    children.append(n.right)
#            q = children
#
#        return ans


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        q = []
        ans = 0
        q.append(root)

        while q:
            ans += 1
            children = []
            for n in q:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            q = children

        return ans


sol = Solution()

root = TreeNode(3)
left = TreeNode(9)
right = TreeNode(20)
right.left = TreeNode(15)
right.right = TreeNode(7)
root.left = left
root.right = right

ans = sol.maxDepth(root)
print(ans)
