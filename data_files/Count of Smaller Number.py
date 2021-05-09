
__author__ = 'Daniel'


class Solution:
    def countOfSmallerNumber(self, A, queries):
        
        return self.search(A, queries)

    def loop(self, A, queries):
        
        cnt = dict(zip(queries, [0 for _ in queries]))
        for elt in A:
            for k in cnt.keys():
                if elt<k:
                    cnt[k] += 1

        return [cnt[i] for i in queries]

    def search(self, A, queries):
        
        A.sort()
        ret = []
        for q in queries:
            ind = self.bin_search(A, q)
            while ind>=0 and A[ind]==q:
                ind -= 1
            ret.append(ind+1)

        return ret

    def bin_search(self, A, t):
        b = 0
        e = len(A)
        while b<e:
            m = (b+e)/2
            if t==A[m]:
                return m
            elif t < A[m]:
                e = m
            else:
                b = m+1
        return b-1


    def segment_tree(self, A, queries):
        
        pass