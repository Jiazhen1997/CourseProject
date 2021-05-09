
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def rotateRight(self, head, k):
        
        if not head:
            return None


        dummy = ListNode(0)
        dummy.next = head

        
        length = 0
        pre = dummy
        while pre.next:
            length += 1
            pre = pre.next
        
        last = pre

        
        k = k%length  

        
        count = 0
        pre = dummy
        while count<length-k:  
            count += 1
            pre = pre.next

        
        if k!=0: 
            pre.next, dummy.next, last.next = None, pre.next, dummy.next

        return dummy.next

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""l""e""n""g""t""h"" ""="" ""1""
"" "" "" "" ""l""s""t"" ""="" ""[""L""i""s""t""N""o""d""e""(""i""+""1"")"" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h"")""]""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""g""t""h""-""1"")"":""
"" "" "" "" "" "" "" "" ""l""s""t""[""i""]"".""n""e""x""t"" ""="" ""l""s""t""[""i""+""1""]""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""r""o""t""a""t""e""R""i""g""h""t""(""l""s""t""[""0""]"","" ""1"")""
