
__author__ = 'Daniel'


def knows(a, b):
    


class Solution(object):
    def findCelebrity(self, n):
        
        i = 0
        j = n-1
        while i < j:
            nxt_i, nxt_j = i, j
            if knows(i, j) or not knows(j, i):
                nxt_i += 1
            if knows(j, i) or not knows(i, j):
                nxt_j -= 1
            i, j = nxt_i, nxt_j

        celebrity = i
        for i in xrange(n):
            if i != celebrity and (not knows(i, celebrity) or knows(celebrity, i)):
                return -1

        return celebrity

    def findCelebrity_set(self, n):
        
        V = set(range(n))

        while len(V) > 1:
            a = V.pop()
            b = V.pop()
            if knows(a, b) and not knows(b, a):
                V.add(b)
            elif not knows(a, b) and knows(b, a):
                V.add(a)

        if not V:
            return -1

        celebrity = V.pop()
        for i in xrange(n):
            if i != celebrity and (not knows(i, celebrity) or knows(celebrity, i)):
                return -1

        return celebrity
