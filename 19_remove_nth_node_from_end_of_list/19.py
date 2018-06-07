# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first, second = head, head
        for i in range(n):
            first = first.next

        pre = None
        while first != None:
            first = first.next
            pre = second
            second = second.next
        
        if pre == None:
            head = head.next
        else:
            pre.next = second.next
        return head

def printList(n):
    while n != None:
        print(n.val, end=',')
        n = n.next
    print()

def makeList(l):
    if len(l) == 0:
        return None

    h = ListNode(l[0])
    tail = h
    for n in l[1:]:
        node = ListNode(n)
        tail.next = node
        tail = node

    return h

        
sol = Solution()

h = makeList([1, 2, 3, 4, 5])
printList(h)
printList(sol.removeNthFromEnd(h, 1))

h = makeList([1, 2, 3, 4, 5])
printList(h)
printList(sol.removeNthFromEnd(h, 2))

h = makeList([1, 2, 3, 4, 5])
printList(h)
printList(sol.removeNthFromEnd(h, 3))


h = makeList([1, 2, 3, 4, 5])
printList(h)
printList(sol.removeNthFromEnd(h, 4))

h = makeList([1, 2, 3, 4, 5])
printList(h)
printList(sol.removeNthFromEnd(h, 5))

