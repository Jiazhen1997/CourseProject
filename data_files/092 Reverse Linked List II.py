
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

    def __str__(self):
        return str(self.val)+"," ""+""s""t""r""(""s""e""l""f"".""n""e""x""t"")""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n"":""
"" "" "" "" ""d""e""f"" ""r""e""v""e""r""s""e""B""e""t""w""e""e""n""(""s""e""l""f"","" ""h""e""a""d"","" ""m"","" ""n"")"":""
"" "" "" "" "" "" "" "" 
        
        if not head or m>=n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cnt = 1  
        pre = dummy

        start_pre = None
        start = None

        cur = pre.next  
        while pre.next:
            
            if cnt==m:
                start_pre = pre
                start = cur

            
            
            
            elif m<cnt<=n:
                
                
                
                

                
                cur.next, pre, cur = pre, cur, cur.next  
                cnt += 1
                continue

            
            elif cnt==n+1:
                end = pre
                start_pre.next = end
                start.next = cur
                break



            pre = pre.next
            cur = cur.next
            cnt += 1

        return dummy.next

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""l""e""n""g""t""h"" ""="" ""3""
"" "" "" "" ""l""s""t"" ""="" ""[""L""i""s""t""N""o""d""e""(""i""+""1"")"" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""g""t""h"")""]""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h""-""1"")"":""
"" "" "" "" "" "" "" "" ""l""s""t""[""i""]"".""n""e""x""t"" ""="" ""l""s""t""[""i""+""1""]""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""r""e""v""e""r""s""e""B""e""t""w""e""e""n""(""l""s""t""[""0""]"","" ""1"","" ""3"")