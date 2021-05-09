


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import math


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        
        l = 0
        node = root
        while node:
            l += 1
            node = node.next


        ret = [[] for _ in range(k)]

        short_chunk_l = l // k
        long_chunk_l = short_chunk_l + 1
        n_long_chunk = l % k  
        n_short_chunk = l - n_long_chunk

        chunk_counter = 0
        cur_l = 0
        node = root
        while node:
            ret[chunk_counter].append(node.val)
            cur_l += 1
            chunk_size = long_chunk_l if chunk_counter < n_long_chunk else short_chunk_l
            if cur_l == chunk_size:
                cur_l = 0
                chunk_counter += 1
            node = node.next

        return ret

    def splitListToParts_2(self, root: ListNode, k: int) -> List[ListNode]:
        
        l = 0
        node = root
        while node:
            l += 1
            node = node.next


        ret = [[] for _ in range(k)]
        node = root
        counter = 0
        cur_l = 0
        i = 0
        part_l = math.ceil((l - counter) / k)
        while node:
            cur_l += 1
            counter += 1
            ret[i].append(node.val)
            if cur_l == part_l:
                k -= 1
                cur_l = 0
                i += 1
                if k != 0:
                    part_l = math.ceil((l - counter) / k)

            node = node.next

        return ret

    def splitListToParts_error(self, root: ListNode, k: int) -> List[ListNode]:
        
        l = 0
        node = root
        while node:
            l += 1
            node = node.next

        part_l = math.ceil(l / k)
        ret = [[] for _ in range(k)]

        node = root
        cur_l = 0
        i = 0
        while node:
            cur_l += 1
            ret[i].append(node.val)
            if cur_l == part_l:
                cur_l = 0
                i += 1

            node = node.next

        return ret
