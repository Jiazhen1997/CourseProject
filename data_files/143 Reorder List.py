
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def reorderList_TLE(self, head):
        
        dummy_head = ListNode(0)
        dummy_head.next = head

        pre_cur = dummy_head
        while(pre_cur and pre_cur.next):
            
            pre_last = pre_cur.next
            if pre_last.next == None:
                return
            while(pre_last.next.next):
                pre_last = pre_last.next

            last = pre_last.next

            
            cur = pre_cur.next
            cur_next = cur.next
            if cur_next!= last and cur!= last:
                cur.next = last
                last.next = cur_next
                
                pre_last.next = None

            if cur_next and cur_next.next==last:
                cur_next.next = None


            pre_cur = pre_cur.next.next

    def reorderList_array(self, head):
        
        lst = []
        cur = head
        while(cur):
            lst.append(cur)
            cur = cur.next

        lst1 = lst[:len(lst)/2]
        lst2 = lst[len(lst)/2:]
        lst2.reverse()

        lst = []
        for i in range(len(lst2)):
            try:
                lst.append(lst1[i])
            except IndexError:
                pass
            lst.append(lst2[i])

        for i in range(len(lst)):
            try:
                lst[i].next = lst[i+1]
            except IndexError:
                lst[i].next = None

    def reorderList(self, head):
        
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head

        
        slow_pre = dummy
        fast_pre = dummy
        while fast_pre.next and fast_pre.next.next:
            fast_pre = fast_pre.next
            fast_pre = fast_pre.next
            slow_pre = slow_pre.next

        
        mid = slow_pre.next

        pre = mid
        cur = pre.next
        while pre and cur:  
            cur.next, pre, cur = pre, cur, cur.next
        mid.next = None

        
        last = pre
        cur = dummy.next
        while cur!=mid and last!=mid:
            cur.next, last.next, last, cur = last, cur.next, last.next, cur.next








if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""l""e""n""g""t""h"" ""="" ""2""
"" "" "" "" ""l""s""t"" ""="" ""[""L""i""s""t""N""o""d""e""(""i""+""1"")"" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""g""t""h"")""]""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""g""t""h""-""1"")"":""
"" "" "" "" "" "" "" "" ""l""s""t""[""i""]"".""n""e""x""t"" ""="" ""l""s""t""[""i""+""1""]""
""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""r""e""o""r""d""e""r""L""i""s""t""(""l""s""t""[""0""]"")""
""
"" "" "" "" ""c""u""r"" ""="" ""l""s""t""[""0""]""
"" "" "" "" ""w""h""i""l""e""(""c""u""r"")"":""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""c""u""r"".""v""a""l""
"" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""c""u""r"".""n""e""x""t""
