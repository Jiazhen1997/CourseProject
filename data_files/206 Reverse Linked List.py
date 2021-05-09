
__author__ = 'Daniel'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = pre.next
        while pre and cur:
            pre, cur.next, cur = cur, pre, cur.next
            
            

        dummy.next.next = None  
        return pre  
