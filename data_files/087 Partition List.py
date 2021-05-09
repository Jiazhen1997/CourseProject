
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def partition(self, head, x):
        
        dummy = ListNode(0)
        dummy.next = head
        dummy_smaller = ListNode(0)
        dummy_larger = ListNode(0)

        pre = dummy
        pre_smaller = dummy_smaller
        pre_larger = dummy_larger
        while pre.next:
            cur = pre.next
            if cur.val<x:
                pre_smaller.next = cur
                pre_smaller = pre_smaller.next
            else:
                pre_larger.next = cur
                pre_larger = pre_larger.next
            pre = pre.next
        
        pre_larger.next = None  
        
        pre_smaller.next = dummy_larger.next
        return dummy_smaller.next

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""l""s""t"" ""="" ""[""L""i""s""t""N""o""d""e""(""2"")"","" ""L""i""s""t""N""o""d""e""(""1"")""]""
"" "" "" "" ""f""o""r"" ""i""n""d"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""(""l""s""t"")""-""1"")"":""
"" "" "" "" "" "" "" "" ""l""s""t""[""i""n""d""]"".""n""e""x""t"" ""="" ""l""s""t""[""i""n""d""+""1""]""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""p""a""r""t""i""t""i""o""n""(""l""s""t""[""0""]"","" ""2"")