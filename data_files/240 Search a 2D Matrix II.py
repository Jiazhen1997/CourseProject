
__author__ = 'Daniel'


class Solution(object):
    def searchMatrix(self, mat, target):
        
        m = len(mat)
        n = len(mat[0])

        i = 0
        j = n-1
        while i < m and 0 <= j:
            if mat[i][j] == target:
                return True
            elif mat[i][j] > target:
                j -= 1
            else:
                i += 1

        return False


class SolutionBinSearch(object):
    def searchMatrix(self, mat, target):
        
        m = len(mat)
        n = len(mat[0])

        col = [mat[i][0] for i in xrange(m)]
        row_by_first = self.bin_search(col, target)

        col = [mat[i][-1] for i in xrange(m)]
        row_by_last = self.bin_search(col, target, False)

        for i in range(row_by_first, row_by_last-1, -1):
            col = self.bin_search(mat[i], target)
            if mat[i][col] == target:
                return True

        return False

    def bin_search(self, A, t, lower=True):
        lo = 0
        hi = len(A)
        while lo < hi:
            mid = (lo+hi)/2
            if A[mid] == t:
                return mid
            elif A[mid] < t:
                lo = mid+1
            else:
                hi = mid

        if lower:
            return lo-1
        else:
            return lo

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""e""a""r""c""h""M""a""t""r""i""x""(""[""[""1"","" ""4""]"","" ""[""2"","" ""5""]""]"","" ""4"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""B""i""n""S""e""a""r""c""h""("")"".""s""e""a""r""c""h""M""a""t""r""i""x""(""[""[""1"","" ""4""]"","" ""[""2"","" ""5""]""]"","" ""4"")"" ""=""="" ""T""r""u""e""
