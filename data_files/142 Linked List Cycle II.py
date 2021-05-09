
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    
    def detectCycle(self, head):
        

        
        hare = head
        tortoise = head
        flag = False
        while hare and hare.next and tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare==tortoise:
                flag = True
                break

        if not flag:
            return None

        
        cur = head
        while cur:
            if cur==tortoise:
                break
            cur = cur.next
            tortoise = tortoise.next

        return cur