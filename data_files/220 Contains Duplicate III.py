
from collections import OrderedDict

__author__ = 'Daniel'


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        
        if k < 1 or t < 0:
            return False

        if t == 0:
            return self.containsNearByDuplicate(nums, k)

        od = OrderedDict()  
        for n in nums:
            key = n/t
            for j in (-1, 0, 1):  
                m = od.get(key+j)
                if m is not None and abs(m-n) <= t:  
                    return True

            while len(od) >= k:
                od.popitem(False)  

            od[key] = n

        return False

    def containsNearByDuplicate(self, nums, k):
        od = OrderedDict()
        for n in nums:
            if od.get(n):
                return True

            while len(od) >= k:
                od.popitem(False)

            od[n] = n

        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""n""t""a""i""n""s""N""e""a""r""b""y""A""l""m""o""s""t""D""u""p""l""i""c""a""t""e""(""[""-""3"","" ""3""]"","" ""2"","" ""4"")