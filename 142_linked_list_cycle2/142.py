# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break

        if not cycle:
            return None

        p = head
        while p != slow:
            p = p.next
            slow = slow.next

        return p


    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        slow, fast = head, head.next
        while fast != slow:
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return None

        slow = slow.next
        while head != slow:
            head = head.next
            slow = slow.next

        return head

        
sol = Solution()

head = ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = head.next.next.next
print(sol.detectCycle(head).val)


head = ListNode(2)
head.next = ListNode(3)
ans = sol.detectCycle(head)
if ans:
    print(ans.val)


head = ListNode(2)
ans = sol.detectCycle(head)
if ans:
    print(ans.val)
