
__author__ = 'Danyang'

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        
        
        dummy = RandomListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next:
            cur = pre.next
            cur_copy = RandomListNode(cur.label)

            temp = cur.next
            cur.next = cur_copy
            cur_copy.next = temp

            pre = pre.next.next

        
        pre = dummy
        while pre.next:
            cur = pre.next

            if cur.random:
                cur.next.random = cur.random.next  

            pre = pre.next.next

        
        pre = dummy
        head_copy = pre.next.next if pre.next else None
        while pre.next:
            cur = pre.next
            cur_copy = cur.next

            cur.next = cur_copy.next
            if cur_copy.next:
                cur_copy.next = cur_copy.next.next

            pre = pre.next


        return head_copy