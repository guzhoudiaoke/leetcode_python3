# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0
        pA, pB = headA, headB

        while pA and pB:
            pA, pB = pA.next, pB.next
            lenA += 1
            lenB += 1

        p1, p2 = headA, headB
        while pA:
            pA, p1 = pA.next, p1.next
        while pB:
            pB, p2 = pB.next, p2.next

        while p1 and p2:
            if p1 is p2:
                return p1
            p1, p2 = p1.next, p2.next

        return None

sol = Solution()

a1 = ListNode('a1')
a2 = ListNode('a2')
b1 = ListNode('b1')
b2 = ListNode('b2')
b3 = ListNode('b3')
c1 = ListNode('c1')
c2 = ListNode('c2')
c3 = ListNode('c3')

a1.next = a2
a2.next = c1
b1.next = b2
b2.next = b3
b3.next = c1

c1.next = c2
c2.next = c3
print(sol.getIntersectionNode(a1, b1).val)
