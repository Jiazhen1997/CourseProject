

__author__ = 'Daniel'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        
        l_a = self._get_len(headA)
        l_b = self._get_len(headB)
        if l_a > l_b:
            l_a, l_b = l_b, l_a
            headA, headB = headB, headA

        cur_a = headA
        cur_b = headB
        for i in xrange(l_b-l_a):
            cur_b = cur_b.next

        while cur_a != cur_b:
            cur_a = cur_a.next
            cur_b = cur_b.next

        return cur_a

    def _get_len(self, head):
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        return n