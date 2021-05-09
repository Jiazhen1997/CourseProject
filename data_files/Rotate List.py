
__author__ = 'Daniel'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        l = self.get_len(head)
        k %= l  
        pre = dummy
        i = 0
        while pre and i < l-k:
            pre = pre.next
            i += 1

        new_head = pre.next
        if not new_head:
            return dummy.next

        cur = new_head
        pre.next = None
        while cur.next:
            cur = cur.next

        cur.next = dummy.next
        dummy.next = new_head
        return dummy.next

    def get_len(self, head):
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next

        return l


