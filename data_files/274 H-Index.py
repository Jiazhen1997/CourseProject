
__author__ = 'Daniel'


class Solution(object):
    def hIndex(self, A):
        
        n = len(A)
        cnt = [0 for _ in xrange(n+1)]
        for e in A:
            if e >= n:  
                cnt[n] += 1
            else:
                cnt[e] += 1

        F = [0 for _ in xrange(n+2)]
        for i in xrange(n, -1, -1):
            F[i] += F[i+1] + cnt[i]
            if F[i] >= i:
                return i

        return 0

    def hIndex_sort(self, citations):
        
        n = len(citations)
        citations.sort()
        for i in xrange(n):
            if citations[i] >= n-i:
                return n-i

        return 0

    def hIndex_reverse_sort(self, citations):
        
        citations.sort(reverse=True)
        citations.append(0)
        h = 0
        for i in xrange(len(citations)-1):
            if citations[i] >= i+1 >= citations[i+1]:
                h = i+1
            elif h:
                break

        return h


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""h""I""n""d""e""x""(""[""3"","" ""0"","" ""6"","" ""1"","" ""5""]"")"" ""=""="" ""3