# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        return self.mergeSort(head, length)
    
    def mergeSort(self, head, length):
        if length <= 1:
            return head

        prev, mid = None, head
        for i in range(length//2):
            prev = mid
            mid = mid.next

        if prev:
            prev.next = None

        left = self.mergeSort(head, length//2)
        right = self.mergeSort(mid, length - length//2)

        return self.merge(left, right)

    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = None
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        tail = head

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return head



    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        l = []
        while p:
            l.append(p.val)
            p = p.next
        
        l.sort()
        p = head
        for n in l:
            p.val = n
            p = p.next

        return head

        
def printList(head):
    while head:
        print(head.val, end=', ')
        head = head.next
    print()


sol = Solution()

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(6)

printList(head)
head = sol.sortList(head)
printList(head)


head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)

printList(head)
head = sol.sortList(head)
printList(head)
