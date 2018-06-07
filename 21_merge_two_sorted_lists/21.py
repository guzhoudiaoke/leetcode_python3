# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        head = None
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        tail = head

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next

        if l1 != None:
            tail.next = l1
        elif l2 != None:
            tail.next = l2

        return head


def makeList(l):
    head = None
    tail = None

    for n in l:
        node = ListNode(n)
        if head == None:
            head = node
        else:
            tail.next = node
        tail = node

    return head

def printList(head):
    node = head
    while node != None:
        print(node.val, end=' ')
        node = node.next
    print()

sol = Solution()

list1 = [1, 2, 4]
list2 = [1, 3, 4]
l1 = makeList(list1)
l2 = makeList(list2)
ans = sol.mergeTwoLists(l1, l2)
printList(ans)

