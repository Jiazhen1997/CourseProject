

from typing import List
import heapq


class DualHeap:
    def __init__(self):
        
        self.max_h = []  
        self.min_h = []
        self.max_sz = 0
        self.min_sz = 0
        self.to_remove = set()  

    def insert(self, num):
        if self.max_h and num > self.max_h[0][1]:
            heapq.heappush(self.min_h, (num, num))
            self.min_sz += 1
        else:
            heapq.heappush(self.max_h, (-num, num))
            self.max_sz += 1
        self.balance()

    def pop(self, num):
        self.to_remove.add(num)
        if self.max_h and num > self.max_h[0][1]:
            self.min_sz -= 1
        else:
            self.max_sz -= 1
        self.balance()

    def clean_top(self):
        while self.max_h and self.max_h[0][1] in self.to_remove:
            _, num = heapq.heappop(self.max_h)
            self.to_remove.remove(num)
        while self.min_h and self.min_h[0][1] in self.to_remove:
            _, num = heapq.heappop(self.min_h)
            self.to_remove.remove(num)

    def balance(self):
        
        while self.max_sz < self.min_sz :
            self.clean_top()
            _, num =heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, (-num, num))
            self.min_sz -= 1
            self.max_sz += 1
        while self.max_sz > self.min_sz + 1:
            self.clean_top()
            _, num = heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, (num, num))
            self.min_sz += 1
            self.max_sz -= 1

        self.clean_top()

    def get_median(self, k):
        self.clean_top()
        if k % 2 == 1:
            return self.max_h[0][1]
        else:
            return 0.5 * (self.max_h[0][1] + self.min_h[0][1])


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        ret = []
        dh = DualHeap()
        for i in range(k):
            dh.insert(nums[i])

        ret.append(dh.get_median(k))

        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.pop(nums[i-k])
            ret.append(dh.get_median(k))

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""e""d""i""a""n""S""l""i""d""i""n""g""W""i""n""d""o""w""(""[""-""2""1""4""7""4""8""3""6""4""8"",""-""2""1""4""7""4""8""3""6""4""8"",""2""1""4""7""4""8""3""6""4""7"",""-""2""1""4""7""4""8""3""6""4""8"",""-""2""1""4""7""4""8""3""6""4""8"",""-""2""1""4""7""4""8""3""6""4""8"",""2""1""4""7""4""8""3""6""4""7"",""2""1""4""7""4""8""3""6""4""7"",""2""1""4""7""4""8""3""6""4""7"",""2""1""4""7""4""8""3""6""4""7"",""-""2""1""4""7""4""8""3""6""4""8"",""2""1""4""7""4""8""3""6""4""7"",""-""2""1""4""7""4""8""3""6""4""8""]"","" ""2"")""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""e""d""i""a""n""S""l""i""d""i""n""g""W""i""n""d""o""w""(""[""1"",""1"",""1"",""1""]"","" ""2"")"" ""=""="" ""[""1"","" ""1"","" ""1""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""e""d""i""a""n""S""l""i""d""i""n""g""W""i""n""d""o""w""(""[""1"",""3"",""-""1"",""-""3"",""5"",""3"",""6"",""7""]"","" ""3"")"" ""=""="" ""[""1"",""-""1"",""-""1"",""3"",""5"",""6""]""
