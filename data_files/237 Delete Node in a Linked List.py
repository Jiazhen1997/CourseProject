
__author__ = 'Daniel'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        
        cur = node
        while cur.next:
            cur.val = cur.next.val
            if not cur.next.next:
                cur.next = None
                break

            cur = cur.next