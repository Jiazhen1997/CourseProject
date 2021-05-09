




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        cur = head

        l = 1
        while l < m:
            nxt = cur.next
            prev = cur
            cur = nxt
            l += 1
        
        
        
        
        
        leftend = prev
        rightend = cur

        while l <= n:  
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            l += 1

        if m != 1:  
            leftend.next = prev
        else:
            head = prev

        rightend.next = cur
        return head
