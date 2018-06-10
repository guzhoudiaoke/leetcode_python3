# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if self.prev:
                self.prev.right = root

            if root:
                left = root.left
                right = root.right

                root.left = self.prev
                self.prev = root

                dfs(left)
                dfs(right)

        self.prev = None
        dfs(root)
        

def printList(head):
    p = head
    prev = None
    while p:
        print(p.val, end=', ')
        prev = p
        p = p.right
    print()

    p = prev
    while p:
        print(p.val, end=', ')
        p = p.left
    print()
    


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
sol.flatten(root)
printList(root)
