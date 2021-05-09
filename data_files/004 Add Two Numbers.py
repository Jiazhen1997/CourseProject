

__author__ = 'Danyang'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        
        return repr(self.val)


class Solution:
    def addTwoNumbers(self, l1, l2):
        
        result_head = ListNode(0)

        cur1 = l1
        cur2 = l2
        cur = result_head
        while cur1 or cur2:
            cur.val = cur.val+self.addNode(cur1, cur2)
            if cur.val < 10:
                if cur1 and cur1.next or cur2 and cur2.next:  
                    cur.next = ListNode(0)
            else:
                cur.val -= 10
                cur.next = ListNode(1)

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            cur = cur.next

        return result_head

    def addNode(self, node1, node2):
        
        if not node1 and not node2:
            raise Exception("t"w"o" "n"o"d"e"s" "a"r"e" "N"o"n"e"")""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""n""o""d""e""1"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""n""o""d""e""2"".""v""a""l""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""n""o""d""e""2"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""n""o""d""e""1"".""v""a""l""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""n""o""d""e""1"".""v""a""l""+""n""o""d""e""2"".""v""a""l""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 