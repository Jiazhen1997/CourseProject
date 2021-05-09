




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        return prev

    def reverseList_complex(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = head
        cur = head.next
        head.next = None
        while prev and cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        return prev
