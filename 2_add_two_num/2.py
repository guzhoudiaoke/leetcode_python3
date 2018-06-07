# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#class Solution:
#    def addTwoNumbers(self, l1, l2):
#        """
#        :type l1: ListNode
#        :type l2: ListNode
#        :rtype: ListNode
#        """
#        length = max(len(l1), len(l2))
#        ans = [0 for i in range(length)]
#        for i in range(length):
#            if i < len(l1):
#                ans[i] += l1[i]
#            if i < len(l2):
#                ans[i] += l2[i]
#            
#            if ans[i] >= 10:
#                ans[i] -= 10
#                if i + 1 == length:
#                    ans.append(1)
#                else:
#                    ans[i+1] += 1
#
#        return ans
#
#
#sol = Solution()
#l1 = [6, 7, 8, 9]
#l2 = [3, 4, 5]
#ans = sol.addTwoNumbers(l1, l2)
#print(ans)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#class Solution:
#    def addTwoNumbers(self, l1, l2):
#        """
#        :type l1: ListNode
#        :type l2: ListNode
#        :rtype: ListNode
#        """
#        
#        if l1 is None or l2 is None:
#            return None
#        
#        ans = None
#        tail = None
#        while l1 is not None or l2 is not None:
#            node = ListNode(0)
#            if l1 is not None:
#                node.val += l1.val
#                l1 = l1.next
#            if l2 is not None:
#                node.val += l2.val
#                l2 = l2.next
#            
#            if ans is None:
#                ans = node
#            else:
#                tail.next = node
#            tail = node
#        
#        tail = ans
#        carry = False
#        while True:
#            if carry:
#                tail.val += 1
#                carry = False
#            if tail.val >= 10:
#                tail.val -= 10
#                carry = True
#            
#            if tail.next is None:
#                break
#                
#            tail = tail.next
#        
#        if carry:
#            node = ListNode(1)
#            tail.next = node
#
#        return ans

#class Solution:
#    def addTwoNumbers(self, l1, l2):
#        """
#        :type l1: ListNode
#        :type l2: ListNode
#        :rtype: ListNode
#        """
#        
#        if l1 is None or l2 is None:
#            return None
#        
#        ans = None
#        tail = None
#        carry = False
#        while l1 is not None or l2 is not None:
#            node = ListNode(0)
#            if l1 is not None:
#                node.val += l1.val
#                l1 = l1.next
#            if l2 is not None:
#                node.val += l2.val
#                l2 = l2.next
#            
#            if carry == True:
#                node.val += 1
#                carry = False
#                
#            if node.val >= 10:
#                node.val -= 10
#                carry = True
#            
#            if ans is None:
#                ans = node
#            else:
#                tail.next = node
#            tail = node
#
#        if carry:
#            node = ListNode(1)
#            tail.next = node
#
#        return ans
#



class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None or l2 is None:
            return None
        
        p1, p2 = l1, l2
        t1, t1 = l1, l2
        carry = 0
        while p1 != None and p2 != None:
            p1.val += p2.val + carry
            carry = p1.val // 10
            p1.val %= 10
            p2.val = p1.val

            t1, t2 = p1, p2
            p1, p2 = p1.next, p2.next

        ans, tail, p = l1, t1, p1
        if p2 != None:
            ans, tail, p = l2, t2, p2

        while p != None:
            p.val += carry
            carry = p.val // 10
            p.val %= 10
            tail = p
            p = p.next

        if carry:
            tail.next = ListNode(carry)
            
        return ans



def makeList(l):
    ret = None
    tail = None
    for x in l:
        node = ListNode(x)
        if ret is None:
            ret = node
        else:
            tail.next = node
        tail = node
    return ret

def printList(l):
    n = l
    p = []
    while n is not None:
        #p.insert(0, n.val)
        p.append(n.val)
        n = n.next
    print(p)


sol = Solution()
l1 = [6, 7, 8, 9]
l2 = [3, 4, 5]

n1 = makeList(l1)
printList(n1)

n2 = makeList(l2)
printList(n2)

ans = sol.addTwoNumbers(n1, n2)
printList(ans)



l1 = [1]
l2 = [9, 9]

n1 = makeList(l1)
printList(n1)

n2 = makeList(l2)
printList(n2)

ans = sol.addTwoNumbers(n1, n2)
printList(ans)

