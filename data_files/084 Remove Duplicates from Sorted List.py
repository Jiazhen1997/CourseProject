
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        
        
        if not head:
            return head
        
        closed_ptr = head
        open_ptr = head.next
        while open_ptr:
            
            while open_ptr and closed_ptr.val==open_ptr.val:
                open_ptr = open_ptr.next

            closed_ptr.next = open_ptr
            closed_ptr = closed_ptr.next
            open_ptr = open_ptr.next if open_ptr else None

        return head

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""n""o""d""e""s"" ""="" ""[""L""i""s""t""N""o""d""e""(""1"")"" ""f""o""r"" ""_"" ""i""n"" ""r""a""n""g""e""(""2"")""]""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""(""n""o""d""e""s"")""-""1"")"":""
"" "" "" "" "" "" "" "" ""n""o""d""e""s""[""i""]"".""n""e""x""t"" ""="" ""n""o""d""e""s""[""i""+""1""]""
""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""d""e""l""e""t""e""D""u""p""l""i""c""a""t""e""s""(""n""o""d""e""s""[""0""]"")