# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        p, q = head, head.next
        head.next = None
        while q:
            p = q
            q = q.next
            p.next = head
            head = p

        return head

def printList(head):
    while head:
        print(head.val, end = ', ')
        head = head.next
    print()
        
sol = Solution()

def test1():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    printList(a)
    printList(sol.reverseList(a))

def test2():
    a = ListNode(1)
    printList(a)
    printList(sol.reverseList(a))
    
def test3():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    printList(a)
    printList(sol.reverseList(a))


test2()
test3()
test1()
