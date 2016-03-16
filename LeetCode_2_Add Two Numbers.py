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
        notEndL1 = True
        notEndL2 = True
        iter1 = l1
        iter2 = l2
        
        # Set up first node
        t = iter1.val + iter2.val
        if t > 9:
            carry = 1
            rNode = ListNode(t - 10)
        else:
            carry = 0
            rNode = ListNode(t)
        if iter1.next:
            iter1 = iter1.next
        else:
            notEndL1 = False
        if iter2.next:
            iter2 = iter2.next
        else:
            notEndL2 = False
        # Rnode's iterator 
        iterR = rNode
        
        while notEndL1 or notEndL2 or carry:
            t = carry + iter1.val if notEndL1 else carry
            if notEndL2:
                t += iter2.val
            if t > 9:
                carry = 1
                newNode = ListNode(t - 10)
            else:
                carry = 0
                newNode = ListNode(t)
            iterR.next = newNode
            iterR = newNode
            if iter1.next:
                iter1 = iter1.next
            else:
                notEndL1 = False
            if iter2.next:
                iter2 = iter2.next
            else:
                notEndL2 = False
        return rNode
