




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next

        mid = l // 2 + 1
        cur_l = 0
        cur = head
        while cur:
            cur_l += 1
            if cur_l == mid:
                return cur
            cur = cur.next

        return None
