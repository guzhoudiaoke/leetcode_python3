from queue import PriorityQueue

# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
#
#class PriorityNode:
#    def __init__(self, node):
#        self.node = node
#    def __lt__(self, other):
#        return self.node.val < other.node.val
#
#class Solution:
#    def mergeKLists(self, lists):
#        """
#        :type lists: List[ListNode]
#        :rtype: ListNode
#        """
#        pq = PriorityQueue()
#
#        for head in lists:
#            if head != None:
#                pq.put(PriorityNode(head))
#
#        if pq.empty():
#            return None
#
#        head, tail = None, None
#        while not pq.empty():
#            node = pq.get().node
#            if node.next != None:
#                pq.put(PriorityNode(node.next))
#
#            node.next = None
#            if tail is None:
#                head = tail = node
#            else:
#                tail.next = node
#            tail = node
#
#        return head
#
        

import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#class Solution:
#    def mergeKLists(self, lists):
#        """
#        :type lists: List[ListNode]
#        :rtype: ListNode
#        """
#        pq = PriorityQueue()
#
#        k = len(lists)
#        for index in range(k):
#            node = lists[index]
#            if node != None:
#                pq.put((node.val, index))
#
#        if pq.empty():
#            return None
#
#        head, tail = None, None
#        while not pq.empty():
#            index = pq.get()[1]
#            node = lists[index]
#            if node.next != None:
#                pq.put((node.next.val, index))
#
#            lists[index] = lists[index].next
#            node.next = None
#            if tail is None:
#                head = tail = node
#            else:
#                tail.next = node
#            tail = node
#
#        return head
#

#class Solution:
#    def mergeKLists(self, lists):
#        """
#        :type lists: List[ListNode]
#        :rtype: ListNode
#        """
#        h = []
#        k = len(lists)
#
#        for index in range(k):
#            node = lists[index]
#            if node != None:
#                heapq.heappush(h, (node.val, index))
#
#        head, tail = None, None
#        while h:
#            index = heapq.heappop(h)[1]
#            node = lists[index]
#
#            next = lists[index].next
#            lists[index] = next
#            if next != None:
#                heapq.heappush(h, (next.val, index))
#
#            node.next = None
#            if tail is None:
#                head = tail = node
#            else:
#                tail.next = node
#            tail = node
#
#        return head

#class Solution:
#    def mergeKLists(self, lists):
#        """
#        :type lists: List[ListNode]
#        :rtype: ListNode
#        """
#        from operator import attrgetter
#
#        nodes = []
#        for head in lists:
#            while head is not None:
#                nodes.append(head)
#                head = head.next
#
#        if len(nodes) == 0:
#            return None
#
#        nodes = sorted(nodes, key = attrgetter('val'))
#        head = nodes[0]
#        tail = head
#        for n in nodes[1 :]:
#            tail.next = n
#            tail = n
#
#        return head
#


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from operator import attrgetter
        nodes = []
        for head in lists:
            while head != None:
                nodes.append(head)
                head = head.next

        nodes = sorted(nodes, key = attrgetter('val'))
        head = ListNode(-1)
        tail = head
        for node in nodes:
            tail.next = node
            tail = node

        return head.next


def makeList(l):
    if not l:
        return None

    head = ListNode(l[0])
    tail = head
    for n in l[1 : ]:
        node = ListNode(n)
        tail.next = node
        tail = node
    return head

def printList(head):
    if not head:
        return

    n = head
    while n != None:
        print(n.val, end = ', ')
        n = n.next
    print()


sol = Solution()

l1 = makeList([1, 4, 5])
printList(l1)
l2 = makeList([1, 3, 4])
printList(l2)
l3 = makeList([2, 6])
printList(l3)

l = [ l1, l2, l3 ]
printList(sol.mergeKLists(l))
