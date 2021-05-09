

__author__ = 'Daniel'
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        
        h = []
        n = len(nums)
        for i, v in enumerate(nums):
            if i < k:
                heapq.heappush(h, v)
            else:
                if v <= h[0]:
                    continue
                heapq.heappop(h)
                heapq.heappush(h, v)

        return heapq.heappop(h)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""K""t""h""L""a""r""g""e""s""t""(""[""3"","" ""2"","" ""1"","" ""5"","" ""6"","" ""4""]"","" ""2"")""
""
