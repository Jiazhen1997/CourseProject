
__author__ = 'Danyang'


class Solution:
    def heapify(self, A):
        
        n = len(A)
        for i in xrange(n/2, -1, -1):
            self.heappush(A, i)

    def heappush(self, A, i):
        
        n = len(A)
        if i >= n:
            return

        l = 2*i+1
        r = 2*i+2
        mini = i
        if l < n and A[l] < A[mini]:
            mini = l
        if r < n and A[r] < A[mini]:
            mini = r
        if i != mini:
            A[i], A[mini] = A[mini], A[i]
            swapped = mini
            self.heappush(A, swapped)

    def heapify_error(self, A, i=0):
        
        n = len(A)
        if i >= n:
            return

        l = 2*i+1
        r = 2*i+2
        mini = i
        if l < n and A[l] < A[mini]:
            mini = l
        if r < n and A[r] < A[mini]:
            mini = r
        A[i], A[mini] = A[mini], A[i]
        self.heapify_error(A, l)
        self.heapify_error(A, r)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""A"" ""="" ""[""4""5"","" ""3""9"","" ""3""2"","" ""1""1""]""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""h""e""a""p""i""f""y""(""A"")""
"" "" "" "" ""a""s""s""e""r""t"" ""A"" ""=""="" ""[""1""1"","" ""3""9"","" ""3""2"","" ""4""5""]""
