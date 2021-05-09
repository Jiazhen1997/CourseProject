
import random

__author__ = 'Daniel'



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, head):
        
        self.head = head

    def getRandom(self):
        
        ret = self.head
        cur = self.head.next
        idx = 1
        while cur:
            if random.randrange(0, idx+1) == 0:
                ret = cur
            cur = cur.next
            idx += 1

        return ret.val




