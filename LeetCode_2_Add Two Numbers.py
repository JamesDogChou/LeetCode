# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        notEndL1 = 1
        notEndL2 = 1
        iter1 = l1
        iter2 = l2
        carry = 0
        
        # Set up first node
        rNode = ListNode(0)
        t = iter1.val*notEndL1 + iter2.val*notEndL2 + carry
        carry = t // 10
        rNode.val = t % 10
        rNode.next = None
        if iter1.next:
            iter1 = iter1.next
        else:
            notEndL1 = 0
        if iter2.next:
            iter2 = iter2.next
        else:
            notEndL2 = 0
        # Rnode's iterator 
        iterR = rNode
        
        while notEndL1 or notEndL2 or carry:
            t = iter1.val*notEndL1 + iter2.val*notEndL2 + carry
            carry = t // 10
            newNode = ListNode(t % 10)
            newNode.next = None
            iterR.next = newNode
            iterR = newNode
            if iter1.next:
                iter1 = iter1.next
            else:
                notEndL1 = 0
            if iter2.next:
                iter2 = iter2.next
            else:
                notEndL2 = 0
        return rNode