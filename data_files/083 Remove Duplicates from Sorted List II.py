
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next:
            cur = pre.next
            if cur.next and cur.next.val==cur.val:  
                
                next_non_duplicate = cur.next
                while next_non_duplicate and cur.val==next_non_duplicate.val:
                    next_non_duplicate = next_non_duplicate.next

                
                pre.next = next_non_duplicate

            else:
                pre = pre.next

        return dummy.next




