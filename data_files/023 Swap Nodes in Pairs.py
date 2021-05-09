
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next and pre.next.next:
            node1 = pre.next
            node2 = pre.next.next

            
            
            
            

            pre.next, node1.next, node2.next = node2, node2.next, node1

            pre = pre.next.next

        return dummy.next