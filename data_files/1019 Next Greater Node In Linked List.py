



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        ret = []
        stk = []  
        i = 0
        cur = head
        while cur:
            while stk and stk[-1][1] < cur.val:
                idx, _ = stk.pop()
                ret[idx] = cur.val

            stk.append([i, cur.val])
            ret.append(0)
            cur = cur.next
            i += 1

        return ret
