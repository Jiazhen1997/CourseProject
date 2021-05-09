
import heapq

__author__ = 'Daniel'


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        
        class Node(object):
            def __init__(self, i, j):
                self.i, self.j = i, j

            def __cmp__(self, other):
                return nums1[self.i] + nums2[self.j] - (nums1[other.i] + nums2[other.j])

            def hasnext(self):
                return self.j + 1 < len(nums2)

            def next(self):
                if self.hasnext():
                    return Node(self.i, self.j + 1)

                raise StopIteration

        if not nums1 or not nums2:
            return []

        h = []
        for i in xrange(min(k, len(nums1))):
            heapq.heappush(h, Node(i, 0))

        ret = []
        while h and len(ret) < k:
            node = heapq.heappop(h)
            ret.append([nums1[node.i], nums2[node.j]])
            if node.hasnext():
                heapq.heappush(h, node.next())

        return ret

    def kSmallestPairsError(self, nums1, nums2, k):
        
        i = 0
        j = 0
        ret = []
        for _ in xrange(k):
            if i < len(nums1) and j < len(nums2):
                ret.append([nums1[i], nums2[j]])
                if nums1[i] < nums2[j]:
                    j += 1
                else:
                    i += 1
            else:
                break

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""S""m""a""l""l""e""s""t""P""a""i""r""s""(""[""1"","" ""7"","" ""1""1""]"","" ""[""2"","" ""4"","" ""6""]"","" ""9"")"" ""=""="" ""[""[""1"","" ""2""]"","" ""[""1"","" ""4""]"","" ""[""1"","" ""6""]"","" ""[""7"","" ""2""]"","" ""[""7"","" ""4""]"","" ""[""1""1"","" ""2""]"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""[""7"","" ""6""]"","" ""[""1""1"","" ""4""]"","" ""[""1""1"","" ""6""]""]