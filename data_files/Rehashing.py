
__author__ = 'Danyang'


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val)


class Solution:
    def rehashing(self, hashTable):
        
        cap = len(hashTable)
        cap *= 2
        ht = [None for _ in xrange(cap)]
        for node in hashTable:
            while node:
                self.__rehash(ht, ListNode(node.val))  
                node = node.next
        return ht

    def __rehash(self, ht, node):
        code = self.__hashcode(node.val, len(ht))
        if ht[code] is None:
            ht[code] = node
        else:
            cur = ht[code]
            while cur.next:
                cur = cur.next
            cur.next = node

    def __hashcode(self, key, capacity):
        return key%capacity


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""h""a""s""h""T""a""b""l""e"" ""="" ""[""N""o""n""e"" ""f""o""r"" ""_"" ""i""n"" ""x""r""a""n""g""e""(""3"")""]""
"" "" "" "" ""n""0"" ""="" ""L""i""s""t""N""o""d""e""(""2""9"")""
"" "" "" "" ""n""1"" ""="" ""L""i""s""t""N""o""d""e""(""5"")""
"" "" "" "" ""n""0"".""n""e""x""t"" ""="" ""n""1""
"" "" "" "" ""h""a""s""h""T""a""b""l""e""[""2""]"" ""="" ""n""0""
""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""r""e""h""a""s""h""i""n""g""(""h""a""s""h""T""a""b""l""e"")