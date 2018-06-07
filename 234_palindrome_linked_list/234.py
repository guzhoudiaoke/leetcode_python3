# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def revertList(self, head):
        if head is None or head.next is None:
            return head

        p, q = head, head.next
        head.next = None
        while q:
            p = q
            q = q.next
            p.next = head
            head = p

        return head

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        revert = self.revertList(slow.next)
        while revert:
            if revert.val != head.val:
                return False
            head, revert = head.next, revert.next

        return True
        
sol = Solution()

def test1():
    head = ListNode(1)
    print(sol.isPalindrome(head))

def test2():
    head = ListNode(1)
    head.next = ListNode(2)
    print(sol.isPalindrome(head))

def test3():
    head = ListNode(1)
    head.next = ListNode(1)
    print(sol.isPalindrome(head))

def test4():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    print(sol.isPalindrome(head))

def test5():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(sol.isPalindrome(head))

def test6():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(1)
    print(sol.isPalindrome(head))

test1()
test2()
test3()
test4()
test5()
test6()
