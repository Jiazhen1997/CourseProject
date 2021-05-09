__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def insertionSortList_TLE(self, head):
        
        comparator = lambda x, y: cmp(x.val, y.val)
        
        dummy_head = ListNode(0)
        dummy_head.next = head


        closed_tail = dummy_head.next
        while(closed_tail and closed_tail.next):
            open_head = closed_tail.next
            

            
            ptr_before = dummy_head
            ptr = dummy_head.next 

            
            while(ptr_before):
                if comparator(ptr, open_head)>0:
                    ptr_before.next = open_head
                    closed_tail.next = open_head.next
                    open_head.next = ptr

                    
                    break

                if ptr==open_head:
                    closed_tail = closed_tail.next
                    break

                ptr_before = ptr_before.next
                ptr = ptr.next


        return dummy_head.next


    def insertionSortList(self, head):
        
        comparator = lambda x, y: cmp(x.val, y.val)
        
        
        dummy = ListNode(0)  
        dummy.next = head

        closed_tail = head
        while (closed_tail and closed_tail.next):
            open_head = closed_tail.next
            open_head_next = closed_tail.next.next
            if not comparator(closed_tail, open_head)<=0:  

                pre = dummy
                while comparator(pre.next, open_head)<0:  
                    pre = pre.next

                
                open_head.next = pre.next
                pre.next = open_head

                closed_tail.next = open_head_next

            else:
                closed_tail = closed_tail.next


        return dummy.next

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""r""a""n""d""o""m""
"" "" "" "" ""l""s""t"" ""="" ""[""L""i""s""t""N""o""d""e""(""i"")"" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""d""o""m"".""s""a""m""p""l""e""(""x""r""a""n""g""e""(""-""1""0""0""0"","" ""1""0""0""0"")"","" ""1""0""0""0"")""]""
"" "" "" "" ""#"" ""l""s""t"" ""="" ""[""L""i""s""t""N""o""d""e""(""1"")"","" ""L""i""s""t""N""o""d""e""(""3"")"","" ""L""i""s""t""N""o""d""e""(""2"")""]""
"" "" "" "" ""#"" ""l""s""t"" ""="" ""[""L""i""s""t""N""o""d""e""(""i"")"" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""1""0"","" ""-""1"","" ""-""1"")""]""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""(""l""s""t"")"")"":""
"" "" "" "" "" "" "" "" ""t""r""y"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t""[""i""]"".""n""e""x""t"" ""="" ""l""s""t""[""i""+""1""]""
"" "" "" "" "" "" "" "" ""e""x""c""e""p""t"" ""I""n""d""e""x""E""r""r""o""r"":"" ""#"" ""l""a""s""t""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t""[""i""]"".""n""e""x""t"" ""="" ""N""o""n""e""
""
""
""
"" "" "" "" ""h""e""a""d"" ""="" ""S""o""l""u""t""i""o""n""("")"".""i""n""s""e""r""t""i""o""n""S""o""r""t""L""i""s""t""(""l""s""t""[""0""]"")""
"" "" "" "" ""c""u""r""r""e""n""t"" ""="" ""h""e""a""d""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""(""l""s""t"")"")"":""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""c""u""r""r""e""n""t"".""v""a""l""
"" "" "" "" "" "" "" "" ""c""u""r""r""e""n""t"" ""="" ""c""u""r""r""e""n""t"".""n""e""x""t""
""
""
""
