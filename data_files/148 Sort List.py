
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def sortList_array(self, head):
        
        if head==None:
            return None
        lst = [] 
        current = head
        while(current):
            lst.append(current)
            current = current.next


        comparator = lambda x, y: cmp(x.val, y.val)
        lst = sorted(lst, comparator)  
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]
        lst[-1].next = None
        return lst[0]

    def sortList(self, head):
        
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        slow_pre = dummy
        fast_pre = dummy
        while fast_pre.next and fast_pre.next.next:
            fast_pre = fast_pre.next.next
            slow_pre = slow_pre.next

        mid_head = slow_pre.next
        dummy_mid = ListNode(0)

        
        slow_pre.next = None  
        head = self.sortList(head)
        mid_head = self.sortList(mid_head)

        
        dummy.next = head
        dummy_mid.next = mid_head
        pre = dummy
        pre_mid = dummy_mid
        while pre.next and pre_mid.next:
            if pre.next.val > pre_mid.next.val:
                pre.next, pre_mid.next.next, pre_mid.next = pre_mid.next, pre.next, pre_mid.next.next
                pre = pre.next
            else:
                pre = pre.next

        
        if  pre_mid.next:
            pre.next = pre_mid.next

        return dummy.next




if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""l""e""n""g""t""h"" ""="" ""5""
"" "" "" "" ""l""s""t"" ""="" ""[""L""i""s""t""N""o""d""e""(""l""e""n""g""t""h""-""i"")"" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""g""t""h"")""]""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""e""n""g""t""h""-""1"")"":""
"" "" "" "" "" "" "" "" ""l""s""t""[""i""]"".""n""e""x""t"" ""="" ""l""s""t""[""i""+""1""]""
""
"" "" "" "" ""h""e""a""d"" ""="" ""S""o""l""u""t""i""o""n""("")"".""s""o""r""t""L""i""s""t""(""l""s""t""[""0""]"")""
""
"" "" "" "" ""c""u""r"" ""="" ""h""e""a""d""
"" "" "" "" ""w""h""i""l""e""(""c""u""r"")"":""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""c""u""r"".""v""a""l""
"" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""c""u""r"".""n""e""x""t