
__author__ = 'Daniel'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next:
            cur = pre.next
            if cur.val == val:
                pre.next = cur.next
                continue

            pre = pre.next

        return dummy.next