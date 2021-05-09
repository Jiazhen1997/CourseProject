
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

    def __str__(self):
        return "%"d"," "%"s""%""(""s""e""l""f"".""v""a""l"","" ""s""e""l""f"".""n""e""x""t"")""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n"":""
"" "" "" "" ""d""e""f"" ""m""e""r""g""e""T""w""o""L""i""s""t""s""(""s""e""l""f"","" ""l""1"","" ""l""2"")"":""
"" "" "" "" "" "" "" "" 
        dummy = ListNode(0)
        dummy.next = l1

        pre = dummy
        the_other = l2
        while pre and pre.next:
            cur = pre.next
            if the_other and cur.val>the_other.val:
                
                temp = the_other.next
                pre.next, the_other.next = the_other, cur

                the_other = temp  
            pre = pre.next


        
        if the_other:
            pre.next = the_other  

        return dummy.next

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""l""e""n""g""t""h"" ""="" ""1""0""
"" "" "" "" ""l""i""s""t""1"" ""="" ""[""L""i""s""t""N""o""d""e""(""2""*""i"")"" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h"")""]""
"" "" "" "" ""l""i""s""t""2"" ""="" ""[""L""i""s""t""N""o""d""e""(""2""*""i""+""1"")"" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h"")""]""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h""-""1"")"":""
"" "" "" "" "" "" "" "" ""l""i""s""t""1""[""i""]"".""n""e""x""t"" ""="" ""l""i""s""t""1""[""i""+""1""]""
"" "" "" "" "" "" "" "" ""l""i""s""t""2""[""i""]"".""n""e""x""t"" ""="" ""l""i""s""t""2""[""i""+""1""]""
""
"" "" "" "" ""l""s""t"" ""="" ""S""o""l""u""t""i""o""n""("")"".""m""e""r""g""e""T""w""o""L""i""s""t""s""(""l""i""s""t""1""[""0""]"","" ""l""i""s""t""2""[""0""]"")""
"" "" "" "" ""p""r""i""n""t"" ""l""s""t""
