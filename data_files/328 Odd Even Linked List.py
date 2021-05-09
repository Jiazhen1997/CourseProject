
__author__ = 'Daniel'



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        
        if not head:
            return

        ptr = head  
        pre = head  
        cnt = 1
        while pre and pre.next:
            cur = pre.next
            cnt += 1
            if cnt % 2 == 0:
                pre = pre.next
            else:
                start = ptr.next
                nxt = cur.next

                ptr.next = cur
                cur.next = start
                pre.next = nxt

                ptr = ptr.next

        return head

    def oddEvenListError(self, head):
        
        if not head:
            return

        ptr = head  
        parity = ptr.val % 2

        pre = head
        while pre and pre.next:
            cur = pre.next
            if cur.val % 2 != parity:
                pre = pre.next
            else:
                start = ptr.next
                nxt = cur.next

                ptr.next = cur
                cur.next = start
                pre.next = nxt

                ptr = ptr.next

        return head
