# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        nl = l1
        if l1.val < l2.val:
            nl = l1
            l1 = l1.next
        else:
            nl = l2
            l2 = l2.next

        c = nl
        while l1 != None and l2 != None:
            if c.val <= l1.val:
                c.next = l1
                l1 = l1.next
            elif c.val <= l2.val :
                c.next = l2
                l2 = l2.next
            c = c.next

        while l1 != None:
            c.next = l1
            l1 = l1.next
            c = c.next
        while l2 != None:
            c.next = l2
            l2 = l2.next
            c = c.next

        return nl