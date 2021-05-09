
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        
        
        dummy = ListNode(0)
        dummy.next = head

        
        length = 0
        pre = dummy
        while pre.next:
            length += 1
            pre=pre.next

        
        pre = dummy
        count = 0
        while pre.next:
            cur = pre.next
            if count==length-n:
                pre.next = cur.next  
                break
            else:
                count += 1
                pre = pre.next

        return dummy.next


